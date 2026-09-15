---
title: xml2 — XPath querying and XSLT functionality
source_url: https://www.postgresql.org/docs/17/xml2.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: xml2.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 3810
---

## xml2 XPath querying and XSLT functionality

xml2

The `xml2` module provides XPath querying and XSLT functionality.

## Deprecation Notice

From PostgreSQL 8.3 on, there is XML-related functionality based on the SQL/XML standard in the core server. That functionality covers XML syntax checking and XPath queries, which is what this module does, and more, but the API is not at all compatible. It is planned that this module will be removed in a future version of PostgreSQL in favor of the newer standard API, so you are encouraged to try converting your applications. If you find that some of the functionality of this module is not available in an adequate form with the newer API, please explain your issue to <pgsql-hackers@lists.postgresql.org> so that the deficiency can be addressed.

## Description of Functions

[ Functions](#xml2-functions-table) shows the functions provided by this module. These functions provide straightforward XML parsing and XPath queries.

<table id="xml2-functions-table">
<caption><code>xml2</code> Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>xml_valid</code> ( <code>document</code> <code>text</code> ) boolean</p>
<p>Parses the given document and returns true if the document is well-formed XML. (Note: this is an alias for the standard PostgreSQL function <code>xml_is_well_formed()</code>. The name <code>xml_valid()</code> is technically incorrect since validity and well-formedness have different meanings in XML.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>xpath_string</code> ( <code>document</code> <code>text</code>, <code>query</code> <code>text</code> ) text</p>
<p>Evaluates the XPath query on the supplied document, and casts the result to <code>text</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>xpath_number</code> ( <code>document</code> <code>text</code>, <code>query</code> <code>text</code> ) real</p>
<p>Evaluates the XPath query on the supplied document, and casts the result to <code>real</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>xpath_bool</code> ( <code>document</code> <code>text</code>, <code>query</code> <code>text</code> ) boolean</p>
<p>Evaluates the XPath query on the supplied document, and casts the result to <code>boolean</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>xpath_nodeset</code> ( <code>document</code> <code>text</code>, <code>query</code> <code>text</code>, <code>toptag</code> <code>text</code>, <code>itemtag</code> <code>text</code> ) text</p>
<p>Evaluates the query on the document and wraps the result in XML tags. If the result is multivalued, the output will look like: &lt;toptag&gt; &lt;itemtag&gt;Value 1 which could be an XML fragment&lt;/itemtag&gt; &lt;itemtag&gt;Value 2....&lt;/itemtag&gt; &lt;/toptag&gt; If either <code>toptag</code> or <code>itemtag</code> is an empty string, the relevant tag is omitted.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>xpath_nodeset</code> ( <code>document</code> <code>text</code>, <code>query</code> <code>text</code>, <code>itemtag</code> <code>text</code> ) text</p>
<p>Like <code>xpath_nodeset(document, query, toptag, itemtag)</code> but result omits <code>toptag</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>xpath_nodeset</code> ( <code>document</code> <code>text</code>, <code>query</code> <code>text</code> ) text</p>
<p>Like <code>xpath_nodeset(document, query, toptag, itemtag)</code> but result omits both tags.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>xpath_list</code> ( <code>document</code> <code>text</code>, <code>query</code> <code>text</code>, <code>separator</code> <code>text</code> ) text</p>
<p>Evaluates the query on the document and returns multiple values separated by the specified separator, for example <code>Value 1,Value 2,Value 3</code> if <code>separator</code> is <code>,</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>xpath_list</code> ( <code>document</code> <code>text</code>, <code>query</code> <code>text</code> ) text</p>
<p>This is a wrapper for the above function that uses <code>,</code> as the separator.</p></td>
</tr>
</tbody>
</table>

## `xpath_table`

xpath_table

xpath_table(text key, text document, text relation, text xpaths, text criteria) returns setof record

`xpath_table` is a table function that evaluates a set of XPath queries on each of a set of documents and returns the results as a table. The primary key field from the original document table is returned as the first column of the result so that the result set can readily be used in joins. The parameters are described in [ Parameters](#xml2-xpath-table-parameters).

| Parameter | Description |
|----|----|
| `key` | the name of the “key” field this is just a field to be used as the first column of the output table, i.e., it identifies the record from which each output row came (see note below about multiple values) |
| `document` | the name of the field containing the XML document |
| `relation` | the name of the table or view containing the documents |
| `xpaths` | one or more XPath expressions, separated by `|` |
| `criteria` | the contents of the WHERE clause. This cannot be omitted, so use `true` or `1=1` if you want to process all the rows in the relation |

`xpath_table` Parameters {#xml2-xpath-table-parameters}

These parameters (except the XPath strings) are just substituted into a plain SQL SELECT statement, so you have some flexibility the statement is

`SELECT <key>, <document> FROM <relation> WHERE <criteria>`

so those parameters can be *anything* valid in those particular locations. The result from this SELECT needs to return exactly two columns (which it will unless you try to list multiple fields for key or document). Beware that this simplistic approach requires that you validate any user-supplied values to avoid SQL injection attacks.

The function has to be used in a `FROM` expression, with an `AS` clause to specify the output columns; for example

    SELECT * FROM
    xpath_table('article_id',
                'article_xml',
                'articles',
                '/article/author|/article/pages|/article/title',
                'date_entered > ''2003-01-01'' ')
    AS t(article_id integer, author text, page_count integer, title text);

The `AS` clause defines the names and types of the columns in the output table. The first is the “key” field and the rest correspond to the XPath queries. If there are more XPath queries than result columns, the extra queries will be ignored. If there are more result columns than XPath queries, the extra columns will be NULL.

Notice that this example defines the page_count result column as an integer. The function deals internally with string representations, so when you say you want an integer in the output, it will take the string representation of the XPath result and use PostgreSQL input functions to transform it into an integer (or whatever type the `AS` clause requests). An error will result if it can't do this for example if the result is empty so you may wish to just stick to `text` as the column type if you think your data has any problems.

The calling `SELECT` statement doesn't necessarily have to be just `SELECT *` it can reference the output columns by name or join them to other tables. The function produces a virtual table with which you can perform any operation you wish (e.g., aggregation, joining, sorting etc.). So we could also have:

    SELECT t.title, p.fullname, p.email
    FROM xpath_table('article_id', 'article_xml', 'articles',
                     '/article/title|/article/author/@id',
                     'xpath_string(article_xml,''/article/@date'') > ''2003-03-20'' ')
           AS t(article_id integer, title text, author_id integer),
         tblPeopleInfo AS p
    WHERE t.author_id = p.person_id;

as a more complicated example. Of course, you could wrap all of this in a view for convenience.

### Multivalued Results

The `xpath_table` function assumes that the results of each XPath query might be multivalued, so the number of rows returned by the function may not be the same as the number of input documents. The first row returned contains the first result from each query, the second row the second result from each query. If one of the queries has fewer values than the others, null values will be returned instead.

In some cases, a user will know that a given XPath query will return only a single result (perhaps a unique document identifier) if used alongside an XPath query returning multiple results, the single-valued result will appear only on the first row of the result. The solution to this is to use the key field as part of a join against a simpler XPath query. As an example:

    CREATE TABLE test (
        id int PRIMARY KEY,
        xml text
    );

    INSERT INTO test VALUES (1, '<doc num="C1">
    <line num="L1"><a>1</a><b>2</b><c>3</c></line>
    <line num="L2"><a>11</a><b>22</b><c>33</c></line>
    </doc>');

    INSERT INTO test VALUES (2, '<doc num="C2">
    <line num="L1"><a>111</a><b>222</b><c>333</c></line>
    <line num="L2"><a>111</a><b>222</b><c>333</c></line>
    </doc>');

    SELECT * FROM
      xpath_table('id','xml','test',
                  '/doc/@num|/doc/line/@num|/doc/line/a|/doc/line/b|/doc/line/c',
                  'true')
      AS t(id int, doc_num varchar(10), line_num varchar(10), val1 int, val2 int, val3 int)
    WHERE id = 1 ORDER BY doc_num, line_num

     id | doc_num | line_num | val1 | val2 | val3
    ----+---------+----------+------+------+------
      1 | C1      | L1       |    1 |    2 |    3
      1 |         | L2       |   11 |   22 |   33

To get `doc_num` on every line, the solution is to use two invocations of `xpath_table` and join the results:

    SELECT t.*,i.doc_num FROM
      xpath_table('id', 'xml', 'test',
                  '/doc/line/@num|/doc/line/a|/doc/line/b|/doc/line/c',
                  'true')
        AS t(id int, line_num varchar(10), val1 int, val2 int, val3 int),
      xpath_table('id', 'xml', 'test', '/doc/@num', 'true')
        AS i(id int, doc_num varchar(10))
    WHERE i.id=t.id AND i.id=1
    ORDER BY doc_num, line_num;

     id | line_num | val1 | val2 | val3 | doc_num
    ----+----------+------+------+------+---------
      1 | L1       |    1 |    2 |    3 | C1
      1 | L2       |   11 |   22 |   33 | C1
    (2 rows)

## XSLT Functions

The following functions are available if libxslt is installed:

### `xslt_process`

xslt_process

xslt_process(text document, text stylesheet, text paramlist) returns text

This function applies the XSL stylesheet to the document and returns the transformed result. The `paramlist` is a list of parameter assignments to be used in the transformation, specified in the form `a=1,b=2`. Note that the parameter parsing is very simple-minded: parameter values cannot contain commas!

There is also a two-parameter version of `xslt_process` which does not pass any parameters to the transformation.

## Author

John Gray <jgray@azuli.co.uk>

Development of this module was sponsored by Torchbox Ltd. (www.torchbox.com). It has the same BSD license as PostgreSQL.
