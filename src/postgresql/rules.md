---
title: The Rule System
source_url: https://www.postgresql.org/docs/17/rules.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: rules.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 3480
---

## The Rule System

rule

This chapter discusses the rule system in PostgreSQL. Production rule systems are conceptually simple, but there are many subtle points involved in actually using them.

Some other database systems define active database rules, which are usually stored procedures and triggers. In PostgreSQL, these can be implemented using functions and triggers as well.

The rule system (more precisely speaking, the query rewrite rule system) is totally different from stored procedures and triggers. It modifies queries to take rules into consideration, and then passes the modified query to the query planner for planning and execution. It is very powerful, and can be used for many things such as query language procedures, views, and versions. The theoretical foundations and the power of this rule system are also discussed in [???](#ston90b) and [???](#ong90).

## The Query Tree

query tree

To understand how the rule system works it is necessary to know when it is invoked and what its input and results are.

The rule system is located between the parser and the planner. It takes the output of the parser, one query tree, and the user-defined rewrite rules, which are also query trees with some extra information, and creates zero or more query trees as result. So its input and output are always things the parser itself could have produced and thus, anything it sees is basically representable as an SQL statement.

Now what is a query tree? It is an internal representation of an SQL statement where the single parts that it is built from are stored separately. These query trees can be shown in the server log if you set the configuration parameters `debug_print_parse`, `debug_print_rewritten`, or `debug_print_plan`. The rule actions are also stored as query trees, in the system catalog pg_rewrite. They are not formatted like the log output, but they contain exactly the same information.

Reading a raw query tree requires some experience. But since SQL representations of query trees are sufficient to understand the rule system, this chapter will not teach how to read them.

When reading the SQL representations of the query trees in this chapter it is necessary to be able to identify the parts the statement is broken into when it is in the query tree structure. The parts of a query tree are

the command type  
This is a simple value telling which command (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) produced the query tree.

the range table <span class="indexterm"></span>  
The range table is a list of relations that are used in the query. In a `SELECT` statement these are the relations given after the `FROM` key word.

Every range table entry identifies a table or view and tells by which name it is called in the other parts of the query. In the query tree, the range table entries are referenced by number rather than by name, so here it doesn't matter if there are duplicate names as it would in an SQL statement. This can happen after the range tables of rules have been merged in. The examples in this chapter will not have this situation.

the result relation  
This is an index into the range table that identifies the relation where the results of the query go.

`SELECT` queries don't have a result relation. (The special case of `SELECT INTO` is mostly identical to `CREATE TABLE` followed by `INSERT ... SELECT`, and is not discussed separately here.)

For `INSERT`, `UPDATE`, and `DELETE` commands, the result relation is the table (or view!) where the changes are to take effect.

the target list <span class="indexterm"></span>  
The target list is a list of expressions that define the result of the query. In the case of a `SELECT`, these expressions are the ones that build the final output of the query. They correspond to the expressions between the key words `SELECT` and `FROM`. (`*` is just an abbreviation for all the column names of a relation. It is expanded by the parser into the individual columns, so the rule system never sees it.)

`DELETE` commands don't need a normal target list because they don't produce any result. Instead, the planner adds a special CTID entry to the empty target list, to allow the executor to find the row to be deleted. (CTID is added when the result relation is an ordinary table. If it is a view, a whole-row variable is added instead, by the rule system, as described in [Updating a View](#rules-views-update).)

For `INSERT` commands, the target list describes the new rows that should go into the result relation. It consists of the expressions in the `VALUES` clause or the ones from the `SELECT` clause in `INSERT ... SELECT`. The first step of the rewrite process adds target list entries for any columns that were not assigned to by the original command but have defaults. Any remaining columns (with neither a given value nor a default) will be filled in by the planner with a constant null expression.

For `UPDATE` commands, the target list describes the new rows that should replace the old ones. In the rule system, it contains just the expressions from the `SET column = expression` part of the command. The planner will handle missing columns by inserting expressions that copy the values from the old row into the new one. Just as for `DELETE`, a CTID or whole-row variable is added so that the executor can identify the old row to be updated.

Every entry in the target list contains an expression that can be a constant value, a variable pointing to a column of one of the relations in the range table, a parameter, or an expression tree made of function calls, constants, variables, operators, etc.

the qualification  
The query's qualification is an expression much like one of those contained in the target list entries. The result value of this expression is a Boolean that tells whether the operation (`INSERT`, `UPDATE`, `DELETE`, or `SELECT`) for the final result row should be executed or not. It corresponds to the `WHERE` clause of an SQL statement.

the join tree  
The query's join tree shows the structure of the `FROM` clause. For a simple query like `SELECT ... FROM a, b, c`, the join tree is just a list of the `FROM` items, because we are allowed to join them in any order. But when `JOIN` expressions, particularly outer joins, are used, we have to join in the order shown by the joins. In that case, the join tree shows the structure of the `JOIN` expressions. The restrictions associated with particular `JOIN` clauses (from `ON` or `USING` expressions) are stored as qualification expressions attached to those join-tree nodes. It turns out to be convenient to store the top-level `WHERE` expression as a qualification attached to the top-level join-tree item, too. So really the join tree represents both the `FROM` and `WHERE` clauses of a `SELECT`.

the others  
The other parts of the query tree like the `ORDER BY` clause aren't of interest here. The rule system substitutes some entries there while applying rules, but that doesn't have much to do with the fundamentals of the rule system.

## Views and the Rule System

rule

and views

view

implementation through rules

Views in PostgreSQL are implemented using the rule system. A view is basically an empty table (having no actual storage) with an `ON SELECT DO INSTEAD` rule. Conventionally, that rule is named `_RETURN`. So a view like

    CREATE VIEW myview AS SELECT * FROM mytab;

is very nearly the same thing as

    CREATE TABLE myview (same column list as mytab);
    CREATE RULE "_RETURN" AS ON SELECT TO myview DO INSTEAD
        SELECT * FROM mytab;

although you can't actually write that, because tables are not allowed to have `ON SELECT` rules.

A view can also have other kinds of `DO INSTEAD` rules, allowing `INSERT`, `UPDATE`, or `DELETE` commands to be performed on the view despite its lack of underlying storage. This is discussed further below, in [Updating a View](#rules-views-update).

### How `SELECT` Rules Work

rule

for SELECT

Rules `ON SELECT` are applied to all queries as the last step, even if the command given is an `INSERT`, `UPDATE` or `DELETE`. And they have different semantics from rules on the other command types in that they modify the query tree in place instead of creating a new one. So `SELECT` rules are described first.

Currently, there can be only one action in an `ON SELECT` rule, and it must be an unconditional `SELECT` action that is `INSTEAD`. This restriction was required to make rules safe enough to open them for ordinary users, and it restricts `ON SELECT` rules to act like views.

The examples for this chapter are two join views that do some calculations and some more views using them in turn. One of the two first views is customized later by adding rules for `INSERT`, `UPDATE`, and `DELETE` operations so that the final result will be a view that behaves like a real table with some magic functionality. This is not such a simple example to start from and this makes things harder to get into. But it's better to have one example that covers all the points discussed step by step rather than having many different ones that might mix up in mind.

The real tables we need in the first two rule system descriptions are these:

    CREATE TABLE shoe_data (
        shoename   text,          -- primary key
        sh_avail   integer,       -- available number of pairs
        slcolor    text,          -- preferred shoelace color
        slminlen   real,          -- minimum shoelace length
        slmaxlen   real,          -- maximum shoelace length
        slunit     text           -- length unit
    );

    CREATE TABLE shoelace_data (
        sl_name    text,          -- primary key
        sl_avail   integer,       -- available number of pairs
        sl_color   text,          -- shoelace color
        sl_len     real,          -- shoelace length
        sl_unit    text           -- length unit
    );

    CREATE TABLE unit (
        un_name    text,          -- primary key
        un_fact    real           -- factor to transform to cm
    );

As you can see, they represent shoe-store data.

The views are created as:

    CREATE VIEW shoe AS
        SELECT sh.shoename,
               sh.sh_avail,
               sh.slcolor,
               sh.slminlen,
               sh.slminlen * un.un_fact AS slminlen_cm,
               sh.slmaxlen,
               sh.slmaxlen * un.un_fact AS slmaxlen_cm,
               sh.slunit
          FROM shoe_data sh, unit un
         WHERE sh.slunit = un.un_name;

    CREATE VIEW shoelace AS
        SELECT s.sl_name,
               s.sl_avail,
               s.sl_color,
               s.sl_len,
               s.sl_unit,
               s.sl_len * u.un_fact AS sl_len_cm
          FROM shoelace_data s, unit u
         WHERE s.sl_unit = u.un_name;

    CREATE VIEW shoe_ready AS
        SELECT rsh.shoename,
               rsh.sh_avail,
               rsl.sl_name,
               rsl.sl_avail,
               least(rsh.sh_avail, rsl.sl_avail) AS total_avail
          FROM shoe rsh, shoelace rsl
         WHERE rsl.sl_color = rsh.slcolor
           AND rsl.sl_len_cm >= rsh.slminlen_cm
           AND rsl.sl_len_cm <= rsh.slmaxlen_cm;

The `CREATE VIEW` command for the `shoelace` view (which is the simplest one we have) will create a relation `shoelace` and an entry in pg_rewrite that tells that there is a rewrite rule that must be applied whenever the relation `shoelace` is referenced in a query's range table. The rule has no rule qualification (discussed later, with the non-`SELECT` rules, since `SELECT` rules currently cannot have them) and it is `INSTEAD`. Note that rule qualifications are not the same as query qualifications. The action of our rule has a query qualification. The action of the rule is one query tree that is a copy of the `SELECT` statement in the view creation command.

> [!NOTE]
> The two extra range table entries for `NEW` and `OLD` that you can see in the pg_rewrite entry aren't of interest for `SELECT` rules.

Now we populate `unit`, `shoe_data` and `shoelace_data` and run a simple query on a view:

    INSERT INTO unit VALUES ('cm', 1.0);
    INSERT INTO unit VALUES ('m', 100.0);
    INSERT INTO unit VALUES ('inch', 2.54);

    INSERT INTO shoe_data VALUES ('sh1', 2, 'black', 70.0, 90.0, 'cm');
    INSERT INTO shoe_data VALUES ('sh2', 0, 'black', 30.0, 40.0, 'inch');
    INSERT INTO shoe_data VALUES ('sh3', 4, 'brown', 50.0, 65.0, 'cm');
    INSERT INTO shoe_data VALUES ('sh4', 3, 'brown', 40.0, 50.0, 'inch');

    INSERT INTO shoelace_data VALUES ('sl1', 5, 'black', 80.0, 'cm');
    INSERT INTO shoelace_data VALUES ('sl2', 6, 'black', 100.0, 'cm');
    INSERT INTO shoelace_data VALUES ('sl3', 0, 'black', 35.0 , 'inch');
    INSERT INTO shoelace_data VALUES ('sl4', 8, 'black', 40.0 , 'inch');
    INSERT INTO shoelace_data VALUES ('sl5', 4, 'brown', 1.0 , 'm');
    INSERT INTO shoelace_data VALUES ('sl6', 0, 'brown', 0.9 , 'm');
    INSERT INTO shoelace_data VALUES ('sl7', 7, 'brown', 60 , 'cm');
    INSERT INTO shoelace_data VALUES ('sl8', 1, 'brown', 40 , 'inch');

    SELECT * FROM shoelace;

     sl_name   | sl_avail | sl_color | sl_len | sl_unit | sl_len_cm
    -----------+----------+----------+--------+---------+-----------
     sl1       |        5 | black    |     80 | cm      |        80
     sl2       |        6 | black    |    100 | cm      |       100
     sl7       |        7 | brown    |     60 | cm      |        60
     sl3       |        0 | black    |     35 | inch    |      88.9
     sl4       |        8 | black    |     40 | inch    |     101.6
     sl8       |        1 | brown    |     40 | inch    |     101.6
     sl5       |        4 | brown    |      1 | m       |       100
     sl6       |        0 | brown    |    0.9 | m       |        90
    (8 rows)

This is the simplest `SELECT` you can do on our views, so we take this opportunity to explain the basics of view rules. The `SELECT * FROM shoelace` was interpreted by the parser and produced the query tree:

    SELECT shoelace.sl_name, shoelace.sl_avail,
           shoelace.sl_color, shoelace.sl_len,
           shoelace.sl_unit, shoelace.sl_len_cm
      FROM shoelace shoelace;

and this is given to the rule system. The rule system walks through the range table and checks if there are rules for any relation. When processing the range table entry for `shoelace` (the only one up to now) it finds the `_RETURN` rule with the query tree:

    SELECT s.sl_name, s.sl_avail,
           s.sl_color, s.sl_len, s.sl_unit,
           s.sl_len * u.un_fact AS sl_len_cm
      FROM shoelace old, shoelace new,
           shoelace_data s, unit u
     WHERE s.sl_unit = u.un_name;

To expand the view, the rewriter simply creates a subquery range-table entry containing the rule's action query tree, and substitutes this range table entry for the original one that referenced the view. The resulting rewritten query tree is almost the same as if you had typed:

    SELECT shoelace.sl_name, shoelace.sl_avail,
           shoelace.sl_color, shoelace.sl_len,
           shoelace.sl_unit, shoelace.sl_len_cm
      FROM (SELECT s.sl_name,
                   s.sl_avail,
                   s.sl_color,
                   s.sl_len,
                   s.sl_unit,
                   s.sl_len * u.un_fact AS sl_len_cm
              FROM shoelace_data s, unit u
             WHERE s.sl_unit = u.un_name) shoelace;

There is one difference however: the subquery's range table has two extra entries `shoelace old` and `shoelace new`. These entries don't participate directly in the query, since they aren't referenced by the subquery's join tree or target list. The rewriter uses them to store the access privilege check information that was originally present in the range-table entry that referenced the view. In this way, the executor will still check that the user has proper privileges to access the view, even though there's no direct use of the view in the rewritten query.

That was the first rule applied. The rule system will continue checking the remaining range-table entries in the top query (in this example there are no more), and it will recursively check the range-table entries in the added subquery to see if any of them reference views. (But it won't expand `old` or `new` otherwise we'd have infinite recursion!) In this example, there are no rewrite rules for `shoelace_data` or `unit`, so rewriting is complete and the above is the final result given to the planner.

Now we want to write a query that finds out for which shoes currently in the store we have the matching shoelaces (color and length) and where the total number of exactly matching pairs is greater than or equal to two.

    SELECT * FROM shoe_ready WHERE total_avail >= 2;

     shoename | sh_avail | sl_name | sl_avail | total_avail
    ----------+----------+---------+----------+-------------
     sh1      |        2 | sl1     |        5 |           2
     sh3      |        4 | sl7     |        7 |           4
    (2 rows)

The output of the parser this time is the query tree:

    SELECT shoe_ready.shoename, shoe_ready.sh_avail,
           shoe_ready.sl_name, shoe_ready.sl_avail,
           shoe_ready.total_avail
      FROM shoe_ready shoe_ready
     WHERE shoe_ready.total_avail >= 2;

The first rule applied will be the one for the `shoe_ready` view and it results in the query tree:

    SELECT shoe_ready.shoename, shoe_ready.sh_avail,
           shoe_ready.sl_name, shoe_ready.sl_avail,
           shoe_ready.total_avail
      FROM (SELECT rsh.shoename,
                   rsh.sh_avail,
                   rsl.sl_name,
                   rsl.sl_avail,
                   least(rsh.sh_avail, rsl.sl_avail) AS total_avail
              FROM shoe rsh, shoelace rsl
             WHERE rsl.sl_color = rsh.slcolor
               AND rsl.sl_len_cm >= rsh.slminlen_cm
               AND rsl.sl_len_cm <= rsh.slmaxlen_cm) shoe_ready
     WHERE shoe_ready.total_avail >= 2;

Similarly, the rules for `shoe` and `shoelace` are substituted into the range table of the subquery, leading to a three-level final query tree:

    SELECT shoe_ready.shoename, shoe_ready.sh_avail,
           shoe_ready.sl_name, shoe_ready.sl_avail,
           shoe_ready.total_avail
      FROM (SELECT rsh.shoename,
                   rsh.sh_avail,
                   rsl.sl_name,
                   rsl.sl_avail,
                   least(rsh.sh_avail, rsl.sl_avail) AS total_avail
              FROM (SELECT sh.shoename,
                           sh.sh_avail,
                           sh.slcolor,
                           sh.slminlen,
                           sh.slminlen * un.un_fact AS slminlen_cm,
                           sh.slmaxlen,
                           sh.slmaxlen * un.un_fact AS slmaxlen_cm,
                           sh.slunit
                      FROM shoe_data sh, unit un
                     WHERE sh.slunit = un.un_name) rsh,
                   (SELECT s.sl_name,
                           s.sl_avail,
                           s.sl_color,
                           s.sl_len,
                           s.sl_unit,
                           s.sl_len * u.un_fact AS sl_len_cm
                      FROM shoelace_data s, unit u
                     WHERE s.sl_unit = u.un_name) rsl
             WHERE rsl.sl_color = rsh.slcolor
               AND rsl.sl_len_cm >= rsh.slminlen_cm
               AND rsl.sl_len_cm <= rsh.slmaxlen_cm) shoe_ready
     WHERE shoe_ready.total_avail >= 2;

This might look inefficient, but the planner will collapse this into a single-level query tree by “pulling up” the subqueries, and then it will plan the joins just as if we'd written them out manually. So collapsing the query tree is an optimization that the rewrite system doesn't have to concern itself with.

### View Rules in Non-`SELECT` Statements

Two details of the query tree aren't touched in the description of view rules above. These are the command type and the result relation. In fact, the command type is not needed by view rules, but the result relation may affect the way in which the query rewriter works, because special care needs to be taken if the result relation is a view.

There are only a few differences between a query tree for a `SELECT` and one for any other command. Obviously, they have a different command type and for a command other than a `SELECT`, the result relation points to the range-table entry where the result should go. Everything else is absolutely the same. So having two tables `t1` and `t2` with columns `a` and `b`, the query trees for the two statements:

    SELECT t2.b FROM t1, t2 WHERE t1.a = t2.a;

    UPDATE t1 SET b = t2.b FROM t2 WHERE t1.a = t2.a;

are nearly identical. In particular:

- The range tables contain entries for the tables `t1` and `t2`.

- The target lists contain one variable that points to column `b` of the range table entry for table `t2`.

- The qualification expressions compare the columns `a` of both range-table entries for equality.

- The join trees show a simple join between `t1` and `t2`.

The consequence is, that both query trees result in similar execution plans: They are both joins over the two tables. For the `UPDATE` the missing columns from `t1` are added to the target list by the planner and the final query tree will read as:

    UPDATE t1 SET a = t1.a, b = t2.b FROM t2 WHERE t1.a = t2.a;

and thus the executor run over the join will produce exactly the same result set as:

    SELECT t1.a, t2.b FROM t1, t2 WHERE t1.a = t2.a;

But there is a little problem in `UPDATE`: the part of the executor plan that does the join does not care what the results from the join are meant for. It just produces a result set of rows. The fact that one is a `SELECT` command and the other is an `UPDATE` is handled higher up in the executor, where it knows that this is an `UPDATE`, and it knows that this result should go into table `t1`. But which of the rows that are there has to be replaced by the new row?

To resolve this problem, another entry is added to the target list in `UPDATE` (and also in `DELETE`) statements: the current tuple ID (CTID).<span class="indexterm"></span> This is a system column containing the file block number and position in the block for the row. Knowing the table, the CTID can be used to retrieve the original row of `t1` to be updated. After adding the CTID to the target list, the query actually looks like:

    SELECT t1.a, t2.b, t1.ctid FROM t1, t2 WHERE t1.a = t2.a;

Now another detail of PostgreSQL enters the stage. Old table rows aren't overwritten, and this is why `ROLLBACK` is fast. In an `UPDATE`, the new result row is inserted into the table (after stripping the CTID) and in the row header of the old row, which the CTID pointed to, the `cmax` and `xmax` entries are set to the current command counter and current transaction ID. Thus the old row is hidden, and after the transaction commits the vacuum cleaner can eventually remove the dead row.

Knowing all that, we can simply apply view rules in absolutely the same way to any command. There is no difference.

### The Power of Views in PostgreSQL

The above demonstrates how the rule system incorporates view definitions into the original query tree. In the second example, a simple `SELECT` from one view created a final query tree that is a join of 4 tables (`unit` was used twice with different names).

The benefit of implementing views with the rule system is that the planner has all the information about which tables have to be scanned plus the relationships between these tables plus the restrictive qualifications from the views plus the qualifications from the original query in one single query tree. And this is still the situation when the original query is already a join over views. The planner has to decide which is the best path to execute the query, and the more information the planner has, the better this decision can be. And the rule system as implemented in PostgreSQL ensures that this is all information available about the query up to that point.

### Updating a View

What happens if a view is named as the target relation for an `INSERT`, `UPDATE`, `DELETE`, or `MERGE`? Doing the substitutions described above would give a query tree in which the result relation points at a subquery range-table entry, which will not work. There are several ways in which PostgreSQL can support the appearance of updating a view, however. In order of user-experienced complexity those are: automatically substitute in the underlying table for the view, execute a user-defined trigger, or rewrite the query per a user-defined rule. These options are discussed below.

If the subquery selects from a single base relation and is simple enough, the rewriter can automatically replace the subquery with the underlying base relation so that the `INSERT`, `UPDATE`, `DELETE`, or `MERGE` is applied to the base relation in the appropriate way. Views that are “simple enough” for this are called automatically updatable. For detailed information on the kinds of view that can be automatically updated, see [???](#sql-createview).

Alternatively, the operation may be handled by a user-provided `INSTEAD OF` trigger on the view (see [???](#sql-createtrigger)). Rewriting works slightly differently in this case. For `INSERT`, the rewriter does nothing at all with the view, leaving it as the result relation for the query. For `UPDATE`, `DELETE`, and `MERGE`, it's still necessary to expand the view query to produce the “old” rows that the command will attempt to update, delete, or merge. So the view is expanded as normal, but another unexpanded range-table entry is added to the query to represent the view in its capacity as the result relation.

The problem that now arises is how to identify the rows to be updated in the view. Recall that when the result relation is a table, a special CTID entry is added to the target list to identify the physical locations of the rows to be updated. This does not work if the result relation is a view, because a view does not have any CTID, since its rows do not have actual physical locations. Instead, for an `UPDATE`, `DELETE`, or `MERGE` operation, a special `wholerow` entry is added to the target list, which expands to include all columns from the view. The executor uses this value to supply the “old” row to the `INSTEAD OF` trigger. It is up to the trigger to work out what to update based on the old and new row values.

Another possibility is for the user to define `INSTEAD` rules that specify substitute actions for `INSERT`, `UPDATE`, and `DELETE` commands on a view. These rules will rewrite the command, typically into a command that updates one or more tables, rather than views. That is the topic of [Rules on , , and ](#rules-update). Note that this will not work with `MERGE`, which currently does not support rules on the target relation other than `SELECT` rules.

Note that rules are evaluated first, rewriting the original query before it is planned and executed. Therefore, if a view has `INSTEAD OF` triggers as well as rules on `INSERT`, `UPDATE`, or `DELETE`, then the rules will be evaluated first, and depending on the result, the triggers may not be used at all.

Automatic rewriting of an `INSERT`, `UPDATE`, `DELETE`, or `MERGE` query on a simple view is always tried last. Therefore, if a view has rules or triggers, they will override the default behavior of automatically updatable views.

If there are no `INSTEAD` rules or `INSTEAD OF` triggers for the view, and the rewriter cannot automatically rewrite the query as an update on the underlying base relation, an error will be thrown because the executor cannot update a view as such.

## Materialized Views

rule

and materialized views

materialized view

implementation through rules

view

materialized

Materialized views in PostgreSQL use the rule system like views do, but persist the results in a table-like form. The main differences between:

    CREATE MATERIALIZED VIEW mymatview AS SELECT * FROM mytab;

and:

    CREATE TABLE mymatview AS SELECT * FROM mytab;

are that the materialized view cannot subsequently be directly updated and that the query used to create the materialized view is stored in exactly the same way that a view's query is stored, so that fresh data can be generated for the materialized view with:

    REFRESH MATERIALIZED VIEW mymatview;

The information about a materialized view in the PostgreSQL system catalogs is exactly the same as it is for a table or view. So for the parser, a materialized view is a relation, just like a table or a view. When a materialized view is referenced in a query, the data is returned directly from the materialized view, like from a table; the rule is only used for populating the materialized view.

While access to the data stored in a materialized view is often much faster than accessing the underlying tables directly or through a view, the data is not always current; yet sometimes current data is not needed. Consider a table which records sales:

    CREATE TABLE invoice (
        invoice_no    integer        PRIMARY KEY,
        seller_no     integer,       -- ID of salesperson
        invoice_date  date,          -- date of sale
        invoice_amt   numeric(13,2)  -- amount of sale
    );

If people want to be able to quickly graph historical sales data, they might want to summarize, and they may not care about the incomplete data for the current date:

    CREATE MATERIALIZED VIEW sales_summary AS
      SELECT
          seller_no,
          invoice_date,
          sum(invoice_amt)::numeric(13,2) as sales_amt
        FROM invoice
        WHERE invoice_date < CURRENT_DATE
        GROUP BY
          seller_no,
          invoice_date;

    CREATE UNIQUE INDEX sales_summary_seller
      ON sales_summary (seller_no, invoice_date);

This materialized view might be useful for displaying a graph in the dashboard created for salespeople. A job could be scheduled to update the statistics each night using this SQL statement:

    REFRESH MATERIALIZED VIEW sales_summary;

Another use for a materialized view is to allow faster access to data brought across from a remote system through a foreign data wrapper. A simple example using `file_fdw` is below, with timings, but since this is using cache on the local system the performance difference compared to access to a remote system would usually be greater than shown here. Notice we are also exploiting the ability to put an index on the materialized view, whereas `file_fdw` does not support indexes; this advantage might not apply for other sorts of foreign data access.

Setup:

    CREATE EXTENSION file_fdw;
    CREATE SERVER local_file FOREIGN DATA WRAPPER file_fdw;
    CREATE FOREIGN TABLE words (word text NOT NULL)
      SERVER local_file
      OPTIONS (filename '/usr/share/dict/words');
    CREATE MATERIALIZED VIEW wrd AS SELECT * FROM words;
    CREATE UNIQUE INDEX wrd_word ON wrd (word);
    CREATE EXTENSION pg_trgm;
    CREATE INDEX wrd_trgm ON wrd USING gist (word gist_trgm_ops);
    VACUUM ANALYZE wrd;

Now let's spell-check a word. Using `file_fdw` directly:

    SELECT count(*) FROM words WHERE word = 'caterpiler';

     count
    -------
         0
    (1 row)

With `EXPLAIN ANALYZE`, we see:

     Aggregate  (cost=21763.99..21764.00 rows=1 width=0) (actual time=188.180..188.181 rows=1 loops=1)
       ->  Foreign Scan on words  (cost=0.00..21761.41 rows=1032 width=0) (actual time=188.177..188.177 rows=0 loops=1)
             Filter: (word = 'caterpiler'::text)
             Rows Removed by Filter: 479829
             Foreign File: /usr/share/dict/words
             Foreign File Size: 4953699
     Planning time: 0.118 ms
     Execution time: 188.273 ms

If the materialized view is used instead, the query is much faster:

     Aggregate  (cost=4.44..4.45 rows=1 width=0) (actual time=0.042..0.042 rows=1 loops=1)
       ->  Index Only Scan using wrd_word on wrd  (cost=0.42..4.44 rows=1 width=0) (actual time=0.039..0.039 rows=0 loops=1)
             Index Cond: (word = 'caterpiler'::text)
             Heap Fetches: 0
     Planning time: 0.164 ms
     Execution time: 0.117 ms

Either way, the word is spelled wrong, so let's look for what we might have wanted. Again using `file_fdw` and `pg_trgm`:

    SELECT word FROM words ORDER BY word <-> 'caterpiler' LIMIT 10;

         word
    ---------------
     cater
     caterpillar
     Caterpillar
     caterpillars
     caterpillar's
     Caterpillar's
     caterer
     caterer's
     caters
     catered
    (10 rows)

     Limit  (cost=11583.61..11583.64 rows=10 width=32) (actual time=1431.591..1431.594 rows=10 loops=1)
       ->  Sort  (cost=11583.61..11804.76 rows=88459 width=32) (actual time=1431.589..1431.591 rows=10 loops=1)
             Sort Key: ((word <-> 'caterpiler'::text))
             Sort Method: top-N heapsort  Memory: 25kB
             ->  Foreign Scan on words  (cost=0.00..9672.05 rows=88459 width=32) (actual time=0.057..1286.455 rows=479829 loops=1)
                   Foreign File: /usr/share/dict/words
                   Foreign File Size: 4953699
     Planning time: 0.128 ms
     Execution time: 1431.679 ms

Using the materialized view:

     Limit  (cost=0.29..1.06 rows=10 width=10) (actual time=187.222..188.257 rows=10 loops=1)
       ->  Index Scan using wrd_trgm on wrd  (cost=0.29..37020.87 rows=479829 width=10) (actual time=187.219..188.252 rows=10 loops=1)
             Order By: (word <-> 'caterpiler'::text)
     Planning time: 0.196 ms
     Execution time: 198.640 ms

If you can tolerate periodic update of the remote data to the local database, the performance benefit can be substantial.

## Rules on `INSERT`, `UPDATE`, and `DELETE`

rule

for INSERT

rule

for UPDATE

rule

for DELETE

Rules that are defined on `INSERT`, `UPDATE`, and `DELETE` are significantly different from the view rules described in the previous sections. First, their `CREATE RULE` command allows more:

- They are allowed to have no action.

- They can have multiple actions.

- They can be `INSTEAD` or `ALSO` (the default).

- The pseudorelations `NEW` and `OLD` become useful.

- They can have rule qualifications.

Second, they don't modify the query tree in place. Instead they create zero or more new query trees and can throw away the original one.

> [!CAUTION]
> In many cases, tasks that could be performed by rules on `INSERT`/`UPDATE`/`DELETE` are better done with triggers. Triggers are notationally a bit more complicated, but their semantics are much simpler to understand. Rules tend to have surprising results when the original query contains volatile functions: volatile functions may get executed more times than expected in the process of carrying out the rules.
>
> Also, there are some cases that are not supported by these types of rules at all, notably including `WITH` clauses in the original query and multiple-assignment sub-`SELECT`s in the `SET` list of `UPDATE` queries. This is because copying these constructs into a rule query would result in multiple evaluations of the sub-query, contrary to the express intent of the query's author.

### How Update Rules Work

Keep the syntax:

    CREATE [ OR REPLACE ] RULE name AS ON event
        TO table [ WHERE condition ]
        DO [ ALSO | INSTEAD ] { NOTHING | command | ( command ; command ... ) }

in mind. In the following, update rules means rules that are defined on `INSERT`, `UPDATE`, or `DELETE`.

Update rules get applied by the rule system when the result relation and the command type of a query tree are equal to the object and event given in the `CREATE RULE` command. For update rules, the rule system creates a list of query trees. Initially the query-tree list is empty. There can be zero (`NOTHING` key word), one, or multiple actions. To simplify, we will look at a rule with one action. This rule can have a qualification or not and it can be `INSTEAD` or `ALSO` (the default).

What is a rule qualification? It is a restriction that tells when the actions of the rule should be done and when not. This qualification can only reference the pseudorelations `NEW` and/or `OLD`, which basically represent the relation that was given as object (but with a special meaning).

So we have three cases that produce the following query trees for a one-action rule.

No qualification, with either `ALSO` or `INSTEAD`  
the query tree from the rule action with the original query tree's qualification added

Qualification given and `ALSO`  
the query tree from the rule action with the rule qualification and the original query tree's qualification added

Qualification given and `INSTEAD`  
the query tree from the rule action with the rule qualification and the original query tree's qualification; and the original query tree with the negated rule qualification added

Finally, if the rule is `ALSO`, the unchanged original query tree is added to the list. Since only qualified `INSTEAD` rules already add the original query tree, we end up with either one or two output query trees for a rule with one action.

For `ON INSERT` rules, the original query (if not suppressed by `INSTEAD`) is done before any actions added by rules. This allows the actions to see the inserted row(s). But for `ON UPDATE` and `ON DELETE` rules, the original query is done after the actions added by rules. This ensures that the actions can see the to-be-updated or to-be-deleted rows; otherwise, the actions might do nothing because they find no rows matching their qualifications.

The query trees generated from rule actions are thrown into the rewrite system again, and maybe more rules get applied resulting in additional or fewer query trees. So a rule's actions must have either a different command type or a different result relation than the rule itself is on, otherwise this recursive process will end up in an infinite loop. (Recursive expansion of a rule will be detected and reported as an error.)

The query trees found in the actions of the pg_rewrite system catalog are only templates. Since they can reference the range-table entries for `NEW` and `OLD`, some substitutions have to be made before they can be used. For any reference to `NEW`, the target list of the original query is searched for a corresponding entry. If found, that entry's expression replaces the reference. Otherwise, `NEW` means the same as `OLD` (for an `UPDATE`) or is replaced by a null value (for an `INSERT`). Any reference to `OLD` is replaced by a reference to the range-table entry that is the result relation.

After the system is done applying update rules, it applies view rules to the produced query tree(s). Views cannot insert new update actions so there is no need to apply update rules to the output of view rewriting.

#### A First Rule Step by Step

Say we want to trace changes to the `sl_avail` column in the `shoelace_data` relation. So we set up a log table and a rule that conditionally writes a log entry when an `UPDATE` is performed on `shoelace_data`.

    CREATE TABLE shoelace_log (
        sl_name    text,          -- shoelace changed
        sl_avail   integer,       -- new available value
        log_who    text,          -- who did it
        log_when   timestamp      -- when
    );

    CREATE RULE log_shoelace AS ON UPDATE TO shoelace_data
        WHERE NEW.sl_avail <> OLD.sl_avail
        DO INSERT INTO shoelace_log VALUES (
                                        NEW.sl_name,
                                        NEW.sl_avail,
                                        current_user,
                                        current_timestamp
                                    );

Now someone does:

    UPDATE shoelace_data SET sl_avail = 6 WHERE sl_name = 'sl7';

and we look at the log table:

    SELECT * FROM shoelace_log;

     sl_name | sl_avail | log_who | log_when
    ---------+----------+---------+----------------------------------
     sl7     |        6 | Al      | Tue Oct 20 16:14:45 1998 MET DST
    (1 row)

That's what we expected. What happened in the background is the following. The parser created the query tree:

    UPDATE shoelace_data SET sl_avail = 6
      FROM shoelace_data shoelace_data
     WHERE shoelace_data.sl_name = 'sl7';

There is a rule `log_shoelace` that is `ON UPDATE` with the rule qualification expression:

    NEW.sl_avail <> OLD.sl_avail

and the action:

    INSERT INTO shoelace_log VALUES (
           new.sl_name, new.sl_avail,
           current_user, current_timestamp )
      FROM shoelace_data new, shoelace_data old;

(This looks a little strange since you cannot normally write `INSERT ... VALUES ... FROM`. The `FROM` clause here is just to indicate that there are range-table entries in the query tree for `new` and `old`. These are needed so that they can be referenced by variables in the `INSERT` command's query tree.)

The rule is a qualified `ALSO` rule, so the rule system has to return two query trees: the modified rule action and the original query tree. In step 1, the range table of the original query is incorporated into the rule's action query tree. This results in:

    INSERT INTO shoelace_log VALUES (
           new.sl_name, new.sl_avail,
           current_user, current_timestamp )
      FROM shoelace_data new, shoelace_data old,
           shoelace_data shoelace_data;

In step 2, the rule qualification is added to it, so the result set is restricted to rows where `sl_avail` changes:

    INSERT INTO shoelace_log VALUES (
           new.sl_name, new.sl_avail,
           current_user, current_timestamp )
      FROM shoelace_data new, shoelace_data old,
           shoelace_data shoelace_data
     WHERE new.sl_avail <> old.sl_avail;

(This looks even stranger, since `INSERT ... VALUES` doesn't have a `WHERE` clause either, but the planner and executor will have no difficulty with it. They need to support this same functionality anyway for `INSERT ... SELECT`.)

In step 3, the original query tree's qualification is added, restricting the result set further to only the rows that would have been touched by the original query:

    INSERT INTO shoelace_log VALUES (
           new.sl_name, new.sl_avail,
           current_user, current_timestamp )
      FROM shoelace_data new, shoelace_data old,
           shoelace_data shoelace_data
     WHERE new.sl_avail <> old.sl_avail
       AND shoelace_data.sl_name = 'sl7';

Step 4 replaces references to `NEW` by the target list entries from the original query tree or by the matching variable references from the result relation:

    INSERT INTO shoelace_log VALUES (
           shoelace_data.sl_name, 6,
           current_user, current_timestamp )
      FROM shoelace_data new, shoelace_data old,
           shoelace_data shoelace_data
     WHERE 6 <> old.sl_avail
       AND shoelace_data.sl_name = 'sl7';

Step 5 changes `OLD` references into result relation references:

    INSERT INTO shoelace_log VALUES (
           shoelace_data.sl_name, 6,
           current_user, current_timestamp )
      FROM shoelace_data new, shoelace_data old,
           shoelace_data shoelace_data
     WHERE 6 <> shoelace_data.sl_avail
       AND shoelace_data.sl_name = 'sl7';

That's it. Since the rule is `ALSO`, we also output the original query tree. In short, the output from the rule system is a list of two query trees that correspond to these statements:

    INSERT INTO shoelace_log VALUES (
           shoelace_data.sl_name, 6,
           current_user, current_timestamp )
      FROM shoelace_data
     WHERE 6 <> shoelace_data.sl_avail
       AND shoelace_data.sl_name = 'sl7';

    UPDATE shoelace_data SET sl_avail = 6
     WHERE sl_name = 'sl7';

These are executed in this order, and that is exactly what the rule was meant to do.

The substitutions and the added qualifications ensure that, if the original query would be, say:

    UPDATE shoelace_data SET sl_color = 'green'
     WHERE sl_name = 'sl7';

no log entry would get written. In that case, the original query tree does not contain a target list entry for `sl_avail`, so `NEW.sl_avail` will get replaced by `shoelace_data.sl_avail`. Thus, the extra command generated by the rule is:

    INSERT INTO shoelace_log VALUES (
           shoelace_data.sl_name, shoelace_data.sl_avail,
           current_user, current_timestamp )
      FROM shoelace_data
     WHERE shoelace_data.sl_avail <> shoelace_data.sl_avail
       AND shoelace_data.sl_name = 'sl7';

and that qualification will never be true.

It will also work if the original query modifies multiple rows. So if someone issued the command:

    UPDATE shoelace_data SET sl_avail = 0
     WHERE sl_color = 'black';

four rows in fact get updated (`sl1`, `sl2`, `sl3`, and `sl4`). But `sl3` already has `sl_avail = 0`. In this case, the original query trees qualification is different and that results in the extra query tree:

    INSERT INTO shoelace_log
    SELECT shoelace_data.sl_name, 0,
           current_user, current_timestamp
      FROM shoelace_data
     WHERE 0 <> shoelace_data.sl_avail
       AND shoelace_data.sl_color = 'black';

being generated by the rule. This query tree will surely insert three new log entries. And that's absolutely correct.

Here we can see why it is important that the original query tree is executed last. If the `UPDATE` had been executed first, all the rows would have already been set to zero, so the logging `INSERT` would not find any row where `0 <> shoelace_data.sl_avail`.

### Cooperation with Views

view

updating

A simple way to protect view relations from the mentioned possibility that someone can try to run `INSERT`, `UPDATE`, or `DELETE` on them is to let those query trees get thrown away. So we could create the rules:

    CREATE RULE shoe_ins_protect AS ON INSERT TO shoe
        DO INSTEAD NOTHING;
    CREATE RULE shoe_upd_protect AS ON UPDATE TO shoe
        DO INSTEAD NOTHING;
    CREATE RULE shoe_del_protect AS ON DELETE TO shoe
        DO INSTEAD NOTHING;

If someone now tries to do any of these operations on the view relation `shoe`, the rule system will apply these rules. Since the rules have no actions and are `INSTEAD`, the resulting list of query trees will be empty and the whole query will become nothing because there is nothing left to be optimized or executed after the rule system is done with it.

A more sophisticated way to use the rule system is to create rules that rewrite the query tree into one that does the right operation on the real tables. To do that on the `shoelace` view, we create the following rules:

    CREATE RULE shoelace_ins AS ON INSERT TO shoelace
        DO INSTEAD
        INSERT INTO shoelace_data VALUES (
               NEW.sl_name,
               NEW.sl_avail,
               NEW.sl_color,
               NEW.sl_len,
               NEW.sl_unit
        );

    CREATE RULE shoelace_upd AS ON UPDATE TO shoelace
        DO INSTEAD
        UPDATE shoelace_data
           SET sl_name = NEW.sl_name,
               sl_avail = NEW.sl_avail,
               sl_color = NEW.sl_color,
               sl_len = NEW.sl_len,
               sl_unit = NEW.sl_unit
         WHERE sl_name = OLD.sl_name;

    CREATE RULE shoelace_del AS ON DELETE TO shoelace
        DO INSTEAD
        DELETE FROM shoelace_data
         WHERE sl_name = OLD.sl_name;

If you want to support `RETURNING` queries on the view, you need to make the rules include `RETURNING` clauses that compute the view rows. This is usually pretty trivial for views on a single table, but it's a bit tedious for join views such as `shoelace`. An example for the insert case is:

    CREATE RULE shoelace_ins AS ON INSERT TO shoelace
        DO INSTEAD
        INSERT INTO shoelace_data VALUES (
               NEW.sl_name,
               NEW.sl_avail,
               NEW.sl_color,
               NEW.sl_len,
               NEW.sl_unit
        )
        RETURNING
               shoelace_data.*,
               (SELECT shoelace_data.sl_len * u.un_fact
                FROM unit u WHERE shoelace_data.sl_unit = u.un_name);

Note that this one rule supports both `INSERT` and `INSERT RETURNING` queries on the view the `RETURNING` clause is simply ignored for `INSERT`.

Now assume that once in a while, a pack of shoelaces arrives at the shop and a big parts list along with it. But you don't want to manually update the `shoelace` view every time. Instead we set up two little tables: one where you can insert the items from the part list, and one with a special trick. The creation commands for these are:

    CREATE TABLE shoelace_arrive (
        arr_name    text,
        arr_quant   integer
    );

    CREATE TABLE shoelace_ok (
        ok_name     text,
        ok_quant    integer
    );

    CREATE RULE shoelace_ok_ins AS ON INSERT TO shoelace_ok
        DO INSTEAD
        UPDATE shoelace
           SET sl_avail = sl_avail + NEW.ok_quant
         WHERE sl_name = NEW.ok_name;

Now you can fill the table `shoelace_arrive` with the data from the parts list:

    SELECT * FROM shoelace_arrive;

     arr_name | arr_quant
    ----------+-----------
     sl3      |        10
     sl6      |        20
     sl8      |        20
    (3 rows)

Take a quick look at the current data:

    SELECT * FROM shoelace;

     sl_name  | sl_avail | sl_color | sl_len | sl_unit | sl_len_cm
    ----------+----------+----------+--------+---------+-----------
     sl1      |        5 | black    |     80 | cm      |        80
     sl2      |        6 | black    |    100 | cm      |       100
     sl7      |        6 | brown    |     60 | cm      |        60
     sl3      |        0 | black    |     35 | inch    |      88.9
     sl4      |        8 | black    |     40 | inch    |     101.6
     sl8      |        1 | brown    |     40 | inch    |     101.6
     sl5      |        4 | brown    |      1 | m       |       100
     sl6      |        0 | brown    |    0.9 | m       |        90
    (8 rows)

Now move the arrived shoelaces in:

    INSERT INTO shoelace_ok SELECT * FROM shoelace_arrive;

and check the results:

    SELECT * FROM shoelace ORDER BY sl_name;

     sl_name  | sl_avail | sl_color | sl_len | sl_unit | sl_len_cm
    ----------+----------+----------+--------+---------+-----------
     sl1      |        5 | black    |     80 | cm      |        80
     sl2      |        6 | black    |    100 | cm      |       100
     sl7      |        6 | brown    |     60 | cm      |        60
     sl4      |        8 | black    |     40 | inch    |     101.6
     sl3      |       10 | black    |     35 | inch    |      88.9
     sl8      |       21 | brown    |     40 | inch    |     101.6
     sl5      |        4 | brown    |      1 | m       |       100
     sl6      |       20 | brown    |    0.9 | m       |        90
    (8 rows)

    SELECT * FROM shoelace_log;

     sl_name | sl_avail | log_who| log_when
    ---------+----------+--------+----------------------------------
     sl7     |        6 | Al     | Tue Oct 20 19:14:45 1998 MET DST
     sl3     |       10 | Al     | Tue Oct 20 19:25:16 1998 MET DST
     sl6     |       20 | Al     | Tue Oct 20 19:25:16 1998 MET DST
     sl8     |       21 | Al     | Tue Oct 20 19:25:16 1998 MET DST
    (4 rows)

It's a long way from the one `INSERT ... SELECT` to these results. And the description of the query-tree transformation will be the last in this chapter. First, there is the parser's output:

    INSERT INTO shoelace_ok
    SELECT shoelace_arrive.arr_name, shoelace_arrive.arr_quant
      FROM shoelace_arrive shoelace_arrive, shoelace_ok shoelace_ok;

Now the first rule `shoelace_ok_ins` is applied and turns this into:

    UPDATE shoelace
       SET sl_avail = shoelace.sl_avail + shoelace_arrive.arr_quant
      FROM shoelace_arrive shoelace_arrive, shoelace_ok shoelace_ok,
           shoelace_ok old, shoelace_ok new,
           shoelace shoelace
     WHERE shoelace.sl_name = shoelace_arrive.arr_name;

and throws away the original `INSERT` on `shoelace_ok`. This rewritten query is passed to the rule system again, and the second applied rule `shoelace_upd` produces:

    UPDATE shoelace_data
       SET sl_name = shoelace.sl_name,
           sl_avail = shoelace.sl_avail + shoelace_arrive.arr_quant,
           sl_color = shoelace.sl_color,
           sl_len = shoelace.sl_len,
           sl_unit = shoelace.sl_unit
      FROM shoelace_arrive shoelace_arrive, shoelace_ok shoelace_ok,
           shoelace_ok old, shoelace_ok new,
           shoelace shoelace, shoelace old,
           shoelace new, shoelace_data shoelace_data
     WHERE shoelace.sl_name = shoelace_arrive.arr_name
       AND shoelace_data.sl_name = shoelace.sl_name;

Again it's an `INSTEAD` rule and the previous query tree is trashed. Note that this query still uses the view `shoelace`. But the rule system isn't finished with this step, so it continues and applies the `_RETURN` rule on it, and we get:

    UPDATE shoelace_data
       SET sl_name = s.sl_name,
           sl_avail = s.sl_avail + shoelace_arrive.arr_quant,
           sl_color = s.sl_color,
           sl_len = s.sl_len,
           sl_unit = s.sl_unit
      FROM shoelace_arrive shoelace_arrive, shoelace_ok shoelace_ok,
           shoelace_ok old, shoelace_ok new,
           shoelace shoelace, shoelace old,
           shoelace new, shoelace_data shoelace_data,
           shoelace old, shoelace new,
           shoelace_data s, unit u
     WHERE s.sl_name = shoelace_arrive.arr_name
       AND shoelace_data.sl_name = s.sl_name;

Finally, the rule `log_shoelace` gets applied, producing the extra query tree:

    INSERT INTO shoelace_log
    SELECT s.sl_name,
           s.sl_avail + shoelace_arrive.arr_quant,
           current_user,
           current_timestamp
      FROM shoelace_arrive shoelace_arrive, shoelace_ok shoelace_ok,
           shoelace_ok old, shoelace_ok new,
           shoelace shoelace, shoelace old,
           shoelace new, shoelace_data shoelace_data,
           shoelace old, shoelace new,
           shoelace_data s, unit u,
           shoelace_data old, shoelace_data new
           shoelace_log shoelace_log
     WHERE s.sl_name = shoelace_arrive.arr_name
       AND shoelace_data.sl_name = s.sl_name
       AND (s.sl_avail + shoelace_arrive.arr_quant) <> s.sl_avail;

After that the rule system runs out of rules and returns the generated query trees.

So we end up with two final query trees that are equivalent to the SQL statements:

    INSERT INTO shoelace_log
    SELECT s.sl_name,
           s.sl_avail + shoelace_arrive.arr_quant,
           current_user,
           current_timestamp
      FROM shoelace_arrive shoelace_arrive, shoelace_data shoelace_data,
           shoelace_data s
     WHERE s.sl_name = shoelace_arrive.arr_name
       AND shoelace_data.sl_name = s.sl_name
       AND s.sl_avail + shoelace_arrive.arr_quant <> s.sl_avail;

    UPDATE shoelace_data
       SET sl_avail = shoelace_data.sl_avail + shoelace_arrive.arr_quant
      FROM shoelace_arrive shoelace_arrive,
           shoelace_data shoelace_data,
           shoelace_data s
     WHERE s.sl_name = shoelace_arrive.sl_name
       AND shoelace_data.sl_name = s.sl_name;

The result is that data coming from one relation inserted into another, changed into updates on a third, changed into updating a fourth plus logging that final update in a fifth gets reduced into two queries.

There is a little detail that's a bit ugly. Looking at the two queries, it turns out that the `shoelace_data` relation appears twice in the range table where it could definitely be reduced to one. The planner does not handle it and so the execution plan for the rule systems output of the `INSERT` will be

    Nested Loop
      ->  Merge Join
            ->  Seq Scan
                  ->  Sort
                        ->  Seq Scan on s
            ->  Seq Scan
                  ->  Sort
                        ->  Seq Scan on shoelace_arrive
      ->  Seq Scan on shoelace_data

while omitting the extra range table entry would result in a

    Merge Join
      ->  Seq Scan
            ->  Sort
                  ->  Seq Scan on s
      ->  Seq Scan
            ->  Sort
                  ->  Seq Scan on shoelace_arrive

which produces exactly the same entries in the log table. Thus, the rule system caused one extra scan on the table `shoelace_data` that is absolutely not necessary. And the same redundant scan is done once more in the `UPDATE`. But it was a really hard job to make that all possible at all.

Now we make a final demonstration of the PostgreSQL rule system and its power. Say you add some shoelaces with extraordinary colors to your database:

    INSERT INTO shoelace VALUES ('sl9', 0, 'pink', 35.0, 'inch', 0.0);
    INSERT INTO shoelace VALUES ('sl10', 1000, 'magenta', 40.0, 'inch', 0.0);

We would like to make a view to check which `shoelace` entries do not fit any shoe in color. The view for this is:

    CREATE VIEW shoelace_mismatch AS
        SELECT * FROM shoelace WHERE NOT EXISTS
            (SELECT shoename FROM shoe WHERE slcolor = sl_color);

Its output is:

    SELECT * FROM shoelace_mismatch;

     sl_name | sl_avail | sl_color | sl_len | sl_unit | sl_len_cm
    ---------+----------+----------+--------+---------+-----------
     sl9     |        0 | pink     |     35 | inch    |      88.9
     sl10    |     1000 | magenta  |     40 | inch    |     101.6

Now we want to set it up so that mismatching shoelaces that are not in stock are deleted from the database. To make it a little harder for PostgreSQL, we don't delete it directly. Instead we create one more view:

    CREATE VIEW shoelace_can_delete AS
        SELECT * FROM shoelace_mismatch WHERE sl_avail = 0;

and do it this way:

    DELETE FROM shoelace WHERE EXISTS
        (SELECT * FROM shoelace_can_delete
                 WHERE sl_name = shoelace.sl_name);

The results are:

    SELECT * FROM shoelace;

     sl_name | sl_avail | sl_color | sl_len | sl_unit | sl_len_cm
    ---------+----------+----------+--------+---------+-----------
     sl1     |        5 | black    |     80 | cm      |        80
     sl2     |        6 | black    |    100 | cm      |       100
     sl7     |        6 | brown    |     60 | cm      |        60
     sl4     |        8 | black    |     40 | inch    |     101.6
     sl3     |       10 | black    |     35 | inch    |      88.9
     sl8     |       21 | brown    |     40 | inch    |     101.6
     sl10    |     1000 | magenta  |     40 | inch    |     101.6
     sl5     |        4 | brown    |      1 | m       |       100
     sl6     |       20 | brown    |    0.9 | m       |        90
    (9 rows)

A `DELETE` on a view, with a subquery qualification that in total uses 4 nesting/joined views, where one of them itself has a subquery qualification containing a view and where calculated view columns are used, gets rewritten into one single query tree that deletes the requested data from a real table.

There are probably only a few situations out in the real world where such a construct is necessary. But it makes you feel comfortable that it works.

## Rules and Privileges

privilege

with rules

privilege

with views

Due to rewriting of queries by the PostgreSQL rule system, other tables/views than those used in the original query get accessed. When update rules are used, this can include write access to tables.

Rewrite rules don't have a separate owner. The owner of a relation (table or view) is automatically the owner of the rewrite rules that are defined for it. The PostgreSQL rule system changes the behavior of the default access control system. With the exception of `SELECT` rules associated with security invoker views (see [`CREATE VIEW`](#sql-createview)), all relations that are used due to rules get checked against the privileges of the rule owner, not the user invoking the rule. This means that, except for security invoker views, users only need the required privileges for the tables/views that are explicitly named in their queries.

For example: A user has a list of phone numbers where some of them are private, the others are of interest for the assistant of the office. The user can construct the following:

    CREATE TABLE phone_data (person text, phone text, private boolean);
    CREATE VIEW phone_number AS
        SELECT person, CASE WHEN NOT private THEN phone END AS phone
        FROM phone_data;
    GRANT SELECT ON phone_number TO assistant;

Nobody except that user (and the database superusers) can access the `phone_data` table. But because of the `GRANT`, the assistant can run a `SELECT` on the `phone_number` view. The rule system will rewrite the `SELECT` from `phone_number` into a `SELECT` from `phone_data`. Since the user is the owner of `phone_number` and therefore the owner of the rule, the read access to `phone_data` is now checked against the user's privileges and the query is permitted. The check for accessing `phone_number` is also performed, but this is done against the invoking user, so nobody but the user and the assistant can use it.

The privileges are checked rule by rule. So the assistant is for now the only one who can see the public phone numbers. But the assistant can set up another view and grant access to that to the public. Then, anyone can see the `phone_number` data through the assistant's view. What the assistant cannot do is to create a view that directly accesses `phone_data`. (Actually the assistant can, but it will not work since every access will be denied during the permission checks.) And as soon as the user notices that the assistant opened their `phone_number` view, the user can revoke the assistant's access. Immediately, any access to the assistant's view would fail.

One might think that this rule-by-rule checking is a security hole, but in fact it isn't. But if it did not work this way, the assistant could set up a table with the same columns as `phone_number` and copy the data to there once per day. Then it's the assistant's own data and the assistant can grant access to everyone they want. A `GRANT` command means, “I trust you”. If someone you trust does the thing above, it's time to think it over and then use `REVOKE`.

Note that while views can be used to hide the contents of certain columns using the technique shown above, they cannot be used to reliably conceal the data in unseen rows unless the `security_barrier` flag has been set. For example, the following view is insecure:

    CREATE VIEW phone_number AS
        SELECT person, phone FROM phone_data WHERE phone NOT LIKE '412%';

This view might seem secure, since the rule system will rewrite any `SELECT` from `phone_number` into a `SELECT` from `phone_data` and add the qualification that only entries where `phone` does not begin with 412 are wanted. But if the user can create their own functions, it is not difficult to convince the planner to execute the user-defined function prior to the `NOT LIKE` expression. For example:

    CREATE FUNCTION tricky(text, text) RETURNS bool AS $$
    BEGIN
        RAISE NOTICE '% => %', $1, $2;
        RETURN true;
    END;
    $$ LANGUAGE plpgsql COST 0.0000000000000000000001;

    SELECT * FROM phone_number WHERE tricky(person, phone);

Every person and phone number in the `phone_data` table will be printed as a `NOTICE`, because the planner will choose to execute the inexpensive `tricky` function before the more expensive `NOT LIKE`. Even if the user is prevented from defining new functions, built-in functions can be used in similar attacks. (For example, most casting functions include their input values in the error messages they produce.)

Similar considerations apply to update rules. In the examples of the previous section, the owner of the tables in the example database could grant the privileges `SELECT`, `INSERT`, `UPDATE`, and `DELETE` on the `shoelace` view to someone else, but only `SELECT` on `shoelace_log`. The rule action to write log entries will still be executed successfully, and that other user could see the log entries. But they could not create fake entries, nor could they manipulate or remove existing ones. In this case, there is no possibility of subverting the rules by convincing the planner to alter the order of operations, because the only rule which references `shoelace_log` is an unqualified `INSERT`. This might not be true in more complex scenarios.

When it is necessary for a view to provide row-level security, the `security_barrier` attribute should be applied to the view. This prevents maliciously-chosen functions and operators from being passed values from rows until after the view has done its work. For example, if the view shown above had been created like this, it would be secure:

    CREATE VIEW phone_number WITH (security_barrier) AS
        SELECT person, phone FROM phone_data WHERE phone NOT LIKE '412%';

Views created with the `security_barrier` may perform far worse than views created without this option. In general, there is no way to avoid this: the fastest possible plan must be rejected if it may compromise security. For this reason, this option is not enabled by default.

The query planner has more flexibility when dealing with functions that have no side effects. Such functions are referred to as `LEAKPROOF`, and include many simple, commonly used operators, such as many equality operators. The query planner can safely allow such functions to be evaluated at any point in the query execution process, since invoking them on rows invisible to the user will not leak any information about the unseen rows. Further, functions which do not take arguments or which are not passed any arguments from the security barrier view do not have to be marked as `LEAKPROOF` to be pushed down, as they never receive data from the view. In contrast, a function that might throw an error depending on the values received as arguments (such as one that throws an error in the event of overflow or division by zero) is not leak-proof, and could provide significant information about the unseen rows if applied before the security view's row filters.

It is important to understand that even a view created with the `security_barrier` option is intended to be secure only in the limited sense that the contents of the invisible tuples will not be passed to possibly-insecure functions. The user may well have other means of making inferences about the unseen data; for example, they can see the query plan using `EXPLAIN`, or measure the run time of queries against the view. A malicious attacker might be able to infer something about the amount of unseen data, or even gain some information about the data distribution or most common values (since these things may affect the run time of the plan; or even, since they are also reflected in the optimizer statistics, the choice of plan). If these types of "covert channel" attacks are of concern, it is probably unwise to grant any access to the data at all.

## Rules and Command Status

The PostgreSQL server returns a command status string, such as `INSERT 149592 1`, for each command it receives. This is simple enough when there are no rules involved, but what happens when the query is rewritten by rules?

Rules affect the command status as follows:

- If there is no unconditional `INSTEAD` rule for the query, then the originally given query will be executed, and its command status will be returned as usual. (But note that if there were any conditional `INSTEAD` rules, the negation of their qualifications will have been added to the original query. This might reduce the number of rows it processes, and if so the reported status will be affected.)

- If there is any unconditional `INSTEAD` rule for the query, then the original query will not be executed at all. In this case, the server will return the command status for the last query that was inserted by an `INSTEAD` rule (conditional or unconditional) and is of the same command type (`INSERT`, `UPDATE`, or `DELETE`) as the original query. If no query meeting those requirements is added by any rule, then the returned command status shows the original query type and zeroes for the row-count and OID fields.

The programmer can ensure that any desired `INSTEAD` rule is the one that sets the command status in the second case, by giving it the alphabetically last rule name among the active rules, so that it gets applied last.

## Rules Versus Triggers

rule

compared with triggers

trigger

compared with rules

Many things that can be done using triggers can also be implemented using the PostgreSQL rule system. One of the things that cannot be implemented by rules are some kinds of constraints, especially foreign keys. It is possible to place a qualified rule that rewrites a command to `NOTHING` if the value of a column does not appear in another table. But then the data is silently thrown away and that's not a good idea. If checks for valid values are required, and in the case of an invalid value an error message should be generated, it must be done by a trigger.

In this chapter, we focused on using rules to update views. All of the update rule examples in this chapter can also be implemented using `INSTEAD OF` triggers on the views. Writing such triggers is often easier than writing rules, particularly if complex logic is required to perform the update.

For the things that can be implemented by both, which is best depends on the usage of the database. A trigger is fired once for each affected row. A rule modifies the query or generates an additional query. So if many rows are affected in one statement, a rule issuing one extra command is likely to be faster than a trigger that is called for every single row and must re-determine what to do many times. However, the trigger approach is conceptually far simpler than the rule approach, and is easier for novices to get right.

Here we show an example of how the choice of rules versus triggers plays out in one situation. There are two tables:

    CREATE TABLE computer (
        hostname        text,    -- indexed
        manufacturer    text     -- indexed
    );

    CREATE TABLE software (
        software        text,    -- indexed
        hostname        text     -- indexed
    );

Both tables have many thousands of rows and the indexes on hostname are unique. The rule or trigger should implement a constraint that deletes rows from `software` that reference a deleted computer. The trigger would use this command:

    DELETE FROM software WHERE hostname = $1;

Since the trigger is called for each individual row deleted from `computer`, it can prepare and save the plan for this command and pass the hostname value in the parameter. The rule would be written as:

    CREATE RULE computer_del AS ON DELETE TO computer
        DO DELETE FROM software WHERE hostname = OLD.hostname;

Now we look at different types of deletes. In the case of a:

    DELETE FROM computer WHERE hostname = 'mypc.local.net';

the table `computer` is scanned by index (fast), and the command issued by the trigger would also use an index scan (also fast). The extra command from the rule would be:

    DELETE FROM software WHERE computer.hostname = 'mypc.local.net'
                           AND software.hostname = computer.hostname;

Since there are appropriate indexes set up, the planner will create a plan of

    Nestloop
      ->  Index Scan using comp_hostidx on computer
      ->  Index Scan using soft_hostidx on software

So there would be not that much difference in speed between the trigger and the rule implementation.

With the next delete we want to get rid of all the 2000 computers where the hostname starts with `old`. There are two possible commands to do that. One is:

    DELETE FROM computer WHERE hostname >= 'old'
                           AND hostname <  'ole'

The command added by the rule will be:

    DELETE FROM software WHERE computer.hostname >= 'old' AND computer.hostname < 'ole'
                           AND software.hostname = computer.hostname;

with the plan

    Hash Join
      ->  Seq Scan on software
      ->  Hash
        ->  Index Scan using comp_hostidx on computer

The other possible command is:

    DELETE FROM computer WHERE hostname ~ '^old';

which results in the following executing plan for the command added by the rule:

    Nestloop
      ->  Index Scan using comp_hostidx on computer
      ->  Index Scan using soft_hostidx on software

This shows, that the planner does not realize that the qualification for hostname in `computer` could also be used for an index scan on `software` when there are multiple qualification expressions combined with `AND`, which is what it does in the regular-expression version of the command. The trigger will get invoked once for each of the 2000 old computers that have to be deleted, and that will result in one index scan over `computer` and 2000 index scans over `software`. The rule implementation will do it with two commands that use indexes. And it depends on the overall size of the table `software` whether the rule will still be faster in the sequential scan situation. 2000 command executions from the trigger over the SPI manager take some time, even if all the index blocks will soon be in the cache.

The last command we look at is:

    DELETE FROM computer WHERE manufacturer = 'bim';

Again this could result in many rows to be deleted from `computer`. So the trigger will again run many commands through the executor. The command generated by the rule will be:

    DELETE FROM software WHERE computer.manufacturer = 'bim'
                           AND software.hostname = computer.hostname;

The plan for that command will again be the nested loop over two index scans, only using a different index on `computer`:

    Nestloop
      ->  Index Scan using comp_manufidx on computer
      ->  Index Scan using soft_hostidx on software

In any of these cases, the extra commands from the rule system will be more or less independent from the number of affected rows in a command.

The summary is, rules will only be significantly slower than triggers if their actions result in large and badly qualified joins, a situation where the planner fails.
