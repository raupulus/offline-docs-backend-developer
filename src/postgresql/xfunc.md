---
title: User-Defined Functions
source_url: https://www.postgresql.org/docs/17/xfunc.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: xfunc.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 3790
---

## User-Defined Functions

function

user-defined

PostgreSQL provides four kinds of functions:

- query language functions (functions written in SQL) ([Query Language () Functions](#xfunc-sql))

- procedural language functions (functions written in, for example, PL/pgSQL or PL/Tcl) ([Procedural Language Functions](#xfunc-pl))

- internal functions ([Internal Functions](#xfunc-internal))

- C-language functions ([C-Language Functions](#xfunc-c))

Every kind of function can take base types, composite types, or combinations of these as arguments (parameters). In addition, every kind of function can return a base type or a composite type. Functions can also be defined to return sets of base or composite values.

Many kinds of functions can take or return certain pseudo-types (such as polymorphic types), but the available facilities vary. Consult the description of each kind of function for more details.

It's easiest to define SQL functions, so we'll start by discussing those. Most of the concepts presented for SQL functions will carry over to the other types of functions.

Throughout this chapter, it can be useful to look at the reference page of the [`CREATE FUNCTION`](#sql-createfunction) command to understand the examples better. Some examples from this chapter can be found in `funcs.sql` and `funcs.c` in the `src/tutorial` directory in the PostgreSQL source distribution.

## User-Defined Procedures

procedure

user-defined

A procedure is a database object similar to a function. The key differences are:

- Procedures are defined with the [`CREATE PROCEDURE`](#sql-createprocedure) command, not `CREATE FUNCTION`.

- Procedures do not return a function value; hence `CREATE PROCEDURE` lacks a `RETURNS` clause. However, procedures can instead return data to their callers via output parameters.

- While a function is called as part of a query or DML command, a procedure is called in isolation using the [`CALL`](#sql-call) command.

- A procedure can commit or roll back transactions during its execution (then automatically beginning a new transaction), so long as the invoking `CALL` command is not part of an explicit transaction block. A function cannot do that.

- Certain function attributes, such as strictness, don't apply to procedures. Those attributes control how the function is used in a query, which isn't relevant to procedures.

The explanations in the following sections about how to define user-defined functions apply to procedures as well, except for the points made above.

Collectively, functions and procedures are also known as routines<span class="indexterm"></span>. There are commands such as [`ALTER ROUTINE`](#sql-alterroutine) and [`DROP ROUTINE`](#sql-droproutine) that can operate on functions and procedures without having to know which kind it is. Note, however, that there is no `CREATE ROUTINE` command.

## Query Language (SQL) Functions

function

user-defined

in SQL

SQL functions execute an arbitrary list of SQL statements, returning the result of the last query in the list. In the simple (non-set) case, the first row of the last query's result will be returned. (Bear in mind that “the first row” of a multirow result is not well-defined unless you use `ORDER BY`.) If the last query happens to return no rows at all, the null value will be returned.

Alternatively, an SQL function can be declared to return a set (that is, multiple rows) by specifying the function's return type as `SETOF sometype`, or equivalently by declaring it as `RETURNS TABLE(columns)`. In this case all rows of the last query's result are returned. Further details appear below.

The body of an SQL function must be a list of SQL statements separated by semicolons. A semicolon after the last statement is optional. Unless the function is declared to return `void`, the last statement must be a `SELECT`, or an `INSERT`, `UPDATE`, `DELETE`, or `MERGE` that has a `RETURNING` clause.

Any collection of commands in the SQL language can be packaged together and defined as a function. Besides `SELECT` queries, the commands can include data modification queries (`INSERT`, `UPDATE`, `DELETE`, and `MERGE`), as well as other SQL commands. (You cannot use transaction control commands, e.g., `COMMIT`, `SAVEPOINT`, and some utility commands, e.g., `VACUUM`, in SQL functions.) However, the final command must be a `SELECT` or have a `RETURNING` clause that returns whatever is specified as the function's return type. Alternatively, if you want to define an SQL function that performs actions but has no useful value to return, you can define it as returning `void`. For example, this function removes rows with negative salaries from the `emp` table:

    CREATE FUNCTION clean_emp() RETURNS void AS '
        DELETE FROM emp
            WHERE salary < 0;
    ' LANGUAGE SQL;

    SELECT clean_emp();

     clean_emp
    -----------

    (1 row)

You can also write this as a procedure, thus avoiding the issue of the return type. For example:

    CREATE PROCEDURE clean_emp() AS '
        DELETE FROM emp
            WHERE salary < 0;
    ' LANGUAGE SQL;

    CALL clean_emp();

In simple cases like this, the difference between a function returning `void` and a procedure is mostly stylistic. However, procedures offer additional functionality such as transaction control that is not available in functions. Also, procedures are SQL standard whereas returning `void` is a PostgreSQL extension.

> [!NOTE]
> The entire body of an SQL function is parsed before any of it is executed. While an SQL function can contain commands that alter the system catalogs (e.g., `CREATE TABLE`), the effects of such commands will not be visible during parse analysis of later commands in the function. Thus, for example, `CREATE TABLE foo (...); INSERT INTO foo VALUES(...);` will not work as desired if packaged up into a single SQL function, since foo won't exist yet when the `INSERT` command is parsed. It's recommended to use PL/pgSQL instead of an SQL function in this type of situation.

The syntax of the `CREATE FUNCTION` command requires the function body to be written as a string constant. It is usually most convenient to use dollar quoting (see [???](#sql-syntax-dollar-quoting)) for the string constant. If you choose to use regular single-quoted string constant syntax, you must double single quote marks (`'`) and backslashes (`\`) (assuming escape string syntax) in the body of the function (see [???](#sql-syntax-strings)).

## Arguments for SQL Functions

function

named argument

Arguments of an SQL function can be referenced in the function body using either names or numbers. Examples of both methods appear below.

To use a name, declare the function argument as having a name, and then just write that name in the function body. If the argument name is the same as any column name in the current SQL command within the function, the column name will take precedence. To override this, qualify the argument name with the name of the function itself, that is `function_name.argument_name`. (If this would conflict with a qualified column name, again the column name wins. You can avoid the ambiguity by choosing a different alias for the table within the SQL command.)

In the older numeric approach, arguments are referenced using the syntax `$n`: `$1` refers to the first input argument, `$2` to the second, and so on. This will work whether or not the particular argument was declared with a name.

If an argument is of a composite type, then the dot notation, e.g., `argname.fieldname` or `$1.fieldname`, can be used to access attributes of the argument. Again, you might need to qualify the argument's name with the function name to make the form with an argument name unambiguous.

SQL function arguments can only be used as data values, not as identifiers. Thus for example this is reasonable:

    INSERT INTO mytable VALUES ($1);

but this will not work:

    INSERT INTO $1 VALUES (42);

> [!NOTE]
> The ability to use names to reference SQL function arguments was added in PostgreSQL 9.2. Functions to be used in older servers must use the `$n` notation.

## SQL Functions on Base Types

The simplest possible SQL function has no arguments and simply returns a base type, such as `integer`:

    CREATE FUNCTION one() RETURNS integer AS $$
        SELECT 1 AS result;
    $$ LANGUAGE SQL;

    -- Alternative syntax for string literal:
    CREATE FUNCTION one() RETURNS integer AS '
        SELECT 1 AS result;
    ' LANGUAGE SQL;

    SELECT one();

     one
    -----
       1

Notice that we defined a column alias within the function body for the result of the function (with the name `result`), but this column alias is not visible outside the function. Hence, the result is labeled `one` instead of `result`.

It is almost as easy to define SQL functions that take base types as arguments:

    CREATE FUNCTION add_em(x integer, y integer) RETURNS integer AS $$
        SELECT x + y;
    $$ LANGUAGE SQL;

    SELECT add_em(1, 2) AS answer;

     answer
    --------
          3

Alternatively, we could dispense with names for the arguments and use numbers:

    CREATE FUNCTION add_em(integer, integer) RETURNS integer AS $$
        SELECT $1 + $2;
    $$ LANGUAGE SQL;

    SELECT add_em(1, 2) AS answer;

     answer
    --------
          3

Here is a more useful function, which might be used to debit a bank account:

    CREATE FUNCTION tf1 (accountno integer, debit numeric) RETURNS numeric AS $$
        UPDATE bank
            SET balance = balance - debit
            WHERE accountno = tf1.accountno;
        SELECT 1;
    $$ LANGUAGE SQL;

A user could execute this function to debit account 17 by \$100.00 as follows:

    SELECT tf1(17, 100.0);

In this example, we chose the name `accountno` for the first argument, but this is the same as the name of a column in the `bank` table. Within the `UPDATE` command, `accountno` refers to the column `bank.accountno`, so `tf1.accountno` must be used to refer to the argument. We could of course avoid this by using a different name for the argument.

In practice one would probably like a more useful result from the function than a constant 1, so a more likely definition is:

    CREATE FUNCTION tf1 (accountno integer, debit numeric) RETURNS numeric AS $$
        UPDATE bank
            SET balance = balance - debit
            WHERE accountno = tf1.accountno;
        SELECT balance FROM bank WHERE accountno = tf1.accountno;
    $$ LANGUAGE SQL;

which adjusts the balance and returns the new balance. The same thing could be done in one command using `RETURNING`:

    CREATE FUNCTION tf1 (accountno integer, debit numeric) RETURNS numeric AS $$
        UPDATE bank
            SET balance = balance - debit
            WHERE accountno = tf1.accountno
        RETURNING balance;
    $$ LANGUAGE SQL;

If the final `SELECT` or `RETURNING` clause in an SQL function does not return exactly the function's declared result type, PostgreSQL will automatically cast the value to the required type, if that is possible with an implicit or assignment cast. Otherwise, you must write an explicit cast. For example, suppose we wanted the previous `add_em` function to return type `float8` instead. It's sufficient to write

    CREATE FUNCTION add_em(integer, integer) RETURNS float8 AS $$
        SELECT $1 + $2;
    $$ LANGUAGE SQL;

since the `integer` sum can be implicitly cast to `float8`. (See [???](#typeconv) or [???](#sql-createcast) for more about casts.)

## SQL Functions on Composite Types

When writing functions with arguments of composite types, we must not only specify which argument we want but also the desired attribute (field) of that argument. For example, suppose that `emp` is a table containing employee data, and therefore also the name of the composite type of each row of the table. Here is a function `double_salary` that computes what someone's salary would be if it were doubled:

    CREATE TABLE emp (
        name        text,
        salary      numeric,
        age         integer,
        cubicle     point
    );

    INSERT INTO emp VALUES ('Bill', 4200, 45, '(2,1)');

    CREATE FUNCTION double_salary(emp) RETURNS numeric AS $$
        SELECT $1.salary * 2 AS salary;
    $$ LANGUAGE SQL;

    SELECT name, double_salary(emp.*) AS dream
        FROM emp
        WHERE emp.cubicle ~= point '(2,1)';

     name | dream
    ------+-------
     Bill |  8400

Notice the use of the syntax `$1.salary` to select one field of the argument row value. Also notice how the calling `SELECT` command uses \<table_name\>`.*` to select the entire current row of a table as a composite value. The table row can alternatively be referenced using just the table name, like this:

    SELECT name, double_salary(emp) AS dream
        FROM emp
        WHERE emp.cubicle ~= point '(2,1)';

but this usage is deprecated since it's easy to get confused. (See [???](#rowtypes-usage) for details about these two notations for the composite value of a table row.)

Sometimes it is handy to construct a composite argument value on-the-fly. This can be done with the `ROW` construct. For example, we could adjust the data being passed to the function:

    SELECT name, double_salary(ROW(name, salary*1.1, age, cubicle)) AS dream
        FROM emp;

It is also possible to build a function that returns a composite type. This is an example of a function that returns a single `emp` row:

    CREATE FUNCTION new_emp() RETURNS emp AS $$
        SELECT text 'None' AS name,
            1000.0 AS salary,
            25 AS age,
            point '(2,2)' AS cubicle;
    $$ LANGUAGE SQL;

In this example we have specified each of the attributes with a constant value, but any computation could have been substituted for these constants.

Note two important things about defining the function:

- The select list order in the query must be exactly the same as that in which the columns appear in the composite type. (Naming the columns, as we did above, is irrelevant to the system.)

- We must ensure each expression's type can be cast to that of the corresponding column of the composite type. Otherwise we'll get errors like this:

      ERROR:  return type mismatch in function declared to return emp
      DETAIL:  Final statement returns text instead of point at column 4.

  As with the base-type case, the system will not insert explicit casts automatically, only implicit or assignment casts.

A different way to define the same function is:

    CREATE FUNCTION new_emp() RETURNS emp AS $$
        SELECT ROW('None', 1000.0, 25, '(2,2)')::emp;
    $$ LANGUAGE SQL;

Here we wrote a `SELECT` that returns just a single column of the correct composite type. This isn't really better in this situation, but it is a handy alternative in some cases for example, if we need to compute the result by calling another function that returns the desired composite value. Another example is that if we are trying to write a function that returns a domain over composite, rather than a plain composite type, it is always necessary to write it as returning a single column, since there is no way to cause a coercion of the whole row result.

We could call this function directly either by using it in a value expression:

    SELECT new_emp();

             new_emp
    --------------------------
     (None,1000.0,25,"(2,2)")

or by calling it as a table function:

    SELECT * FROM new_emp();

     name | salary | age | cubicle
    ------+--------+-----+---------
     None | 1000.0 |  25 | (2,2)

The second way is described more fully in [ Functions as Table Sources](#xfunc-sql-table-functions).

When you use a function that returns a composite type, you might want only one field (attribute) from its result. You can do that with syntax like this:

    SELECT (new_emp()).name;

     name
    ------
     None

The extra parentheses are needed to keep the parser from getting confused. If you try to do it without them, you get something like this:

    SELECT new_emp().name;
    ERROR:  syntax error at or near "."
    LINE 1: SELECT new_emp().name;
                            ^

Another option is to use functional notation for extracting an attribute:

    SELECT name(new_emp());

     name
    ------
     None

As explained in [???](#rowtypes-usage), the field notation and functional notation are equivalent.

Another way to use a function returning a composite type is to pass the result to another function that accepts the correct row type as input:

    CREATE FUNCTION getname(emp) RETURNS text AS $$
        SELECT $1.name;
    $$ LANGUAGE SQL;

    SELECT getname(new_emp());
     getname
    ---------
     None
    (1 row)

## SQL Functions with Output Parameters

function

output parameter

An alternative way of describing a function's results is to define it with output parameters, as in this example:

    CREATE FUNCTION add_em (IN x int, IN y int, OUT sum int)
    AS 'SELECT x + y'
    LANGUAGE SQL;

    SELECT add_em(3,7);
     add_em
    --------
         10
    (1 row)

This is not essentially different from the version of `add_em` shown in [ Functions on Base Types](#xfunc-sql-base-functions). The real value of output parameters is that they provide a convenient way of defining functions that return several columns. For example,

    CREATE FUNCTION sum_n_product (x int, y int, OUT sum int, OUT product int)
    AS 'SELECT x + y, x * y'
    LANGUAGE SQL;

     SELECT * FROM sum_n_product(11,42);
     sum | product
    -----+---------
      53 |     462
    (1 row)

What has essentially happened here is that we have created an anonymous composite type for the result of the function. The above example has the same end result as

    CREATE TYPE sum_prod AS (sum int, product int);

    CREATE FUNCTION sum_n_product (int, int) RETURNS sum_prod
    AS 'SELECT $1 + $2, $1 * $2'
    LANGUAGE SQL;

but not having to bother with the separate composite type definition is often handy. Notice that the names attached to the output parameters are not just decoration, but determine the column names of the anonymous composite type. (If you omit a name for an output parameter, the system will choose a name on its own.)

Notice that output parameters are not included in the calling argument list when invoking such a function from SQL. This is because PostgreSQL considers only the input parameters to define the function's calling signature. That means also that only the input parameters matter when referencing the function for purposes such as dropping it. We could drop the above function with either of

    DROP FUNCTION sum_n_product (x int, y int, OUT sum int, OUT product int);
    DROP FUNCTION sum_n_product (int, int);

Parameters can be marked as `IN` (the default), `OUT`, `INOUT`, or `VARIADIC`. An `INOUT` parameter serves as both an input parameter (part of the calling argument list) and an output parameter (part of the result record type). `VARIADIC` parameters are input parameters, but are treated specially as described below.

## SQL Procedures with Output Parameters

procedures

output parameter

Output parameters are also supported in procedures, but they work a bit differently from functions. In `CALL` commands, output parameters must be included in the argument list. For example, the bank account debiting routine from earlier could be written like this:

    CREATE PROCEDURE tp1 (accountno integer, debit numeric, OUT new_balance numeric) AS $$
        UPDATE bank
            SET balance = balance - debit
            WHERE accountno = tp1.accountno
        RETURNING balance;
    $$ LANGUAGE SQL;

To call this procedure, an argument matching the `OUT` parameter must be included. It's customary to write `NULL`:

    CALL tp1(17, 100.0, NULL);

If you write something else, it must be an expression that is implicitly coercible to the declared type of the parameter, just as for input parameters. Note however that such an expression will not be evaluated.

When calling a procedure from PL/pgSQL, instead of writing `NULL` you must write a variable that will receive the procedure's output. See [???](#plpgsql-statements-calling-procedure) for details.

## SQL Functions with Variable Numbers of Arguments

function

variadic

variadic function

SQL functions can be declared to accept variable numbers of arguments, so long as all the “optional” arguments are of the same data type. The optional arguments will be passed to the function as an array. The function is declared by marking the last parameter as `VARIADIC`; this parameter must be declared as being of an array type. For example:

    CREATE FUNCTION mleast(VARIADIC arr numeric[]) RETURNS numeric AS $$
        SELECT min($1[i]) FROM generate_subscripts($1, 1) g(i);
    $$ LANGUAGE SQL;

    SELECT mleast(10, -1, 5, 4.4);
     mleast
    --------
         -1
    (1 row)

Effectively, all the actual arguments at or beyond the `VARIADIC` position are gathered up into a one-dimensional array, as if you had written

    SELECT mleast(ARRAY[10, -1, 5, 4.4]);    -- doesn't work

You can't actually write that, though or at least, it will not match this function definition. A parameter marked `VARIADIC` matches one or more occurrences of its element type, not of its own type.

Sometimes it is useful to be able to pass an already-constructed array to a variadic function; this is particularly handy when one variadic function wants to pass on its array parameter to another one. Also, this is the only secure way to call a variadic function found in a schema that permits untrusted users to create objects; see [???](#typeconv-func). You can do this by specifying `VARIADIC` in the call:

    SELECT mleast(VARIADIC ARRAY[10, -1, 5, 4.4]);

This prevents expansion of the function's variadic parameter into its element type, thereby allowing the array argument value to match normally. `VARIADIC` can only be attached to the last actual argument of a function call.

Specifying `VARIADIC` in the call is also the only way to pass an empty array to a variadic function, for example:

    SELECT mleast(VARIADIC ARRAY[]::numeric[]);

Simply writing `SELECT mleast()` does not work because a variadic parameter must match at least one actual argument. (You could define a second function also named `mleast`, with no parameters, if you wanted to allow such calls.)

The array element parameters generated from a variadic parameter are treated as not having any names of their own. This means it is not possible to call a variadic function using named arguments ([???](#sql-syntax-calling-funcs)), except when you specify `VARIADIC`. For example, this will work:

    SELECT mleast(VARIADIC arr => ARRAY[10, -1, 5, 4.4]);

but not these:

    SELECT mleast(arr => 10);
    SELECT mleast(arr => ARRAY[10, -1, 5, 4.4]);

## SQL Functions with Default Values for Arguments

function

default values for arguments

Functions can be declared with default values for some or all input arguments. The default values are inserted whenever the function is called with insufficiently many actual arguments. Since arguments can only be omitted from the end of the actual argument list, all parameters after a parameter with a default value have to have default values as well. (Although the use of named argument notation could allow this restriction to be relaxed, it's still enforced so that positional argument notation works sensibly.) Whether or not you use it, this capability creates a need for precautions when calling functions in databases where some users mistrust other users; see [???](#typeconv-func).

For example:

    CREATE FUNCTION foo(a int, b int DEFAULT 2, c int DEFAULT 3)
    RETURNS int
    LANGUAGE SQL
    AS $$
        SELECT $1 + $2 + $3;
    $$;

    SELECT foo(10, 20, 30);
     foo
    -----
      60
    (1 row)

    SELECT foo(10, 20);
     foo
    -----
      33
    (1 row)

    SELECT foo(10);
     foo
    -----
      15
    (1 row)

    SELECT foo();  -- fails since there is no default for the first argument
    ERROR:  function foo() does not exist

The `=` sign can also be used in place of the key word `DEFAULT`.

## SQL Functions as Table Sources

All SQL functions can be used in the `FROM` clause of a query, but it is particularly useful for functions returning composite types. If the function is defined to return a base type, the table function produces a one-column table. If the function is defined to return a composite type, the table function produces a column for each attribute of the composite type.

Here is an example:

    CREATE TABLE foo (fooid int, foosubid int, fooname text);
    INSERT INTO foo VALUES (1, 1, 'Joe');
    INSERT INTO foo VALUES (1, 2, 'Ed');
    INSERT INTO foo VALUES (2, 1, 'Mary');

    CREATE FUNCTION getfoo(int) RETURNS foo AS $$
        SELECT * FROM foo WHERE fooid = $1;
    $$ LANGUAGE SQL;

    SELECT *, upper(fooname) FROM getfoo(1) AS t1;

     fooid | foosubid | fooname | upper
    -------+----------+---------+-------
         1 |        1 | Joe     | JOE
    (1 row)

As the example shows, we can work with the columns of the function's result just the same as if they were columns of a regular table.

Note that we only got one row out of the function. This is because we did not use `SETOF`. That is described in the next section.

## SQL Functions Returning Sets

function

with SETOF

When an SQL function is declared as returning `SETOF sometype`, the function's final query is executed to completion, and each row it outputs is returned as an element of the result set.

This feature is normally used when calling the function in the `FROM` clause. In this case each row returned by the function becomes a row of the table seen by the query. For example, assume that table `foo` has the same contents as above, and we say:

    CREATE FUNCTION getfoo(int) RETURNS SETOF foo AS $$
        SELECT * FROM foo WHERE fooid = $1;
    $$ LANGUAGE SQL;

    SELECT * FROM getfoo(1) AS t1;

Then we would get:

     fooid | foosubid | fooname
    -------+----------+---------
         1 |        1 | Joe
         1 |        2 | Ed
    (2 rows)

It is also possible to return multiple rows with the columns defined by output parameters, like this:

    CREATE TABLE tab (y int, z int);
    INSERT INTO tab VALUES (1, 2), (3, 4), (5, 6), (7, 8);

    CREATE FUNCTION sum_n_product_with_tab (x int, OUT sum int, OUT product int)
    RETURNS SETOF record
    AS $$
        SELECT $1 + tab.y, $1 * tab.y FROM tab;
    $$ LANGUAGE SQL;

    SELECT * FROM sum_n_product_with_tab(10);
     sum | product
    -----+---------
      11 |      10
      13 |      30
      15 |      50
      17 |      70
    (4 rows)

The key point here is that you must write `RETURNS SETOF record` to indicate that the function returns multiple rows instead of just one. If there is only one output parameter, write that parameter's type instead of `record`.

It is frequently useful to construct a query's result by invoking a set-returning function multiple times, with the parameters for each invocation coming from successive rows of a table or subquery. The preferred way to do this is to use the `LATERAL` key word, which is described in [???](#queries-lateral). Here is an example using a set-returning function to enumerate elements of a tree structure:

    SELECT * FROM nodes;
       name    | parent
    -----------+--------
     Top       |
     Child1    | Top
     Child2    | Top
     Child3    | Top
     SubChild1 | Child1
     SubChild2 | Child1
    (6 rows)

    CREATE FUNCTION listchildren(text) RETURNS SETOF text AS $$
        SELECT name FROM nodes WHERE parent = $1
    $$ LANGUAGE SQL STABLE;

    SELECT * FROM listchildren('Top');
     listchildren
    --------------
     Child1
     Child2
     Child3
    (3 rows)

    SELECT name, child FROM nodes, LATERAL listchildren(name) AS child;
      name  |   child
    --------+-----------
     Top    | Child1
     Top    | Child2
     Top    | Child3
     Child1 | SubChild1
     Child1 | SubChild2
    (5 rows)

This example does not do anything that we couldn't have done with a simple join, but in more complex calculations the option to put some of the work into a function can be quite convenient.

Functions returning sets can also be called in the select list of a query. For each row that the query generates by itself, the set-returning function is invoked, and an output row is generated for each element of the function's result set. The previous example could also be done with queries like these:

    SELECT listchildren('Top');
     listchildren
    --------------
     Child1
     Child2
     Child3
    (3 rows)

    SELECT name, listchildren(name) FROM nodes;
      name  | listchildren
    --------+--------------
     Top    | Child1
     Top    | Child2
     Top    | Child3
     Child1 | SubChild1
     Child1 | SubChild2
    (5 rows)

In the last `SELECT`, notice that no output row appears for `Child2`, `Child3`, etc. This happens because `listchildren` returns an empty set for those arguments, so no result rows are generated. This is the same behavior as we got from an inner join to the function result when using the `LATERAL` syntax.

PostgreSQL's behavior for a set-returning function in a query's select list is almost exactly the same as if the set-returning function had been written in a `LATERAL FROM`-clause item instead. For example,

    SELECT x, generate_series(1,5) AS g FROM tab;

is almost equivalent to

    SELECT x, g FROM tab, LATERAL generate_series(1,5) AS g;

It would be exactly the same, except that in this specific example, the planner could choose to put g on the outside of the nested-loop join, since g has no actual lateral dependency on tab. That would result in a different output row order. Set-returning functions in the select list are always evaluated as though they are on the inside of a nested-loop join with the rest of the `FROM` clause, so that the function(s) are run to completion before the next row from the `FROM` clause is considered.

If there is more than one set-returning function in the query's select list, the behavior is similar to what you get from putting the functions into a single `LATERAL ROWS FROM( ... )` `FROM`-clause item. For each row from the underlying query, there is an output row using the first result from each function, then an output row using the second result, and so on. If some of the set-returning functions produce fewer outputs than others, null values are substituted for the missing data, so that the total number of rows emitted for one underlying row is the same as for the set-returning function that produced the most outputs. Thus the set-returning functions run “in lockstep” until they are all exhausted, and then execution continues with the next underlying row.

Set-returning functions can be nested in a select list, although that is not allowed in `FROM`-clause items. In such cases, each level of nesting is treated separately, as though it were a separate `LATERAL ROWS FROM( ... )` item. For example, in

    SELECT srf1(srf2(x), srf3(y)), srf4(srf5(z)) FROM tab;

the set-returning functions `srf2`, `srf3`, and `srf5` would be run in lockstep for each row of tab, and then `srf1` and `srf4` would be applied in lockstep to each row produced by the lower functions.

Set-returning functions cannot be used within conditional-evaluation constructs, such as `CASE` or `COALESCE`. For example, consider

    SELECT x, CASE WHEN x > 0 THEN generate_series(1, 5) ELSE 0 END FROM tab;

It might seem that this should produce five repetitions of input rows that have `x > 0`, and a single repetition of those that do not; but actually, because `generate_series(1, 5)` would be run in an implicit `LATERAL FROM` item before the `CASE` expression is ever evaluated, it would produce five repetitions of every input row. To reduce confusion, such cases produce a parse-time error instead.

> [!NOTE]
> If a function's last command is `INSERT`, `UPDATE`, `DELETE`, or `MERGE` with `RETURNING`, that command will always be executed to completion, even if the function is not declared with `SETOF` or the calling query does not fetch all the result rows. Any extra rows produced by the `RETURNING` clause are silently dropped, but the commanded table modifications still happen (and are all completed before returning from the function).

> [!NOTE]
> Before PostgreSQL 10, putting more than one set-returning function in the same select list did not behave very sensibly unless they always produced equal numbers of rows. Otherwise, what you got was a number of output rows equal to the least common multiple of the numbers of rows produced by the set-returning functions. Also, nested set-returning functions did not work as described above; instead, a set-returning function could have at most one set-returning argument, and each nest of set-returning functions was run independently. Also, conditional execution (set-returning functions inside `CASE` etc.) was previously allowed, complicating things even more. Use of the `LATERAL` syntax is recommended when writing queries that need to work in older PostgreSQL versions, because that will give consistent results across different versions. If you have a query that is relying on conditional execution of a set-returning function, you may be able to fix it by moving the conditional test into a custom set-returning function. For example,
>
>     SELECT x, CASE WHEN y > 0 THEN generate_series(1, z) ELSE 5 END FROM tab;
>
> could become
>
>     CREATE FUNCTION case_generate_series(cond bool, start int, fin int, els int)
>       RETURNS SETOF int AS $$
>     BEGIN
>       IF cond THEN
>         RETURN QUERY SELECT generate_series(start, fin);
>       ELSE
>         RETURN QUERY SELECT els;
>       END IF;
>     END$$ LANGUAGE plpgsql;
>
>     SELECT x, case_generate_series(y > 0, 1, z, 5) FROM tab;
>
> This formulation will work the same in all versions of PostgreSQL.

## SQL Functions Returning `TABLE`

function

RETURNS TABLE

There is another way to declare a function as returning a set, which is to use the syntax `RETURNS TABLE(columns)`. This is equivalent to using one or more `OUT` parameters plus marking the function as returning `SETOF record` (or `SETOF` a single output parameter's type, as appropriate). This notation is specified in recent versions of the SQL standard, and thus may be more portable than using `SETOF`.

For example, the preceding sum-and-product example could also be done this way:

    CREATE FUNCTION sum_n_product_with_tab (x int)
    RETURNS TABLE(sum int, product int) AS $$
        SELECT $1 + tab.y, $1 * tab.y FROM tab;
    $$ LANGUAGE SQL;

It is not allowed to use explicit `OUT` or `INOUT` parameters with the `RETURNS TABLE` notation you must put all the output columns in the `TABLE` list.

## Polymorphic SQL Functions

SQL functions can be declared to accept and return the polymorphic types described in [???](#extend-types-polymorphic). Here is a polymorphic function `make_array` that builds up an array from two arbitrary data type elements:

    CREATE FUNCTION make_array(anyelement, anyelement) RETURNS anyarray AS $$
        SELECT ARRAY[$1, $2];
    $$ LANGUAGE SQL;

    SELECT make_array(1, 2) AS intarray, make_array('a'::text, 'b') AS textarray;
     intarray | textarray
    ----------+-----------
     {1,2}    | {a,b}
    (1 row)

Notice the use of the typecast `'a'::text` to specify that the argument is of type `text`. This is required if the argument is just a string literal, since otherwise it would be treated as type `unknown`, and array of `unknown` is not a valid type. Without the typecast, you will get errors like this:

    ERROR:  could not determine polymorphic type because input has type unknown

With `make_array` declared as above, you must provide two arguments that are of exactly the same data type; the system will not attempt to resolve any type differences. Thus for example this does not work:

    SELECT make_array(1, 2.5) AS numericarray;
    ERROR:  function make_array(integer, numeric) does not exist

An alternative approach is to use the “common” family of polymorphic types, which allows the system to try to identify a suitable common type:

    CREATE FUNCTION make_array2(anycompatible, anycompatible)
    RETURNS anycompatiblearray AS $$
        SELECT ARRAY[$1, $2];
    $$ LANGUAGE SQL;

    SELECT make_array2(1, 2.5) AS numericarray;
     numericarray
    --------------
     {1,2.5}
    (1 row)

Because the rules for common type resolution default to choosing type `text` when all inputs are of unknown types, this also works:

    SELECT make_array2('a', 'b') AS textarray;
     textarray
    -----------
     {a,b}
    (1 row)

It is permitted to have polymorphic arguments with a fixed return type, but the converse is not. For example:

    CREATE FUNCTION is_greater(anyelement, anyelement) RETURNS boolean AS $$
        SELECT $1 > $2;
    $$ LANGUAGE SQL;

    SELECT is_greater(1, 2);
     is_greater
    ------------
     f
    (1 row)

    CREATE FUNCTION invalid_func() RETURNS anyelement AS $$
        SELECT 1;
    $$ LANGUAGE SQL;
    ERROR:  cannot determine result data type
    DETAIL:  A result of type anyelement requires at least one input of type anyelement, anyarray, anynonarray, anyenum, or anyrange.

Polymorphism can be used with functions that have output arguments. For example:

    CREATE FUNCTION dup (f1 anyelement, OUT f2 anyelement, OUT f3 anyarray)
    AS 'select $1, array[$1,$1]' LANGUAGE SQL;

    SELECT * FROM dup(22);
     f2 |   f3
    ----+---------
     22 | {22,22}
    (1 row)

Polymorphism can also be used with variadic functions. For example:

    CREATE FUNCTION anyleast (VARIADIC anyarray) RETURNS anyelement AS $$
        SELECT min($1[i]) FROM generate_subscripts($1, 1) g(i);
    $$ LANGUAGE SQL;

    SELECT anyleast(10, -1, 5, 4);
     anyleast
    ----------
           -1
    (1 row)

    SELECT anyleast('abc'::text, 'def');
     anyleast
    ----------
     abc
    (1 row)

    CREATE FUNCTION concat_values(text, VARIADIC anyarray) RETURNS text AS $$
        SELECT array_to_string($2, $1);
    $$ LANGUAGE SQL;

    SELECT concat_values('|', 1, 4, 2);
     concat_values
    ---------------
     1|4|2
    (1 row)

## SQL Functions with Collations

collation

in SQL functions

When an SQL function has one or more parameters of collatable data types, a collation is identified for each function call depending on the collations assigned to the actual arguments, as described in [???](#collation). If a collation is successfully identified (i.e., there are no conflicts of implicit collations among the arguments) then all the collatable parameters are treated as having that collation implicitly. This will affect the behavior of collation-sensitive operations within the function. For example, using the `anyleast` function described above, the result of

    SELECT anyleast('abc'::text, 'ABC');

will depend on the database's default collation. In `C` locale the result will be `ABC`, but in many other locales it will be `abc`. The collation to use can be forced by adding a `COLLATE` clause to any of the arguments, for example

    SELECT anyleast('abc'::text, 'ABC' COLLATE "C");

Alternatively, if you wish a function to operate with a particular collation regardless of what it is called with, insert `COLLATE` clauses as needed in the function definition. This version of `anyleast` would always use `en_US` locale to compare strings:

    CREATE FUNCTION anyleast (VARIADIC anyarray) RETURNS anyelement AS $$
        SELECT min($1[i] COLLATE "en_US") FROM generate_subscripts($1, 1) g(i);
    $$ LANGUAGE SQL;

But note that this will throw an error if applied to a non-collatable data type.

If no common collation can be identified among the actual arguments, then an SQL function treats its parameters as having their data types' default collation (which is usually the database's default collation, but could be different for parameters of domain types).

The behavior of collatable parameters can be thought of as a limited form of polymorphism, applicable only to textual data types.

## Function Overloading

overloading

functions

More than one function can be defined with the same SQL name, so long as the arguments they take are different. In other words, function names can be overloaded. Whether or not you use it, this capability entails security precautions when calling functions in databases where some users mistrust other users; see [???](#typeconv-func). When a query is executed, the server will determine which function to call from the data types and the number of the provided arguments. Overloading can also be used to simulate functions with a variable number of arguments, up to a finite maximum number.

When creating a family of overloaded functions, one should be careful not to create ambiguities. For instance, given the functions:

    CREATE FUNCTION test(int, real) RETURNS ...
    CREATE FUNCTION test(smallint, double precision) RETURNS ...

it is not immediately clear which function would be called with some trivial input like `test(1, 1.5)`. The currently implemented resolution rules are described in [???](#typeconv), but it is unwise to design a system that subtly relies on this behavior.

A function that takes a single argument of a composite type should generally not have the same name as any attribute (field) of that type. Recall that `attribute(table)` is considered equivalent to `table.attribute`. In the case that there is an ambiguity between a function on a composite type and an attribute of the composite type, the attribute will always be used. It is possible to override that choice by schema-qualifying the function name (that is, `schema.func(table)`) but it's better to avoid the problem by not choosing conflicting names.

Another possible conflict is between variadic and non-variadic functions. For instance, it is possible to create both `foo(numeric)` and `foo(VARIADIC numeric[])`. In this case it is unclear which one should be matched to a call providing a single numeric argument, such as `foo(10.1)`. The rule is that the function appearing earlier in the search path is used, or if the two functions are in the same schema, the non-variadic one is preferred.

When overloading C-language functions, there is an additional constraint: The C name of each function in the family of overloaded functions must be different from the C names of all other functions, either internal or dynamically loaded. If this rule is violated, the behavior is not portable. You might get a run-time linker error, or one of the functions will get called (usually the internal one). The alternative form of the `AS` clause for the SQL `CREATE FUNCTION` command decouples the SQL function name from the function name in the C source code. For instance:

    CREATE FUNCTION test(int) RETURNS int
        AS 'filename', 'test_1arg'
        LANGUAGE C;
    CREATE FUNCTION test(int, int) RETURNS int
        AS 'filename', 'test_2arg'
        LANGUAGE C;

The names of the C functions here reflect one of many possible conventions.

## Function Volatility Categories

volatility

functions

VOLATILE

STABLE

IMMUTABLE

Every function has a volatility classification, with the possibilities being `VOLATILE`, `STABLE`, or `IMMUTABLE`. `VOLATILE` is the default if the [`CREATE FUNCTION`](#sql-createfunction) command does not specify a category. The volatility category is a promise to the optimizer about the behavior of the function:

- A `VOLATILE` function can do anything, including modifying the database. It can return different results on successive calls with the same arguments. The optimizer makes no assumptions about the behavior of such functions. A query using a volatile function will re-evaluate the function at every row where its value is needed.

- A `STABLE` function cannot modify the database and is guaranteed to return the same results given the same arguments for all rows within a single statement. This category allows the optimizer to optimize multiple calls of the function to a single call. In particular, it is safe to use an expression containing such a function in an index scan condition. (Since an index scan will evaluate the comparison value only once, not once at each row, it is not valid to use a `VOLATILE` function in an index scan condition.)

- An `IMMUTABLE` function cannot modify the database and is guaranteed to return the same results given the same arguments forever. This category allows the optimizer to pre-evaluate the function when a query calls it with constant arguments. For example, a query like `SELECT ... WHERE x = 2 + 2` can be simplified on sight to `SELECT ... WHERE x = 4`, because the function underlying the integer addition operator is marked `IMMUTABLE`.

For best optimization results, you should label your functions with the strictest volatility category that is valid for them.

Any function with side-effects *must* be labeled `VOLATILE`, so that calls to it cannot be optimized away. Even a function with no side-effects needs to be labeled `VOLATILE` if its value can change within a single query; some examples are `random()`, `currval()`, `timeofday()`.

Another important example is that the `current_timestamp` family of functions qualify as `STABLE`, since their values do not change within a transaction.

There is relatively little difference between `STABLE` and `IMMUTABLE` categories when considering simple interactive queries that are planned and immediately executed: it doesn't matter a lot whether a function is executed once during planning or once during query execution startup. But there is a big difference if the plan is saved and reused later. Labeling a function `IMMUTABLE` when it really isn't might allow it to be prematurely folded to a constant during planning, resulting in a stale value being re-used during subsequent uses of the plan. This is a hazard when using prepared statements or when using function languages that cache plans (such as PL/pgSQL).

For functions written in SQL or in any of the standard procedural languages, there is a second important property determined by the volatility category, namely the visibility of any data changes that have been made by the SQL command that is calling the function. A `VOLATILE` function will see such changes, a `STABLE` or `IMMUTABLE` function will not. This behavior is implemented using the snapshotting behavior of MVCC (see [???](#mvcc)): `STABLE` and `IMMUTABLE` functions use a snapshot established as of the start of the calling query, whereas `VOLATILE` functions obtain a fresh snapshot at the start of each query they execute.

> [!NOTE]
> Functions written in C can manage snapshots however they want, but it's usually a good idea to make C functions work this way too.

Because of this snapshotting behavior, a function containing only `SELECT` commands can safely be marked `STABLE`, even if it selects from tables that might be undergoing modifications by concurrent queries. PostgreSQL will execute all commands of a `STABLE` function using the snapshot established for the calling query, and so it will see a fixed view of the database throughout that query.

The same snapshotting behavior is used for `SELECT` commands within `IMMUTABLE` functions. It is generally unwise to select from database tables within an `IMMUTABLE` function at all, since the immutability will be broken if the table contents ever change. However, PostgreSQL does not enforce that you do not do that.

A common error is to label a function `IMMUTABLE` when its results depend on a configuration parameter. For example, a function that manipulates timestamps might well have results that depend on the [???](#guc-timezone) setting. For safety, such functions should be labeled `STABLE` instead.

> [!NOTE]
> PostgreSQL requires that `STABLE` and `IMMUTABLE` functions contain no SQL commands other than `SELECT` to prevent data modification. (This is not a completely bulletproof test, since such functions could still call `VOLATILE` functions that modify the database. If you do that, you will find that the `STABLE` or `IMMUTABLE` function does not notice the database changes applied by the called function, since they are hidden from its snapshot.)

## Procedural Language Functions

PostgreSQL allows user-defined functions to be written in other languages besides SQL and C. These other languages are generically called procedural languages (PLs). Procedural languages aren't built into the PostgreSQL server; they are offered by loadable modules. See [???](#xplang) and following chapters for more information.

## Internal Functions

function

internal

Internal functions are functions written in C that have been statically linked into the PostgreSQL server. The “body” of the function definition specifies the C-language name of the function, which need not be the same as the name being declared for SQL use. (For reasons of backward compatibility, an empty body is accepted as meaning that the C-language function name is the same as the SQL name.)

Normally, all internal functions present in the server are declared during the initialization of the database cluster (see [???](#creating-cluster)), but a user could use `CREATE FUNCTION` to create additional alias names for an internal function. Internal functions are declared in `CREATE FUNCTION` with language name `internal`. For instance, to create an alias for the `sqrt` function:

    CREATE FUNCTION square_root(double precision) RETURNS double precision
        AS 'dsqrt'
        LANGUAGE internal
        STRICT;

(Most internal functions expect to be declared “strict”.)

> [!NOTE]
> Not all “predefined” functions are “internal” in the above sense. Some predefined functions are written in SQL.

## C-Language Functions

function

user-defined

in C

User-defined functions can be written in C (or a language that can be made compatible with C, such as C++). Such functions are compiled into dynamically loadable objects (also called shared libraries) and are loaded by the server on demand. The dynamic loading feature is what distinguishes “C language” functions from “internal” functions the actual coding conventions are essentially the same for both. (Hence, the standard internal function library is a rich source of coding examples for user-defined C functions.)

Currently only one calling convention is used for C functions (“version 1”). Support for that calling convention is indicated by writing a `PG_FUNCTION_INFO_V1()` macro call for the function, as illustrated below.

## Dynamic Loading

dynamic loading

The first time a user-defined function in a particular loadable object file is called in a session, the dynamic loader loads that object file into memory so that the function can be called. The `CREATE FUNCTION` for a user-defined C function must therefore specify two pieces of information for the function: the name of the loadable object file, and the C name (link symbol) of the specific function to call within that object file. If the C name is not explicitly specified then it is assumed to be the same as the SQL function name.

The following algorithm is used to locate the shared object file based on the name given in the `CREATE FUNCTION` command:

1.  If the name is an absolute path, the given file is loaded.

2.  If the name starts with the string `$libdir`, that part is replaced by the PostgreSQL package library directory name, which is determined at build time.<span class="indexterm"></span>

3.  If the name does not contain a directory part, the file is searched for in the path specified by the configuration variable [???](#guc-dynamic-library-path).<span class="indexterm"></span>

4.  Otherwise (the file was not found in the path, or it contains a non-absolute directory part), the dynamic loader will try to take the name as given, which will most likely fail. (It is unreliable to depend on the current working directory.)

If this sequence does not work, the platform-specific shared library file name extension (often `.so`) is appended to the given name and this sequence is tried again. If that fails as well, the load will fail.

It is recommended to locate shared libraries either relative to `$libdir` or through the dynamic library path. This simplifies version upgrades if the new installation is at a different location. The actual directory that `$libdir` stands for can be found out with the command `pg_config --pkglibdir`.

The user ID the PostgreSQL server runs as must be able to traverse the path to the file you intend to load. Making the file or a higher-level directory not readable and/or not executable by the `postgres` user is a common mistake.

In any case, the file name that is given in the `CREATE FUNCTION` command is recorded literally in the system catalogs, so if the file needs to be loaded again the same procedure is applied.

> [!NOTE]
> PostgreSQL will not compile a C function automatically. The object file must be compiled before it is referenced in a `CREATE FUNCTION` command. See [???](#dfunc) for additional information.

magic block

To ensure that a dynamically loaded object file is not loaded into an incompatible server, PostgreSQL checks that the file contains a “magic block” with the appropriate contents. This allows the server to detect obvious incompatibilities, such as code compiled for a different major version of PostgreSQL. To include a magic block, write this in one (and only one) of the module source files, after having included the header `fmgr.h`:

    PG_MODULE_MAGIC;

After it is used for the first time, a dynamically loaded object file is retained in memory. Future calls in the same session to the function(s) in that file will only incur the small overhead of a symbol table lookup. If you need to force a reload of an object file, for example after recompiling it, begin a fresh session.

\_PG_init

library initialization function

Optionally, a dynamically loaded file can contain an initialization function. If the file includes a function named `_PG_init`, that function will be called immediately after loading the file. The function receives no parameters and should return void. There is presently no way to unload a dynamically loaded file.

## Base Types in C-Language Functions

data type

internal organization

To know how to write C-language functions, you need to know how PostgreSQL internally represents base data types and how they can be passed to and from functions. Internally, PostgreSQL regards a base type as a “blob of memory”. The user-defined functions that you define over a type in turn define the way that PostgreSQL can operate on it. That is, PostgreSQL will only store and retrieve the data from disk and use your user-defined functions to input, process, and output the data.

Base types can have one of three internal formats:

- pass by value, fixed-length

- pass by reference, fixed-length

- pass by reference, variable-length

By-value types can only be 1, 2, or 4 bytes in length (also 8 bytes, if `sizeof(Datum)` is 8 on your machine). You should be careful to define your types such that they will be the same size (in bytes) on all architectures. For example, the `long` type is dangerous because it is 4 bytes on some machines and 8 bytes on others, whereas `int` type is 4 bytes on most Unix machines. A reasonable implementation of the `int4` type on Unix machines might be:

    /* 4-byte integer, passed by value */
    typedef int int4;

(The actual PostgreSQL C code calls this type `int32`, because it is a convention in C that `intXX` means \<XX\> *bits*. Note therefore also that the C type `int8` is 1 byte in size. The SQL type `int8` is called `int64` in C. See also [Equivalent C Types for Built-in SQL Types](#xfunc-c-type-table).)

On the other hand, fixed-length types of any size can be passed by-reference. For example, here is a sample implementation of a PostgreSQL type:

    /* 16-byte structure, passed by reference */
    typedef struct
    {
        double  x, y;
    } Point;

Only pointers to such types can be used when passing them in and out of PostgreSQL functions. To return a value of such a type, allocate the right amount of memory with `palloc`, fill in the allocated memory, and return a pointer to it. (Also, if you just want to return the same value as one of your input arguments that's of the same data type, you can skip the extra `palloc` and just return the pointer to the input value.)

Finally, all variable-length types must also be passed by reference. All variable-length types must begin with an opaque length field of exactly 4 bytes, which will be set by `SET_VARSIZE`; never set this field directly! All data to be stored within that type must be located in the memory immediately following that length field. The length field contains the total length of the structure, that is, it includes the size of the length field itself.

Another important point is to avoid leaving any uninitialized bits within data type values; for example, take care to zero out any alignment padding bytes that might be present in structs. Without this, logically-equivalent constants of your data type might be seen as unequal by the planner, leading to inefficient (though not incorrect) plans.

> [!WARNING]
> *Never* modify the contents of a pass-by-reference input value. If you do so you are likely to corrupt on-disk data, since the pointer you are given might point directly into a disk buffer. The sole exception to this rule is explained in [???](#xaggr).

As an example, we can define the type `text` as follows:

    typedef struct {
        int32 length;
        char data[FLEXIBLE_ARRAY_MEMBER];
    } text;

The `[FLEXIBLE_ARRAY_MEMBER]` notation means that the actual length of the data part is not specified by this declaration.

When manipulating variable-length types, we must be careful to allocate the correct amount of memory and set the length field correctly. For example, if we wanted to store 40 bytes in a text structure, we might use a code fragment like this:

    #include "postgres.h"
    ...
    char buffer[40]; /* our source data */
    ...
    text *destination = (text *) palloc(VARHDRSZ + 40);
    SET_VARSIZE(destination, VARHDRSZ + 40);
    memcpy(destination->data, buffer, 40);
    ...

`VARHDRSZ` is the same as `sizeof(int32)`, but it's considered good style to use the macro `VARHDRSZ` to refer to the size of the overhead for a variable-length type. Also, the length field *must* be set using the `SET_VARSIZE` macro, not by simple assignment.

[Equivalent C Types for Built-in SQL Types](#xfunc-c-type-table) shows the C types corresponding to many of the built-in SQL data types of PostgreSQL. The “Defined In” column gives the header file that needs to be included to get the type definition. (The actual definition might be in a different file that is included by the listed file. It is recommended that users stick to the defined interface.) Note that you should always include `postgres.h` first in any source file of server code, because it declares a number of things that you will need anyway, and because including other headers first can cause portability issues.

| SQL Type | C Type | Defined In |
|----|----|----|
| `boolean` | `bool` | `postgres.h` (maybe compiler built-in) |
| `box` | `BOX*` | `utils/geo_decls.h` |
| `bytea` | `bytea*` | `postgres.h` |
| `"char"` | `char` | (compiler built-in) |
| `character` | `BpChar*` | `postgres.h` |
| `cid` | `CommandId` | `postgres.h` |
| `date` | `DateADT` | `utils/date.h` |
| `float4` (`real`) | `float4` | `postgres.h` |
| `float8` (`double precision`) | `float8` | `postgres.h` |
| `int2` (`smallint`) | `int16` | `postgres.h` |
| `int4` (`integer`) | `int32` | `postgres.h` |
| `int8` (`bigint`) | `int64` | `postgres.h` |
| `interval` | `Interval*` | `datatype/timestamp.h` |
| `lseg` | `LSEG*` | `utils/geo_decls.h` |
| `name` | `Name` | `postgres.h` |
| `numeric` | `Numeric` | `utils/numeric.h` |
| `oid` | `Oid` | `postgres.h` |
| `oidvector` | `oidvector*` | `postgres.h` |
| `path` | `PATH*` | `utils/geo_decls.h` |
| `point` | `POINT*` | `utils/geo_decls.h` |
| `regproc` | `RegProcedure` | `postgres.h` |
| `text` | `text*` | `postgres.h` |
| `tid` | `ItemPointer` | `storage/itemptr.h` |
| `time` | `TimeADT` | `utils/date.h` |
| `time with time zone` | `TimeTzADT` | `utils/date.h` |
| `timestamp` | `Timestamp` | `datatype/timestamp.h` |
| `timestamp with time zone` | `TimestampTz` | `datatype/timestamp.h` |
| `varchar` | `VarChar*` | `postgres.h` |
| `xid` | `TransactionId` | `postgres.h` |

Equivalent C Types for Built-in SQL Types {#xfunc-c-type-table}

Now that we've gone over all of the possible structures for base types, we can show some examples of real functions.

## Version 1 Calling Conventions

The version-1 calling convention relies on macros to suppress most of the complexity of passing arguments and results. The C declaration of a version-1 function is always:

    Datum funcname(PG_FUNCTION_ARGS)

In addition, the macro call:

    PG_FUNCTION_INFO_V1(funcname);

must appear in the same source file. (Conventionally, it's written just before the function itself.) This macro call is not needed for `internal`-language functions, since PostgreSQL assumes that all internal functions use the version-1 convention. It is, however, required for dynamically-loaded functions.

In a version-1 function, each actual argument is fetched using a `PG_GETARG_xxx()` macro that corresponds to the argument's data type. (In non-strict functions there needs to be a previous check about argument null-ness using `PG_ARGISNULL()`; see below.) The result is returned using a `PG_RETURN_xxx()` macro for the return type. `PG_GETARG_xxx()` takes as its argument the number of the function argument to fetch, where the count starts at 0. `PG_RETURN_xxx()` takes as its argument the actual value to return.

Here are some examples using the version-1 calling convention:

    #include "postgres.h"
    #include <string.h>
    #include "fmgr.h"
    #include "utils/geo_decls.h"
    #include "varatt.h"

    PG_MODULE_MAGIC;

    /* by value */

    PG_FUNCTION_INFO_V1(add_one);

    Datum
    add_one(PG_FUNCTION_ARGS)
    {
        int32   arg = PG_GETARG_INT32(0);

        PG_RETURN_INT32(arg + 1);
    }

    /* by reference, fixed length */

    PG_FUNCTION_INFO_V1(add_one_float8);

    Datum
    add_one_float8(PG_FUNCTION_ARGS)
    {
        /* The macros for FLOAT8 hide its pass-by-reference nature. */
        float8   arg = PG_GETARG_FLOAT8(0);

        PG_RETURN_FLOAT8(arg + 1.0);
    }

    PG_FUNCTION_INFO_V1(makepoint);

    Datum
    makepoint(PG_FUNCTION_ARGS)
    {
        /* Here, the pass-by-reference nature of Point is not hidden. */
        Point     *pointx = PG_GETARG_POINT_P(0);
        Point     *pointy = PG_GETARG_POINT_P(1);
        Point     *new_point = (Point *) palloc(sizeof(Point));

        new_point->x = pointx->x;
        new_point->y = pointy->y;

        PG_RETURN_POINT_P(new_point);
    }

    /* by reference, variable length */

    PG_FUNCTION_INFO_V1(copytext);

    Datum
    copytext(PG_FUNCTION_ARGS)
    {
        text     *t = PG_GETARG_TEXT_PP(0);

        /*
         * VARSIZE_ANY_EXHDR is the size of the struct in bytes, minus the
         * VARHDRSZ or VARHDRSZ_SHORT of its header.  Construct the copy with a
         * full-length header.
         */
        text     *new_t = (text *) palloc(VARSIZE_ANY_EXHDR(t) + VARHDRSZ);
        SET_VARSIZE(new_t, VARSIZE_ANY_EXHDR(t) + VARHDRSZ);

        /*
         * VARDATA is a pointer to the data region of the new struct.  The source
         * could be a short datum, so retrieve its data through VARDATA_ANY.
         */
        memcpy(VARDATA(new_t),          /* destination */
               VARDATA_ANY(t),          /* source */
               VARSIZE_ANY_EXHDR(t));   /* how many bytes */
        PG_RETURN_TEXT_P(new_t);
    }

    PG_FUNCTION_INFO_V1(concat_text);

    Datum
    concat_text(PG_FUNCTION_ARGS)
    {
        text  *arg1 = PG_GETARG_TEXT_PP(0);
        text  *arg2 = PG_GETARG_TEXT_PP(1);
        int32 arg1_size = VARSIZE_ANY_EXHDR(arg1);
        int32 arg2_size = VARSIZE_ANY_EXHDR(arg2);
        int32 new_text_size = arg1_size + arg2_size + VARHDRSZ;
        text *new_text = (text *) palloc(new_text_size);

        SET_VARSIZE(new_text, new_text_size);
        memcpy(VARDATA(new_text), VARDATA_ANY(arg1), arg1_size);
        memcpy(VARDATA(new_text) + arg1_size, VARDATA_ANY(arg2), arg2_size);
        PG_RETURN_TEXT_P(new_text);
    }

Supposing that the above code has been prepared in file `funcs.c` and compiled into a shared object, we could define the functions to PostgreSQL with commands like this:

    CREATE FUNCTION add_one(integer) RETURNS integer
         AS 'DIRECTORY/funcs', 'add_one'
         LANGUAGE C STRICT;

    -- note overloading of SQL function name "add_one"
    CREATE FUNCTION add_one(double precision) RETURNS double precision
         AS 'DIRECTORY/funcs', 'add_one_float8'
         LANGUAGE C STRICT;

    CREATE FUNCTION makepoint(point, point) RETURNS point
         AS 'DIRECTORY/funcs', 'makepoint'
         LANGUAGE C STRICT;

    CREATE FUNCTION copytext(text) RETURNS text
         AS 'DIRECTORY/funcs', 'copytext'
         LANGUAGE C STRICT;

    CREATE FUNCTION concat_text(text, text) RETURNS text
         AS 'DIRECTORY/funcs', 'concat_text'
         LANGUAGE C STRICT;

Here, \<DIRECTORY\> stands for the directory of the shared library file (for instance the PostgreSQL tutorial directory, which contains the code for the examples used in this section). (Better style would be to use just `'funcs'` in the `AS` clause, after having added \<DIRECTORY\> to the search path. In any case, we can omit the system-specific extension for a shared library, commonly `.so`.)

Notice that we have specified the functions as “strict”, meaning that the system should automatically assume a null result if any input value is null. By doing this, we avoid having to check for null inputs in the function code. Without this, we'd have to check for null values explicitly, using `PG_ARGISNULL()`.

The macro `PG_ARGISNULL(n)` allows a function to test whether each input is null. (Of course, doing this is only necessary in functions not declared “strict”.) As with the `PG_GETARG_xxx()` macros, the input arguments are counted beginning at zero. Note that one should refrain from executing `PG_GETARG_xxx()` until one has verified that the argument isn't null. To return a null result, execute `PG_RETURN_NULL()`; this works in both strict and nonstrict functions.

At first glance, the version-1 coding conventions might appear to be just pointless obscurantism, compared to using plain `C` calling conventions. They do however allow us to deal with `NULL`able arguments/return values, and “toasted” (compressed or out-of-line) values.

Other options provided by the version-1 interface are two variants of the `PG_GETARG_xxx()` macros. The first of these, `PG_GETARG_xxx_COPY()`, guarantees to return a copy of the specified argument that is safe for writing into. (The normal macros will sometimes return a pointer to a value that is physically stored in a table, which must not be written to. Using the `PG_GETARG_xxx_COPY()` macros guarantees a writable result.) The second variant consists of the `PG_GETARG_xxx_SLICE()` macros which take three arguments. The first is the number of the function argument (as above). The second and third are the offset and length of the segment to be returned. Offsets are counted from zero, and a negative length requests that the remainder of the value be returned. These macros provide more efficient access to parts of large values in the case where they have storage type “external”. (The storage type of a column can be specified using `ALTER TABLE tablename ALTER COLUMN colname SET STORAGE storagetype`. \<storagetype\> is one of `plain`, `external`, `extended`, or `main`.)

Finally, the version-1 function call conventions make it possible to return set results ([Returning Sets](#xfunc-c-return-set)) and implement trigger functions ([???](#triggers)) and procedural-language call handlers ([???](#plhandler)). For more details see `src/backend/utils/fmgr/README` in the source distribution.

## Writing Code

Before we turn to the more advanced topics, we should discuss some coding rules for PostgreSQL C-language functions. While it might be possible to load functions written in languages other than C into PostgreSQL, this is usually difficult (when it is possible at all) because other languages, such as C++, FORTRAN, or Pascal often do not follow the same calling convention as C. That is, other languages do not pass argument and return values between functions in the same way. For this reason, we will assume that your C-language functions are actually written in C.

The basic rules for writing and building C functions are as follows:

- Use `pg_config --includedir-server`<span class="indexterm"></span> to find out where the PostgreSQL server header files are installed on your system (or the system that your users will be running on).

- Compiling and linking your code so that it can be dynamically loaded into PostgreSQL always requires special flags. See [???](#dfunc) for a detailed explanation of how to do it for your particular operating system.

- Remember to define a “magic block” for your shared library, as described in [Dynamic Loading](#xfunc-c-dynload).

- When allocating memory, use the PostgreSQL functions `palloc`<span class="indexterm"></span> and `pfree`<span class="indexterm"></span> instead of the corresponding C library functions `malloc` and `free`. The memory allocated by `palloc` will be freed automatically at the end of each transaction, preventing memory leaks.

- Always zero the bytes of your structures using `memset` (or allocate them with `palloc0` in the first place). Even if you assign to each field of your structure, there might be alignment padding (holes in the structure) that contain garbage values. Without this, it's difficult to support hash indexes or hash joins, as you must pick out only the significant bits of your data structure to compute a hash. The planner also sometimes relies on comparing constants via bitwise equality, so you can get undesirable planning results if logically-equivalent values aren't bitwise equal.

- Most of the internal PostgreSQL types are declared in `postgres.h`, while the function manager interfaces (`PG_FUNCTION_ARGS`, etc.) are in `fmgr.h`, so you will need to include at least these two files. For portability reasons it's best to include `postgres.h` *first*, before any other system or user header files. Including `postgres.h` will also include `elog.h` and `palloc.h` for you.

- Symbol names defined within object files must not conflict with each other or with symbols defined in the PostgreSQL server executable. You will have to rename your functions or variables if you get error messages to this effect.

## Composite-Type Arguments

Composite types do not have a fixed layout like C structures. Instances of a composite type can contain null fields. In addition, composite types that are part of an inheritance hierarchy can have different fields than other members of the same inheritance hierarchy. Therefore, PostgreSQL provides a function interface for accessing fields of composite types from C.

Suppose we want to write a function to answer the query:

    SELECT name, c_overpaid(emp, 1500) AS overpaid
        FROM emp
        WHERE name = 'Bill' OR name = 'Sam';

Using the version-1 calling conventions, we can define `c_overpaid` as:

    #include "postgres.h"
    #include "executor/executor.h"  /* for GetAttributeByName() */

    PG_MODULE_MAGIC;

    PG_FUNCTION_INFO_V1(c_overpaid);

    Datum
    c_overpaid(PG_FUNCTION_ARGS)
    {
        HeapTupleHeader  t = PG_GETARG_HEAPTUPLEHEADER(0);
        int32            limit = PG_GETARG_INT32(1);
        bool isnull;
        Datum salary;

        salary = GetAttributeByName(t, "salary", &isnull);
        if (isnull)
            PG_RETURN_BOOL(false);
        /* Alternatively, we might prefer to do PG_RETURN_NULL() for null salary. */

        PG_RETURN_BOOL(DatumGetInt32(salary) > limit);
    }

`GetAttributeByName` is the PostgreSQL system function that returns attributes out of the specified row. It has three arguments: the argument of type `HeapTupleHeader` passed into the function, the name of the desired attribute, and a return parameter that tells whether the attribute is null. `GetAttributeByName` returns a `Datum` value that you can convert to the proper data type by using the appropriate `DatumGetXXX()` function. Note that the return value is meaningless if the null flag is set; always check the null flag before trying to do anything with the result.

There is also `GetAttributeByNum`, which selects the target attribute by column number instead of name.

The following command declares the function `c_overpaid` in SQL:

    CREATE FUNCTION c_overpaid(emp, integer) RETURNS boolean
        AS 'DIRECTORY/funcs', 'c_overpaid'
        LANGUAGE C STRICT;

Notice we have used `STRICT` so that we did not have to check whether the input arguments were NULL.

## Returning Rows (Composite Types)

To return a row or composite-type value from a C-language function, you can use a special API that provides macros and functions to hide most of the complexity of building composite data types. To use this API, the source file must include:

    #include "funcapi.h"

There are two ways you can build a composite data value (henceforth a “tuple”): you can build it from an array of Datum values, or from an array of C strings that can be passed to the input conversion functions of the tuple's column data types. In either case, you first need to obtain or construct a TupleDesc descriptor for the tuple structure. When working with Datums, you pass the TupleDesc to `BlessTupleDesc`, and then call `heap_form_tuple` for each row. When working with C strings, you pass the TupleDesc to `TupleDescGetAttInMetadata`, and then call `BuildTupleFromCStrings` for each row. In the case of a function returning a set of tuples, the setup steps can all be done once during the first call of the function.

Several helper functions are available for setting up the needed TupleDesc. The recommended way to do this in most functions returning composite values is to call:

    TypeFuncClass get_call_result_type(FunctionCallInfo fcinfo,
                                       Oid *resultTypeId,
                                       TupleDesc *resultTupleDesc)

passing the same `fcinfo` struct passed to the calling function itself. (This of course requires that you use the version-1 calling conventions.) `resultTypeId` can be specified as `NULL` or as the address of a local variable to receive the function's result type OID. `resultTupleDesc` should be the address of a local TupleDesc variable. Check that the result is `TYPEFUNC_COMPOSITE`; if so, `resultTupleDesc` has been filled with the needed TupleDesc. (If it is not, you can report an error along the lines of “function returning record called in context that cannot accept type record”.)

> [!TIP]
> `get_call_result_type` can resolve the actual type of a polymorphic function result; so it is useful in functions that return scalar polymorphic results, not only functions that return composites. The `resultTypeId` output is primarily useful for functions returning polymorphic scalars.

> [!NOTE]
> `get_call_result_type` has a sibling `get_expr_result_type`, which can be used to resolve the expected output type for a function call represented by an expression tree. This can be used when trying to determine the result type from outside the function itself. There is also `get_func_result_type`, which can be used when only the function's OID is available. However these functions are not able to deal with functions declared to return record, and `get_func_result_type` cannot resolve polymorphic types, so you should preferentially use `get_call_result_type`.

Older, now-deprecated functions for obtaining TupleDescs are:

    TupleDesc RelationNameGetTupleDesc(const char *relname)

to get a TupleDesc for the row type of a named relation, and:

    TupleDesc TypeGetTupleDesc(Oid typeoid, List *colaliases)

to get a TupleDesc based on a type OID. This can be used to get a TupleDesc for a base or composite type. It will not work for a function that returns record, however, and it cannot resolve polymorphic types.

Once you have a TupleDesc, call:

    TupleDesc BlessTupleDesc(TupleDesc tupdesc)

if you plan to work with Datums, or:

    AttInMetadata *TupleDescGetAttInMetadata(TupleDesc tupdesc)

if you plan to work with C strings. If you are writing a function returning set, you can save the results of these functions in the FuncCallContext structure use the tuple_desc or attinmeta field respectively.

When working with Datums, use:

    HeapTuple heap_form_tuple(TupleDesc tupdesc, Datum *values, bool *isnull)

to build a HeapTuple given user data in Datum form.

When working with C strings, use:

    HeapTuple BuildTupleFromCStrings(AttInMetadata *attinmeta, char **values)

to build a HeapTuple given user data in C string form. `values` is an array of C strings, one for each attribute of the return row. Each C string should be in the form expected by the input function of the attribute data type. In order to return a null value for one of the attributes, the corresponding pointer in the `values` array should be set to `NULL`. This function will need to be called again for each row you return.

Once you have built a tuple to return from your function, it must be converted into a `Datum`. Use:

    HeapTupleGetDatum(HeapTuple tuple)

to convert a HeapTuple into a valid Datum. This `Datum` can be returned directly if you intend to return just a single row, or it can be used as the current return value in a set-returning function.

An example appears in the next section.

## Returning Sets

C-language functions have two options for returning sets (multiple rows). In one method, called ValuePerCall mode, a set-returning function is called repeatedly (passing the same arguments each time) and it returns one new row on each call, until it has no more rows to return and signals that by returning NULL. The set-returning function (SRF) must therefore save enough state across calls to remember what it was doing and return the correct next item on each call. In the other method, called Materialize mode, an SRF fills and returns a tuplestore object containing its entire result; then only one call occurs for the whole result, and no inter-call state is needed.

When using ValuePerCall mode, it is important to remember that the query is not guaranteed to be run to completion; that is, due to options such as `LIMIT`, the executor might stop making calls to the set-returning function before all rows have been fetched. This means it is not safe to perform cleanup activities in the last call, because that might not ever happen. It's recommended to use Materialize mode for functions that need access to external resources, such as file descriptors.

The remainder of this section documents a set of helper macros that are commonly used (though not required to be used) for SRFs using ValuePerCall mode. Additional details about Materialize mode can be found in `src/backend/utils/fmgr/README`. Also, the `contrib` modules in the PostgreSQL source distribution contain many examples of SRFs using both ValuePerCall and Materialize mode.

To use the ValuePerCall support macros described here, include `funcapi.h`. These macros work with a structure FuncCallContext that contains the state that needs to be saved across calls. Within the calling SRF, `fcinfo->flinfo->fn_extra` is used to hold a pointer to FuncCallContext across calls. The macros automatically fill that field on first use, and expect to find the same pointer there on subsequent uses.

    typedef struct FuncCallContext
    {
        /*
         * Number of times we've been called before
         *
         * call_cntr is initialized to 0 for you by SRF_FIRSTCALL_INIT(), and
         * incremented for you every time SRF_RETURN_NEXT() is called.
         */
        uint64 call_cntr;

        /*
         * OPTIONAL maximum number of calls
         *
         * max_calls is here for convenience only and setting it is optional.
         * If not set, you must provide alternative means to know when the
         * function is done.
         */
        uint64 max_calls;

        /*
         * OPTIONAL pointer to miscellaneous user-provided context information
         *
         * user_fctx is for use as a pointer to your own data to retain
         * arbitrary context information between calls of your function.
         */
        void *user_fctx;

        /*
         * OPTIONAL pointer to struct containing attribute type input metadata
         *
         * attinmeta is for use when returning tuples (i.e., composite data types)
         * and is not used when returning base data types. It is only needed
         * if you intend to use BuildTupleFromCStrings() to create the return
         * tuple.
         */
        AttInMetadata *attinmeta;

        /*
         * memory context used for structures that must live for multiple calls
         *
         * multi_call_memory_ctx is set by SRF_FIRSTCALL_INIT() for you, and used
         * by SRF_RETURN_DONE() for cleanup. It is the most appropriate memory
         * context for any memory that is to be reused across multiple calls
         * of the SRF.
         */
        MemoryContext multi_call_memory_ctx;

        /*
         * OPTIONAL pointer to struct containing tuple description
         *
         * tuple_desc is for use when returning tuples (i.e., composite data types)
         * and is only needed if you are going to build the tuples with
         * heap_form_tuple() rather than with BuildTupleFromCStrings().  Note that
         * the TupleDesc pointer stored here should usually have been run through
         * BlessTupleDesc() first.
         */
        TupleDesc tuple_desc;

    } FuncCallContext;

The macros to be used by an SRF using this infrastructure are:

    SRF_IS_FIRSTCALL()

Use this to determine if your function is being called for the first or a subsequent time. On the first call (only), call:

    SRF_FIRSTCALL_INIT()

to initialize the FuncCallContext. On every function call, including the first, call:

    SRF_PERCALL_SETUP()

to set up for using the FuncCallContext.

If your function has data to return in the current call, use:

    SRF_RETURN_NEXT(funcctx, result)

to return it to the caller. (`result` must be of type `Datum`, either a single value or a tuple prepared as described above.) Finally, when your function is finished returning data, use:

    SRF_RETURN_DONE(funcctx)

to clean up and end the SRF.

The memory context that is current when the SRF is called is a transient context that will be cleared between calls. This means that you do not need to call `pfree` on everything you allocated using `palloc`; it will go away anyway. However, if you want to allocate any data structures to live across calls, you need to put them somewhere else. The memory context referenced by multi_call_memory_ctx is a suitable location for any data that needs to survive until the SRF is finished running. In most cases, this means that you should switch into multi_call_memory_ctx while doing the first-call setup. Use `funcctx->user_fctx` to hold a pointer to any such cross-call data structures. (Data you allocate in multi_call_memory_ctx will go away automatically when the query ends, so it is not necessary to free that data manually, either.)

> [!WARNING]
> While the actual arguments to the function remain unchanged between calls, if you detoast the argument values (which is normally done transparently by the `PG_GETARG_xxx` macro) in the transient context then the detoasted copies will be freed on each cycle. Accordingly, if you keep references to such values in your user_fctx, you must either copy them into the multi_call_memory_ctx after detoasting, or ensure that you detoast the values only in that context.

A complete pseudo-code example looks like the following:

    Datum
    my_set_returning_function(PG_FUNCTION_ARGS)
    {
        FuncCallContext  *funcctx;
        Datum             result;
        further declarations as needed

        if (SRF_IS_FIRSTCALL())
        {
            MemoryContext oldcontext;

            funcctx = SRF_FIRSTCALL_INIT();
            oldcontext = MemoryContextSwitchTo(funcctx->multi_call_memory_ctx);
            /* One-time setup code appears here: */
            user code
            if returning composite
                build TupleDesc, and perhaps AttInMetadata
            endif returning composite
            user code
            MemoryContextSwitchTo(oldcontext);
        }

        /* Each-time setup code appears here: */
        user code
        funcctx = SRF_PERCALL_SETUP();
        user code

        /* this is just one way we might test whether we are done: */
        if (funcctx->call_cntr < funcctx->max_calls)
        {
            /* Here we want to return another item: */
            user code
            obtain result Datum
            SRF_RETURN_NEXT(funcctx, result);
        }
        else
        {
            /* Here we are done returning items, so just report that fact. */
            /* (Resist the temptation to put cleanup code here.) */
            SRF_RETURN_DONE(funcctx);
        }
    }

A complete example of a simple SRF returning a composite type looks like:

    PG_FUNCTION_INFO_V1(retcomposite);

    Datum
    retcomposite(PG_FUNCTION_ARGS)
    {
        FuncCallContext     *funcctx;
        int                  call_cntr;
        int                  max_calls;
        TupleDesc            tupdesc;
        AttInMetadata       *attinmeta;

        /* stuff done only on the first call of the function */
        if (SRF_IS_FIRSTCALL())
        {
            MemoryContext   oldcontext;

            /* create a function context for cross-call persistence */
            funcctx = SRF_FIRSTCALL_INIT();

            /* switch to memory context appropriate for multiple function calls */
            oldcontext = MemoryContextSwitchTo(funcctx->multi_call_memory_ctx);

            /* total number of tuples to be returned */
            funcctx->max_calls = PG_GETARG_INT32(0);

            /* Build a tuple descriptor for our result type */
            if (get_call_result_type(fcinfo, NULL, &tupdesc) != TYPEFUNC_COMPOSITE)
                ereport(ERROR,
                        (errcode(ERRCODE_FEATURE_NOT_SUPPORTED),
                         errmsg("function returning record called in context "
                                "that cannot accept type record")));

            /*
             * generate attribute metadata needed later to produce tuples from raw
             * C strings
             */
            attinmeta = TupleDescGetAttInMetadata(tupdesc);
            funcctx->attinmeta = attinmeta;

            MemoryContextSwitchTo(oldcontext);
        }

        /* stuff done on every call of the function */
        funcctx = SRF_PERCALL_SETUP();

        call_cntr = funcctx->call_cntr;
        max_calls = funcctx->max_calls;
        attinmeta = funcctx->attinmeta;

        if (call_cntr < max_calls)    /* do when there is more left to send */
        {
            char       **values;
            HeapTuple    tuple;
            Datum        result;

            /*
             * Prepare a values array for building the returned tuple.
             * This should be an array of C strings which will
             * be processed later by the type input functions.
             */
            values = (char **) palloc(3 * sizeof(char *));
            values[0] = (char *) palloc(16 * sizeof(char));
            values[1] = (char *) palloc(16 * sizeof(char));
            values[2] = (char *) palloc(16 * sizeof(char));

            snprintf(values[0], 16, "%d", 1 * PG_GETARG_INT32(1));
            snprintf(values[1], 16, "%d", 2 * PG_GETARG_INT32(1));
            snprintf(values[2], 16, "%d", 3 * PG_GETARG_INT32(1));

            /* build a tuple */
            tuple = BuildTupleFromCStrings(attinmeta, values);

            /* make the tuple into a datum */
            result = HeapTupleGetDatum(tuple);

            /* clean up (this is not really necessary) */
            pfree(values[0]);
            pfree(values[1]);
            pfree(values[2]);
            pfree(values);

            SRF_RETURN_NEXT(funcctx, result);
        }
        else    /* do when there is no more left */
        {
            SRF_RETURN_DONE(funcctx);
        }
    }

One way to declare this function in SQL is:

    CREATE TYPE __retcomposite AS (f1 integer, f2 integer, f3 integer);

    CREATE OR REPLACE FUNCTION retcomposite(integer, integer)
        RETURNS SETOF __retcomposite
        AS 'filename', 'retcomposite'
        LANGUAGE C IMMUTABLE STRICT;

A different way is to use OUT parameters:

    CREATE OR REPLACE FUNCTION retcomposite(IN integer, IN integer,
        OUT f1 integer, OUT f2 integer, OUT f3 integer)
        RETURNS SETOF record
        AS 'filename', 'retcomposite'
        LANGUAGE C IMMUTABLE STRICT;

Notice that in this method the output type of the function is formally an anonymous record type.

## Polymorphic Arguments and Return Types

C-language functions can be declared to accept and return the polymorphic types described in [???](#extend-types-polymorphic). When a function's arguments or return types are defined as polymorphic types, the function author cannot know in advance what data type it will be called with, or need to return. There are two routines provided in `fmgr.h` to allow a version-1 C function to discover the actual data types of its arguments and the type it is expected to return. The routines are called `get_fn_expr_rettype(FmgrInfo *flinfo)` and `get_fn_expr_argtype(FmgrInfo *flinfo, int argnum)`. They return the result or argument type OID, or `InvalidOid` if the information is not available. The structure `flinfo` is normally accessed as `fcinfo->flinfo`. The parameter `argnum` is zero based. `get_call_result_type` can also be used as an alternative to `get_fn_expr_rettype`. There is also `get_fn_expr_variadic`, which can be used to find out whether variadic arguments have been merged into an array. This is primarily useful for `VARIADIC "any"` functions, since such merging will always have occurred for variadic functions taking ordinary array types.

For example, suppose we want to write a function to accept a single element of any type, and return a one-dimensional array of that type:

    PG_FUNCTION_INFO_V1(make_array);
    Datum
    make_array(PG_FUNCTION_ARGS)
    {
        ArrayType  *result;
        Oid         element_type = get_fn_expr_argtype(fcinfo->flinfo, 0);
        Datum       element;
        bool        isnull;
        int16       typlen;
        bool        typbyval;
        char        typalign;
        int         ndims;
        int         dims[MAXDIM];
        int         lbs[MAXDIM];

        if (!OidIsValid(element_type))
            elog(ERROR, "could not determine data type of input");

        /* get the provided element, being careful in case it's NULL */
        isnull = PG_ARGISNULL(0);
        if (isnull)
            element = (Datum) 0;
        else
            element = PG_GETARG_DATUM(0);

        /* we have one dimension */
        ndims = 1;
        /* and one element */
        dims[0] = 1;
        /* and lower bound is 1 */
        lbs[0] = 1;

        /* get required info about the element type */
        get_typlenbyvalalign(element_type, &typlen, &typbyval, &typalign);

        /* now build the array */
        result = construct_md_array(&element, &isnull, ndims, dims, lbs,
                                    element_type, typlen, typbyval, typalign);

        PG_RETURN_ARRAYTYPE_P(result);
    }

The following command declares the function `make_array` in SQL:

    CREATE FUNCTION make_array(anyelement) RETURNS anyarray
        AS 'DIRECTORY/funcs', 'make_array'
        LANGUAGE C IMMUTABLE;

There is a variant of polymorphism that is only available to C-language functions: they can be declared to take parameters of type `"any"`. (Note that this type name must be double-quoted, since it's also an SQL reserved word.) This works like `anyelement` except that it does not constrain different `"any"` arguments to be the same type, nor do they help determine the function's result type. A C-language function can also declare its final parameter to be `VARIADIC "any"`. This will match one or more actual arguments of any type (not necessarily the same type). These arguments will *not* be gathered into an array as happens with normal variadic functions; they will just be passed to the function separately. The `PG_NARGS()` macro and the methods described above must be used to determine the number of actual arguments and their types when using this feature. Also, users of such a function might wish to use the `VARIADIC` keyword in their function call, with the expectation that the function would treat the array elements as separate arguments. The function itself must implement that behavior if wanted, after using `get_fn_expr_variadic` to detect that the actual argument was marked with `VARIADIC`.

## Shared Memory

### Requesting Shared Memory at Startup

Add-ins can reserve shared memory on server startup. To do so, the add-in's shared library must be preloaded by specifying it in [???](#guc-shared-preload-libraries)<span class="indexterm"></span>. The shared library should also register a `shmem_request_hook` in its `_PG_init` function. This `shmem_request_hook` can reserve shared memory by calling:

    void RequestAddinShmemSpace(Size size)

Each backend should obtain a pointer to the reserved shared memory by calling:

    void *ShmemInitStruct(const char *name, Size size, bool *foundPtr)

If this function sets `foundPtr` to `false`, the caller should proceed to initialize the contents of the reserved shared memory. If `foundPtr` is set to `true`, the shared memory was already initialized by another backend, and the caller need not initialize further.

To avoid race conditions, each backend should use the LWLock `AddinShmemInitLock` when initializing its allocation of shared memory, as shown here:

    static mystruct *ptr = NULL;
    bool        found;

    LWLockAcquire(AddinShmemInitLock, LW_EXCLUSIVE);
    ptr = ShmemInitStruct("my struct name", size, &found);
    if (!found)
    {
        ... initialize contents of shared memory ...
        ptr->locks = GetNamedLWLockTranche("my tranche name");
    }
    LWLockRelease(AddinShmemInitLock);

`shmem_startup_hook` provides a convenient place for the initialization code, but it is not strictly required that all such code be placed in this hook. On Windows (and anywhere else where `EXEC_BACKEND` is defined), each backend executes the registered `shmem_startup_hook` shortly after it attaches to shared memory, so add-ins should still acquire `AddinShmemInitLock` within this hook, as shown in the example above. On other platforms, only the postmaster process executes the `shmem_startup_hook`, and each backend automatically inherits the pointers to shared memory.

An example of a `shmem_request_hook` and `shmem_startup_hook` can be found in `contrib/pg_stat_statements/pg_stat_statements.c` in the PostgreSQL source tree.

### Requesting Shared Memory After Startup

There is another, more flexible method of reserving shared memory that can be done after server startup and outside a `shmem_request_hook`. To do so, each backend that will use the shared memory should obtain a pointer to it by calling:

    void *GetNamedDSMSegment(const char *name, size_t size,
                             void (*init_callback) (void *ptr),
                             bool *found)

If a dynamic shared memory segment with the given name does not yet exist, this function will allocate it and initialize it with the provided `init_callback` callback function. If the segment has already been allocated and initialized by another backend, this function simply attaches the existing dynamic shared memory segment to the current backend.

Unlike shared memory reserved at server startup, there is no need to acquire `AddinShmemInitLock` or otherwise take action to avoid race conditions when reserving shared memory with `GetNamedDSMSegment`. This function ensures that only one backend allocates and initializes the segment and that all other backends receive a pointer to the fully allocated and initialized segment.

A complete usage example of `GetNamedDSMSegment` can be found in `src/test/modules/test_dsm_registry/test_dsm_registry.c` in the PostgreSQL source tree.

## LWLocks

### Requesting LWLocks at Startup

Add-ins can reserve LWLocks on server startup. As with shared memory reserved at server startup, the add-in's shared library must be preloaded by specifying it in [???](#guc-shared-preload-libraries)<span class="indexterm"></span>, and the shared library should register a `shmem_request_hook` in its `_PG_init` function. This `shmem_request_hook` can reserve LWLocks by calling:

    void RequestNamedLWLockTranche(const char *tranche_name, int num_lwlocks)

This ensures that an array of `num_lwlocks` LWLocks is available under the name `tranche_name`. A pointer to this array can be obtained by calling:

    LWLockPadded *GetNamedLWLockTranche(const char *tranche_name)

### Requesting LWLocks After Startup

There is another, more flexible method of obtaining LWLocks that can be done after server startup and outside a `shmem_request_hook`. To do so, first allocate a `tranche_id` by calling:

    int LWLockNewTrancheId(void)

Next, initialize each LWLock, passing the new `tranche_id` as an argument:

    void LWLockInitialize(LWLock *lock, int tranche_id)

Similar to shared memory, each backend should ensure that only one process allocates a new `tranche_id` and initializes each new LWLock. One way to do this is to only call these functions in your shared memory initialization code with the `AddinShmemInitLock` held exclusively. If using `GetNamedDSMSegment`, calling these functions in the `init_callback` callback function is sufficient to avoid race conditions.

Finally, each backend using the `tranche_id` should associate it with a `tranche_name` by calling:

    void LWLockRegisterTranche(int tranche_id, const char *tranche_name)

A complete usage example of `LWLockNewTrancheId`, `LWLockInitialize`, and `LWLockRegisterTranche` can be found in `contrib/pg_prewarm/autoprewarm.c` in the PostgreSQL source tree.

## Custom Wait Events

Add-ins can define custom wait events under the wait event type `Extension` by calling:

    uint32 WaitEventExtensionNew(const char *wait_event_name)

The wait event is associated to a user-facing custom string. An example can be found in `src/test/modules/worker_spi` in the PostgreSQL source tree.

Custom wait events can be viewed in [pg_stat_activity](#monitoring-pg-stat-activity-view):

    =# SELECT wait_event_type, wait_event FROM pg_stat_activity
         WHERE backend_type ~ 'worker_spi';
     wait_event_type |  wait_event
    -----------------+---------------
     Extension       | WorkerSpiMain
    (1 row)

## Injection Points

An injection point with a given `name` is declared using macro:

    INJECTION_POINT(name);

There are a few injection points already declared at strategic points within the server code. After adding a new injection point the code needs to be compiled in order for that injection point to be available in the binary. Add-ins written in C-language can declare injection points in their own code using the same macro. The injection point names should use lower-case characters, with terms separated by dashes.

Add-ins can attach callbacks to an already-declared injection point by calling:

    extern void InjectionPointAttach(const char *name,
                                     const char *library,
                                     const char *function,
                                     const void *private_data,
                                     int private_data_size);

`name` is the name of the injection point, which when reached during execution will execute the `function` loaded from `library`. `private_data` is a private area of data of size `private_data_size` given as argument to the callback when executed.

Here is an example of callback for `InjectionPointCallback`:

    static void
    custom_injection_callback(const char *name, const void *private_data)
    {
        uint32 wait_event_info = WaitEventInjectionPointNew(name);

        pgstat_report_wait_start(wait_event_info);
        elog(NOTICE, "%s: executed custom callback", name);
        pgstat_report_wait_end();
    }

This callback prints a message to server error log with severity `NOTICE`, but callbacks may implement more complex logic.

Optionally, it is possible to detach an injection point by calling:

    extern bool InjectionPointDetach(const char *name);

On success, `true` is returned, `false` otherwise.

A callback attached to an injection point is available across all the backends including the backends started after `InjectionPointAttach` is called. It remains attached while the server is running or until the injection point is detached using `InjectionPointDetach`.

An example can be found in `src/test/modules/injection_points` in the PostgreSQL source tree.

Enabling injections points requires `--enable-injection-points` with `configure` or `-Dinjection_points=true` with Meson.

## Using C++ for Extensibility

C++

Although the PostgreSQL backend is written in C, it is possible to write extensions in C++ if these guidelines are followed:

- All functions accessed by the backend must present a C interface to the backend; these C functions can then call C++ functions. For example, `extern C` linkage is required for backend-accessed functions. This is also necessary for any functions that are passed as pointers between the backend and C++ code.

- Free memory using the appropriate deallocation method. For example, most backend memory is allocated using `palloc()`, so use `pfree()` to free it. Using C++ `delete` in such cases will fail.

- Prevent exceptions from propagating into the C code (use a catch-all block at the top level of all `extern C` functions). This is necessary even if the C++ code does not explicitly throw any exceptions, because events like out-of-memory can still throw exceptions. Any exceptions must be caught and appropriate errors passed back to the C interface. If possible, compile C++ with `-fno-exceptions` to eliminate exceptions entirely; in such cases, you must check for failures in your C++ code, e.g., check for NULL returned by `new()`.

- If calling backend functions from C++ code, be sure that the C++ call stack contains only plain old data structures (POD). This is necessary because backend errors generate a distant `longjmp()` that does not properly unroll a C++ call stack with non-POD objects.

In summary, it is best to place C++ code behind a wall of `extern C` functions that interface to the backend, and avoid exception, memory, and call stack leakage.

## Function Optimization Information

optimization information

for functions

By default, a function is just a “black box” that the database system knows very little about the behavior of. However, that means that queries using the function may be executed much less efficiently than they could be. It is possible to supply additional knowledge that helps the planner optimize function calls.

Some basic facts can be supplied by declarative annotations provided in the [`CREATE FUNCTION`](#sql-createfunction) command. Most important of these is the function's [volatility category](#xfunc-volatility) (`IMMUTABLE`, `STABLE`, or `VOLATILE`); one should always be careful to specify this correctly when defining a function. The parallel safety property (`PARALLEL UNSAFE`, `PARALLEL RESTRICTED`, or `PARALLEL SAFE`) must also be specified if you hope to use the function in parallelized queries. It can also be useful to specify the function's estimated execution cost, and/or the number of rows a set-returning function is estimated to return. However, the declarative way of specifying those two facts only allows specifying a constant value, which is often inadequate.

It is also possible to attach a planner support function to an SQL-callable function (called its target function), and thereby provide knowledge about the target function that is too complex to be represented declaratively. Planner support functions have to be written in C (although their target functions might not be), so this is an advanced feature that relatively few people will use.

A planner support function must have the SQL signature

    supportfn(internal) returns internal

It is attached to its target function by specifying the `SUPPORT` clause when creating the target function.

The details of the API for planner support functions can be found in file `src/include/nodes/supportnodes.h` in the PostgreSQL source code. Here we provide just an overview of what planner support functions can do. The set of possible requests to a support function is extensible, so more things might be possible in future versions.

Some function calls can be simplified during planning based on properties specific to the function. For example, `int4mul(n, 1)` could be simplified to just `n`. This type of transformation can be performed by a planner support function, by having it implement the `SupportRequestSimplify` request type. The support function will be called for each instance of its target function found in a query parse tree. If it finds that the particular call can be simplified into some other form, it can build and return a parse tree representing that expression. This will automatically work for operators based on the function, too in the example just given, `n * 1` would also be simplified to `n`. (But note that this is just an example; this particular optimization is not actually performed by standard PostgreSQL.) We make no guarantee that PostgreSQL will never call the target function in cases that the support function could simplify. Ensure rigorous equivalence between the simplified expression and an actual execution of the target function.

For target functions that return `boolean`, it is often useful to estimate the fraction of rows that will be selected by a `WHERE` clause using that function. This can be done by a support function that implements the `SupportRequestSelectivity` request type.

If the target function's run time is highly dependent on its inputs, it may be useful to provide a non-constant cost estimate for it. This can be done by a support function that implements the `SupportRequestCost` request type.

For target functions that return sets, it is often useful to provide a non-constant estimate for the number of rows that will be returned. This can be done by a support function that implements the `SupportRequestRows` request type.

For target functions that return `boolean`, it may be possible to convert a function call appearing in `WHERE` into an indexable operator clause or clauses. The converted clauses might be exactly equivalent to the function's condition, or they could be somewhat weaker (that is, they might accept some values that the function condition does not). In the latter case the index condition is said to be lossy; it can still be used to scan an index, but the function call will have to be executed for each row returned by the index to see if it really passes the `WHERE` condition or not. To create such conditions, the support function must implement the `SupportRequestIndexCondition` request type.
