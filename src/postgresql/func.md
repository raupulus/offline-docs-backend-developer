---
title: Functions and Operators
source_url: https://www.postgresql.org/docs/17/functions.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: func.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 560
---

## Functions and Operators

function

operator

PostgreSQL provides a large number of functions and operators for the built-in data types. This chapter describes most of them, although additional special-purpose functions appear in relevant sections of the manual. Users can also define their own functions and operators, as described in [???](#server-programming). The psql commands `\df` and `\do` can be used to list all available functions and operators, respectively.

The notation used throughout this chapter to describe the argument and result data types of a function or operator is like this: `repeat` ( `text`, `integer` ) text which says that the function `repeat` takes one text and one integer argument and returns a result of type text. The right arrow is also used to indicate the result of an example, thus:

    repeat('Pg', 4) PgPgPgPg

If you are concerned about portability then note that most of the functions and operators described in this chapter, with the exception of the most trivial arithmetic and comparison operators and some explicitly marked functions, are not specified by the SQL standard. Some of this extended functionality is present in other SQL database management systems, and in many cases this functionality is compatible and consistent between the various implementations.

## Logical Operators

operator

logical

Boolean

operators

operators, logical

The usual logical operators are available: <span class="indexterm"></span> <span class="indexterm"></span> <span class="indexterm"></span> <span class="indexterm"></span> <span class="indexterm"></span> <span class="indexterm"></span> `boolean` `AND` `boolean` boolean `boolean` `OR` `boolean` boolean `NOT` `boolean` boolean SQL uses a three-valued logic system with true, false, and `null`, which represents “unknown”. Observe the following truth tables:

| \<a\> | \<b\> | \<a\> AND \<b\> | \<a\> OR \<b\> |
|-------|-------|-----------------|----------------|
| TRUE  | TRUE  | TRUE            | TRUE           |
| TRUE  | FALSE | FALSE           | TRUE           |
| TRUE  | NULL  | NULL            | TRUE           |
| FALSE | FALSE | FALSE           | FALSE          |
| FALSE | NULL  | FALSE           | NULL           |
| NULL  | NULL  | NULL            | NULL           |

| \<a\> | NOT \<a\> |
|-------|-----------|
| TRUE  | FALSE     |
| FALSE | TRUE      |
| NULL  | NULL      |

The operators `AND` and `OR` are commutative, that is, you can switch the left and right operands without affecting the result. (However, it is not guaranteed that the left operand is evaluated before the right operand. See [???](#syntax-express-eval) for more information about the order of evaluation of subexpressions.)

## Comparison Functions and Operators

comparison

operators

The usual comparison operators are available, as shown in [Comparison Operators](#functions-comparison-op-table).

| Operator                               | Description              |
|----------------------------------------|--------------------------|
| \<datatype\> `<` \<datatype\> boolean  | Less than                |
| \<datatype\> `>` \<datatype\> boolean  | Greater than             |
| \<datatype\> `<=` \<datatype\> boolean | Less than or equal to    |
| \<datatype\> `>=` \<datatype\> boolean | Greater than or equal to |
| \<datatype\> `=` \<datatype\> boolean  | Equal                    |
| \<datatype\> `<>` \<datatype\> boolean | Not equal                |
| \<datatype\> `!=` \<datatype\> boolean | Not equal                |

Comparison Operators {#functions-comparison-op-table}

> [!NOTE]
> `<>` is the standard SQL notation for “not equal”. `!=` is an alias, which is converted to `<>` at a very early stage of parsing. Hence, it is not possible to implement `!=` and `<>` operators that do different things.

These comparison operators are available for all built-in data types that have a natural ordering, including numeric, string, and date/time types. In addition, arrays, composite types, and ranges can be compared if their component data types are comparable.

It is usually possible to compare values of related data types as well; for example `integer` `>` `bigint` will work. Some cases of this sort are implemented directly by “cross-type” comparison operators, but if no such operator is available, the parser will coerce the less-general type to the more-general type and apply the latter's comparison operator.

As shown above, all comparison operators are binary operators that return values of type `boolean`. Thus, expressions like `1 < 2 < 3` are not valid (because there is no `<` operator to compare a Boolean value with `3`). Use the `BETWEEN` predicates shown below to perform range tests.

There are also some comparison predicates, as shown in [Comparison Predicates](#functions-comparison-pred-table). These behave much like operators, but have special syntax mandated by the SQL standard.

<table id="functions-comparison-pred-table">
<caption>Comparison Predicates</caption>
<thead>
<tr>
<th><p role="func_signature">Predicate</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature">&lt;datatype&gt; <code>BETWEEN</code> &lt;datatype&gt; <code>AND</code> &lt;datatype&gt; boolean</p>
<p>Between (inclusive of the range endpoints).</p>
<p><code>2 BETWEEN 1 AND 3</code> t</p>
<p><code>2 BETWEEN 3 AND 1</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;datatype&gt; <code>NOT BETWEEN</code> &lt;datatype&gt; <code>AND</code> &lt;datatype&gt; boolean</p>
<p>Not between (the negation of <code>BETWEEN</code>).</p>
<p><code>2 NOT BETWEEN 1 AND 3</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;datatype&gt; <code>BETWEEN SYMMETRIC</code> &lt;datatype&gt; <code>AND</code> &lt;datatype&gt; boolean</p>
<p>Between, after sorting the two endpoint values.</p>
<p><code>2 BETWEEN SYMMETRIC 3 AND 1</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;datatype&gt; <code>NOT BETWEEN SYMMETRIC</code> &lt;datatype&gt; <code>AND</code> &lt;datatype&gt; boolean</p>
<p>Not between, after sorting the two endpoint values.</p>
<p><code>2 NOT BETWEEN SYMMETRIC 3 AND 1</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;datatype&gt; <code>IS DISTINCT FROM</code> &lt;datatype&gt; boolean</p>
<p>Not equal, treating null as a comparable value.</p>
<p><code>1 IS DISTINCT FROM NULL</code> t (rather than <code>NULL</code>)</p>
<p><code>NULL IS DISTINCT FROM NULL</code> f (rather than <code>NULL</code>)</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;datatype&gt; <code>IS NOT DISTINCT FROM</code> &lt;datatype&gt; boolean</p>
<p>Equal, treating null as a comparable value.</p>
<p><code>1 IS NOT DISTINCT FROM NULL</code> f (rather than <code>NULL</code>)</p>
<p><code>NULL IS NOT DISTINCT FROM NULL</code> t (rather than <code>NULL</code>)</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;datatype&gt; <code>IS NULL</code> boolean</p>
<p>Test whether value is null.</p>
<p><code>1.5 IS NULL</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;datatype&gt; <code>IS NOT NULL</code> boolean</p>
<p>Test whether value is not null.</p>
<p><code>'null' IS NOT NULL</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;datatype&gt; <code>ISNULL</code> boolean</p>
<p>Test whether value is null (nonstandard syntax).</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;datatype&gt; <code>NOTNULL</code> boolean</p>
<p>Test whether value is not null (nonstandard syntax).</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>boolean</code> <code>IS TRUE</code> boolean</p>
<p>Test whether boolean expression yields true.</p>
<p><code>true IS TRUE</code> t</p>
<p><code>NULL::boolean IS TRUE</code> f (rather than <code>NULL</code>)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>boolean</code> <code>IS NOT TRUE</code> boolean</p>
<p>Test whether boolean expression yields false or unknown.</p>
<p><code>true IS NOT TRUE</code> f</p>
<p><code>NULL::boolean IS NOT TRUE</code> t (rather than <code>NULL</code>)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>boolean</code> <code>IS FALSE</code> boolean</p>
<p>Test whether boolean expression yields false.</p>
<p><code>true IS FALSE</code> f</p>
<p><code>NULL::boolean IS FALSE</code> f (rather than <code>NULL</code>)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>boolean</code> <code>IS NOT FALSE</code> boolean</p>
<p>Test whether boolean expression yields true or unknown.</p>
<p><code>true IS NOT FALSE</code> t</p>
<p><code>NULL::boolean IS NOT FALSE</code> t (rather than <code>NULL</code>)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>boolean</code> <code>IS UNKNOWN</code> boolean</p>
<p>Test whether boolean expression yields unknown.</p>
<p><code>true IS UNKNOWN</code> f</p>
<p><code>NULL::boolean IS UNKNOWN</code> t (rather than <code>NULL</code>)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>boolean</code> <code>IS NOT UNKNOWN</code> boolean</p>
<p>Test whether boolean expression yields true or false.</p>
<p><code>true IS NOT UNKNOWN</code> t</p>
<p><code>NULL::boolean IS NOT UNKNOWN</code> f (rather than <code>NULL</code>)</p></td>
</tr>
</tbody>
</table>

<span class="indexterm"></span> <span class="indexterm"></span> The BETWEEN predicate simplifies range tests: \<a\> BETWEEN \<x\> AND \<y\> is equivalent to \<a\> \>= \<x\> AND \<a\> \<= \<y\> Notice that BETWEEN treats the endpoint values as included in the range. `BETWEEN SYMMETRIC` is like `BETWEEN` except there is no requirement that the argument to the left of `AND` be less than or equal to the argument on the right. If it is not, those two arguments are automatically swapped, so that a nonempty range is always implied.

The various variants of `BETWEEN` are implemented in terms of the ordinary comparison operators, and therefore will work for any data type(s) that can be compared.

> [!NOTE]
> The use of `AND` in the `BETWEEN` syntax creates an ambiguity with the use of `AND` as a logical operator. To resolve this, only a limited set of expression types are allowed as the second argument of a `BETWEEN` clause. If you need to write a more complex sub-expression in `BETWEEN`, write parentheses around the sub-expression.

<span class="indexterm"></span> <span class="indexterm"></span> Ordinary comparison operators yield null (signifying “unknown”), not true or false, when either input is null. For example, `7 = NULL` yields null, as does `7 <> NULL`. When this behavior is not suitable, use the `IS NOT DISTINCT FROM` predicates: \<a\> IS DISTINCT FROM \<b\> \<a\> IS NOT DISTINCT FROM \<b\> For non-null inputs, `IS DISTINCT FROM` is the same as the `<>` operator. However, if both inputs are null it returns false, and if only one input is null it returns true. Similarly, `IS NOT DISTINCT FROM` is identical to `=` for non-null inputs, but it returns true when both inputs are null, and false when only one input is null. Thus, these predicates effectively act as though null were a normal data value, rather than “unknown”.

<span class="indexterm"></span> <span class="indexterm"></span> <span class="indexterm"></span> <span class="indexterm"></span> To check whether a value is or is not null, use the predicates: \<expression\> IS NULL \<expression\> IS NOT NULL or the equivalent, but nonstandard, predicates: \<expression\> ISNULL \<expression\> NOTNULL <span class="indexterm"></span>

Do *not* write `expression = NULL` because `NULL` is not “equal to” `NULL`. (The null value represents an unknown value, and it is not known whether two unknown values are equal.)

> [!TIP]
> Some applications might expect that `expression = NULL` returns true if \<expression\> evaluates to the null value. It is highly recommended that these applications be modified to comply with the SQL standard. However, if that cannot be done the [???](#guc-transform-null-equals) configuration variable is available. If it is enabled, PostgreSQL will convert `x = NULL` clauses to `x IS NULL`.

If the \<expression\> is row-valued, then `IS NULL` is true when the row expression itself is null or when all the row's fields are null, while `IS NOT NULL` is true when the row expression itself is non-null and all the row's fields are non-null. Because of this behavior, `IS NULL` and `IS NOT NULL` do not always return inverse results for row-valued expressions; in particular, a row-valued expression that contains both null and non-null fields will return false for both tests. For example:

    SELECT ROW(1,2.5,'this is a test') = ROW(1, 3, 'not the same');

    SELECT ROW(table.*) IS NULL FROM table;  -- detect all-null rows

    SELECT ROW(table.*) IS NOT NULL FROM table;  -- detect all-non-null rows

    SELECT NOT(ROW(table.*) IS NOT NULL) FROM TABLE; -- detect at least one null in rows

In some cases, it may be preferable to write \<row\> `IS DISTINCT FROM NULL` or \<row\> `IS NOT DISTINCT FROM NULL`, which will simply check whether the overall row value is null without any additional tests on the row fields.

<span class="indexterm"></span> <span class="indexterm"></span> <span class="indexterm"></span> <span class="indexterm"></span> <span class="indexterm"></span> <span class="indexterm"></span> Boolean values can also be tested using the predicates \<boolean_expression\> IS TRUE \<boolean_expression\> IS NOT TRUE \<boolean_expression\> IS FALSE \<boolean_expression\> IS NOT FALSE \<boolean_expression\> IS UNKNOWN \<boolean_expression\> IS NOT UNKNOWN These will always return true or false, never a null value, even when the operand is null. A null input is treated as the logical value “unknown”. Notice that `IS UNKNOWN` and `IS NOT UNKNOWN` are effectively the same as `IS NULL` and `IS NOT NULL`, respectively, except that the input expression must be of Boolean type.

Some comparison-related functions are also available, as shown in [Comparison Functions](#functions-comparison-func-table).

<table id="functions-comparison-func-table">
<caption>Comparison Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>num_nonnulls</code> ( <code>VARIADIC</code> <code>"any"</code> ) integer</p>
<p>Returns the number of non-null arguments.</p>
<p><code>num_nonnulls(1, NULL, 2)</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>num_nulls</code> ( <code>VARIADIC</code> <code>"any"</code> ) integer</p>
<p>Returns the number of null arguments.</p>
<p><code>num_nulls(1, NULL, 2)</code> 1</p></td>
</tr>
</tbody>
</table>

## Mathematical Functions and Operators

Mathematical operators are provided for many PostgreSQL types. For types without standard mathematical conventions (e.g., date/time types) we describe the actual behavior in subsequent sections.

[Mathematical Operators](#functions-math-op-table) shows the mathematical operators that are available for the standard numeric types. Unless otherwise noted, operators shown as accepting \<numeric_type\> are available for all the types `smallint`, `integer`, `bigint`, `numeric`, `real`, and `double precision`. Operators shown as accepting \<integral_type\> are available for the types `smallint`, `integer`, and `bigint`. Except where noted, each form of an operator returns the same data type as its argument(s). Calls involving multiple argument data types, such as `integer` `+` `numeric`, are resolved by using the type appearing later in these lists.

<table id="functions-math-op-table">
<caption>Mathematical Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature">&lt;numeric_type&gt; <code>+</code> &lt;numeric_type&gt; &lt;numeric_type&gt;</p>
<p>Addition</p>
<p><code>2 + 3</code> 5</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>+</code> &lt;numeric_type&gt; &lt;numeric_type&gt;</p>
<p>Unary plus (no operation)</p>
<p><code>+ 3.5</code> 3.5</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;numeric_type&gt; <code>-</code> &lt;numeric_type&gt; &lt;numeric_type&gt;</p>
<p>Subtraction</p>
<p><code>2 - 3</code> -1</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>-</code> &lt;numeric_type&gt; &lt;numeric_type&gt;</p>
<p>Negation</p>
<p><code>- (-4)</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;numeric_type&gt; <code>*</code> &lt;numeric_type&gt; &lt;numeric_type&gt;</p>
<p>Multiplication</p>
<p><code>2 * 3</code> 6</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;numeric_type&gt; <code>/</code> &lt;numeric_type&gt; &lt;numeric_type&gt;</p>
<p>Division (for integral types, division truncates the result towards zero)</p>
<p><code>5.0 / 2</code> 2.5000000000000000</p>
<p><code>5 / 2</code> 2</p>
<p><code>(-5) / 2</code> -2</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;numeric_type&gt; <code>%</code> &lt;numeric_type&gt; &lt;numeric_type&gt;</p>
<p>Modulo (remainder); available for <code>smallint</code>, <code>integer</code>, <code>bigint</code>, and <code>numeric</code></p>
<p><code>5 % 4</code> 1</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>numeric</code> <code>^</code> <code>numeric</code> numeric</p>
<p role="func_signature"><code>double precision</code> <code>^</code> <code>double precision</code> double precision</p>
<p>Exponentiation</p>
<p><code>2 ^ 3</code> 8</p>
<p>Unlike typical mathematical practice, multiple uses of <code>^</code> will associate left to right by default:</p>
<p><code>2 ^ 3 ^ 3</code> 512</p>
<p><code>2 ^ (3 ^ 3)</code> 134217728</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>|/</code> <code>double precision</code> double precision</p>
<p>Square root</p>
<p><code>|/ 25.0</code> 5</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>||/</code> <code>double precision</code> double precision</p>
<p>Cube root</p>
<p><code>||/ 64.0</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>@</code> &lt;numeric_type&gt; &lt;numeric_type&gt;</p>
<p>Absolute value</p>
<p><code>@ -5.0</code> 5.0</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;integral_type&gt; <code>&amp;</code> &lt;integral_type&gt; &lt;integral_type&gt;</p>
<p>Bitwise AND</p>
<p><code>91 &amp; 15</code> 11</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;integral_type&gt; <code>|</code> &lt;integral_type&gt; &lt;integral_type&gt;</p>
<p>Bitwise OR</p>
<p><code>32 | 3</code> 35</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;integral_type&gt; <code>#</code> &lt;integral_type&gt; &lt;integral_type&gt;</p>
<p>Bitwise exclusive OR</p>
<p><code>17 # 5</code> 20</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>~</code> &lt;integral_type&gt; &lt;integral_type&gt;</p>
<p>Bitwise NOT</p>
<p><code>~1</code> -2</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;integral_type&gt; <code>&lt;&lt;</code> <code>integer</code> &lt;integral_type&gt;</p>
<p>Bitwise shift left</p>
<p><code>1 &lt;&lt; 4</code> 16</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;integral_type&gt; <code>&gt;&gt;</code> <code>integer</code> &lt;integral_type&gt;</p>
<p>Bitwise shift right</p>
<p><code>8 &gt;&gt; 2</code> 2</p></td>
</tr>
</tbody>
</table>

[Mathematical Functions](#functions-math-func-table) shows the available mathematical functions. Many of these functions are provided in multiple forms with different argument types. Except where noted, any given form of a function returns the same data type as its argument(s); cross-type cases are resolved in the same way as explained above for operators. The functions working with `double precision` data are mostly implemented on top of the host system's C library; accuracy and behavior in boundary cases can therefore vary depending on the host system.

<table id="functions-math-func-table">
<caption>Mathematical Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>abs</code> ( &lt;numeric_type&gt; ) &lt;numeric_type&gt;</p>
<p>Absolute value</p>
<p><code>abs(-17.4)</code> 17.4</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>cbrt</code> ( <code>double precision</code> ) double precision</p>
<p>Cube root</p>
<p><code>cbrt(64.0)</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ceil</code> ( <code>numeric</code> ) numeric</p>
<p role="func_signature"><code>ceil</code> ( <code>double precision</code> ) double precision</p>
<p>Nearest integer greater than or equal to argument</p>
<p><code>ceil(42.2)</code> 43</p>
<p><code>ceil(-42.8)</code> -42</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ceiling</code> ( <code>numeric</code> ) numeric</p>
<p role="func_signature"><code>ceiling</code> ( <code>double precision</code> ) double precision</p>
<p>Nearest integer greater than or equal to argument (same as <code>ceil</code>)</p>
<p><code>ceiling(95.3)</code> 96</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>degrees</code> ( <code>double precision</code> ) double precision</p>
<p>Converts radians to degrees</p>
<p><code>degrees(0.5)</code> 28.64788975654116</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>div</code> ( <code>y</code> <code>numeric</code>, <code>x</code> <code>numeric</code> ) numeric</p>
<p>Integer quotient of <code>y</code>/<code>x</code> (truncates towards zero)</p>
<p><code>div(9, 4)</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>erf</code> ( <code>double precision</code> ) double precision</p>
<p>Error function</p>
<p><code>erf(1.0)</code> 0.8427007929497149</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>erfc</code> ( <code>double precision</code> ) double precision</p>
<p>Complementary error function (<code>1 - erf(x)</code>, without loss of precision for large inputs)</p>
<p><code>erfc(1.0)</code> 0.15729920705028513</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>exp</code> ( <code>numeric</code> ) numeric</p>
<p role="func_signature"><code>exp</code> ( <code>double precision</code> ) double precision</p>
<p>Exponential (<code>e</code> raised to the given power)</p>
<p><code>exp(1.0)</code> 2.7182818284590452</p></td>
</tr>
<tr>
<td><p role="func_signature"><span id="function-factorial" class="indexterm"></span> <code>factorial</code> ( <code>bigint</code> ) numeric</p>
<p>Factorial</p>
<p><code>factorial(5)</code> 120</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>floor</code> ( <code>numeric</code> ) numeric</p>
<p role="func_signature"><code>floor</code> ( <code>double precision</code> ) double precision</p>
<p>Nearest integer less than or equal to argument</p>
<p><code>floor(42.8)</code> 42</p>
<p><code>floor(-42.8)</code> -43</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>gcd</code> ( &lt;numeric_type&gt;, &lt;numeric_type&gt; ) &lt;numeric_type&gt;</p>
<p>Greatest common divisor (the largest positive number that divides both inputs with no remainder); returns <code>0</code> if both inputs are zero; available for <code>integer</code>, <code>bigint</code>, and <code>numeric</code></p>
<p><code>gcd(1071, 462)</code> 21</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lcm</code> ( &lt;numeric_type&gt;, &lt;numeric_type&gt; ) &lt;numeric_type&gt;</p>
<p>Least common multiple (the smallest strictly positive number that is an integral multiple of both inputs); returns <code>0</code> if either input is zero; available for <code>integer</code>, <code>bigint</code>, and <code>numeric</code></p>
<p><code>lcm(1071, 462)</code> 23562</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ln</code> ( <code>numeric</code> ) numeric</p>
<p role="func_signature"><code>ln</code> ( <code>double precision</code> ) double precision</p>
<p>Natural logarithm</p>
<p><code>ln(2.0)</code> 0.6931471805599453</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>log</code> ( <code>numeric</code> ) numeric</p>
<p role="func_signature"><code>log</code> ( <code>double precision</code> ) double precision</p>
<p>Base 10 logarithm</p>
<p><code>log(100)</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>log10</code> ( <code>numeric</code> ) numeric</p>
<p role="func_signature"><code>log10</code> ( <code>double precision</code> ) double precision</p>
<p>Base 10 logarithm (same as <code>log</code>)</p>
<p><code>log10(1000)</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>log</code> ( <code>b</code> <code>numeric</code>, <code>x</code> <code>numeric</code> ) numeric</p>
<p>Logarithm of <code>x</code> to base <code>b</code></p>
<p><code>log(2.0, 64.0)</code> 6.0000000000000000</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>min_scale</code> ( <code>numeric</code> ) integer</p>
<p>Minimum scale (number of fractional decimal digits) needed to represent the supplied value precisely</p>
<p><code>min_scale(8.4100)</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>mod</code> ( <code>y</code> &lt;numeric_type&gt;, <code>x</code> &lt;numeric_type&gt; ) &lt;numeric_type&gt;</p>
<p>Remainder of <code>y</code>/<code>x</code>; available for <code>smallint</code>, <code>integer</code>, <code>bigint</code>, and <code>numeric</code></p>
<p><code>mod(9, 4)</code> 1</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pi</code> ( ) double precision</p>
<p>Approximate value of <span class="symbol_font" role="symbol_font"></span></p>
<p><code>pi()</code> 3.141592653589793</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>power</code> ( <code>a</code> <code>numeric</code>, <code>b</code> <code>numeric</code> ) numeric</p>
<p role="func_signature"><code>power</code> ( <code>a</code> <code>double precision</code>, <code>b</code> <code>double precision</code> ) double precision</p>
<p><code>a</code> raised to the power of <code>b</code></p>
<p><code>power(9, 3)</code> 729</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>radians</code> ( <code>double precision</code> ) double precision</p>
<p>Converts degrees to radians</p>
<p><code>radians(45.0)</code> 0.7853981633974483</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>round</code> ( <code>numeric</code> ) numeric</p>
<p role="func_signature"><code>round</code> ( <code>double precision</code> ) double precision</p>
<p>Rounds to nearest integer. For <code>numeric</code>, ties are broken by rounding away from zero. For <code>double precision</code>, the tie-breaking behavior is platform dependent, but “round to nearest even” is the most common rule.</p>
<p><code>round(42.4)</code> 42</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>round</code> ( <code>v</code> <code>numeric</code>, <code>s</code> <code>integer</code> ) numeric</p>
<p>Rounds <code>v</code> to <code>s</code> decimal places. Ties are broken by rounding away from zero.</p>
<p><code>round(42.4382, 2)</code> 42.44</p>
<p><code>round(1234.56, -1)</code> 1230</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>scale</code> ( <code>numeric</code> ) integer</p>
<p>Scale of the argument (the number of decimal digits in the fractional part)</p>
<p><code>scale(8.4100)</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>sign</code> ( <code>numeric</code> ) numeric</p>
<p role="func_signature"><code>sign</code> ( <code>double precision</code> ) double precision</p>
<p>Sign of the argument (-1, 0, or +1)</p>
<p><code>sign(-8.4)</code> -1</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>sqrt</code> ( <code>numeric</code> ) numeric</p>
<p role="func_signature"><code>sqrt</code> ( <code>double precision</code> ) double precision</p>
<p>Square root</p>
<p><code>sqrt(2)</code> 1.4142135623730951</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>trim_scale</code> ( <code>numeric</code> ) numeric</p>
<p>Reduces the value's scale (number of fractional decimal digits) by removing trailing zeroes</p>
<p><code>trim_scale(8.4100)</code> 8.41</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>trunc</code> ( <code>numeric</code> ) numeric</p>
<p role="func_signature"><code>trunc</code> ( <code>double precision</code> ) double precision</p>
<p>Truncates to integer (towards zero)</p>
<p><code>trunc(42.8)</code> 42</p>
<p><code>trunc(-42.8)</code> -42</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>trunc</code> ( <code>v</code> <code>numeric</code>, <code>s</code> <code>integer</code> ) numeric</p>
<p>Truncates <code>v</code> to <code>s</code> decimal places</p>
<p><code>trunc(42.4382, 2)</code> 42.43</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>width_bucket</code> ( <code>operand</code> <code>numeric</code>, <code>low</code> <code>numeric</code>, <code>high</code> <code>numeric</code>, <code>count</code> <code>integer</code> ) integer</p>
<p role="func_signature"><code>width_bucket</code> ( <code>operand</code> <code>double precision</code>, <code>low</code> <code>double precision</code>, <code>high</code> <code>double precision</code>, <code>count</code> <code>integer</code> ) integer</p>
<p>Returns the number of the bucket in which <code>operand</code> falls in a histogram having <code>count</code> equal-width buckets spanning the range <code>low</code> to <code>high</code>. The buckets have inclusive lower bounds and exclusive upper bounds. Returns <code>0</code> for an input less than <code>low</code>, or <code>count+1</code> for an input greater than or equal to <code>high</code>. If <code>low</code> &gt; <code>high</code>, the behavior is mirror-reversed, with bucket <code>1</code> now being the one just below <code>low</code>, and the inclusive bounds now being on the upper side.</p>
<p><code>width_bucket(5.35, 0.024, 10.06, 5)</code> 3</p>
<p><code>width_bucket(9, 10, 0, 10)</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>width_bucket</code> ( <code>operand</code> <code>anycompatible</code>, <code>thresholds</code> <code>anycompatiblearray</code> ) integer</p>
<p>Returns the number of the bucket in which <code>operand</code> falls given an array listing the inclusive lower bounds of the buckets. Returns <code>0</code> for an input less than the first lower bound. <code>operand</code> and the array elements can be of any type having standard comparison operators. The <code>thresholds</code> array <em>must be sorted</em>, smallest first, or unexpected results will be obtained.</p>
<p><code>width_bucket(now(), array['yesterday', 'today', 'tomorrow']::timestamptz[])</code> 2</p></td>
</tr>
</tbody>
</table>

[Random Functions](#functions-math-random-table) shows functions for generating random numbers.

<table id="functions-math-random-table">
<caption>Random Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>random</code> ( ) double precision</p>
<p>Returns a random value in the range 0.0 &lt;= x &lt; 1.0</p>
<p><code>random()</code> 0.897124072839091</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>random</code> ( <code>min</code> <code>integer</code>, <code>max</code> <code>integer</code> ) integer</p>
<p role="func_signature"><code>random</code> ( <code>min</code> <code>bigint</code>, <code>max</code> <code>bigint</code> ) bigint</p>
<p role="func_signature"><code>random</code> ( <code>min</code> <code>numeric</code>, <code>max</code> <code>numeric</code> ) numeric</p>
<p>Returns a random value in the range <code>min</code> &lt;= x &lt;= <code>max</code>. For type <code>numeric</code>, the result will have the same number of fractional decimal digits as <code>min</code> or <code>max</code>, whichever has more.</p>
<p><code>random(1, 10)</code> 7</p>
<p><code>random(-0.499, 0.499)</code> 0.347</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>random_normal</code> ( [<code>mean</code> <code>double precision</code> [, <code>stddev</code> <code>double precision</code>]] ) double precision</p>
<p>Returns a random value from the normal distribution with the given parameters; <code>mean</code> defaults to 0.0 and <code>stddev</code> defaults to 1.0</p>
<p><code>random_normal(0.0, 1.0)</code> 0.051285419</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>setseed</code> ( <code>double precision</code> ) void</p>
<p>Sets the seed for subsequent <code>random()</code> and <code>random_normal()</code> calls; argument must be between -1.0 and 1.0, inclusive</p>
<p><code>setseed(0.12345)</code></p></td>
</tr>
</tbody>
</table>

The `random()` and `random_normal()` functions listed in [Random Functions](#functions-math-random-table) use a deterministic pseudo-random number generator. It is fast but not suitable for cryptographic applications; see the [???](#pgcrypto) module for a more secure alternative. If `setseed()` is called, the series of results of subsequent calls to these functions in the current session can be repeated by re-issuing `setseed()` with the same argument. Without any prior `setseed()` call in the same session, the first call to any of these functions obtains a seed from a platform-dependent source of random bits.

[Trigonometric Functions](#functions-math-trig-table) shows the available trigonometric functions. Each of these functions comes in two variants, one that measures angles in radians and one that measures angles in degrees.

<table id="functions-math-trig-table">
<caption>Trigonometric Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>acos</code> ( <code>double precision</code> ) double precision</p>
<p>Inverse cosine, result in radians</p>
<p><code>acos(1)</code> 0</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>acosd</code> ( <code>double precision</code> ) double precision</p>
<p>Inverse cosine, result in degrees</p>
<p><code>acosd(0.5)</code> 60</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>asin</code> ( <code>double precision</code> ) double precision</p>
<p>Inverse sine, result in radians</p>
<p><code>asin(1)</code> 1.5707963267948966</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>asind</code> ( <code>double precision</code> ) double precision</p>
<p>Inverse sine, result in degrees</p>
<p><code>asind(0.5)</code> 30</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>atan</code> ( <code>double precision</code> ) double precision</p>
<p>Inverse tangent, result in radians</p>
<p><code>atan(1)</code> 0.7853981633974483</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>atand</code> ( <code>double precision</code> ) double precision</p>
<p>Inverse tangent, result in degrees</p>
<p><code>atand(1)</code> 45</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>atan2</code> ( <code>y</code> <code>double precision</code>, <code>x</code> <code>double precision</code> ) double precision</p>
<p>Inverse tangent of <code>y</code>/<code>x</code>, result in radians</p>
<p><code>atan2(1, 0)</code> 1.5707963267948966</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>atan2d</code> ( <code>y</code> <code>double precision</code>, <code>x</code> <code>double precision</code> ) double precision</p>
<p>Inverse tangent of <code>y</code>/<code>x</code>, result in degrees</p>
<p><code>atan2d(1, 0)</code> 90</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>cos</code> ( <code>double precision</code> ) double precision</p>
<p>Cosine, argument in radians</p>
<p><code>cos(0)</code> 1</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>cosd</code> ( <code>double precision</code> ) double precision</p>
<p>Cosine, argument in degrees</p>
<p><code>cosd(60)</code> 0.5</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>cot</code> ( <code>double precision</code> ) double precision</p>
<p>Cotangent, argument in radians</p>
<p><code>cot(0.5)</code> 1.830487721712452</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>cotd</code> ( <code>double precision</code> ) double precision</p>
<p>Cotangent, argument in degrees</p>
<p><code>cotd(45)</code> 1</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>sin</code> ( <code>double precision</code> ) double precision</p>
<p>Sine, argument in radians</p>
<p><code>sin(1)</code> 0.8414709848078965</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>sind</code> ( <code>double precision</code> ) double precision</p>
<p>Sine, argument in degrees</p>
<p><code>sind(30)</code> 0.5</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>tan</code> ( <code>double precision</code> ) double precision</p>
<p>Tangent, argument in radians</p>
<p><code>tan(1)</code> 1.5574077246549023</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>tand</code> ( <code>double precision</code> ) double precision</p>
<p>Tangent, argument in degrees</p>
<p><code>tand(45)</code> 1</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> Another way to work with angles measured in degrees is to use the unit transformation functions `radians()` and `degrees()` shown earlier. However, using the degree-based trigonometric functions is preferred, as that way avoids round-off error for special cases such as `sind(30)`.

[Hyperbolic Functions](#functions-math-hyp-table) shows the available hyperbolic functions.

<table id="functions-math-hyp-table">
<caption>Hyperbolic Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>sinh</code> ( <code>double precision</code> ) double precision</p>
<p>Hyperbolic sine</p>
<p><code>sinh(1)</code> 1.1752011936438014</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>cosh</code> ( <code>double precision</code> ) double precision</p>
<p>Hyperbolic cosine</p>
<p><code>cosh(0)</code> 1</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>tanh</code> ( <code>double precision</code> ) double precision</p>
<p>Hyperbolic tangent</p>
<p><code>tanh(1)</code> 0.7615941559557649</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>asinh</code> ( <code>double precision</code> ) double precision</p>
<p>Inverse hyperbolic sine</p>
<p><code>asinh(1)</code> 0.881373587019543</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>acosh</code> ( <code>double precision</code> ) double precision</p>
<p>Inverse hyperbolic cosine</p>
<p><code>acosh(1)</code> 0</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>atanh</code> ( <code>double precision</code> ) double precision</p>
<p>Inverse hyperbolic tangent</p>
<p><code>atanh(0.5)</code> 0.5493061443340548</p></td>
</tr>
</tbody>
</table>

## String Functions and Operators

This section describes functions and operators for examining and manipulating string values. Strings in this context include values of the types `character`, `character varying`, and `text`. Except where noted, these functions and operators are declared to accept and return type `text`. They will interchangeably accept `character varying` arguments. Values of type `character` will be converted to `text` before the function or operator is applied, resulting in stripping any trailing spaces in the `character` value.

SQL defines some string functions that use key words, rather than commas, to separate arguments. Details are in [ String Functions and Operators](#functions-string-sql). PostgreSQL also provides versions of these functions that use the regular function invocation syntax (see [Other String Functions and Operators](#functions-string-other)).

> [!NOTE]
> The string concatenation operator (`||`) will accept non-string input, so long as at least one input is of string type, as shown in [ String Functions and Operators](#functions-string-sql). For other cases, inserting an explicit coercion to `text` can be used to have non-string input accepted.

<table id="functions-string-sql">
<caption>SQL String Functions and Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Function/Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>text</code> <code>||</code> <code>text</code> text</p>
<p>Concatenates the two strings.</p>
<p><code>'Post' || 'greSQL'</code> PostgreSQL</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>text</code> <code>||</code> <code>anynonarray</code> text</p>
<p role="func_signature"><code>anynonarray</code> <code>||</code> <code>text</code> text</p>
<p>Converts the non-string input to text, then concatenates the two strings. (The non-string input cannot be of an array type, because that would create ambiguity with the array <code>||</code> operators. If you want to concatenate an array's text equivalent, cast it to <code>text</code> explicitly.)</p>
<p><code>'Value: ' || 42</code> Value: 42</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>btrim</code> ( <code>string</code> <code>text</code> [, <code>characters</code> <code>text</code>] ) text</p>
<p>Removes the longest string containing only characters in <code>characters</code> (a space by default) from the start and end of <code>string</code>.</p>
<p><code>btrim('xyxtrimyyx', 'xyz')</code> trim</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>text</code> <code>IS</code> [<code>NOT</code>] [<code>form</code>] <code>NORMALIZED</code> boolean</p>
<p>Checks whether the string is in the specified Unicode normalization form. The optional <code>form</code> key word specifies the form: <code>NFC</code> (the default), <code>NFD</code>, <code>NFKC</code>, or <code>NFKD</code>. This expression can only be used when the server encoding is <code>UTF8</code>. Note that checking for normalization using this expression is often faster than normalizing possibly already normalized strings.</p>
<p><code>U&amp;'\0061\0308bc' IS NFD NORMALIZED</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>bit_length</code> ( <code>text</code> ) integer</p>
<p>Returns number of bits in the string (8 times the <code>octet_length</code>).</p>
<p><code>bit_length('jose')</code> 32</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <span class="indexterm"></span> <code>char_length</code> ( <code>text</code> ) integer</p>
<p role="func_signature"><span class="indexterm"></span> <code>character_length</code> ( <code>text</code> ) integer</p>
<p>Returns number of characters in the string.</p>
<p><code>char_length('jos')</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lower</code> ( <code>text</code> ) text</p>
<p>Converts the string to all lower case, according to the rules of the database's locale.</p>
<p><code>lower('TOM')</code> tom</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lpad</code> ( <code>string</code> <code>text</code>, <code>length</code> <code>integer</code> [, <code>fill</code> <code>text</code>] ) text</p>
<p>Extends the <code>string</code> to length <code>length</code> by prepending the characters <code>fill</code> (a space by default). If the <code>string</code> is already longer than <code>length</code> then it is truncated (on the right).</p>
<p><code>lpad('hi', 5, 'xy')</code> xyxhi</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ltrim</code> ( <code>string</code> <code>text</code> [, <code>characters</code> <code>text</code>] ) text</p>
<p>Removes the longest string containing only characters in <code>characters</code> (a space by default) from the start of <code>string</code>.</p>
<p><code>ltrim('zzzytest', 'xyz')</code> test</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>normalize</code> ( <code>text</code> [, <code>form</code>] ) text</p>
<p>Converts the string to the specified Unicode normalization form. The optional <code>form</code> key word specifies the form: <code>NFC</code> (the default), <code>NFD</code>, <code>NFKC</code>, or <code>NFKD</code>. This function can only be used when the server encoding is <code>UTF8</code>.</p>
<p><code>normalize(U&amp;'\0061\0308bc', NFC)</code> U&amp;'\00E4bc'</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>octet_length</code> ( <code>text</code> ) integer</p>
<p>Returns number of bytes in the string.</p>
<p><code>octet_length('jos')</code> 5 (if server encoding is UTF8)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>octet_length</code> ( <code>character</code> ) integer</p>
<p>Returns number of bytes in the string. Since this version of the function accepts type <code>character</code> directly, it will not strip trailing spaces.</p>
<p><code>octet_length('abc '::character(4))</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>overlay</code> ( <code>string</code> <code>text</code> <code>PLACING</code> <code>newsubstring</code> <code>text</code> <code>FROM</code> <code>start</code> <code>integer</code> [<code>FOR</code> <code>count</code> <code>integer</code>] ) text</p>
<p>Replaces the substring of <code>string</code> that starts at the <code>start</code>'th character and extends for <code>count</code> characters with <code>newsubstring</code>. If <code>count</code> is omitted, it defaults to the length of <code>newsubstring</code>.</p>
<p><code>overlay('Txxxxas' placing 'hom' from 2 for 4)</code> Thomas</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>position</code> ( <code>substring</code> <code>text</code> <code>IN</code> <code>string</code> <code>text</code> ) integer</p>
<p>Returns first starting index of the specified <code>substring</code> within <code>string</code>, or zero if it's not present.</p>
<p><code>position('om' in 'Thomas')</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>rpad</code> ( <code>string</code> <code>text</code>, <code>length</code> <code>integer</code> [, <code>fill</code> <code>text</code>] ) text</p>
<p>Extends the <code>string</code> to length <code>length</code> by appending the characters <code>fill</code> (a space by default). If the <code>string</code> is already longer than <code>length</code> then it is truncated.</p>
<p><code>rpad('hi', 5, 'xy')</code> hixyx</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>rtrim</code> ( <code>string</code> <code>text</code> [, <code>characters</code> <code>text</code>] ) text</p>
<p>Removes the longest string containing only characters in <code>characters</code> (a space by default) from the end of <code>string</code>.</p>
<p><code>rtrim('testxxzx', 'xyz')</code> test</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>substring</code> ( <code>string</code> <code>text</code> [<code>FROM</code> <code>start</code> <code>integer</code>] [<code>FOR</code> <code>count</code> <code>integer</code>] ) text</p>
<p>Extracts the substring of <code>string</code> starting at the <code>start</code>'th character if that is specified, and stopping after <code>count</code> characters if that is specified. Provide at least one of <code>start</code> and <code>count</code>.</p>
<p><code>substring('Thomas' from 2 for 3)</code> hom</p>
<p><code>substring('Thomas' from 3)</code> omas</p>
<p><code>substring('Thomas' for 2)</code> Th</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>substring</code> ( <code>string</code> <code>text</code> <code>FROM</code> <code>pattern</code> <code>text</code> ) text</p>
<p>Extracts the first substring matching POSIX regular expression; see <a href="#functions-posix-regexp"> Regular Expressions</a>.</p>
<p><code>substring('Thomas' from '...$')</code> mas</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>substring</code> ( <code>string</code> <code>text</code> <code>SIMILAR</code> <code>pattern</code> <code>text</code> <code>ESCAPE</code> <code>escape</code> <code>text</code> ) text</p>
<p role="func_signature"><code>substring</code> ( <code>string</code> <code>text</code> <code>FROM</code> <code>pattern</code> <code>text</code> <code>FOR</code> <code>escape</code> <code>text</code> ) text</p>
<p>Extracts the first substring matching SQL regular expression; see <a href="#functions-similarto-regexp"> Regular Expressions</a>. The first form has been specified since SQL:2003; the second form was only in SQL:1999 and should be considered obsolete.</p>
<p><code>substring('Thomas' similar '%#"o_a#"_' escape '#')</code> oma</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>trim</code> ( [<code>LEADING</code> | <code>TRAILING</code> | <code>BOTH</code>] [<code>characters</code> <code>text</code>] <code>FROM</code> <code>string</code> <code>text</code> ) text</p>
<p>Removes the longest string containing only characters in <code>characters</code> (a space by default) from the start, end, or both ends (<code>BOTH</code> is the default) of <code>string</code>.</p>
<p><code>trim(both 'xyz' from 'yxTomxx')</code> Tom</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>trim</code> ( [<code>LEADING</code> | <code>TRAILING</code> | <code>BOTH</code>] [<code>FROM</code>] <code>string</code> <code>text</code> [, <code>characters</code> <code>text</code>] ) text</p>
<p>This is a non-standard syntax for <code>trim()</code>.</p>
<p><code>trim(both from 'yxTomxx', 'xyz')</code> Tom</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>unicode_assigned</code> ( <code>text</code> ) boolean</p>
<p>Returns <code>true</code> if all characters in the string are assigned Unicode codepoints; <code>false</code> otherwise. This function can only be used when the server encoding is <code>UTF8</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>upper</code> ( <code>text</code> ) text</p>
<p>Converts the string to all upper case, according to the rules of the database's locale.</p>
<p><code>upper('tom')</code> TOM</p></td>
</tr>
</tbody>
</table>

Additional string manipulation functions and operators are available and are listed in [Other String Functions and Operators](#functions-string-other). (Some of these are used internally to implement the SQL-standard string functions listed in [ String Functions and Operators](#functions-string-sql).) There are also pattern-matching operators, which are described in [Pattern Matching](#functions-matching), and operators for full-text search, which are described in [???](#textsearch).

<table id="functions-string-other">
<caption>Other String Functions and Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Function/Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>text</code> <code>^@</code> <code>text</code> boolean</p>
<p>Returns true if the first string starts with the second string (equivalent to the <code>starts_with()</code> function).</p>
<p><code>'alphabet' ^@ 'alph'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ascii</code> ( <code>text</code> ) integer</p>
<p>Returns the numeric code of the first character of the argument. In UTF8 encoding, returns the Unicode code point of the character. In other multibyte encodings, the argument must be an ASCII character.</p>
<p><code>ascii('x')</code> 120</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>chr</code> ( <code>integer</code> ) text</p>
<p>Returns the character with the given code. In UTF8 encoding the argument is treated as a Unicode code point. In other multibyte encodings the argument must designate an ASCII character. <code>chr(0)</code> is disallowed because text data types cannot store that character.</p>
<p><code>chr(65)</code> A</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>concat</code> ( <code>val1</code> <code>"any"</code> [, <code>val2</code> <code>"any"</code> [, ...] ] ) text</p>
<p>Concatenates the text representations of all the arguments. NULL arguments are ignored.</p>
<p><code>concat('abcde', 2, NULL, 22)</code> abcde222</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>concat_ws</code> ( <code>sep</code> <code>text</code>, <code>val1</code> <code>"any"</code> [, <code>val2</code> <code>"any"</code> [, ...] ] ) text</p>
<p>Concatenates all but the first argument, with separators. The first argument is used as the separator string, and should not be NULL. Other NULL arguments are ignored.</p>
<p><code>concat_ws(',', 'abcde', 2, NULL, 22)</code> abcde,2,22</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>format</code> ( <code>formatstr</code> <code>text</code> [, <code>formatarg</code> <code>"any"</code> [, ...] ] ) text</p>
<p>Formats arguments according to a format string; see <a href="#functions-string-format"></a>. This function is similar to the C function <code>sprintf</code>.</p>
<p><code>format('Hello %s, %1$s', 'World')</code> Hello World, World</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>initcap</code> ( <code>text</code> ) text</p>
<p>Converts the first letter of each word to upper case and the rest to lower case. Words are sequences of alphanumeric characters separated by non-alphanumeric characters.</p>
<p><code>initcap('hi THOMAS')</code> Hi Thomas</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>left</code> ( <code>string</code> <code>text</code>, <code>n</code> <code>integer</code> ) text</p>
<p>Returns first <code>n</code> characters in the string, or when <code>n</code> is negative, returns all but last |<code>n</code>| characters.</p>
<p><code>left('abcde', 2)</code> ab</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>length</code> ( <code>text</code> ) integer</p>
<p>Returns the number of characters in the string.</p>
<p><code>length('jose')</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>md5</code> ( <code>text</code> ) text</p>
<p>Computes the MD5 <a href="#functions-hash-note">hash</a> of the argument, with the result written in hexadecimal.</p>
<p><code>md5('abc')</code> 900150983cd24fb0​d6963f7d28e17f72</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>parse_ident</code> ( <code>qualified_identifier</code> <code>text</code> [, <code>strict_mode</code> <code>boolean</code> <code>DEFAULT</code> <code>true</code> ] ) text[]</p>
<p>Splits <code>qualified_identifier</code> into an array of identifiers, removing any quoting of individual identifiers. By default, extra characters after the last identifier are considered an error; but if the second parameter is <code>false</code>, then such extra characters are ignored. (This behavior is useful for parsing names for objects like functions.) Note that this function does not truncate over-length identifiers. If you want truncation you can cast the result to <code>name[]</code>.</p>
<p><code>parse_ident('"SomeSchema".someTable')</code> {SomeSchema,sometable}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_client_encoding</code> ( ) name</p>
<p>Returns current client encoding name.</p>
<p><code>pg_client_encoding()</code> UTF8</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>quote_ident</code> ( <code>text</code> ) text</p>
<p>Returns the given string suitably quoted to be used as an identifier in an SQL statement string. Quotes are added only if necessary (i.e., if the string contains non-identifier characters or would be case-folded). Embedded quotes are properly doubled. See also <a href="#plpgsql-quote-literal-example">???</a>.</p>
<p><code>quote_ident('Foo bar')</code> "Foo bar"</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>quote_literal</code> ( <code>text</code> ) text</p>
<p>Returns the given string suitably quoted to be used as a string literal in an SQL statement string. Embedded single-quotes and backslashes are properly doubled. Note that <code>quote_literal</code> returns null on null input; if the argument might be null, <code>quote_nullable</code> is often more suitable. See also <a href="#plpgsql-quote-literal-example">???</a>.</p>
<p><code>quote_literal(E'O\'Reilly')</code> 'O''Reilly'</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>quote_literal</code> ( <code>anyelement</code> ) text</p>
<p>Converts the given value to text and then quotes it as a literal. Embedded single-quotes and backslashes are properly doubled.</p>
<p><code>quote_literal(42.5)</code> '42.5'</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>quote_nullable</code> ( <code>text</code> ) text</p>
<p>Returns the given string suitably quoted to be used as a string literal in an SQL statement string; or, if the argument is null, returns <code>NULL</code>. Embedded single-quotes and backslashes are properly doubled. See also <a href="#plpgsql-quote-literal-example">???</a>.</p>
<p><code>quote_nullable(NULL)</code> NULL</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>quote_nullable</code> ( <code>anyelement</code> ) text</p>
<p>Converts the given value to text and then quotes it as a literal; or, if the argument is null, returns <code>NULL</code>. Embedded single-quotes and backslashes are properly doubled.</p>
<p><code>quote_nullable(42.5)</code> '42.5'</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regexp_count</code> ( <code>string</code> <code>text</code>, <code>pattern</code> <code>text</code> [, <code>start</code> <code>integer</code> [, <code>flags</code> <code>text</code> ] ] ) integer</p>
<p>Returns the number of times the POSIX regular expression <code>pattern</code> matches in the <code>string</code>; see <a href="#functions-posix-regexp"> Regular Expressions</a>.</p>
<p><code>regexp_count('123456789012', '\d\d\d', 2)</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regexp_instr</code> ( <code>string</code> <code>text</code>, <code>pattern</code> <code>text</code> [, <code>start</code> <code>integer</code> [, <code>N</code> <code>integer</code> [, <code>endoption</code> <code>integer</code> [, <code>flags</code> <code>text</code> [, <code>subexpr</code> <code>integer</code> ] ] ] ] ] ) integer</p>
<p>Returns the position within <code>string</code> where the <code>N</code>'th match of the POSIX regular expression <code>pattern</code> occurs, or zero if there is no such match; see <a href="#functions-posix-regexp"> Regular Expressions</a>.</p>
<p><code>regexp_instr('ABCDEF', 'c(.)(..)', 1, 1, 0, 'i')</code> 3</p>
<p><code>regexp_instr('ABCDEF', 'c(.)(..)', 1, 1, 0, 'i', 2)</code> 5</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regexp_like</code> ( <code>string</code> <code>text</code>, <code>pattern</code> <code>text</code> [, <code>flags</code> <code>text</code> ] ) boolean</p>
<p>Checks whether a match of the POSIX regular expression <code>pattern</code> occurs within <code>string</code>; see <a href="#functions-posix-regexp"> Regular Expressions</a>.</p>
<p><code>regexp_like('Hello World', 'world$', 'i')</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regexp_match</code> ( <code>string</code> <code>text</code>, <code>pattern</code> <code>text</code> [, <code>flags</code> <code>text</code> ] ) text[]</p>
<p>Returns substrings within the first match of the POSIX regular expression <code>pattern</code> to the <code>string</code>; see <a href="#functions-posix-regexp"> Regular Expressions</a>.</p>
<p><code>regexp_match('foobarbequebaz', '(bar)(beque)')</code> {bar,beque}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regexp_matches</code> ( <code>string</code> <code>text</code>, <code>pattern</code> <code>text</code> [, <code>flags</code> <code>text</code> ] ) setof text[]</p>
<p>Returns substrings within the first match of the POSIX regular expression <code>pattern</code> to the <code>string</code>, or substrings within all such matches if the <code>g</code> flag is used; see <a href="#functions-posix-regexp"> Regular Expressions</a>.</p>
<p><code>regexp_matches('foobarbequebaz', 'ba.', 'g')</code></p>
<pre><code> {bar}
 {baz}</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regexp_replace</code> ( <code>string</code> <code>text</code>, <code>pattern</code> <code>text</code>, <code>replacement</code> <code>text</code> [, <code>start</code> <code>integer</code> ] [, <code>flags</code> <code>text</code> ] ) text</p>
<p>Replaces the substring that is the first match to the POSIX regular expression <code>pattern</code>, or all such matches if the <code>g</code> flag is used; see <a href="#functions-posix-regexp"> Regular Expressions</a>.</p>
<p><code>regexp_replace('Thomas', '.[mN]a.', 'M')</code> ThM</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>regexp_replace</code> ( <code>string</code> <code>text</code>, <code>pattern</code> <code>text</code>, <code>replacement</code> <code>text</code>, <code>start</code> <code>integer</code>, <code>N</code> <code>integer</code> [, <code>flags</code> <code>text</code> ] ) text</p>
<p>Replaces the substring that is the <code>N</code>'th match to the POSIX regular expression <code>pattern</code>, or all such matches if <code>N</code> is zero; see <a href="#functions-posix-regexp"> Regular Expressions</a>.</p>
<p><code>regexp_replace('Thomas', '.', 'X', 3, 2)</code> ThoXas</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regexp_split_to_array</code> ( <code>string</code> <code>text</code>, <code>pattern</code> <code>text</code> [, <code>flags</code> <code>text</code> ] ) text[]</p>
<p>Splits <code>string</code> using a POSIX regular expression as the delimiter, producing an array of results; see <a href="#functions-posix-regexp"> Regular Expressions</a>.</p>
<p><code>regexp_split_to_array('hello world', '\s+')</code> {hello,world}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regexp_split_to_table</code> ( <code>string</code> <code>text</code>, <code>pattern</code> <code>text</code> [, <code>flags</code> <code>text</code> ] ) setof text</p>
<p>Splits <code>string</code> using a POSIX regular expression as the delimiter, producing a set of results; see <a href="#functions-posix-regexp"> Regular Expressions</a>.</p>
<p><code>regexp_split_to_table('hello world', '\s+')</code></p>
<pre><code> hello
 world</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regexp_substr</code> ( <code>string</code> <code>text</code>, <code>pattern</code> <code>text</code> [, <code>start</code> <code>integer</code> [, <code>N</code> <code>integer</code> [, <code>flags</code> <code>text</code> [, <code>subexpr</code> <code>integer</code> ] ] ] ] ) text</p>
<p>Returns the substring within <code>string</code> that matches the <code>N</code>'th occurrence of the POSIX regular expression <code>pattern</code>, or <code>NULL</code> if there is no such match; see <a href="#functions-posix-regexp"> Regular Expressions</a>.</p>
<p><code>regexp_substr('ABCDEF', 'c(.)(..)', 1, 1, 'i')</code> CDEF</p>
<p><code>regexp_substr('ABCDEF', 'c(.)(..)', 1, 1, 'i', 2)</code> EF</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>repeat</code> ( <code>string</code> <code>text</code>, <code>number</code> <code>integer</code> ) text</p>
<p>Repeats <code>string</code> the specified <code>number</code> of times.</p>
<p><code>repeat('Pg', 4)</code> PgPgPgPg</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>replace</code> ( <code>string</code> <code>text</code>, <code>from</code> <code>text</code>, <code>to</code> <code>text</code> ) text</p>
<p>Replaces all occurrences in <code>string</code> of substring <code>from</code> with substring <code>to</code>.</p>
<p><code>replace('abcdefabcdef', 'cd', 'XX')</code> abXXefabXXef</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>reverse</code> ( <code>text</code> ) text</p>
<p>Reverses the order of the characters in the string.</p>
<p><code>reverse('abcde')</code> edcba</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>right</code> ( <code>string</code> <code>text</code>, <code>n</code> <code>integer</code> ) text</p>
<p>Returns last <code>n</code> characters in the string, or when <code>n</code> is negative, returns all but first |<code>n</code>| characters.</p>
<p><code>right('abcde', 2)</code> de</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>split_part</code> ( <code>string</code> <code>text</code>, <code>delimiter</code> <code>text</code>, <code>n</code> <code>integer</code> ) text</p>
<p>Splits <code>string</code> at occurrences of <code>delimiter</code> and returns the <code>n</code>'th field (counting from one), or when <code>n</code> is negative, returns the |<code>n</code>|'th-from-last field.</p>
<p><code>split_part('abc~@~def~@~ghi', '~@~', 2)</code> def</p>
<p><code>split_part('abc,def,ghi,jkl', ',', -2)</code> ghi</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>starts_with</code> ( <code>string</code> <code>text</code>, <code>prefix</code> <code>text</code> ) boolean</p>
<p>Returns true if <code>string</code> starts with <code>prefix</code>.</p>
<p><code>starts_with('alphabet', 'alph')</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span id="function-string-to-array" class="indexterm"></span> <code>string_to_array</code> ( <code>string</code> <code>text</code>, <code>delimiter</code> <code>text</code> [, <code>null_string</code> <code>text</code>] ) text[]</p>
<p>Splits the <code>string</code> at occurrences of <code>delimiter</code> and forms the resulting fields into a <code>text</code> array. If <code>delimiter</code> is <code>NULL</code>, each character in the <code>string</code> will become a separate element in the array. If <code>delimiter</code> is an empty string, then the <code>string</code> is treated as a single field. If <code>null_string</code> is supplied and is not <code>NULL</code>, fields matching that string are replaced by <code>NULL</code>. See also <a href="#function-array-to-string"><code>array_to_string</code></a>.</p>
<p><code>string_to_array('xx~~yy~~zz', '~~', 'yy')</code> {xx,NULL,zz}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>string_to_table</code> ( <code>string</code> <code>text</code>, <code>delimiter</code> <code>text</code> [, <code>null_string</code> <code>text</code>] ) setof text</p>
<p>Splits the <code>string</code> at occurrences of <code>delimiter</code> and returns the resulting fields as a set of <code>text</code> rows. If <code>delimiter</code> is <code>NULL</code>, each character in the <code>string</code> will become a separate row of the result. If <code>delimiter</code> is an empty string, then the <code>string</code> is treated as a single field. If <code>null_string</code> is supplied and is not <code>NULL</code>, fields matching that string are replaced by <code>NULL</code>.</p>
<p><code>string_to_table('xx~^~yy~^~zz', '~^~', 'yy')</code></p>
<pre><code> xx
 NULL
 zz</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>strpos</code> ( <code>string</code> <code>text</code>, <code>substring</code> <code>text</code> ) integer</p>
<p>Returns first starting index of the specified <code>substring</code> within <code>string</code>, or zero if it's not present. (Same as <code>position(substring in string)</code>, but note the reversed argument order.)</p>
<p><code>strpos('high', 'ig')</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>substr</code> ( <code>string</code> <code>text</code>, <code>start</code> <code>integer</code> [, <code>count</code> <code>integer</code>] ) text</p>
<p>Extracts the substring of <code>string</code> starting at the <code>start</code>'th character, and extending for <code>count</code> characters if that is specified. (Same as <code>substring(string from start for count)</code>.)</p>
<p><code>substr('alphabet', 3)</code> phabet</p>
<p><code>substr('alphabet', 3, 2)</code> ph</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_ascii</code> ( <code>string</code> <code>text</code> ) text</p>
<p role="func_signature"><code>to_ascii</code> ( <code>string</code> <code>text</code>, <code>encoding</code> <code>name</code> ) text</p>
<p role="func_signature"><code>to_ascii</code> ( <code>string</code> <code>text</code>, <code>encoding</code> <code>integer</code> ) text</p>
<p>Converts <code>string</code> to ASCII from another encoding, which may be identified by name or number. If <code>encoding</code> is omitted the database encoding is assumed (which in practice is the only useful case). The conversion consists primarily of dropping accents. Conversion is only supported from <code>LATIN1</code>, <code>LATIN2</code>, <code>LATIN9</code>, and <code>WIN1250</code> encodings. (See the <a href="#unaccent">???</a> module for another, more flexible solution.)</p>
<p><code>to_ascii('Karl')</code> Karel</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_bin</code> ( <code>integer</code> ) text</p>
<p role="func_signature"><code>to_bin</code> ( <code>bigint</code> ) text</p>
<p>Converts the number to its equivalent two's complement binary representation.</p>
<p><code>to_bin(2147483647)</code> 1111111111111111111111111111111</p>
<p><code>to_bin(-1234)</code> 11111111111111111111101100101110</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_hex</code> ( <code>integer</code> ) text</p>
<p role="func_signature"><code>to_hex</code> ( <code>bigint</code> ) text</p>
<p>Converts the number to its equivalent two's complement hexadecimal representation.</p>
<p><code>to_hex(2147483647)</code> 7fffffff</p>
<p><code>to_hex(-1234)</code> fffffb2e</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_oct</code> ( <code>integer</code> ) text</p>
<p role="func_signature"><code>to_oct</code> ( <code>bigint</code> ) text</p>
<p>Converts the number to its equivalent two's complement octal representation.</p>
<p><code>to_oct(2147483647)</code> 17777777777</p>
<p><code>to_oct(-1234)</code> 37777775456</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>translate</code> ( <code>string</code> <code>text</code>, <code>from</code> <code>text</code>, <code>to</code> <code>text</code> ) text</p>
<p>Replaces each character in <code>string</code> that matches a character in the <code>from</code> set with the corresponding character in the <code>to</code> set. If <code>from</code> is longer than <code>to</code>, occurrences of the extra characters in <code>from</code> are deleted.</p>
<p><code>translate('12345', '143', 'ax')</code> a2x5</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>unistr</code> ( <code>text</code> ) text</p>
<p>Evaluate escaped Unicode characters in the argument. Unicode characters can be specified as <code>\XXXX</code> (4 hexadecimal digits), <code>\+XXXXXX</code> (6 hexadecimal digits), <code>\uXXXX</code> (4 hexadecimal digits), or <code>\UXXXXXXXX</code> (8 hexadecimal digits). To specify a backslash, write two backslashes. All other characters are taken literally.</p>
<p>If the server encoding is not UTF-8, the Unicode code point identified by one of these escape sequences is converted to the actual server encoding; an error is reported if that's not possible.</p>
<p>This function provides a (non-standard) alternative to string constants with Unicode escapes (see <a href="#sql-syntax-strings-uescape">???</a>).</p>
<p><code>unistr('d\0061t\+000061')</code> data</p>
<p><code>unistr('d\u0061t\U00000061')</code> data</p></td>
</tr>
</tbody>
</table>

The `concat`, `concat_ws` and `format` functions are variadic, so it is possible to pass the values to be concatenated or formatted as an array marked with the `VARIADIC` keyword (see [???](#xfunc-sql-variadic-functions)). The array's elements are treated as if they were separate ordinary arguments to the function. If the variadic array argument is NULL, `concat` and `concat_ws` return NULL, but `format` treats a NULL as a zero-element array.

See also the aggregate function `string_agg` in [Aggregate Functions](#functions-aggregate), and the functions for converting between strings and the `bytea` type in [Text/Binary String Conversion Functions](#functions-binarystring-conversions).

### `format`

format

The function `format` produces output formatted according to a format string, in a style similar to the C function `sprintf`.

`format`(`formatstr` `text` \[, `formatarg` `"any"` \[, ...\] \]) `formatstr` is a format string that specifies how the result should be formatted. Text in the format string is copied directly to the result, except where format specifiers are used. Format specifiers act as placeholders in the string, defining how subsequent function arguments should be formatted and inserted into the result. Each `formatarg` argument is converted to text according to the usual output rules for its data type, and then formatted and inserted into the result string according to the format specifier(s).

Format specifiers are introduced by a `%` character and have the form %\[`position`\]\[`flags`\]\[`width`\]`type` where the component fields are:

`position` (optional)  
A string of the form `n$` where `n` is the index of the argument to print. Index 1 means the first argument after `formatstr`. If the `position` is omitted, the default is to use the next argument in sequence.

`flags` (optional)  
Additional options controlling how the format specifier's output is formatted. Currently the only supported flag is a minus sign (`-`) which will cause the format specifier's output to be left-justified. This has no effect unless the `width` field is also specified.

`width` (optional)  
Specifies the *minimum* number of characters to use to display the format specifier's output. The output is padded on the left or right (depending on the `-` flag) with spaces as needed to fill the width. A too-small width does not cause truncation of the output, but is simply ignored. The width may be specified using any of the following: a positive integer; an asterisk (`*`) to use the next function argument as the width; or a string of the form `*n$` to use the `n`th function argument as the width.

If the width comes from a function argument, that argument is consumed before the argument that is used for the format specifier's value. If the width argument is negative, the result is left aligned (as if the `-` flag had been specified) within a field of length `abs`(`width`).

`type` (required)  
The type of format conversion to use to produce the format specifier's output. The following types are supported:

- `s` formats the argument value as a simple string. A null value is treated as an empty string.

- `I` treats the argument value as an SQL identifier, double-quoting it if necessary. It is an error for the value to be null (equivalent to `quote_ident`).

- `L` quotes the argument value as an SQL literal. A null value is displayed as the string `NULL`, without quotes (equivalent to `quote_nullable`).

In addition to the format specifiers described above, the special sequence `%%` may be used to output a literal `%` character.

Here are some examples of the basic format conversions:

    SELECT format('Hello %s', 'World');
    Result: Hello World

    SELECT format('Testing %s, %s, %s, %%', 'one', 'two', 'three');
    Result: Testing one, two, three, %

    SELECT format('INSERT INTO %I VALUES(%L)', 'Foo bar', E'O\'Reilly');
    Result: INSERT INTO "Foo bar" VALUES('O''Reilly')

    SELECT format('INSERT INTO %I VALUES(%L)', 'locations', 'C:\Program Files');
    Result: INSERT INTO locations VALUES('C:\Program Files')

Here are examples using `width` fields and the `-` flag:

    SELECT format('|%10s|', 'foo');
    Result: |       foo|

    SELECT format('|%-10s|', 'foo');
    Result: |foo       |

    SELECT format('|%*s|', 10, 'foo');
    Result: |       foo|

    SELECT format('|%*s|', -10, 'foo');
    Result: |foo       |

    SELECT format('|%-*s|', 10, 'foo');
    Result: |foo       |

    SELECT format('|%-*s|', -10, 'foo');
    Result: |foo       |

These examples show use of `position` fields:

    SELECT format('Testing %3$s, %2$s, %1$s', 'one', 'two', 'three');
    Result: Testing three, two, one

    SELECT format('|%*2$s|', 'foo', 10, 'bar');
    Result: |       bar|

    SELECT format('|%1$*2$s|', 'foo', 10, 'bar');
    Result: |       foo|

Unlike the standard C function `sprintf`, PostgreSQL's `format` function allows format specifiers with and without `position` fields to be mixed in the same format string. A format specifier without a `position` field always uses the next argument after the last argument consumed. In addition, the `format` function does not require all function arguments to be used in the format string. For example:

    SELECT format('Testing %3$s, %2$s, %s', 'one', 'two', 'three');
    Result: Testing three, two, three

The `%I` and `%L` format specifiers are particularly useful for safely constructing dynamic SQL statements. See [???](#plpgsql-quote-literal-example).

## Binary String Functions and Operators

binary data

functions

This section describes functions and operators for examining and manipulating binary strings, that is values of type `bytea`. Many of these are equivalent, in purpose and syntax, to the text-string functions described in the previous section.

SQL defines some string functions that use key words, rather than commas, to separate arguments. Details are in [ Binary String Functions and Operators](#functions-binarystring-sql). PostgreSQL also provides versions of these functions that use the regular function invocation syntax (see [Other Binary String Functions](#functions-binarystring-other)).

<table id="functions-binarystring-sql">
<caption>SQL Binary String Functions and Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Function/Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>bytea</code> <code>||</code> <code>bytea</code> bytea</p>
<p>Concatenates the two binary strings.</p>
<p><code>'\x123456'::bytea || '\x789a00bcde'::bytea</code> \x123456789a00bcde</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>bit_length</code> ( <code>bytea</code> ) integer</p>
<p>Returns number of bits in the binary string (8 times the <code>octet_length</code>).</p>
<p><code>bit_length('\x123456'::bytea)</code> 24</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>btrim</code> ( <code>bytes</code> <code>bytea</code>, <code>bytesremoved</code> <code>bytea</code> ) bytea</p>
<p>Removes the longest string containing only bytes appearing in <code>bytesremoved</code> from the start and end of <code>bytes</code>.</p>
<p><code>btrim('\x1234567890'::bytea, '\x9012'::bytea)</code> \x345678</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ltrim</code> ( <code>bytes</code> <code>bytea</code>, <code>bytesremoved</code> <code>bytea</code> ) bytea</p>
<p>Removes the longest string containing only bytes appearing in <code>bytesremoved</code> from the start of <code>bytes</code>.</p>
<p><code>ltrim('\x1234567890'::bytea, '\x9012'::bytea)</code> \x34567890</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>octet_length</code> ( <code>bytea</code> ) integer</p>
<p>Returns number of bytes in the binary string.</p>
<p><code>octet_length('\x123456'::bytea)</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>overlay</code> ( <code>bytes</code> <code>bytea</code> <code>PLACING</code> <code>newsubstring</code> <code>bytea</code> <code>FROM</code> <code>start</code> <code>integer</code> [<code>FOR</code> <code>count</code> <code>integer</code>] ) bytea</p>
<p>Replaces the substring of <code>bytes</code> that starts at the <code>start</code>'th byte and extends for <code>count</code> bytes with <code>newsubstring</code>. If <code>count</code> is omitted, it defaults to the length of <code>newsubstring</code>.</p>
<p><code>overlay('\x1234567890'::bytea placing '\002\003'::bytea from 2 for 3)</code> \x12020390</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>position</code> ( <code>substring</code> <code>bytea</code> <code>IN</code> <code>bytes</code> <code>bytea</code> ) integer</p>
<p>Returns first starting index of the specified <code>substring</code> within <code>bytes</code>, or zero if it's not present.</p>
<p><code>position('\x5678'::bytea in '\x1234567890'::bytea)</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>rtrim</code> ( <code>bytes</code> <code>bytea</code>, <code>bytesremoved</code> <code>bytea</code> ) bytea</p>
<p>Removes the longest string containing only bytes appearing in <code>bytesremoved</code> from the end of <code>bytes</code>.</p>
<p><code>rtrim('\x1234567890'::bytea, '\x9012'::bytea)</code> \x12345678</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>substring</code> ( <code>bytes</code> <code>bytea</code> [<code>FROM</code> <code>start</code> <code>integer</code>] [<code>FOR</code> <code>count</code> <code>integer</code>] ) bytea</p>
<p>Extracts the substring of <code>bytes</code> starting at the <code>start</code>'th byte if that is specified, and stopping after <code>count</code> bytes if that is specified. Provide at least one of <code>start</code> and <code>count</code>.</p>
<p><code>substring('\x1234567890'::bytea from 3 for 2)</code> \x5678</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>trim</code> ( [<code>LEADING</code> | <code>TRAILING</code> | <code>BOTH</code>] <code>bytesremoved</code> <code>bytea</code> <code>FROM</code> <code>bytes</code> <code>bytea</code> ) bytea</p>
<p>Removes the longest string containing only bytes appearing in <code>bytesremoved</code> from the start, end, or both ends (<code>BOTH</code> is the default) of <code>bytes</code>.</p>
<p><code>trim('\x9012'::bytea from '\x1234567890'::bytea)</code> \x345678</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>trim</code> ( [<code>LEADING</code> | <code>TRAILING</code> | <code>BOTH</code>] [<code>FROM</code>] <code>bytes</code> <code>bytea</code>, <code>bytesremoved</code> <code>bytea</code> ) bytea</p>
<p>This is a non-standard syntax for <code>trim()</code>.</p>
<p><code>trim(both from '\x1234567890'::bytea, '\x9012'::bytea)</code> \x345678</p></td>
</tr>
</tbody>
</table>

Additional binary string manipulation functions are available and are listed in [Other Binary String Functions](#functions-binarystring-other). Some of them are used internally to implement the SQL-standard string functions listed in [ Binary String Functions and Operators](#functions-binarystring-sql).

<table id="functions-binarystring-other">
<caption>Other Binary String Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>bit_count</code> ( <code>bytes</code> <code>bytea</code> ) bigint</p>
<p>Returns the number of bits set in the binary string (also known as “popcount”).</p>
<p><code>bit_count('\x1234567890'::bytea)</code> 15</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>get_bit</code> ( <code>bytes</code> <code>bytea</code>, <code>n</code> <code>bigint</code> ) integer</p>
<p>Extracts <a href="#functions-zerobased-note">n'th</a> bit from binary string.</p>
<p><code>get_bit('\x1234567890'::bytea, 30)</code> 1</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>get_byte</code> ( <code>bytes</code> <code>bytea</code>, <code>n</code> <code>integer</code> ) integer</p>
<p>Extracts <a href="#functions-zerobased-note">n'th</a> byte from binary string.</p>
<p><code>get_byte('\x1234567890'::bytea, 4)</code> 144</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <span class="indexterm"></span> <code>length</code> ( <code>bytea</code> ) integer</p>
<p>Returns the number of bytes in the binary string.</p>
<p><code>length('\x1234567890'::bytea)</code> 5</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>length</code> ( <code>bytes</code> <code>bytea</code>, <code>encoding</code> <code>name</code> ) integer</p>
<p>Returns the number of characters in the binary string, assuming that it is text in the given <code>encoding</code>.</p>
<p><code>length('jose'::bytea, 'UTF8')</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>md5</code> ( <code>bytea</code> ) text</p>
<p>Computes the MD5 <a href="#functions-hash-note">hash</a> of the binary string, with the result written in hexadecimal.</p>
<p><code>md5('Th\000omas'::bytea)</code> 8ab2d3c9689aaf18​b4958c334c82d8b1</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>set_bit</code> ( <code>bytes</code> <code>bytea</code>, <code>n</code> <code>bigint</code>, <code>newvalue</code> <code>integer</code> ) bytea</p>
<p>Sets <a href="#functions-zerobased-note">n'th</a> bit in binary string to <code>newvalue</code>.</p>
<p><code>set_bit('\x1234567890'::bytea, 30, 0)</code> \x1234563890</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>set_byte</code> ( <code>bytes</code> <code>bytea</code>, <code>n</code> <code>integer</code>, <code>newvalue</code> <code>integer</code> ) bytea</p>
<p>Sets <a href="#functions-zerobased-note">n'th</a> byte in binary string to <code>newvalue</code>.</p>
<p><code>set_byte('\x1234567890'::bytea, 4, 64)</code> \x1234567840</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>sha224</code> ( <code>bytea</code> ) bytea</p>
<p>Computes the SHA-224 <a href="#functions-hash-note">hash</a> of the binary string.</p>
<p><code>sha224('abc'::bytea)</code> \x23097d223405d8228642a477bda2​55b32aadbce4bda0b3f7e36c9da7</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>sha256</code> ( <code>bytea</code> ) bytea</p>
<p>Computes the SHA-256 <a href="#functions-hash-note">hash</a> of the binary string.</p>
<p><code>sha256('abc'::bytea)</code> \xba7816bf8f01cfea414140de5dae2223​b00361a396177a9cb410ff61f20015ad</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>sha384</code> ( <code>bytea</code> ) bytea</p>
<p>Computes the SHA-384 <a href="#functions-hash-note">hash</a> of the binary string.</p>
<p><code>sha384('abc'::bytea)</code> \xcb00753f45a35e8bb5a03d699ac65007​272c32ab0eded1631a8b605a43ff5bed​8086072ba1e7cc2358baeca134c825a7</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>sha512</code> ( <code>bytea</code> ) bytea</p>
<p>Computes the SHA-512 <a href="#functions-hash-note">hash</a> of the binary string.</p>
<p><code>sha512('abc'::bytea)</code> \xddaf35a193617abacc417349ae204131​12e6fa4e89a97ea20a9eeee64b55d39a​2192992a274fc1a836ba3c23a3feebbd​454d4423643ce80e2a9ac94fa54ca49f</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>substr</code> ( <code>bytes</code> <code>bytea</code>, <code>start</code> <code>integer</code> [, <code>count</code> <code>integer</code>] ) bytea</p>
<p>Extracts the substring of <code>bytes</code> starting at the <code>start</code>'th byte, and extending for <code>count</code> bytes if that is specified. (Same as <code>substring(bytes from start for count)</code>.)</p>
<p><code>substr('\x1234567890'::bytea, 3, 2)</code> \x5678</p></td>
</tr>
</tbody>
</table>

Functions `get_byte` and `set_byte` number the first byte of a binary string as byte 0. Functions `get_bit` and `set_bit` number bits from the right within each byte; for example bit 0 is the least significant bit of the first byte, and bit 15 is the most significant bit of the second byte.

For historical reasons, the function `md5` returns a hex-encoded value of type `text` whereas the SHA-2 functions return type `bytea`. Use the functions [`encode`](#function-encode) and [`decode`](#function-decode) to convert between the two. For example write `encode(sha256('abc'), 'hex')` to get a hex-encoded text representation, or `decode(md5('abc'), 'hex')` to get a `bytea` value.

<span class="indexterm"></span> <span class="indexterm"></span> Functions for converting strings between different character sets (encodings), and for representing arbitrary binary data in textual form, are shown in [Text/Binary String Conversion Functions](#functions-binarystring-conversions). For these functions, an argument or result of type `text` is expressed in the database's default encoding, while arguments or results of type `bytea` are in an encoding named by another argument.

<table id="functions-binarystring-conversions">
<caption>Text/Binary String Conversion Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>convert</code> ( <code>bytes</code> <code>bytea</code>, <code>src_encoding</code> <code>name</code>, <code>dest_encoding</code> <code>name</code> ) bytea</p>
<p>Converts a binary string representing text in encoding <code>src_encoding</code> to a binary string in encoding <code>dest_encoding</code> (see <a href="#multibyte-conversions-supported">???</a> for available conversions).</p>
<p><code>convert('text_in_utf8', 'UTF8', 'LATIN1')</code> \x746578745f696e5f75746638</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>convert_from</code> ( <code>bytes</code> <code>bytea</code>, <code>src_encoding</code> <code>name</code> ) text</p>
<p>Converts a binary string representing text in encoding <code>src_encoding</code> to <code>text</code> in the database encoding (see <a href="#multibyte-conversions-supported">???</a> for available conversions).</p>
<p><code>convert_from('text_in_utf8', 'UTF8')</code> text_in_utf8</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>convert_to</code> ( <code>string</code> <code>text</code>, <code>dest_encoding</code> <code>name</code> ) bytea</p>
<p>Converts a <code>text</code> string (in the database encoding) to a binary string encoded in encoding <code>dest_encoding</code> (see <a href="#multibyte-conversions-supported">???</a> for available conversions).</p>
<p><code>convert_to('some_text', 'UTF8')</code> \x736f6d655f74657874</p></td>
</tr>
<tr>
<td><p role="func_signature"><span id="function-encode" class="indexterm"></span> <code>encode</code> ( <code>bytes</code> <code>bytea</code>, <code>format</code> <code>text</code> ) text</p>
<p>Encodes binary data into a textual representation; supported <code>format</code> values are: <a href="#encode-format-base64"><code>base64</code></a>, <a href="#encode-format-escape"><code>escape</code></a>, <a href="#encode-format-hex"><code>hex</code></a>.</p>
<p><code>encode('123\000\001', 'base64')</code> MTIzAAE=</p></td>
</tr>
<tr>
<td><p role="func_signature"><span id="function-decode" class="indexterm"></span> <code>decode</code> ( <code>string</code> <code>text</code>, <code>format</code> <code>text</code> ) bytea</p>
<p>Decodes binary data from a textual representation; supported <code>format</code> values are the same as for <code>encode</code>.</p>
<p><code>decode('MTIzAAE=', 'base64')</code> \x3132330001</p></td>
</tr>
</tbody>
</table>

The `encode` and `decode` functions support the following textual formats:

base64 <span class="indexterm"></span>  
The `base64` format is that of [RFC 2045 Section 6.8](https://datatracker.ietf.org/doc/html/rfc2045#section-6.8). As per the RFC, encoded lines are broken at 76 characters. However instead of the MIME CRLF end-of-line marker, only a newline is used for end-of-line. The `decode` function ignores carriage-return, newline, space, and tab characters. Otherwise, an error is raised when `decode` is supplied invalid base64 data including when trailing padding is incorrect.

escape <span class="indexterm"></span>  
The `escape` format converts zero bytes and bytes with the high bit set into octal escape sequences (`\`\<nnn\>), and it doubles backslashes. Other byte values are represented literally. The `decode` function will raise an error if a backslash is not followed by either a second backslash or three octal digits; it accepts other byte values unchanged.

hex <span class="indexterm"></span>  
The `hex` format represents each 4 bits of data as one hexadecimal digit, `0` through `f`, writing the higher-order digit of each byte first. The `encode` function outputs the `a`-`f` hex digits in lower case. Because the smallest unit of data is 8 bits, there are always an even number of characters returned by `encode`. The `decode` function accepts the `a`-`f` characters in either upper or lower case. An error is raised when `decode` is given invalid hex data including when given an odd number of characters.

See also the aggregate function `string_agg` in [Aggregate Functions](#functions-aggregate) and the large object functions in [???](#lo-funcs).

## Bit String Functions and Operators

bit strings

functions

This section describes functions and operators for examining and manipulating bit strings, that is values of the types `bit` and `bit varying`. (While only type `bit` is mentioned in these tables, values of type `bit varying` can be used interchangeably.) Bit strings support the usual comparison operators shown in [Comparison Operators](#functions-comparison-op-table), as well as the operators shown in [Bit String Operators](#functions-bit-string-op-table).

<table id="functions-bit-string-op-table">
<caption>Bit String Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>bit</code> <code>||</code> <code>bit</code> bit</p>
<p>Concatenation</p>
<p><code>B'10001' || B'011'</code> 10001011</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>bit</code> <code>&amp;</code> <code>bit</code> bit</p>
<p>Bitwise AND (inputs must be of equal length)</p>
<p><code>B'10001' &amp; B'01101'</code> 00001</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>bit</code> <code>|</code> <code>bit</code> bit</p>
<p>Bitwise OR (inputs must be of equal length)</p>
<p><code>B'10001' | B'01101'</code> 11101</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>bit</code> <code>#</code> <code>bit</code> bit</p>
<p>Bitwise exclusive OR (inputs must be of equal length)</p>
<p><code>B'10001' # B'01101'</code> 11100</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>~</code> <code>bit</code> bit</p>
<p>Bitwise NOT</p>
<p><code>~ B'10001'</code> 01110</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>bit</code> <code>&lt;&lt;</code> <code>integer</code> bit</p>
<p>Bitwise shift left (string length is preserved)</p>
<p><code>B'10001' &lt;&lt; 3</code> 01000</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>bit</code> <code>&gt;&gt;</code> <code>integer</code> bit</p>
<p>Bitwise shift right (string length is preserved)</p>
<p><code>B'10001' &gt;&gt; 2</code> 00100</p></td>
</tr>
</tbody>
</table>

Some of the functions available for binary strings are also available for bit strings, as shown in [Bit String Functions](#functions-bit-string-table).

<table id="functions-bit-string-table">
<caption>Bit String Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>bit_count</code> ( <code>bit</code> ) bigint</p>
<p>Returns the number of bits set in the bit string (also known as “popcount”).</p>
<p><code>bit_count(B'10111')</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>bit_length</code> ( <code>bit</code> ) integer</p>
<p>Returns number of bits in the bit string.</p>
<p><code>bit_length(B'10111')</code> 5</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>length</code> ( <code>bit</code> ) integer</p>
<p>Returns number of bits in the bit string.</p>
<p><code>length(B'10111')</code> 5</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>octet_length</code> ( <code>bit</code> ) integer</p>
<p>Returns number of bytes in the bit string.</p>
<p><code>octet_length(B'1011111011')</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>overlay</code> ( <code>bits</code> <code>bit</code> <code>PLACING</code> <code>newsubstring</code> <code>bit</code> <code>FROM</code> <code>start</code> <code>integer</code> [<code>FOR</code> <code>count</code> <code>integer</code>] ) bit</p>
<p>Replaces the substring of <code>bits</code> that starts at the <code>start</code>'th bit and extends for <code>count</code> bits with <code>newsubstring</code>. If <code>count</code> is omitted, it defaults to the length of <code>newsubstring</code>.</p>
<p><code>overlay(B'01010101010101010' placing B'11111' from 2 for 3)</code> 0111110101010101010</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>position</code> ( <code>substring</code> <code>bit</code> <code>IN</code> <code>bits</code> <code>bit</code> ) integer</p>
<p>Returns first starting index of the specified <code>substring</code> within <code>bits</code>, or zero if it's not present.</p>
<p><code>position(B'010' in B'000001101011')</code> 8</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>substring</code> ( <code>bits</code> <code>bit</code> [<code>FROM</code> <code>start</code> <code>integer</code>] [<code>FOR</code> <code>count</code> <code>integer</code>] ) bit</p>
<p>Extracts the substring of <code>bits</code> starting at the <code>start</code>'th bit if that is specified, and stopping after <code>count</code> bits if that is specified. Provide at least one of <code>start</code> and <code>count</code>.</p>
<p><code>substring(B'110010111111' from 3 for 2)</code> 00</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>get_bit</code> ( <code>bits</code> <code>bit</code>, <code>n</code> <code>integer</code> ) integer</p>
<p>Extracts <code>n</code>'th bit from bit string; the first (leftmost) bit is bit 0.</p>
<p><code>get_bit(B'101010101010101010', 6)</code> 1</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>set_bit</code> ( <code>bits</code> <code>bit</code>, <code>n</code> <code>integer</code>, <code>newvalue</code> <code>integer</code> ) bit</p>
<p>Sets <code>n</code>'th bit in bit string to <code>newvalue</code>; the first (leftmost) bit is bit 0.</p>
<p><code>set_bit(B'101010101010101010', 6, 0)</code> 101010001010101010</p></td>
</tr>
</tbody>
</table>

In addition, it is possible to cast integral values to and from type `bit`. Casting an integer to `bit(n)` copies the rightmost `n` bits. Casting an integer to a bit string width wider than the integer itself will sign-extend on the left. Some examples:

    44::bit(10)                    0000101100
    44::bit(3)                     100
    cast(-44 as bit(12))           111111010100
    '1110'::bit(4)::integer        14

Note that casting to just “bit” means casting to `bit(1)`, and so will deliver only the least significant bit of the integer.

## Pattern Matching

pattern matching

There are three separate approaches to pattern matching provided by PostgreSQL: the traditional SQL `LIKE` operator, the more recent `SIMILAR TO` operator (added in SQL:1999), and POSIX-style regular expressions. Aside from the basic “does this string match this pattern?” operators, functions are available to extract or replace matching substrings and to split a string at matching locations.

> [!TIP]
> If you have pattern matching needs that go beyond this, consider writing a user-defined function in Perl or Tcl.

> [!CAUTION]
> While most regular-expression searches can be executed very quickly, regular expressions can be contrived that take arbitrary amounts of time and memory to process. Be wary of accepting regular-expression search patterns from hostile sources. If you must do so, it is advisable to impose a statement timeout.
>
> Searches using `SIMILAR TO` patterns have the same security hazards, since `SIMILAR TO` provides many of the same capabilities as POSIX-style regular expressions.
>
> `LIKE` searches, being much simpler than the other two options, are safer to use with possibly-hostile pattern sources.

The pattern matching operators of all three kinds do not support nondeterministic collations. If required, apply a different collation to the expression to work around this limitation.

### `LIKE`

LIKE

string

LIKE

pattern

ESCAPE

escape-character

string

NOT LIKE

pattern

ESCAPE

escape-character

The `LIKE` expression returns true if the \<string\> matches the supplied \<pattern\>. (As expected, the `NOT LIKE` expression returns false if `LIKE` returns true, and vice versa. An equivalent expression is `NOT (string LIKE pattern)`.)

If \<pattern\> does not contain percent signs or underscores, then the pattern only represents the string itself; in that case `LIKE` acts like the equals operator. An underscore (`_`) in \<pattern\> stands for (matches) any single character; a percent sign (`%`) matches any sequence of zero or more characters.

Some examples:

    'abc' LIKE 'abc'    true
    'abc' LIKE 'a%'     true
    'abc' LIKE '_b_'    true
    'abc' LIKE 'c'      false

`LIKE` pattern matching always covers the entire string. Therefore, if it's desired to match a sequence anywhere within a string, the pattern must start and end with a percent sign.

To match a literal underscore or percent sign without matching other characters, the respective character in \<pattern\> must be preceded by the escape character. The default escape character is the backslash but a different one can be selected by using the `ESCAPE` clause. To match the escape character itself, write two escape characters.

> [!NOTE]
> If you have [???](#guc-standard-conforming-strings) turned off, any backslashes you write in literal string constants will need to be doubled. See [???](#sql-syntax-strings) for more information.

It's also possible to select no escape character by writing `ESCAPE ''`. This effectively disables the escape mechanism, which makes it impossible to turn off the special meaning of underscore and percent signs in the pattern.

According to the SQL standard, omitting `ESCAPE` means there is no escape character (rather than defaulting to a backslash), and a zero-length `ESCAPE` value is disallowed. PostgreSQL's behavior in this regard is therefore slightly nonstandard.

The key word ILIKE can be used instead of LIKE to make the match case-insensitive according to the active locale. This is not in the SQL standard but is a PostgreSQL extension.

The operator `~~` is equivalent to `LIKE`, and `~~*` corresponds to `ILIKE`. There are also `!~~` and `!~~*` operators that represent `NOT LIKE` and `NOT ILIKE`, respectively. All of these operators are PostgreSQL-specific. You may see these operator names in `EXPLAIN` output and similar places, since the parser actually translates `LIKE` et al. to these operators.

The phrases `LIKE`, `ILIKE`, `NOT LIKE`, and `NOT ILIKE` are generally treated as operators in PostgreSQL syntax; for example they can be used in \<expression\> \<operator\> ANY (\<subquery\>) constructs, although an `ESCAPE` clause cannot be included there. In some obscure cases it may be necessary to use the underlying operator names instead.

Also see the starts-with operator `^@` and the corresponding `starts_with()` function, which are useful in cases where simply matching the beginning of a string is needed.

### `SIMILAR TO` Regular Expressions

regular expression

SIMILAR TO

substring

string

SIMILAR TO

pattern

ESCAPE

escape-character

string

NOT SIMILAR TO

pattern

ESCAPE

escape-character

The `SIMILAR TO` operator returns true or false depending on whether its pattern matches the given string. It is similar to `LIKE`, except that it interprets the pattern using the SQL standard's definition of a regular expression. SQL regular expressions are a curious cross between `LIKE` notation and common (POSIX) regular expression notation.

Like `LIKE`, the `SIMILAR TO` operator succeeds only if its pattern matches the entire string; this is unlike common regular expression behavior where the pattern can match any part of the string. Also like `LIKE`, `SIMILAR TO` uses `_` and `%` as wildcard characters denoting any single character and any string, respectively (these are comparable to `.` and `.*` in POSIX regular expressions).

In addition to these facilities borrowed from `LIKE`, `SIMILAR TO` supports these pattern-matching metacharacters borrowed from POSIX regular expressions:

- `|` denotes alternation (either of two alternatives).

- `*` denotes repetition of the previous item zero or more times.

- `+` denotes repetition of the previous item one or more times.

- `?` denotes repetition of the previous item zero or one time.

- `{`\<m\>`}` denotes repetition of the previous item exactly \<m\> times.

- `{`\<m\>`,}` denotes repetition of the previous item \<m\> or more times.

- `{`\<m\>`,`\<n\>`}` denotes repetition of the previous item at least \<m\> and not more than \<n\> times.

- Parentheses `()` can be used to group items into a single logical item.

- A bracket expression `[...]` specifies a character class, just as in POSIX regular expressions.

Notice that the period (`.`) is not a metacharacter for `SIMILAR TO`.

As with `LIKE`, a backslash disables the special meaning of any of these metacharacters. A different escape character can be specified with `ESCAPE`, or the escape capability can be disabled by writing `ESCAPE ''`.

According to the SQL standard, omitting `ESCAPE` means there is no escape character (rather than defaulting to a backslash), and a zero-length `ESCAPE` value is disallowed. PostgreSQL's behavior in this regard is therefore slightly nonstandard.

Another nonstandard extension is that following the escape character with a letter or digit provides access to the escape sequences defined for POSIX regular expressions; see [Regular Expression Character-Entry Escapes](#posix-character-entry-escapes-table), [Regular Expression Class-Shorthand Escapes](#posix-class-shorthand-escapes-table), and [Regular Expression Constraint Escapes](#posix-constraint-escapes-table) below.

Some examples:

    'abc' SIMILAR TO 'abc'          true
    'abc' SIMILAR TO 'a'            false
    'abc' SIMILAR TO '%(b|d)%'      true
    'abc' SIMILAR TO '(b|c)%'       false
    '-abc-' SIMILAR TO '%\mabc\M%'  true
    'xabcy' SIMILAR TO '%\mabc\M%'  false

The `substring` function with three parameters provides extraction of a substring that matches an SQL regular expression pattern. The function can be written according to standard SQL syntax: substring(\<string\> similar \<pattern\> escape \<escape-character\>) or using the now obsolete SQL:1999 syntax: substring(\<string\> from \<pattern\> for \<escape-character\>) or as a plain three-argument function: substring(\<string\>, \<pattern\>, \<escape-character\>) As with `SIMILAR TO`, the specified pattern must match the entire data string, or else the function fails and returns null. To indicate the part of the pattern for which the matching data sub-string is of interest, the pattern should contain two occurrences of the escape character followed by a double quote (`"`). The text matching the portion of the pattern between these separators is returned when the match is successful.

The escape-double-quote separators actually divide `substring`'s pattern into three independent regular expressions; for example, a vertical bar (`|`) in any of the three sections affects only that section. Also, the first and third of these regular expressions are defined to match the smallest possible amount of text, not the largest, when there is any ambiguity about how much of the data string matches which pattern. (In POSIX parlance, the first and third regular expressions are forced to be non-greedy.)

As an extension to the SQL standard, PostgreSQL allows there to be just one escape-double-quote separator, in which case the third regular expression is taken as empty; or no separators, in which case the first and third regular expressions are taken as empty.

Some examples, with `#"` delimiting the return string:

    substring('foobar' similar '%#"o_b#"%' escape '#')   oob
    substring('foobar' similar '#"o_b#"%' escape '#')    NULL

### POSIX Regular Expressions

regular expression

pattern matching

substring

regexp_count

regexp_instr

regexp_like

regexp_match

regexp_matches

regexp_replace

regexp_split_to_table

regexp_split_to_array

regexp_substr

[Regular Expression Match Operators](#functions-posix-table) lists the available operators for pattern matching using POSIX regular expressions.

<table id="functions-posix-table">
<caption>Regular Expression Match Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>text</code> <code>~</code> <code>text</code> boolean</p>
<p>String matches regular expression, case sensitively</p>
<p><code>'thomas' ~ 't.*ma'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>text</code> <code>~*</code> <code>text</code> boolean</p>
<p>String matches regular expression, case-insensitively</p>
<p><code>'thomas' ~* 'T.*ma'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>text</code> <code>!~</code> <code>text</code> boolean</p>
<p>String does not match regular expression, case sensitively</p>
<p><code>'thomas' !~ 't.*max'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>text</code> <code>!~*</code> <code>text</code> boolean</p>
<p>String does not match regular expression, case-insensitively</p>
<p><code>'thomas' !~* 'T.*ma'</code> f</p></td>
</tr>
</tbody>
</table>

POSIX regular expressions provide a more powerful means for pattern matching than the `LIKE` and `SIMILAR TO` operators. Many Unix tools such as `egrep`, `sed`, or `awk` use a pattern matching language that is similar to the one described here.

A regular expression is a character sequence that is an abbreviated definition of a set of strings (a regular set). A string is said to match a regular expression if it is a member of the regular set described by the regular expression. As with `LIKE`, pattern characters match string characters exactly unless they are special characters in the regular expression language but regular expressions use different special characters than `LIKE` does. Unlike `LIKE` patterns, a regular expression is allowed to match anywhere within a string, unless the regular expression is explicitly anchored to the beginning or end of the string.

Some examples:

    'abcd' ~ 'bc'     true
    'abcd' ~ 'a.c'    true  dot matches any character
    'abcd' ~ 'a.*d'   true  * repeats the preceding pattern item
    'abcd' ~ '(b|x)'  true  | means OR, parentheses group
    'abcd' ~ '^a'     true  ^ anchors to start of string
    'abcd' ~ '^(b|c)' false  would match except for anchoring

The POSIX pattern language is described in much greater detail below.

The `substring` function with two parameters, `substring(string from pattern)`, provides extraction of a substring that matches a POSIX regular expression pattern. It returns null if there is no match, otherwise the first portion of the text that matched the pattern. But if the pattern contains any parentheses, the portion of the text that matched the first parenthesized subexpression (the one whose left parenthesis comes first) is returned. You can put parentheses around the whole expression if you want to use parentheses within it without triggering this exception. If you need parentheses in the pattern before the subexpression you want to extract, see the non-capturing parentheses described below.

Some examples:

    substring('foobar' from 'o.b')     oob
    substring('foobar' from 'o(.)b')   o

The `regexp_count` function counts the number of places where a POSIX regular expression pattern matches a string. It has the syntax `regexp_count`(\<string\>, \<pattern\> \[, \<start\> \[, \<flags\>\]\]). \<pattern\> is searched for in \<string\>, normally from the beginning of the string, but if the \<start\> parameter is provided then beginning from that character index. The \<flags\> parameter is an optional text string containing zero or more single-letter flags that change the function's behavior. For example, including `i` in \<flags\> specifies case-insensitive matching. Supported flags are described in [ARE Embedded-Option Letters](#posix-embedded-options-table).

Some examples:

    regexp_count('ABCABCAXYaxy', 'A.')          3
    regexp_count('ABCABCAXYaxy', 'A.', 1, 'i')  4

The `regexp_instr` function returns the starting or ending position of the \<N\>'th match of a POSIX regular expression pattern to a string, or zero if there is no such match. It has the syntax `regexp_instr`(\<string\>, \<pattern\> \[, \<start\> \[, \<N\> \[, \<endoption\> \[, \<flags\> \[, \<subexpr\>\]\]\]\]\]). \<pattern\> is searched for in \<string\>, normally from the beginning of the string, but if the \<start\> parameter is provided then beginning from that character index. If \<N\> is specified then the \<N\>'th match of the pattern is located, otherwise the first match is located. If the \<endoption\> parameter is omitted or specified as zero, the function returns the position of the first character of the match. Otherwise, \<endoption\> must be one, and the function returns the position of the character following the match. The \<flags\> parameter is an optional text string containing zero or more single-letter flags that change the function's behavior. Supported flags are described in [ARE Embedded-Option Letters](#posix-embedded-options-table). For a pattern containing parenthesized subexpressions, \<subexpr\> is an integer indicating which subexpression is of interest: the result identifies the position of the substring matching that subexpression. Subexpressions are numbered in the order of their leading parentheses. When \<subexpr\> is omitted or zero, the result identifies the position of the whole match regardless of parenthesized subexpressions.

Some examples:

    regexp_instr('number of your street, town zip, FR', '[^,]+', 1, 2)
                                       23
    regexp_instr('ABCDEFGHI', '(c..)(...)', 1, 1, 0, 'i', 2)
                                       6

The `regexp_like` function checks whether a match of a POSIX regular expression pattern occurs within a string, returning boolean true or false. It has the syntax `regexp_like`(\<string\>, \<pattern\> \[, \<flags\>\]). The \<flags\> parameter is an optional text string containing zero or more single-letter flags that change the function's behavior. Supported flags are described in [ARE Embedded-Option Letters](#posix-embedded-options-table). This function has the same results as the `~` operator if no flags are specified. If only the `i` flag is specified, it has the same results as the `~*` operator.

Some examples:

    regexp_like('Hello World', 'world')       false
    regexp_like('Hello World', 'world', 'i')  true

The `regexp_match` function returns a text array of matching substring(s) within the first match of a POSIX regular expression pattern to a string. It has the syntax `regexp_match`(\<string\>, \<pattern\> \[, \<flags\>\]). If there is no match, the result is `NULL`. If a match is found, and the \<pattern\> contains no parenthesized subexpressions, then the result is a single-element text array containing the substring matching the whole pattern. If a match is found, and the \<pattern\> contains parenthesized subexpressions, then the result is a text array whose \<n\>'th element is the substring matching the \<n\>'th parenthesized subexpression of the \<pattern\> (not counting “non-capturing” parentheses; see below for details). The \<flags\> parameter is an optional text string containing zero or more single-letter flags that change the function's behavior. Supported flags are described in [ARE Embedded-Option Letters](#posix-embedded-options-table).

Some examples:

    SELECT regexp_match('foobarbequebaz', 'bar.*que');
     regexp_match
    --------------
     {barbeque}
    (1 row)

    SELECT regexp_match('foobarbequebaz', '(bar)(beque)');
     regexp_match
    --------------
     {bar,beque}
    (1 row)

> [!TIP]
> In the common case where you just want the whole matching substring or `NULL` for no match, the best solution is to use `regexp_substr()`. However, `regexp_substr()` only exists in PostgreSQL version 15 and up. When working in older versions, you can extract the first element of `regexp_match()`'s result, for example:
>
>     SELECT (regexp_match('foobarbequebaz', 'bar.*que'))[1];
>      regexp_match
>     --------------
>      barbeque
>     (1 row)

The `regexp_matches` function returns a set of text arrays of matching substring(s) within matches of a POSIX regular expression pattern to a string. It has the same syntax as `regexp_match`. This function returns no rows if there is no match, one row if there is a match and the `g` flag is not given, or \<N\> rows if there are \<N\> matches and the `g` flag is given. Each returned row is a text array containing the whole matched substring or the substrings matching parenthesized subexpressions of the \<pattern\>, just as described above for `regexp_match`. `regexp_matches` accepts all the flags shown in [ARE Embedded-Option Letters](#posix-embedded-options-table), plus the `g` flag which commands it to return all matches, not just the first one.

Some examples:

    SELECT regexp_matches('foo', 'not there');
     regexp_matches
    ----------------
    (0 rows)

    SELECT regexp_matches('foobarbequebazilbarfbonk', '(b[^b]+)(b[^b]+)', 'g');
     regexp_matches
    ----------------
     {bar,beque}
     {bazil,barf}
    (2 rows)

> [!TIP]
> In most cases `regexp_matches()` should be used with the `g` flag, since if you only want the first match, it's easier and more efficient to use `regexp_match()`. However, `regexp_match()` only exists in PostgreSQL version 10 and up. When working in older versions, a common trick is to place a `regexp_matches()` call in a sub-select, for example:
>
>     SELECT col1, (SELECT regexp_matches(col2, '(bar)(beque)')) FROM tab;
>
> This produces a text array if there's a match, or `NULL` if not, the same as `regexp_match()` would do. Without the sub-select, this query would produce no output at all for table rows without a match, which is typically not the desired behavior.

The `regexp_replace` function provides substitution of new text for substrings that match POSIX regular expression patterns. It has the syntax `regexp_replace`(\<source\>, \<pattern\>, \<replacement\> \[, \<start\> \[, \<N\>\]\] \[, \<flags\>\]). (Notice that \<N\> cannot be specified unless \<start\> is, but \<flags\> can be given in any case.) The \<source\> string is returned unchanged if there is no match to the \<pattern\>. If there is a match, the \<source\> string is returned with the \<replacement\> string substituted for the matching substring. The \<replacement\> string can contain `\`\<n\>, where \<n\> is 1 through 9, to indicate that the source substring matching the \<n\>'th parenthesized subexpression of the pattern should be inserted, and it can contain `\&` to indicate that the substring matching the entire pattern should be inserted. Write `\\` if you need to put a literal backslash in the replacement text. \<pattern\> is searched for in \<string\>, normally from the beginning of the string, but if the \<start\> parameter is provided then beginning from that character index. By default, only the first match of the pattern is replaced. If \<N\> is specified and is greater than zero, then the \<N\>'th match of the pattern is replaced. If the `g` flag is given, or if \<N\> is specified and is zero, then all matches at or after the \<start\> position are replaced. (The `g` flag is ignored when \<N\> is specified.) The \<flags\> parameter is an optional text string containing zero or more single-letter flags that change the function's behavior. Supported flags (though not `g`) are described in [ARE Embedded-Option Letters](#posix-embedded-options-table).

Some examples:

    regexp_replace('foobarbaz', 'b..', 'X')
                                       fooXbaz
    regexp_replace('foobarbaz', 'b..', 'X', 'g')
                                       fooXX
    regexp_replace('foobarbaz', 'b(..)', 'X\1Y', 'g')
                                       fooXarYXazY
    regexp_replace('A PostgreSQL function', 'a|e|i|o|u', 'X', 1, 0, 'i')
                                       X PXstgrXSQL fXnctXXn
    regexp_replace('A PostgreSQL function', 'a|e|i|o|u', 'X', 1, 3, 'i')
                                       A PostgrXSQL function

The `regexp_split_to_table` function splits a string using a POSIX regular expression pattern as a delimiter. It has the syntax `regexp_split_to_table`(\<string\>, \<pattern\> \[, \<flags\>\]). If there is no match to the \<pattern\>, the function returns the \<string\>. If there is at least one match, for each match it returns the text from the end of the last match (or the beginning of the string) to the beginning of the match. When there are no more matches, it returns the text from the end of the last match to the end of the string. The \<flags\> parameter is an optional text string containing zero or more single-letter flags that change the function's behavior. `regexp_split_to_table` supports the flags described in [ARE Embedded-Option Letters](#posix-embedded-options-table).

The `regexp_split_to_array` function behaves the same as `regexp_split_to_table`, except that `regexp_split_to_array` returns its result as an array of `text`. It has the syntax `regexp_split_to_array`(\<string\>, \<pattern\> \[, \<flags\>\]). The parameters are the same as for `regexp_split_to_table`.

Some examples:

    SELECT foo FROM regexp_split_to_table('the quick brown fox jumps over the lazy dog', '\s+') AS foo;
      foo
    -------
     the
     quick
     brown
     fox
     jumps
     over
     the
     lazy
     dog
    (9 rows)

    SELECT regexp_split_to_array('the quick brown fox jumps over the lazy dog', '\s+');
                  regexp_split_to_array
    -----------------------------------------------
     {the,quick,brown,fox,jumps,over,the,lazy,dog}
    (1 row)

    SELECT foo FROM regexp_split_to_table('the quick brown fox', '\s*') AS foo;
     foo
    -----
     t
     h
     e
     q
     u
     i
     c
     k
     b
     r
     o
     w
     n
     f
     o
     x
    (16 rows)

As the last example demonstrates, the regexp split functions ignore zero-length matches that occur at the start or end of the string or immediately after a previous match. This is contrary to the strict definition of regexp matching that is implemented by the other regexp functions, but is usually the most convenient behavior in practice. Other software systems such as Perl use similar definitions.

The `regexp_substr` function returns the substring that matches a POSIX regular expression pattern, or `NULL` if there is no match. It has the syntax `regexp_substr`(\<string\>, \<pattern\> \[, \<start\> \[, \<N\> \[, \<flags\> \[, \<subexpr\>\]\]\]\]). \<pattern\> is searched for in \<string\>, normally from the beginning of the string, but if the \<start\> parameter is provided then beginning from that character index. If \<N\> is specified then the \<N\>'th match of the pattern is returned, otherwise the first match is returned. The \<flags\> parameter is an optional text string containing zero or more single-letter flags that change the function's behavior. Supported flags are described in [ARE Embedded-Option Letters](#posix-embedded-options-table). For a pattern containing parenthesized subexpressions, \<subexpr\> is an integer indicating which subexpression is of interest: the result is the substring matching that subexpression. Subexpressions are numbered in the order of their leading parentheses. When \<subexpr\> is omitted or zero, the result is the whole match regardless of parenthesized subexpressions.

Some examples:

    regexp_substr('number of your street, town zip, FR', '[^,]+', 1, 2)
                                        town zip
    regexp_substr('ABCDEFGHI', '(c..)(...)', 1, 1, 'i', 2)
                                       FGH

#### Regular Expression Details

PostgreSQL's regular expressions are implemented using a software package written by Henry Spencer. Much of the description of regular expressions below is copied verbatim from his manual.

Regular expressions (REs), as defined in POSIX 1003.2, come in two forms: extended REs or EREs (roughly those of `egrep`), and basic REs or BREs (roughly those of `ed`). PostgreSQL supports both forms, and also implements some extensions that are not in the POSIX standard, but have become widely used due to their availability in programming languages such as Perl and Tcl. REs using these non-POSIX extensions are called advanced REs or AREs in this documentation. AREs are almost an exact superset of EREs, but BREs have several notational incompatibilities (as well as being much more limited). We first describe the ARE and ERE forms, noting features that apply only to AREs, and then describe how BREs differ.

> [!NOTE]
> PostgreSQL always initially presumes that a regular expression follows the ARE rules. However, the more limited ERE or BRE rules can be chosen by prepending an embedded option to the RE pattern, as described in [Regular Expression Metasyntax](#posix-metasyntax). This can be useful for compatibility with applications that expect exactly the POSIX 1003.2 rules.

A regular expression is defined as one or more branches, separated by `|`. It matches anything that matches one of the branches.

A branch is zero or more quantified atoms or constraints, concatenated. It matches a match for the first, followed by a match for the second, etc.; an empty branch matches the empty string.

A quantified atom is an atom possibly followed by a single quantifier. Without a quantifier, it matches a match for the atom. With a quantifier, it can match some number of matches of the atom. An atom can be any of the possibilities shown in [Regular Expression Atoms](#posix-atoms-table). The possible quantifiers and their meanings are shown in [Regular Expression Quantifiers](#posix-quantifiers-table).

A constraint matches an empty string, but matches only when specific conditions are met. A constraint can be used where an atom could be used, except it cannot be followed by a quantifier. The simple constraints are shown in [Regular Expression Constraints](#posix-constraints-table); some more constraints are described later.

| Atom | Description |
|----|----|
| `(`\<re\>`)` | (where \<re\> is any regular expression) matches a match for \<re\>, with the match noted for possible reporting |
| `(?:`\<re\>`)` | as above, but the match is not noted for reporting (a “non-capturing” set of parentheses) (AREs only) |
| `.` | matches any single character |
| `[`\<chars\>`]` | a bracket expression, matching any one of the \<chars\> (see [Bracket Expressions](#posix-bracket-expressions) for more detail) |
| `\`\<k\> | (where \<k\> is a non-alphanumeric character) matches that character taken as an ordinary character, e.g., `\\` matches a backslash character |
| `\`\<c\> | where \<c\> is alphanumeric (possibly followed by other characters) is an escape, see [Regular Expression Escapes](#posix-escape-sequences) (AREs only; in EREs and BREs, this matches \<c\>) |
| `{` | when followed by a character other than a digit, matches the left-brace character `{`; when followed by a digit, it is the beginning of a \<bound\> (see below) |
| \<x\> | where \<x\> is a single character with no other significance, matches that character |

Regular Expression Atoms {#posix-atoms-table}

An RE cannot end with a backslash (`\`).

> [!NOTE]
> If you have [???](#guc-standard-conforming-strings) turned off, any backslashes you write in literal string constants will need to be doubled. See [???](#sql-syntax-strings) for more information.

| Quantifier | Matches |
|----|----|
| `*` | a sequence of 0 or more matches of the atom |
| `+` | a sequence of 1 or more matches of the atom |
| `?` | a sequence of 0 or 1 matches of the atom |
| `{`\<m\>`}` | a sequence of exactly \<m\> matches of the atom |
| `{`\<m\>`,}` | a sequence of \<m\> or more matches of the atom |
| `{`\<m\>`,`\<n\>`}` | a sequence of \<m\> through \<n\> (inclusive) matches of the atom; \<m\> cannot exceed \<n\> |
| `*?` | non-greedy version of `*` |
| `+?` | non-greedy version of `+` |
| `??` | non-greedy version of `?` |
| `{`\<m\>`}?` | non-greedy version of `{`\<m\>`}` |
| `{`\<m\>`,}?` | non-greedy version of `{`\<m\>`,}` |
| `{`\<m\>`,`\<n\>`}?` | non-greedy version of `{`\<m\>`,`\<n\>`}` |

Regular Expression Quantifiers {#posix-quantifiers-table}

The forms using `{`\<...\>`}` are known as bounds. The numbers \<m\> and \<n\> within a bound are unsigned decimal integers with permissible values from 0 to 255 inclusive.

Non-greedy quantifiers (available in AREs only) match the same possibilities as their corresponding normal (greedy) counterparts, but prefer the smallest number rather than the largest number of matches. See [Regular Expression Matching Rules](#posix-matching-rules) for more detail.

> [!NOTE]
> A quantifier cannot immediately follow another quantifier, e.g., `**` is invalid. A quantifier cannot begin an expression or subexpression or follow `^` or `|`.

| Constraint | Description |
|----|----|
| `^` | matches at the beginning of the string |
| `$` | matches at the end of the string |
| `(?=`\<re\>`)` | positive lookahead matches at any point where a substring matching \<re\> begins (AREs only) |
| `(?!`\<re\>`)` | negative lookahead matches at any point where no substring matching \<re\> begins (AREs only) |
| `(?<=`\<re\>`)` | positive lookbehind matches at any point where a substring matching \<re\> ends (AREs only) |
| `(?<!`\<re\>`)` | negative lookbehind matches at any point where no substring matching \<re\> ends (AREs only) |

Regular Expression Constraints {#posix-constraints-table}

Lookahead and lookbehind constraints cannot contain back references (see [Regular Expression Escapes](#posix-escape-sequences)), and all parentheses within them are considered non-capturing.

#### Bracket Expressions

A bracket expression is a list of characters enclosed in `[]`. It normally matches any single character from the list (but see below). If the list begins with `^`, it matches any single character *not* from the rest of the list. If two characters in the list are separated by `-`, this is shorthand for the full range of characters between those two (inclusive) in the collating sequence, e.g., `[0-9]` in ASCII matches any decimal digit. It is illegal for two ranges to share an endpoint, e.g., `a-c-e`. Ranges are very collating-sequence-dependent, so portable programs should avoid relying on them.

To include a literal `]` in the list, make it the first character (after `^`, if that is used). To include a literal `-`, make it the first or last character, or the second endpoint of a range. To use a literal `-` as the first endpoint of a range, enclose it in `[.` and `.]` to make it a collating element (see below). With the exception of these characters, some combinations using `[` (see next paragraphs), and escapes (AREs only), all other special characters lose their special significance within a bracket expression. In particular, `\` is not special when following ERE or BRE rules, though it is special (as introducing an escape) in AREs.

Within a bracket expression, a collating element (a character, a multiple-character sequence that collates as if it were a single character, or a collating-sequence name for either) enclosed in `[.` and `.]` stands for the sequence of characters of that collating element. The sequence is treated as a single element of the bracket expression's list. This allows a bracket expression containing a multiple-character collating element to match more than one character, e.g., if the collating sequence includes a `ch` collating element, then the RE `[[.ch.]]*c` matches the first five characters of `chchcc`.

> [!NOTE]
> PostgreSQL currently does not support multi-character collating elements. This information describes possible future behavior.

Within a bracket expression, a collating element enclosed in `[=` and `=]` is an equivalence class, standing for the sequences of characters of all collating elements equivalent to that one, including itself. (If there are no other equivalent collating elements, the treatment is as if the enclosing delimiters were `[.` and `.]`.) For example, if `o` and `^` are the members of an equivalence class, then `[[=o=]]`, `[[=^=]]`, and `[o^]` are all synonymous. An equivalence class cannot be an endpoint of a range.

Within a bracket expression, the name of a character class enclosed in `[:` and `:]` stands for the list of all characters belonging to that class. A character class cannot be used as an endpoint of a range. The POSIX standard defines these character class names: `alnum` (letters and numeric digits), `alpha` (letters), `blank` (space and tab), `cntrl` (control characters), `digit` (numeric digits), `graph` (printable characters except space), `lower` (lower-case letters), `print` (printable characters including space), `punct` (punctuation), `space` (any white space), `upper` (upper-case letters), and `xdigit` (hexadecimal digits). The behavior of these standard character classes is generally consistent across platforms for characters in the 7-bit ASCII set. Whether a given non-ASCII character is considered to belong to one of these classes depends on the collation that is used for the regular-expression function or operator (see [???](#collation)), or by default on the database's `LC_CTYPE` locale setting (see [???](#locale)). The classification of non-ASCII characters can vary across platforms even in similarly-named locales. (But the `C` locale never considers any non-ASCII characters to belong to any of these classes.) In addition to these standard character classes, PostgreSQL defines the `word` character class, which is the same as `alnum` plus the underscore (`_`) character, and the `ascii` character class, which contains exactly the 7-bit ASCII set.

There are two special cases of bracket expressions: the bracket expressions `[[:<:]]` and `[[:>:]]` are constraints, matching empty strings at the beginning and end of a word respectively. A word is defined as a sequence of word characters that is neither preceded nor followed by word characters. A word character is any character belonging to the `word` character class, that is, any letter, digit, or underscore. This is an extension, compatible with but not specified by POSIX 1003.2, and should be used with caution in software intended to be portable to other systems. The constraint escapes described below are usually preferable; they are no more standard, but are easier to type.

#### Regular Expression Escapes

Escapes are special sequences beginning with `\` followed by an alphanumeric character. Escapes come in several varieties: character entry, class shorthands, constraint escapes, and back references. A `\` followed by an alphanumeric character but not constituting a valid escape is illegal in AREs. In EREs, there are no escapes: outside a bracket expression, a `\` followed by an alphanumeric character merely stands for that character as an ordinary character, and inside a bracket expression, `\` is an ordinary character. (The latter is the one actual incompatibility between EREs and AREs.)

Character-entry escapes exist to make it easier to specify non-printing and other inconvenient characters in REs. They are shown in [Regular Expression Character-Entry Escapes](#posix-character-entry-escapes-table).

Class-shorthand escapes provide shorthands for certain commonly-used character classes. They are shown in [Regular Expression Class-Shorthand Escapes](#posix-class-shorthand-escapes-table).

A constraint escape is a constraint, matching the empty string if specific conditions are met, written as an escape. They are shown in [Regular Expression Constraint Escapes](#posix-constraint-escapes-table).

A back reference (`\`\<n\>) matches the same string matched by the previous parenthesized subexpression specified by the number \<n\> (see [Regular Expression Back References](#posix-constraint-backref-table)). For example, `([bc])\1` matches `bb` or `cc` but not `bc` or `cb`. The subexpression must entirely precede the back reference in the RE. Subexpressions are numbered in the order of their leading parentheses. Non-capturing parentheses do not define subexpressions. The back reference considers only the string characters matched by the referenced subexpression, not any constraints contained in it. For example, `(^\d)\1` will match `22`.

| Escape | Description |
|----|----|
| `\a` | alert (bell) character, as in C |
| `\b` | backspace, as in C |
| `\B` | synonym for backslash (`\`) to help reduce the need for backslash doubling |
| `\c`\<X\> | (where \<X\> is any character) the character whose low-order 5 bits are the same as those of \<X\>, and whose other bits are all zero |
| `\e` | the character whose collating-sequence name is `ESC`, or failing that, the character with octal value `033` |
| `\f` | form feed, as in C |
| `\n` | newline, as in C |
| `\r` | carriage return, as in C |
| `\t` | horizontal tab, as in C |
| `\u`\<wxyz\> | (where \<wxyz\> is exactly four hexadecimal digits) the character whose hexadecimal value is `0x`\<wxyz\> |
| `\U`\<stuvwxyz\> | (where \<stuvwxyz\> is exactly eight hexadecimal digits) the character whose hexadecimal value is `0x`\<stuvwxyz\> |
| `\v` | vertical tab, as in C |
| `\x`\<hhh\> | (where \<hhh\> is any sequence of hexadecimal digits) the character whose hexadecimal value is `0x`\<hhh\> (a single character no matter how many hexadecimal digits are used) |
| `\0` | the character whose value is `0` (the null byte) |
| `\`\<xy\> | (where \<xy\> is exactly two octal digits, and is not a back reference) the character whose octal value is `0`\<xy\> |
| `\`\<xyz\> | (where \<xyz\> is exactly three octal digits, and is not a back reference) the character whose octal value is `0`\<xyz\> |

Regular Expression Character-Entry Escapes {#posix-character-entry-escapes-table}

Hexadecimal digits are `0`-`9`, `a`-`f`, and `A`-`F`. Octal digits are `0`-`7`.

Numeric character-entry escapes specifying values outside the ASCII range (0127) have meanings dependent on the database encoding. When the encoding is UTF-8, escape values are equivalent to Unicode code points, for example `\u1234` means the character `U+1234`. For other multibyte encodings, character-entry escapes usually just specify the concatenation of the byte values for the character. If the escape value does not correspond to any legal character in the database encoding, no error will be raised, but it will never match any data.

The character-entry escapes are always taken as ordinary characters. For example, `\135` is `]` in ASCII, but `\135` does not terminate a bracket expression.

| Escape | Description                                               |
|--------|-----------------------------------------------------------|
| `\d`   | matches any digit, like `[[:digit:]]`                     |
| `\s`   | matches any whitespace character, like `[[:space:]]`      |
| `\w`   | matches any word character, like `[[:word:]]`             |
| `\D`   | matches any non-digit, like `[^[:digit:]]`                |
| `\S`   | matches any non-whitespace character, like `[^[:space:]]` |
| `\W`   | matches any non-word character, like `[^[:word:]]`        |

Regular Expression Class-Shorthand Escapes {#posix-class-shorthand-escapes-table}

The class-shorthand escapes also work within bracket expressions, although the definitions shown above are not quite syntactically valid in that context. For example, `[a-c\d]` is equivalent to `[a-c[:digit:]]`.

| Escape | Description |
|----|----|
| `\A` | matches only at the beginning of the string (see [Regular Expression Matching Rules](#posix-matching-rules) for how this differs from `^`) |
| `\m` | matches only at the beginning of a word |
| `\M` | matches only at the end of a word |
| `\y` | matches only at the beginning or end of a word |
| `\Y` | matches only at a point that is not the beginning or end of a word |
| `\Z` | matches only at the end of the string (see [Regular Expression Matching Rules](#posix-matching-rules) for how this differs from `$`) |

Regular Expression Constraint Escapes {#posix-constraint-escapes-table}

A word is defined as in the specification of `[[:<:]]` and `[[:>:]]` above. Constraint escapes are illegal within bracket expressions.

| Escape | Description |
|----|----|
| `\`\<m\> | (where \<m\> is a nonzero digit) a back reference to the \<m\>'th subexpression |
| `\`\<mnn\> | (where \<m\> is a nonzero digit, and \<nn\> is some more digits, and the decimal value \<mnn\> is not greater than the number of closing capturing parentheses seen so far) a back reference to the \<mnn\>'th subexpression |

Regular Expression Back References {#posix-constraint-backref-table}

> [!NOTE]
> There is an inherent ambiguity between octal character-entry escapes and back references, which is resolved by the following heuristics, as hinted at above. A leading zero always indicates an octal escape. A single non-zero digit, not followed by another digit, is always taken as a back reference. A multi-digit sequence not starting with a zero is taken as a back reference if it comes after a suitable subexpression (i.e., the number is in the legal range for a back reference), and otherwise is taken as octal.

#### Regular Expression Metasyntax

In addition to the main syntax described above, there are some special forms and miscellaneous syntactic facilities available.

An RE can begin with one of two special director prefixes. If an RE begins with `***:`, the rest of the RE is taken as an ARE. (This normally has no effect in PostgreSQL, since REs are assumed to be AREs; but it does have an effect if ERE or BRE mode had been specified by the \<flags\> parameter to a regex function.) If an RE begins with `***=`, the rest of the RE is taken to be a literal string, with all characters considered ordinary characters.

An ARE can begin with embedded options: a sequence `(?`\<xyz\>`)` (where \<xyz\> is one or more alphabetic characters) specifies options affecting the rest of the RE. These options override any previously determined options in particular, they can override the case-sensitivity behavior implied by a regex operator, or the \<flags\> parameter to a regex function. The available option letters are shown in [ARE Embedded-Option Letters](#posix-embedded-options-table). Note that these same option letters are used in the \<flags\> parameters of regex functions.

| Option | Description |
|----|----|
| `b` | rest of RE is a BRE |
| `c` | case-sensitive matching (overrides operator type) |
| `e` | rest of RE is an ERE |
| `i` | case-insensitive matching (see [Regular Expression Matching Rules](#posix-matching-rules)) (overrides operator type) |
| `m` | historical synonym for `n` |
| `n` | newline-sensitive matching (see [Regular Expression Matching Rules](#posix-matching-rules)) |
| `p` | partial newline-sensitive matching (see [Regular Expression Matching Rules](#posix-matching-rules)) |
| `q` | rest of RE is a literal (“quoted”) string, all ordinary characters |
| `s` | non-newline-sensitive matching (default) |
| `t` | tight syntax (default; see below) |
| `w` | inverse partial newline-sensitive (“weird”) matching (see [Regular Expression Matching Rules](#posix-matching-rules)) |
| `x` | expanded syntax (see below) |

ARE Embedded-Option Letters {#posix-embedded-options-table}

Embedded options take effect at the `)` terminating the sequence. They can appear only at the start of an ARE (after the `***:` director if any).

In addition to the usual (tight) RE syntax, in which all characters are significant, there is an expanded syntax, available by specifying the embedded `x` option. In the expanded syntax, white-space characters in the RE are ignored, as are all characters between a `#` and the following newline (or the end of the RE). This permits paragraphing and commenting a complex RE. There are three exceptions to that basic rule:

- a white-space character or `#` preceded by `\` is retained

- white space or `#` within a bracket expression is retained

- white space and comments cannot appear within multi-character symbols, such as `(?:`

For this purpose, white-space characters are blank, tab, newline, and any character that belongs to the \<space\> character class.

Finally, in an ARE, outside bracket expressions, the sequence `(?#`\<ttt\>`)` (where \<ttt\> is any text not containing a `)`) is a comment, completely ignored. Again, this is not allowed between the characters of multi-character symbols, like `(?:`. Such comments are more a historical artifact than a useful facility, and their use is deprecated; use the expanded syntax instead.

*None* of these metasyntax extensions is available if an initial `***=` director has specified that the user's input be treated as a literal string rather than as an RE.

#### Regular Expression Matching Rules

In the event that an RE could match more than one substring of a given string, the RE matches the one starting earliest in the string. If the RE could match more than one substring starting at that point, either the longest possible match or the shortest possible match will be taken, depending on whether the RE is greedy or non-greedy.

Whether an RE is greedy or not is determined by the following rules:

- Most atoms, and all constraints, have no greediness attribute (because they cannot match variable amounts of text anyway).

- Adding parentheses around an RE does not change its greediness.

- A quantified atom with a fixed-repetition quantifier (`{`\<m\>`}` or `{`\<m\>`}?`) has the same greediness (possibly none) as the atom itself.

- A quantified atom with other normal quantifiers (including `{`\<m\>`,`\<n\>`}` with \<m\> equal to \<n\>) is greedy (prefers longest match).

- A quantified atom with a non-greedy quantifier (including `{`\<m\>`,`\<n\>`}?` with \<m\> equal to \<n\>) is non-greedy (prefers shortest match).

- A branch that is, an RE that has no top-level `|` operator has the same greediness as the first quantified atom in it that has a greediness attribute.

- An RE consisting of two or more branches connected by the `|` operator is always greedy.

The above rules associate greediness attributes not only with individual quantified atoms, but with branches and entire REs that contain quantified atoms. What that means is that the matching is done in such a way that the branch, or whole RE, matches the longest or shortest possible substring *as a whole*. Once the length of the entire match is determined, the part of it that matches any particular subexpression is determined on the basis of the greediness attribute of that subexpression, with subexpressions starting earlier in the RE taking priority over ones starting later.

An example of what this means:

    SELECT SUBSTRING('XY1234Z', 'Y*([0-9]{1,3})');
    Result: 123
    SELECT SUBSTRING('XY1234Z', 'Y*?([0-9]{1,3})');
    Result: 1

In the first case, the RE as a whole is greedy because `Y*` is greedy. It can match beginning at the `Y`, and it matches the longest possible string starting there, i.e., `Y123`. The output is the parenthesized part of that, or `123`. In the second case, the RE as a whole is non-greedy because `Y*?` is non-greedy. It can match beginning at the `Y`, and it matches the shortest possible string starting there, i.e., `Y1`. The subexpression `[0-9]{1,3}` is greedy but it cannot change the decision as to the overall match length; so it is forced to match just `1`.

In short, when an RE contains both greedy and non-greedy subexpressions, the total match length is either as long as possible or as short as possible, according to the attribute assigned to the whole RE. The attributes assigned to the subexpressions only affect how much of that match they are allowed to “eat” relative to each other.

The quantifiers `{1,1}` and `{1,1}?` can be used to force greediness or non-greediness, respectively, on a subexpression or a whole RE. This is useful when you need the whole RE to have a greediness attribute different from what's deduced from its elements. As an example, suppose that we are trying to separate a string containing some digits into the digits and the parts before and after them. We might try to do that like this:

    SELECT regexp_match('abc01234xyz', '(.*)(\d+)(.*)');
    Result: {abc0123,4,xyz}

That didn't work: the first `.*` is greedy so it “eats” as much as it can, leaving the `\d+` to match at the last possible place, the last digit. We might try to fix that by making it non-greedy:

    SELECT regexp_match('abc01234xyz', '(.*?)(\d+)(.*)');
    Result: {abc,0,""}

That didn't work either, because now the RE as a whole is non-greedy and so it ends the overall match as soon as possible. We can get what we want by forcing the RE as a whole to be greedy:

    SELECT regexp_match('abc01234xyz', '(?:(.*?)(\d+)(.*)){1,1}');
    Result: {abc,01234,xyz}

Controlling the RE's overall greediness separately from its components' greediness allows great flexibility in handling variable-length patterns.

When deciding what is a longer or shorter match, match lengths are measured in characters, not collating elements. An empty string is considered longer than no match at all. For example: `bb*` matches the three middle characters of `abbbc`; `(week|wee)(night|knights)` matches all ten characters of `weeknights`; when `(.*).*` is matched against `abc` the parenthesized subexpression matches all three characters; and when `(a*)*` is matched against `bc` both the whole RE and the parenthesized subexpression match an empty string.

If case-independent matching is specified, the effect is much as if all case distinctions had vanished from the alphabet. When an alphabetic that exists in multiple cases appears as an ordinary character outside a bracket expression, it is effectively transformed into a bracket expression containing both cases, e.g., `x` becomes `[xX]`. When it appears inside a bracket expression, all case counterparts of it are added to the bracket expression, e.g., `[x]` becomes `[xX]` and `[^x]` becomes `[^xX]`.

If newline-sensitive matching is specified, `.` and bracket expressions using `^` will never match the newline character (so that matches will not cross lines unless the RE explicitly includes a newline) and `^` and `$` will match the empty string after and before a newline respectively, in addition to matching at beginning and end of string respectively. But the ARE escapes `\A` and `\Z` continue to match beginning or end of string *only*. Also, the character class shorthands `\D` and `\W` will match a newline regardless of this mode. (Before PostgreSQL 14, they did not match newlines when in newline-sensitive mode. Write `[^[:digit:]]` or `[^[:word:]]` to get the old behavior.)

If partial newline-sensitive matching is specified, this affects `.` and bracket expressions as with newline-sensitive matching, but not `^` and `$`.

If inverse partial newline-sensitive matching is specified, this affects `^` and `$` as with newline-sensitive matching, but not `.` and bracket expressions. This isn't very useful but is provided for symmetry.

#### Limits and Compatibility

No particular limit is imposed on the length of REs in this implementation. However, programs intended to be highly portable should not employ REs longer than 256 bytes, as a POSIX-compliant implementation can refuse to accept such REs.

The only feature of AREs that is actually incompatible with POSIX EREs is that `\` does not lose its special significance inside bracket expressions. All other ARE features use syntax which is illegal or has undefined or unspecified effects in POSIX EREs; the `***` syntax of directors likewise is outside the POSIX syntax for both BREs and EREs.

Many of the ARE extensions are borrowed from Perl, but some have been changed to clean them up, and a few Perl extensions are not present. Incompatibilities of note include `\b`, `\B`, the lack of special treatment for a trailing newline, the addition of complemented bracket expressions to the things affected by newline-sensitive matching, the restrictions on parentheses and back references in lookahead/lookbehind constraints, and the longest/shortest-match (rather than first-match) matching semantics.

#### Basic Regular Expressions

BREs differ from EREs in several respects. In BREs, `|`, `+`, and `?` are ordinary characters and there is no equivalent for their functionality. The delimiters for bounds are `\{` and `\}`, with `{` and `}` by themselves ordinary characters. The parentheses for nested subexpressions are `\(` and `\)`, with `(` and `)` by themselves ordinary characters. `^` is an ordinary character except at the beginning of the RE or the beginning of a parenthesized subexpression, `$` is an ordinary character except at the end of the RE or the end of a parenthesized subexpression, and `*` is an ordinary character if it appears at the beginning of the RE or the beginning of a parenthesized subexpression (after a possible leading `^`). Finally, single-digit back references are available, and `\<` and `\>` are synonyms for `[[:<:]]` and `[[:>:]]` respectively; no other escapes are available in BREs.

#### Differences from SQL Standard and XQuery

LIKE_REGEX

OCCURRENCES_REGEX

POSITION_REGEX

SUBSTRING_REGEX

TRANSLATE_REGEX

XQuery regular expressions

Since SQL:2008, the SQL standard includes regular expression operators and functions that performs pattern matching according to the XQuery regular expression standard:

- `LIKE_REGEX`

- `OCCURRENCES_REGEX`

- `POSITION_REGEX`

- `SUBSTRING_REGEX`

- `TRANSLATE_REGEX`

PostgreSQL does not currently implement these operators and functions. You can get approximately equivalent functionality in each case as shown in [Regular Expression Functions Equivalencies](#functions-regexp-sql-table). (Various optional clauses on both sides have been omitted in this table.)

| SQL standard | PostgreSQL |
|----|----|
| `string LIKE_REGEX pattern` | `regexp_like(string, pattern)` or `string ~ pattern` |
| `OCCURRENCES_REGEX(pattern IN string)` | `regexp_count(string, pattern)` |
| `POSITION_REGEX(pattern IN string)` | `regexp_instr(string, pattern)` |
| `SUBSTRING_REGEX(pattern IN string)` | `regexp_substr(string, pattern)` |
| `TRANSLATE_REGEX(pattern IN string WITH replacement)` | `regexp_replace(string, pattern, replacement)` |

Regular Expression Functions Equivalencies {#functions-regexp-sql-table}

Regular expression functions similar to those provided by PostgreSQL are also available in a number of other SQL implementations, whereas the SQL-standard functions are not as widely implemented. Some of the details of the regular expression syntax will likely differ in each implementation.

The SQL-standard operators and functions use XQuery regular expressions, which are quite close to the ARE syntax described above. Notable differences between the existing POSIX-based regular-expression feature and XQuery regular expressions include:

- XQuery character class subtraction is not supported. An example of this feature is using the following to match only English consonants: `[a-z-[aeiou]]`.

- XQuery character class shorthands `\c`, `\C`, `\i`, and `\I` are not supported.

- XQuery character class elements using `\p{UnicodeProperty}` or the inverse `\P{UnicodeProperty}` are not supported.

- POSIX interprets character classes such as `\w` (see [Regular Expression Class-Shorthand Escapes](#posix-class-shorthand-escapes-table)) according to the prevailing locale (which you can control by attaching a `COLLATE` clause to the operator or function). XQuery specifies these classes by reference to Unicode character properties, so equivalent behavior is obtained only with a locale that follows the Unicode rules.

- The SQL standard (not XQuery itself) attempts to cater for more variants of “newline” than POSIX does. The newline-sensitive matching options described above consider only ASCII NL (`\n`) to be a newline, but SQL would have us treat CR (`\r`), CRLF (`\r\n`) (a Windows-style newline), and some Unicode-only characters like LINE SEPARATOR (U+2028) as newlines as well. Notably, `.` and `\s` should count `\r\n` as one character not two according to SQL.

- Of the character-entry escapes described in [Regular Expression Character-Entry Escapes](#posix-character-entry-escapes-table), XQuery supports only `\n`, `\r`, and `\t`.

- XQuery does not support the `[:name:]` syntax for character classes within bracket expressions.

- XQuery does not have lookahead or lookbehind constraints, nor any of the constraint escapes described in [Regular Expression Constraint Escapes](#posix-constraint-escapes-table).

- The metasyntax forms described in [Regular Expression Metasyntax](#posix-metasyntax) do not exist in XQuery.

- The regular expression flag letters defined by XQuery are related to but not the same as the option letters for POSIX ([ARE Embedded-Option Letters](#posix-embedded-options-table)). While the `i` and `q` options behave the same, others do not:

  - XQuery's `s` (allow dot to match newline) and `m` (allow `^` and `$` to match at newlines) flags provide access to the same behaviors as POSIX's `n`, `p` and `w` flags, but they do *not* match the behavior of POSIX's `s` and `m` flags. Note in particular that dot-matches-newline is the default behavior in POSIX but not XQuery.

  - XQuery's `x` (ignore whitespace in pattern) flag is noticeably different from POSIX's expanded-mode flag. POSIX's `x` flag also allows `#` to begin a comment in the pattern, and POSIX will not ignore a whitespace character after a backslash.

## Data Type Formatting Functions

formatting

The PostgreSQL formatting functions provide a powerful set of tools for converting various data types (date/time, integer, floating point, numeric) to formatted strings and for converting from formatted strings to specific data types. [Formatting Functions](#functions-formatting-table) lists them. These functions all follow a common calling convention: the first argument is the value to be formatted and the second argument is a template that defines the output or input format.

<table id="functions-formatting-table">
<caption>Formatting Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_char</code> ( <code>timestamp</code>, <code>text</code> ) text</p>
<p role="func_signature"><code>to_char</code> ( <code>timestamp with time zone</code>, <code>text</code> ) text</p>
<p>Converts time stamp to string according to the given format.</p>
<p><code>to_char(timestamp '2002-04-20 17:31:12.66', 'HH12:MI:SS')</code> 05:31:12</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>to_char</code> ( <code>interval</code>, <code>text</code> ) text</p>
<p>Converts interval to string according to the given format.</p>
<p><code>to_char(interval '15h 2m 12s', 'HH24:MI:SS')</code> 15:02:12</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>to_char</code> ( &lt;numeric_type&gt;, <code>text</code> ) text</p>
<p>Converts number to string according to the given format; available for <code>integer</code>, <code>bigint</code>, <code>numeric</code>, <code>real</code>, <code>double precision</code>.</p>
<p><code>to_char(125, '999')</code> 125</p>
<p><code>to_char(125.8::real, '999D9')</code> 125.8</p>
<p><code>to_char(-125.8, '999D99S')</code> 125.80-</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_date</code> ( <code>text</code>, <code>text</code> ) date</p>
<p>Converts string to date according to the given format.</p>
<p><code>to_date('05 Dec 2000', 'DD Mon YYYY')</code> 2000-12-05</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_number</code> ( <code>text</code>, <code>text</code> ) numeric</p>
<p>Converts string to numeric according to the given format.</p>
<p><code>to_number('12,454.8-', '99G999D9S')</code> -12454.8</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_timestamp</code> ( <code>text</code>, <code>text</code> ) timestamp with time zone</p>
<p>Converts string to time stamp according to the given format. (See also <code>to_timestamp(double precision)</code> in <a href="#functions-datetime-table">Date/Time Functions</a>.)</p>
<p><code>to_timestamp('05 Dec 2000', 'DD Mon YYYY')</code> 2000-12-05 00:00:00-05</p></td>
</tr>
</tbody>
</table>

> [!TIP]
> `to_timestamp` and `to_date` exist to handle input formats that cannot be converted by simple casting. For most standard date/time formats, simply casting the source string to the required data type works, and is much easier. Similarly, `to_number` is unnecessary for standard numeric representations.

In a `to_char` output template string, there are certain patterns that are recognized and replaced with appropriately-formatted data based on the given value. Any text that is not a template pattern is simply copied verbatim. Similarly, in an input template string (for the other functions), template patterns identify the values to be supplied by the input data string. If there are characters in the template string that are not template patterns, the corresponding characters in the input data string are simply skipped over (whether or not they are equal to the template string characters).

[Template Patterns for Date/Time Formatting](#functions-formatting-datetime-table) shows the template patterns available for formatting date and time values.

| Pattern | Description |
|----|----|
| `HH` | hour of day (0112) |
| `HH12` | hour of day (0112) |
| `HH24` | hour of day (0023) |
| `MI` | minute (0059) |
| `SS` | second (0059) |
| `MS` | millisecond (000999) |
| `US` | microsecond (000000999999) |
| `FF1` | tenth of second (09) |
| `FF2` | hundredth of second (0099) |
| `FF3` | millisecond (000999) |
| `FF4` | tenth of a millisecond (00009999) |
| `FF5` | hundredth of a millisecond (0000099999) |
| `FF6` | microsecond (000000999999) |
| `SSSS`, `SSSSS` | seconds past midnight (086399) |
| `AM`, `am`, `PM` or `pm` | meridiem indicator (without periods) |
| `A.M.`, `a.m.`, `P.M.` or `p.m.` | meridiem indicator (with periods) |
| `Y,YYY` | year (4 or more digits) with comma |
| `YYYY` | year (4 or more digits) |
| `YYY` | last 3 digits of year |
| `YY` | last 2 digits of year |
| `Y` | last digit of year |
| `IYYY` | ISO 8601 week-numbering year (4 or more digits) |
| `IYY` | last 3 digits of ISO 8601 week-numbering year |
| `IY` | last 2 digits of ISO 8601 week-numbering year |
| `I` | last digit of ISO 8601 week-numbering year |
| `BC`, `bc`, `AD` or `ad` | era indicator (without periods) |
| `B.C.`, `b.c.`, `A.D.` or `a.d.` | era indicator (with periods) |
| `MONTH` | full upper case month name (blank-padded to 9 chars) |
| `Month` | full capitalized month name (blank-padded to 9 chars) |
| `month` | full lower case month name (blank-padded to 9 chars) |
| `MON` | abbreviated upper case month name (3 chars in English, localized lengths vary) |
| `Mon` | abbreviated capitalized month name (3 chars in English, localized lengths vary) |
| `mon` | abbreviated lower case month name (3 chars in English, localized lengths vary) |
| `MM` | month number (0112) |
| `DAY` | full upper case day name (blank-padded to 9 chars) |
| `Day` | full capitalized day name (blank-padded to 9 chars) |
| `day` | full lower case day name (blank-padded to 9 chars) |
| `DY` | abbreviated upper case day name (3 chars in English, localized lengths vary) |
| `Dy` | abbreviated capitalized day name (3 chars in English, localized lengths vary) |
| `dy` | abbreviated lower case day name (3 chars in English, localized lengths vary) |
| `DDD` | day of year (001366) |
| `IDDD` | day of ISO 8601 week-numbering year (001371; day 1 of the year is Monday of the first ISO week) |
| `DD` | day of month (0131) |
| `D` | day of the week, Sunday (`1`) to Saturday (`7`) |
| `ID` | ISO 8601 day of the week, Monday (`1`) to Sunday (`7`) |
| `W` | week of month (15) (the first week starts on the first day of the month) |
| `WW` | week number of year (153) (the first week starts on the first day of the year) |
| `IW` | week number of ISO 8601 week-numbering year (0153; the first Thursday of the year is in week 1) |
| `CC` | century (2 digits) (the twenty-first century starts on 2001-01-01) |
| `J` | Julian Date (integer days since November 24, 4714 BC at local midnight; see [???](#datetime-julian-dates)) |
| `Q` | quarter |
| `RM` | month in upper case Roman numerals (IXII; I=January) |
| `rm` | month in lower case Roman numerals (ixii; i=January) |
| `TZ` | upper case time-zone abbreviation |
| `tz` | lower case time-zone abbreviation |
| `TZH` | time-zone hours |
| `TZM` | time-zone minutes |
| `OF` | time-zone offset from UTC (\<HH\> or \<HH\>`:`\<MM\>) |

Template Patterns for Date/Time Formatting {#functions-formatting-datetime-table}

Modifiers can be applied to any template pattern to alter its behavior. For example, `FMMonth` is the `Month` pattern with the `FM` modifier. [Template Pattern Modifiers for Date/Time Formatting](#functions-formatting-datetimemod-table) shows the modifier patterns for date/time formatting.

| Modifier | Description | Example |
|----|----|----|
| `FM` prefix | fill mode (suppress leading zeroes and padding blanks) | `FMMonth` |
| `TH` suffix | upper case ordinal number suffix | `DDTH`, e.g., `12TH` |
| `th` suffix | lower case ordinal number suffix | `DDth`, e.g., `12th` |
| `FX` prefix | fixed format global option (see usage notes) | `FXMonthDDDay` |
| `TM` prefix | translation mode (use localized day and month names based on [???](#guc-lc-time)) | `TMMonth` |
| `SP` suffix | spell mode (not implemented) | `DDSP` |

Template Pattern Modifiers for Date/Time Formatting {#functions-formatting-datetimemod-table}

Usage notes for date/time formatting:

- `FM` suppresses leading zeroes and trailing blanks that would otherwise be added to make the output of a pattern be fixed-width. In PostgreSQL, `FM` modifies only the next specification, while in Oracle `FM` affects all subsequent specifications, and repeated `FM` modifiers toggle fill mode on and off.

- `TM` suppresses trailing blanks whether or not `FM` is specified.

- `to_timestamp` and `to_date` ignore letter case in the input; so for example `MON`, `Mon`, and `mon` all accept the same strings. When using the `TM` modifier, case-folding is done according to the rules of the function's input collation (see [???](#collation)).

- `to_timestamp` and `to_date` skip multiple blank spaces at the beginning of the input string and around date and time values unless the `FX` option is used. For example, `to_timestamp('2000JUN', 'YYYY MON')` and `to_timestamp('2000 - JUN', 'YYYY-MON')` work, but `to_timestamp('2000JUN', 'FXYYYY MON')` returns an error because `to_timestamp` expects only a single space. `FX` must be specified as the first item in the template.

- A separator (a space or non-letter/non-digit character) in the template string of `to_timestamp` and `to_date` matches any single separator in the input string or is skipped, unless the `FX` option is used. For example, `to_timestamp('2000JUN', 'YYYY///MON')` and `to_timestamp('2000/JUN', 'YYYY MON')` work, but `to_timestamp('2000//JUN', 'YYYY/MON')` returns an error because the number of separators in the input string exceeds the number of separators in the template.

  If `FX` is specified, a separator in the template string matches exactly one character in the input string. But note that the input string character is not required to be the same as the separator from the template string. For example, `to_timestamp('2000/JUN', 'FXYYYY MON')` works, but `to_timestamp('2000/JUN', 'FXYYYYMON')` returns an error because the second space in the template string consumes the letter `J` from the input string.

- A `TZH` template pattern can match a signed number. Without the `FX` option, minus signs may be ambiguous, and could be interpreted as a separator. This ambiguity is resolved as follows: If the number of separators before `TZH` in the template string is less than the number of separators before the minus sign in the input string, the minus sign is interpreted as part of `TZH`. Otherwise, the minus sign is considered to be a separator between values. For example, `to_timestamp('2000 -10', 'YYYY TZH')` matches `-10` to `TZH`, but `to_timestamp('2000 -10', 'YYYYTZH')` matches `10` to `TZH`.

- Ordinary text is allowed in `to_char` templates and will be output literally. You can put a substring in double quotes to force it to be interpreted as literal text even if it contains template patterns. For example, in `'"Hello Year "YYYY'`, the `YYYY` will be replaced by the year data, but the single `Y` in `Year` will not be. In `to_date`, `to_number`, and `to_timestamp`, literal text and double-quoted strings result in skipping the number of characters contained in the string; for example `"XX"` skips two input characters (whether or not they are `XX`).

  > [!TIP]
  > Prior to PostgreSQL 12, it was possible to skip arbitrary text in the input string using non-letter or non-digit characters. For example, `to_timestamp('2000y6m1d', 'yyyy-MM-DD')` used to work. Now you can only use letter characters for this purpose. For example, `to_timestamp('2000y6m1d', 'yyyytMMtDDt')` and `to_timestamp('2000y6m1d', 'yyyy"y"MM"m"DD"d"')` skip `y`, `m`, and `d`.

- If you want to have a double quote in the output you must precede it with a backslash, for example `'\"YYYY Month\"'`. Backslashes are not otherwise special outside of double-quoted strings. Within a double-quoted string, a backslash causes the next character to be taken literally, whatever it is (but this has no special effect unless the next character is a double quote or another backslash).

- In `to_timestamp` and `to_date`, if the year format specification is less than four digits, e.g., `YYY`, and the supplied year is less than four digits, the year will be adjusted to be nearest to the year 2020, e.g., `95` becomes 1995.

- In `to_timestamp` and `to_date`, negative years are treated as signifying BC. If you write both a negative year and an explicit `BC` field, you get AD again. An input of year zero is treated as 1 BC.

- In `to_timestamp` and `to_date`, the `YYYY` conversion has a restriction when processing years with more than 4 digits. You must use some non-digit character or template after `YYYY`, otherwise the year is always interpreted as 4 digits. For example (with the year 20000): `to_date('200001130', 'YYYYMMDD')` will be interpreted as a 4-digit year; instead use a non-digit separator after the year, like `to_date('20000-1130', 'YYYY-MMDD')` or `to_date('20000Nov30', 'YYYYMonDD')`.

- In `to_timestamp` and `to_date`, the `CC` (century) field is accepted but ignored if there is a `YYY`, `YYYY` or `Y,YYY` field. If `CC` is used with `YY` or `Y` then the result is computed as that year in the specified century. If the century is specified but the year is not, the first year of the century is assumed.

- In `to_timestamp` and `to_date`, weekday names or numbers (`DAY`, `D`, and related field types) are accepted but are ignored for purposes of computing the result. The same is true for quarter (`Q`) fields.

- In `to_timestamp` and `to_date`, an ISO 8601 week-numbering date (as distinct from a Gregorian date) can be specified in one of two ways:

  - Year, week number, and weekday: for example `to_date('2006-42-4', 'IYYY-IW-ID')` returns the date `2006-10-19`. If you omit the weekday it is assumed to be 1 (Monday).

  - Year and day of year: for example `to_date('2006-291', 'IYYY-IDDD')` also returns `2006-10-19`.

  Attempting to enter a date using a mixture of ISO 8601 week-numbering fields and Gregorian date fields is nonsensical, and will cause an error. In the context of an ISO 8601 week-numbering year, the concept of a “month” or “day of month” has no meaning. In the context of a Gregorian year, the ISO week has no meaning.

  > [!CAUTION]
  > While `to_date` will reject a mixture of Gregorian and ISO week-numbering date fields, `to_char` will not, since output format specifications like `YYYY-MM-DD (IYYY-IDDD)` can be useful. But avoid writing something like `IYYY-MM-DD`; that would yield surprising results near the start of the year. (See [, ](#functions-datetime-extract) for more information.)

- In `to_timestamp`, millisecond (`MS`) or microsecond (`US`) fields are used as the seconds digits after the decimal point. For example `to_timestamp('12.3', 'SS.MS')` is not 3 milliseconds, but 300, because the conversion treats it as 12 + 0.3 seconds. So, for the format `SS.MS`, the input values `12.3`, `12.30`, and `12.300` specify the same number of milliseconds. To get three milliseconds, one must write `12.003`, which the conversion treats as 12 + 0.003 = 12.003 seconds.

  Here is a more complex example: `to_timestamp('15:12:02.020.001230', 'HH24:MI:SS.MS.US')` is 15 hours, 12 minutes, and 2 seconds + 20 milliseconds + 1230 microseconds = 2.021230 seconds.

- `to_char(..., 'ID')`'s day of the week numbering matches the `extract(isodow from ...)` function, but `to_char(..., 'D')`'s does not match `extract(dow from ...)`'s day numbering.

- `to_char(interval)` formats `HH` and `HH12` as shown on a 12-hour clock, for example zero hours and 36 hours both output as `12`, while `HH24` outputs the full hour value, which can exceed 23 in an `interval` value.

[Template Patterns for Numeric Formatting](#functions-formatting-numeric-table) shows the template patterns available for formatting numeric values.

| Pattern      | Description                                                 |
|--------------|-------------------------------------------------------------|
| `9`          | digit position (can be dropped if insignificant)            |
| `0`          | digit position (will not be dropped, even if insignificant) |
| `.` (period) | decimal point                                               |
| `,` (comma)  | group (thousands) separator                                 |
| `PR`         | negative value in angle brackets                            |
| `S`          | sign anchored to number (uses locale)                       |
| `L`          | currency symbol (uses locale)                               |
| `D`          | decimal point (uses locale)                                 |
| `G`          | group separator (uses locale)                               |
| `MI`         | minus sign in specified position (if number \< 0)           |
| `PL`         | plus sign in specified position (if number \> 0)            |
| `SG`         | plus/minus sign in specified position                       |
| `RN`         | Roman numeral (input between 1 and 3999)                    |
| `TH` or `th` | ordinal number suffix                                       |
| `V`          | shift specified number of digits (see notes)                |
| `EEEE`       | exponent for scientific notation                            |

Template Patterns for Numeric Formatting {#functions-formatting-numeric-table}

Usage notes for numeric formatting:

- `0` specifies a digit position that will always be printed, even if it contains a leading/trailing zero. `9` also specifies a digit position, but if it is a leading zero then it will be replaced by a space, while if it is a trailing zero and fill mode is specified then it will be deleted. (For `to_number()`, these two pattern characters are equivalent.)

- If the format provides fewer fractional digits than the number being formatted, `to_char()` will round the number to the specified number of fractional digits.

- The pattern characters `S`, `L`, `D`, and `G` represent the sign, currency symbol, decimal point, and thousands separator characters defined by the current locale (see [???](#guc-lc-monetary) and [???](#guc-lc-numeric)). The pattern characters period and comma represent those exact characters, with the meanings of decimal point and thousands separator, regardless of locale.

- If no explicit provision is made for a sign in `to_char()`'s pattern, one column will be reserved for the sign, and it will be anchored to (appear just left of) the number. If `S` appears just left of some `9`'s, it will likewise be anchored to the number.

- A sign formatted using `SG`, `PL`, or `MI` is not anchored to the number; for example, `to_char(-12, 'MI9999')` produces `'-12'` but `to_char(-12, 'S9999')` produces `'-12'`. (The Oracle implementation does not allow the use of `MI` before `9`, but rather requires that `9` precede `MI`.)

- `TH` does not convert values less than zero and does not convert fractional numbers.

- `PL`, `SG`, and `TH` are PostgreSQL extensions.

- In `to_number`, if non-data template patterns such as `L` or `TH` are used, the corresponding number of input characters are skipped, whether or not they match the template pattern, unless they are data characters (that is, digits, sign, decimal point, or comma). For example, `TH` would skip two non-data characters.

- `V` with `to_char` multiplies the input values by `10^n`, where \<n\> is the number of digits following `V`. `V` with `to_number` divides in a similar manner. `to_char` and `to_number` do not support the use of `V` combined with a decimal point (e.g., `99.9V99` is not allowed).

- `EEEE` (scientific notation) cannot be used in combination with any of the other formatting patterns or modifiers other than digit and decimal point patterns, and must be at the end of the format string (e.g., `9.99EEEE` is a valid pattern).

Certain modifiers can be applied to any template pattern to alter its behavior. For example, `FM99.99` is the `99.99` pattern with the `FM` modifier. [Template Pattern Modifiers for Numeric Formatting](#functions-formatting-numericmod-table) shows the modifier patterns for numeric formatting.

| Modifier | Description | Example |
|----|----|----|
| `FM` prefix | fill mode (suppress trailing zeroes and padding blanks) | `FM99.99` |
| `TH` suffix | upper case ordinal number suffix | `999TH` |
| `th` suffix | lower case ordinal number suffix | `999th` |

Template Pattern Modifiers for Numeric Formatting {#functions-formatting-numericmod-table}

[ Examples](#functions-formatting-examples-table) shows some examples of the use of the `to_char` function.

| Expression | Result |
|----|----|
| `to_char(current_timestamp, 'Day,DDHH12:MI:SS')` | `'Tuesday,0605:39:18'` |
| `to_char(current_timestamp, 'FMDay,FMDDHH12:MI:SS')` | `'Tuesday,605:39:18'` |
| `to_char(current_timestamp AT TIME ZONE 'UTC', 'YYYY-MM-DD"T"HH24:MI:SS"Z"')` | `'2022-12-06T05:39:18Z'`, ISO 8601 extended format |
| `to_char(-0.1, '99.99')` | `'-.10'` |
| `to_char(-0.1, 'FM9.99')` | `'-.1'` |
| `to_char(-0.1, 'FM90.99')` | `'-0.1'` |
| `to_char(0.1, '0.9')` | `'0.1'` |
| `to_char(12, '9990999.9')` | `'0012.0'` |
| `to_char(12, 'FM9990999.9')` | `'0012.'` |
| `to_char(485, '999')` | `'485'` |
| `to_char(-485, '999')` | `'-485'` |
| `to_char(485, '999')` | `'485'` |
| `to_char(1485, '9,999')` | `'1,485'` |
| `to_char(1485, '9G999')` | `'1485'` |
| `to_char(148.5, '999.999')` | `'148.500'` |
| `to_char(148.5, 'FM999.999')` | `'148.5'` |
| `to_char(148.5, 'FM999.990')` | `'148.500'` |
| `to_char(148.5, '999D999')` | `'148,500'` |
| `to_char(3148.5, '9G999D999')` | `'3148,500'` |
| `to_char(-485, '999S')` | `'485-'` |
| `to_char(-485, '999MI')` | `'485-'` |
| `to_char(485, '999MI')` | `'485'` |
| `to_char(485, 'FM999MI')` | `'485'` |
| `to_char(485, 'PL999')` | `'+485'` |
| `to_char(485, 'SG999')` | `'+485'` |
| `to_char(-485, 'SG999')` | `'-485'` |
| `to_char(-485, '9SG99')` | `'4-85'` |
| `to_char(-485, '999PR')` | `'<485>'` |
| `to_char(485, 'L999')` | `'DM485'` |
| `to_char(485, 'RN')` | `'CDLXXXV'` |
| `to_char(485, 'FMRN')` | `'CDLXXXV'` |
| `to_char(5.2, 'FMRN')` | `'V'` |
| `to_char(482, '999th')` | `'482nd'` |
| `to_char(485, '"Goodnumber:"999')` | `'Goodnumber:485'` |
| `to_char(485.8, '"Pre:"999"Post:".999')` | `'Pre:485Post:.800'` |
| `to_char(12, '99V999')` | `'12000'` |
| `to_char(12.4, '99V999')` | `'12400'` |
| `to_char(12.45, '99V9')` | `'125'` |
| `to_char(0.0004859, '9.99EEEE')` | `' 4.86e-04'` |

`to_char` Examples {#functions-formatting-examples-table}

## Date/Time Functions and Operators

[Date/Time Functions](#functions-datetime-table) shows the available functions for date/time value processing, with details appearing in the following subsections. [Date/Time Operators](#operators-datetime-table) illustrates the behaviors of the basic arithmetic operators (`+`, `*`, etc.). For formatting functions, refer to [Data Type Formatting Functions](#functions-formatting). You should be familiar with the background information on date/time data types from [???](#datatype-datetime).

In addition, the usual comparison operators shown in [Comparison Operators](#functions-comparison-op-table) are available for the date/time types. Dates and timestamps (with or without time zone) are all comparable, while times (with or without time zone) and intervals can only be compared to other values of the same data type. When comparing a timestamp without time zone to a timestamp with time zone, the former value is assumed to be given in the time zone specified by the [???](#guc-timezone) configuration parameter, and is rotated to UTC for comparison to the latter value (which is already in UTC internally). Similarly, a date value is assumed to represent midnight in the `TimeZone` zone when comparing it to a timestamp.

All the functions and operators described below that take `time` or `timestamp` inputs actually come in two variants: one that takes `time with time zone` or `timestamp with time zone`, and one that takes `time without time zone` or `timestamp without time zone`. For brevity, these variants are not shown separately. Also, the `+` and `*` operators come in commutative pairs (for example both `date` `+` `integer` and `integer` `+` `date`); we show only one of each such pair.

<table id="operators-datetime-table">
<caption>Date/Time Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>date</code> <code>+</code> <code>integer</code> date</p>
<p>Add a number of days to a date</p>
<p><code>date '2001-09-28' + 7</code> 2001-10-05</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>date</code> <code>+</code> <code>interval</code> timestamp</p>
<p>Add an interval to a date</p>
<p><code>date '2001-09-28' + interval '1 hour'</code> 2001-09-28 01:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>date</code> <code>+</code> <code>time</code> timestamp</p>
<p>Add a time-of-day to a date</p>
<p><code>date '2001-09-28' + time '03:00'</code> 2001-09-28 03:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>interval</code> <code>+</code> <code>interval</code> interval</p>
<p>Add intervals</p>
<p><code>interval '1 day' + interval '1 hour'</code> 1 day 01:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>timestamp</code> <code>+</code> <code>interval</code> timestamp</p>
<p>Add an interval to a timestamp</p>
<p><code>timestamp '2001-09-28 01:00' + interval '23 hours'</code> 2001-09-29 00:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>time</code> <code>+</code> <code>interval</code> time</p>
<p>Add an interval to a time</p>
<p><code>time '01:00' + interval '3 hours'</code> 04:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>-</code> <code>interval</code> interval</p>
<p>Negate an interval</p>
<p><code>- interval '23 hours'</code> -23:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>date</code> <code>-</code> <code>date</code> integer</p>
<p>Subtract dates, producing the number of days elapsed</p>
<p><code>date '2001-10-01' - date '2001-09-28'</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>date</code> <code>-</code> <code>integer</code> date</p>
<p>Subtract a number of days from a date</p>
<p><code>date '2001-10-01' - 7</code> 2001-09-24</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>date</code> <code>-</code> <code>interval</code> timestamp</p>
<p>Subtract an interval from a date</p>
<p><code>date '2001-09-28' - interval '1 hour'</code> 2001-09-27 23:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>time</code> <code>-</code> <code>time</code> interval</p>
<p>Subtract times</p>
<p><code>time '05:00' - time '03:00'</code> 02:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>time</code> <code>-</code> <code>interval</code> time</p>
<p>Subtract an interval from a time</p>
<p><code>time '05:00' - interval '2 hours'</code> 03:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>timestamp</code> <code>-</code> <code>interval</code> timestamp</p>
<p>Subtract an interval from a timestamp</p>
<p><code>timestamp '2001-09-28 23:00' - interval '23 hours'</code> 2001-09-28 00:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>interval</code> <code>-</code> <code>interval</code> interval</p>
<p>Subtract intervals</p>
<p><code>interval '1 day' - interval '1 hour'</code> 1 day -01:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>timestamp</code> <code>-</code> <code>timestamp</code> interval</p>
<p>Subtract timestamps (converting 24-hour intervals into days, similarly to <a href="#function-justify-hours"><code>justify_hours()</code></a>)</p>
<p><code>timestamp '2001-09-29 03:00' - timestamp '2001-07-27 12:00'</code> 63 days 15:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>interval</code> <code>*</code> <code>double precision</code> interval</p>
<p>Multiply an interval by a scalar</p>
<p><code>interval '1 second' * 900</code> 00:15:00</p>
<p><code>interval '1 day' * 21</code> 21 days</p>
<p><code>interval '1 hour' * 3.5</code> 03:30:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>interval</code> <code>/</code> <code>double precision</code> interval</p>
<p>Divide an interval by a scalar</p>
<p><code>interval '1 hour' / 1.5</code> 00:40:00</p></td>
</tr>
</tbody>
</table>

<table id="functions-datetime-table">
<caption>Date/Time Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>age</code> ( <code>timestamp</code>, <code>timestamp</code> ) interval</p>
<p>Subtract arguments, producing a “symbolic” result that uses years and months, rather than just days</p>
<p><code>age(timestamp '2001-04-10', timestamp '1957-06-13')</code> 43 years 9 mons 27 days</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>age</code> ( <code>timestamp</code> ) interval</p>
<p>Subtract argument from <code>current_date</code> (at midnight)</p>
<p><code>age(timestamp '1957-06-13')</code> 62 years 6 mons 10 days</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>clock_timestamp</code> ( ) timestamp with time zone</p>
<p>Current date and time (changes during statement execution); see <a href="#functions-datetime-current">Current Date/Time</a></p>
<p><code>clock_timestamp()</code> 2019-12-23 14:39:53.662522-05</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>current_date</code> date</p>
<p>Current date; see <a href="#functions-datetime-current">Current Date/Time</a></p>
<p><code>current_date</code> 2019-12-23</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>current_time</code> time with time zone</p>
<p>Current time of day; see <a href="#functions-datetime-current">Current Date/Time</a></p>
<p><code>current_time</code> 14:39:53.662522-05</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>current_time</code> ( <code>integer</code> ) time with time zone</p>
<p>Current time of day, with limited precision; see <a href="#functions-datetime-current">Current Date/Time</a></p>
<p><code>current_time(2)</code> 14:39:53.66-05</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>current_timestamp</code> timestamp with time zone</p>
<p>Current date and time (start of current transaction); see <a href="#functions-datetime-current">Current Date/Time</a></p>
<p><code>current_timestamp</code> 2019-12-23 14:39:53.662522-05</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>current_timestamp</code> ( <code>integer</code> ) timestamp with time zone</p>
<p>Current date and time (start of current transaction), with limited precision; see <a href="#functions-datetime-current">Current Date/Time</a></p>
<p><code>current_timestamp(0)</code> 2019-12-23 14:39:53-05</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>date_add</code> ( <code>timestamp with time zone</code>, <code>interval</code> [, <code>text</code>] ) timestamp with time zone</p>
<p>Add an <code>interval</code> to a <code>timestamp with time zone</code>, computing times of day and daylight-savings adjustments according to the time zone named by the third argument, or the current <a href="#guc-timezone">???</a> setting if that is omitted. The form with two arguments is equivalent to the <code>timestamp with time zone</code> <code>+</code> <code>interval</code> operator.</p>
<p><code>date_add('2021-10-31 00:00:00+02'::timestamptz, '1 day'::interval, 'Europe/Warsaw')</code> 2021-10-31 23:00:00+00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>date_bin</code> ( <code>interval</code>, <code>timestamp</code>, <code>timestamp</code> ) timestamp</p>
<p>Bin input into specified interval aligned with specified origin; see <a href="#functions-datetime-bin"></a></p>
<p><code>date_bin('15 minutes', timestamp '2001-02-16 20:38:40', timestamp '2001-02-16 20:05:00')</code> 2001-02-16 20:35:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>date_part</code> ( <code>text</code>, <code>timestamp</code> ) double precision</p>
<p>Get timestamp subfield (equivalent to <code>extract</code>); see <a href="#functions-datetime-extract">, </a></p>
<p><code>date_part('hour', timestamp '2001-02-16 20:38:40')</code> 20</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>date_part</code> ( <code>text</code>, <code>interval</code> ) double precision</p>
<p>Get interval subfield (equivalent to <code>extract</code>); see <a href="#functions-datetime-extract">, </a></p>
<p><code>date_part('month', interval '2 years 3 months')</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>date_subtract</code> ( <code>timestamp with time zone</code>, <code>interval</code> [, <code>text</code>] ) timestamp with time zone</p>
<p>Subtract an <code>interval</code> from a <code>timestamp with time zone</code>, computing times of day and daylight-savings adjustments according to the time zone named by the third argument, or the current <a href="#guc-timezone">???</a> setting if that is omitted. The form with two arguments is equivalent to the <code>timestamp with time zone</code> <code>-</code> <code>interval</code> operator.</p>
<p><code>date_subtract('2021-11-01 00:00:00+01'::timestamptz, '1 day'::interval, 'Europe/Warsaw')</code> 2021-10-30 22:00:00+00</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>date_trunc</code> ( <code>text</code>, <code>timestamp</code> ) timestamp</p>
<p>Truncate to specified precision; see <a href="#functions-datetime-trunc"></a></p>
<p><code>date_trunc('hour', timestamp '2001-02-16 20:38:40')</code> 2001-02-16 20:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>date_trunc</code> ( <code>text</code>, <code>timestamp with time zone</code>, <code>text</code> ) timestamp with time zone</p>
<p>Truncate to specified precision in the specified time zone; see <a href="#functions-datetime-trunc"></a></p>
<p><code>date_trunc('day', timestamptz '2001-02-16 20:38:40+00', 'Australia/Sydney')</code> 2001-02-16 13:00:00+00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>date_trunc</code> ( <code>text</code>, <code>interval</code> ) interval</p>
<p>Truncate to specified precision; see <a href="#functions-datetime-trunc"></a></p>
<p><code>date_trunc('hour', interval '2 days 3 hours 40 minutes')</code> 2 days 03:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>extract</code> ( <code>field</code> <code>from</code> <code>timestamp</code> ) numeric</p>
<p>Get timestamp subfield; see <a href="#functions-datetime-extract">, </a></p>
<p><code>extract(hour from timestamp '2001-02-16 20:38:40')</code> 20</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>extract</code> ( <code>field</code> <code>from</code> <code>interval</code> ) numeric</p>
<p>Get interval subfield; see <a href="#functions-datetime-extract">, </a></p>
<p><code>extract(month from interval '2 years 3 months')</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>isfinite</code> ( <code>date</code> ) boolean</p>
<p>Test for finite date (not +/-infinity)</p>
<p><code>isfinite(date '2001-02-16')</code> true</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>isfinite</code> ( <code>timestamp</code> ) boolean</p>
<p>Test for finite timestamp (not +/-infinity)</p>
<p><code>isfinite(timestamp 'infinity')</code> false</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>isfinite</code> ( <code>interval</code> ) boolean</p>
<p>Test for finite interval (not +/-infinity)</p>
<p><code>isfinite(interval '4 hours')</code> true</p></td>
</tr>
<tr>
<td><p role="func_signature"><span id="function-justify-days" class="indexterm"></span> <code>justify_days</code> ( <code>interval</code> ) interval</p>
<p>Adjust interval, converting 30-day time periods to months</p>
<p><code>justify_days(interval '1 year 65 days')</code> 1 year 2 mons 5 days</p></td>
</tr>
<tr>
<td><p role="func_signature"><span id="function-justify-hours" class="indexterm"></span> <code>justify_hours</code> ( <code>interval</code> ) interval</p>
<p>Adjust interval, converting 24-hour time periods to days</p>
<p><code>justify_hours(interval '50 hours 10 minutes')</code> 2 days 02:10:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>justify_interval</code> ( <code>interval</code> ) interval</p>
<p>Adjust interval using <code>justify_days</code> and <code>justify_hours</code>, with additional sign adjustments</p>
<p><code>justify_interval(interval '1 mon -1 hour')</code> 29 days 23:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>localtime</code> time</p>
<p>Current time of day; see <a href="#functions-datetime-current">Current Date/Time</a></p>
<p><code>localtime</code> 14:39:53.662522</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>localtime</code> ( <code>integer</code> ) time</p>
<p>Current time of day, with limited precision; see <a href="#functions-datetime-current">Current Date/Time</a></p>
<p><code>localtime(0)</code> 14:39:53</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>localtimestamp</code> timestamp</p>
<p>Current date and time (start of current transaction); see <a href="#functions-datetime-current">Current Date/Time</a></p>
<p><code>localtimestamp</code> 2019-12-23 14:39:53.662522</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>localtimestamp</code> ( <code>integer</code> ) timestamp</p>
<p>Current date and time (start of current transaction), with limited precision; see <a href="#functions-datetime-current">Current Date/Time</a></p>
<p><code>localtimestamp(2)</code> 2019-12-23 14:39:53.66</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>make_date</code> ( <code>year</code> <code>int</code>, <code>month</code> <code>int</code>, <code>day</code> <code>int</code> ) date</p>
<p>Create date from year, month and day fields (negative years signify BC)</p>
<p><code>make_date(2013, 7, 15)</code> 2013-07-15</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>make_interval</code> ( [<code>years</code> <code>int</code> [, <code>months</code> <code>int</code> [, <code>weeks</code> <code>int</code> [, <code>days</code> <code>int</code> [, <code>hours</code> <code>int</code> [, <code>mins</code> <code>int</code> [, <code>secs</code> <code>double precision</code>]]]]]]] ) interval</p>
<p>Create interval from years, months, weeks, days, hours, minutes and seconds fields, each of which can default to zero</p>
<p><code>make_interval(days =&gt; 10)</code> 10 days</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>make_time</code> ( <code>hour</code> <code>int</code>, <code>min</code> <code>int</code>, <code>sec</code> <code>double precision</code> ) time</p>
<p>Create time from hour, minute and seconds fields</p>
<p><code>make_time(8, 15, 23.5)</code> 08:15:23.5</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>make_timestamp</code> ( <code>year</code> <code>int</code>, <code>month</code> <code>int</code>, <code>day</code> <code>int</code>, <code>hour</code> <code>int</code>, <code>min</code> <code>int</code>, <code>sec</code> <code>double precision</code> ) timestamp</p>
<p>Create timestamp from year, month, day, hour, minute and seconds fields (negative years signify BC)</p>
<p><code>make_timestamp(2013, 7, 15, 8, 15, 23.5)</code> 2013-07-15 08:15:23.5</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>make_timestamptz</code> ( <code>year</code> <code>int</code>, <code>month</code> <code>int</code>, <code>day</code> <code>int</code>, <code>hour</code> <code>int</code>, <code>min</code> <code>int</code>, <code>sec</code> <code>double precision</code> [, <code>timezone</code> <code>text</code>] ) timestamp with time zone</p>
<p>Create timestamp with time zone from year, month, day, hour, minute and seconds fields (negative years signify BC). If <code>timezone</code> is not specified, the current time zone is used; the examples assume the session time zone is <code>Europe/London</code></p>
<p><code>make_timestamptz(2013, 7, 15, 8, 15, 23.5)</code> 2013-07-15 08:15:23.5+01</p>
<p><code>make_timestamptz(2013, 7, 15, 8, 15, 23.5, 'America/New_York')</code> 2013-07-15 13:15:23.5+01</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>now</code> ( ) timestamp with time zone</p>
<p>Current date and time (start of current transaction); see <a href="#functions-datetime-current">Current Date/Time</a></p>
<p><code>now()</code> 2019-12-23 14:39:53.662522-05</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>statement_timestamp</code> ( ) timestamp with time zone</p>
<p>Current date and time (start of current statement); see <a href="#functions-datetime-current">Current Date/Time</a></p>
<p><code>statement_timestamp()</code> 2019-12-23 14:39:53.662522-05</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>timeofday</code> ( ) text</p>
<p>Current date and time (like <code>clock_timestamp</code>, but as a <code>text</code> string); see <a href="#functions-datetime-current">Current Date/Time</a></p>
<p><code>timeofday()</code> Mon Dec 23 14:39:53.662522 2019 EST</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>transaction_timestamp</code> ( ) timestamp with time zone</p>
<p>Current date and time (start of current transaction); see <a href="#functions-datetime-current">Current Date/Time</a></p>
<p><code>transaction_timestamp()</code> 2019-12-23 14:39:53.662522-05</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_timestamp</code> ( <code>double precision</code> ) timestamp with time zone</p>
<p>Convert Unix epoch (seconds since 1970-01-01 00:00:00+00) to timestamp with time zone</p>
<p><code>to_timestamp(1284352323)</code> 2010-09-13 04:32:03+00</p></td>
</tr>
</tbody>
</table>

<span class="indexterm"></span> In addition to these functions, the SQL `OVERLAPS` operator is supported: (\<start1\>, \<end1\>) OVERLAPS (\<start2\>, \<end2\>) (\<start1\>, \<length1\>) OVERLAPS (\<start2\>, \<length2\>) This expression yields true when two time periods (defined by their endpoints) overlap, false when they do not overlap. The endpoints can be specified as pairs of dates, times, or time stamps; or as a date, time, or time stamp followed by an interval. When a pair of values is provided, either the start or the end can be written first; `OVERLAPS` automatically takes the earlier value of the pair as the start. Each time period is considered to represent the half-open interval \<start\> `<=` \<time\> `<` \<end\>, unless \<start\> and \<end\> are equal in which case it represents that single time instant. This means for instance that two time periods with only an endpoint in common do not overlap.

    SELECT (DATE '2001-02-16', DATE '2001-12-21') OVERLAPS
           (DATE '2001-10-30', DATE '2002-10-30');
    Result: true
    SELECT (DATE '2001-02-16', INTERVAL '100 days') OVERLAPS
           (DATE '2001-10-30', DATE '2002-10-30');
    Result: false
    SELECT (DATE '2001-10-29', DATE '2001-10-30') OVERLAPS
           (DATE '2001-10-30', DATE '2001-10-31');
    Result: false
    SELECT (DATE '2001-10-30', DATE '2001-10-30') OVERLAPS
           (DATE '2001-10-30', DATE '2001-10-31');
    Result: true

When adding an `interval` value to (or subtracting an `interval` value from) a `timestamp` or `timestamp with time zone` value, the months, days, and microseconds fields of the `interval` value are handled in turn. First, a nonzero months field advances or decrements the date of the timestamp by the indicated number of months, keeping the day of month the same unless it would be past the end of the new month, in which case the last day of that month is used. (For example, March 31 plus 1 month becomes April 30, but March 31 plus 2 months becomes May 31.) Then the days field advances or decrements the date of the timestamp by the indicated number of days. In both these steps the local time of day is kept the same. Finally, if there is a nonzero microseconds field, it is added or subtracted literally. When doing arithmetic on a `timestamp with time zone` value in a time zone that recognizes DST, this means that adding or subtracting (say) `interval '1 day'` does not necessarily have the same result as adding or subtracting `interval '24 hours'`. For example, with the session time zone set to `America/Denver`:

    SELECT timestamp with time zone '2005-04-02 12:00:00-07' + interval '1 day';
    Result: 2005-04-03 12:00:00-06
    SELECT timestamp with time zone '2005-04-02 12:00:00-07' + interval '24 hours';
    Result: 2005-04-03 13:00:00-06

This happens because an hour was skipped due to a change in daylight saving time at `2005-04-03 02:00:00` in time zone `America/Denver`.

Note there can be ambiguity in the `months` field returned by `age` because different months have different numbers of days. PostgreSQL's approach uses the month from the earlier of the two dates when calculating partial months. For example, `age('2004-06-01', '2004-04-30')` uses April to yield `1 mon 1 day`, while using May would yield `1 mon 2 days` because May has 31 days, while April has only 30.

Subtraction of dates and timestamps can also be complex. One conceptually simple way to perform subtraction is to convert each value to a number of seconds using `EXTRACT(EPOCH FROM ...)`, then subtract the results; this produces the number of *seconds* between the two values. This will adjust for the number of days in each month, timezone changes, and daylight saving time adjustments. Subtraction of date or timestamp values with the “`-`” operator returns the number of days (24-hours) and hours/minutes/seconds between the values, making the same adjustments. The `age` function returns years, months, days, and hours/minutes/seconds, performing field-by-field subtraction and then adjusting for negative field values. The following queries illustrate the differences in these approaches. The sample results were produced with `timezone = 'US/Eastern'`; there is a daylight saving time change between the two dates used:

    SELECT EXTRACT(EPOCH FROM timestamptz '2013-07-01 12:00:00') -
           EXTRACT(EPOCH FROM timestamptz '2013-03-01 12:00:00');
    Result: 10537200.000000
    SELECT (EXTRACT(EPOCH FROM timestamptz '2013-07-01 12:00:00') -
            EXTRACT(EPOCH FROM timestamptz '2013-03-01 12:00:00'))
            / 60 / 60 / 24;
    Result: 121.9583333333333333
    SELECT timestamptz '2013-07-01 12:00:00' - timestamptz '2013-03-01 12:00:00';
    Result: 121 days 23:00:00
    SELECT age(timestamptz '2013-07-01 12:00:00', timestamptz '2013-03-01 12:00:00');
    Result: 4 mons

### `EXTRACT`, `date_part`

date_part

extract

EXTRACT(

field

FROM

source

)

The `extract` function retrieves subfields such as year or hour from date/time values. \<source\> must be a value expression of type `timestamp`, `date`, `time`, or `interval`. (Timestamps and times can be with or without time zone.) \<field\> is an identifier or string that selects what field to extract from the source value. Not all fields are valid for every input data type; for example, fields smaller than a day cannot be extracted from a `date`, while fields of a day or more cannot be extracted from a `time`. The `extract` function returns values of type `numeric`.

The following are valid field names:

`century`  
The century; for `interval` values, the year field divided by 100

    SELECT EXTRACT(CENTURY FROM TIMESTAMP '2000-12-16 12:21:13');
    Result: 20
    SELECT EXTRACT(CENTURY FROM TIMESTAMP '2001-02-16 20:38:40');
    Result: 21
    SELECT EXTRACT(CENTURY FROM DATE '0001-01-01 AD');
    Result: 1
    SELECT EXTRACT(CENTURY FROM DATE '0001-12-31 BC');
    Result: -1
    SELECT EXTRACT(CENTURY FROM INTERVAL '2001 years');
    Result: 20

`day`  
The day of the month (131); for `interval` values, the number of days

    SELECT EXTRACT(DAY FROM TIMESTAMP '2001-02-16 20:38:40');
    Result: 16
    SELECT EXTRACT(DAY FROM INTERVAL '40 days 1 minute');
    Result: 40

`decade`  
The year field divided by 10

    SELECT EXTRACT(DECADE FROM TIMESTAMP '2001-02-16 20:38:40');
    Result: 200

`dow`  
The day of the week as Sunday (`0`) to Saturday (`6`)

    SELECT EXTRACT(DOW FROM TIMESTAMP '2001-02-16 20:38:40');
    Result: 5

Note that `extract`'s day of the week numbering differs from that of the `to_char(..., 'D')` function.

`doy`  
The day of the year (1365/366)

    SELECT EXTRACT(DOY FROM TIMESTAMP '2001-02-16 20:38:40');
    Result: 47

`epoch`  
For `timestamp with time zone` values, the number of seconds since 1970-01-01 00:00:00 UTC (negative for timestamps before that); for `date` and `timestamp` values, the nominal number of seconds since 1970-01-01 00:00:00, without regard to timezone or daylight-savings rules; for `interval` values, the total number of seconds in the interval

    SELECT EXTRACT(EPOCH FROM TIMESTAMP WITH TIME ZONE '2001-02-16 20:38:40.12-08');
    Result: 982384720.120000
    SELECT EXTRACT(EPOCH FROM TIMESTAMP '2001-02-16 20:38:40.12');
    Result: 982355920.120000
    SELECT EXTRACT(EPOCH FROM INTERVAL '5 days 3 hours');
    Result: 442800.000000

You can convert an epoch value back to a `timestamp with time zone` with `to_timestamp`:

    SELECT to_timestamp(982384720.12);
    Result: 2001-02-17 04:38:40.12+00

Beware that applying `to_timestamp` to an epoch extracted from a `date` or `timestamp` value could produce a misleading result: the result will effectively assume that the original value had been given in UTC, which might not be the case.

`hour`  
The hour field (023 in timestamps, unrestricted in intervals)

    SELECT EXTRACT(HOUR FROM TIMESTAMP '2001-02-16 20:38:40');
    Result: 20

`isodow`  
The day of the week as Monday (`1`) to Sunday (`7`)

    SELECT EXTRACT(ISODOW FROM TIMESTAMP '2001-02-18 20:38:40');
    Result: 7

This is identical to `dow` except for Sunday. This matches the ISO 8601 day of the week numbering.

`isoyear`  
The ISO 8601 week-numbering year that the date falls in

    SELECT EXTRACT(ISOYEAR FROM DATE '2006-01-01');
    Result: 2005
    SELECT EXTRACT(ISOYEAR FROM DATE '2006-01-02');
    Result: 2006

Each ISO 8601 week-numbering year begins with the Monday of the week containing the 4th of January, so in early January or late December the ISO year may be different from the Gregorian year. See the `week` field for more information.

`julian`  
The Julian Date corresponding to the date or timestamp. Timestamps that are not local midnight result in a fractional value. See [???](#datetime-julian-dates) for more information.

    SELECT EXTRACT(JULIAN FROM DATE '2006-01-01');
    Result: 2453737
    SELECT EXTRACT(JULIAN FROM TIMESTAMP '2006-01-01 12:00');
    Result: 2453737.50000000000000000000

`microseconds`  
The seconds field, including fractional parts, multiplied by 1 000 000; note that this includes full seconds

    SELECT EXTRACT(MICROSECONDS FROM TIME '17:12:28.5');
    Result: 28500000

`millennium`  
The millennium; for `interval` values, the year field divided by 1000

    SELECT EXTRACT(MILLENNIUM FROM TIMESTAMP '2001-02-16 20:38:40');
    Result: 3
    SELECT EXTRACT(MILLENNIUM FROM INTERVAL '2001 years');
    Result: 2

Years in the 1900s are in the second millennium. The third millennium started January 1, 2001.

`milliseconds`  
The seconds field, including fractional parts, multiplied by 1000. Note that this includes full seconds.

    SELECT EXTRACT(MILLISECONDS FROM TIME '17:12:28.5');
    Result: 28500.000

`minute`  
The minutes field (059)

    SELECT EXTRACT(MINUTE FROM TIMESTAMP '2001-02-16 20:38:40');
    Result: 38

`month`  
The number of the month within the year (112); for `interval` values, the number of months modulo 12 (011)

    SELECT EXTRACT(MONTH FROM TIMESTAMP '2001-02-16 20:38:40');
    Result: 2
    SELECT EXTRACT(MONTH FROM INTERVAL '2 years 3 months');
    Result: 3
    SELECT EXTRACT(MONTH FROM INTERVAL '2 years 13 months');
    Result: 1

`quarter`  
The quarter of the year (14) that the date is in

    SELECT EXTRACT(QUARTER FROM TIMESTAMP '2001-02-16 20:38:40');
    Result: 1

`second`  
The seconds field, including any fractional seconds

    SELECT EXTRACT(SECOND FROM TIMESTAMP '2001-02-16 20:38:40');
    Result: 40.000000
    SELECT EXTRACT(SECOND FROM TIME '17:12:28.5');
    Result: 28.500000

`timezone`  
The time zone offset from UTC, measured in seconds. Positive values correspond to time zones east of UTC, negative values to zones west of UTC. (Technically, PostgreSQL does not use UTC because leap seconds are not handled.)

`timezone_hour`  
The hour component of the time zone offset

`timezone_minute`  
The minute component of the time zone offset

`week`  
The number of the ISO 8601 week-numbering week of the year. By definition, ISO weeks start on Mondays and the first week of a year contains January 4 of that year. In other words, the first Thursday of a year is in week 1 of that year.

In the ISO week-numbering system, it is possible for early-January dates to be part of the 52nd or 53rd week of the previous year, and for late-December dates to be part of the first week of the next year. For example, `2005-01-01` is part of the 53rd week of year 2004, and `2006-01-01` is part of the 52nd week of year 2005, while `2012-12-31` is part of the first week of 2013. It's recommended to use the `isoyear` field together with `week` to get consistent results.

    SELECT EXTRACT(WEEK FROM TIMESTAMP '2001-02-16 20:38:40');
    Result: 7

`year`  
The year field. Keep in mind there is no `0 AD`, so subtracting `BC` years from `AD` years should be done with care.

    SELECT EXTRACT(YEAR FROM TIMESTAMP '2001-02-16 20:38:40');
    Result: 2001

When processing an `interval` value, the `extract` function produces field values that match the interpretation used by the interval output function. This can produce surprising results if one starts with a non-normalized interval representation, for example:

    SELECT INTERVAL '80 minutes';
    Result: 01:20:00
    SELECT EXTRACT(MINUTES FROM INTERVAL '80 minutes');
    Result: 20

> [!NOTE]
> When the input value is +/-Infinity, `extract` returns +/-Infinity for monotonically-increasing fields (`epoch`, `julian`, `year`, `isoyear`, `decade`, `century`, and `millennium` for `timestamp` inputs; `epoch`, `hour`, `day`, `year`, `decade`, `century`, and `millennium` for `interval` inputs). For other fields, NULL is returned. PostgreSQL versions before 9.6 returned zero for all cases of infinite input.

The `extract` function is primarily intended for computational processing. For formatting date/time values for display, see [Data Type Formatting Functions](#functions-formatting).

The `date_part` function is modeled on the traditional Ingres equivalent to the SQL-standard function `extract`: date_part('\<field\>', \<source\>) Note that here the \<field\> parameter needs to be a string value, not a name. The valid field names for `date_part` are the same as for `extract`. For historical reasons, the `date_part` function returns values of type `double precision`. This can result in a loss of precision in certain uses. Using `extract` is recommended instead.

    SELECT date_part('day', TIMESTAMP '2001-02-16 20:38:40');
    Result: 16
    SELECT date_part('hour', INTERVAL '4 hours 3 minutes');
    Result: 4

### `date_trunc`

date_trunc

The function `date_trunc` is conceptually similar to the `trunc` function for numbers.

date_trunc(\<field\>, \<source\> \[, \<time_zone\> \]) \<source\> is a value expression of type `timestamp`, `timestamp with time zone`, or `interval`. (Values of type `date` and `time` are cast automatically to `timestamp` or `interval`, respectively.) \<field\> selects to which precision to truncate the input value. The return value is likewise of type `timestamp`, `timestamp with time zone`, or `interval`, and it has all fields that are less significant than the selected one set to zero (or one, for day and month).

Valid values for \<field\> are: `microseconds`, `milliseconds`, `second`, `minute`, `hour`, `day`, `week`, `month`, `quarter`, `year`, `decade`, `century`, `millennium`

When the input value is of type `timestamp with time zone`, the truncation is performed with respect to a particular time zone; for example, truncation to `day` produces a value that is midnight in that zone. By default, truncation is done with respect to the current [???](#guc-timezone) setting, but the optional \<time_zone\> argument can be provided to specify a different time zone. The time zone name can be specified in any of the ways described in [???](#datatype-timezones).

A time zone cannot be specified when processing `timestamp without time zone` or `interval` inputs. These are always taken at face value.

Examples (assuming the local time zone is `America/New_York`):

    SELECT date_trunc('hour', TIMESTAMP '2001-02-16 20:38:40');
    Result: 2001-02-16 20:00:00
    SELECT date_trunc('year', TIMESTAMP '2001-02-16 20:38:40');
    Result: 2001-01-01 00:00:00
    SELECT date_trunc('day', TIMESTAMP WITH TIME ZONE '2001-02-16 20:38:40+00');
    Result: 2001-02-16 00:00:00-05
    SELECT date_trunc('day', TIMESTAMP WITH TIME ZONE '2001-02-16 20:38:40+00', 'Australia/Sydney');
    Result: 2001-02-16 08:00:00-05
    SELECT date_trunc('hour', INTERVAL '3 days 02:47:33');
    Result: 3 days 02:00:00

### `date_bin`

date_bin

The function `date_bin` “bins” the input timestamp into the specified interval (the stride) aligned with a specified origin.

date_bin(\<stride\>, \<source\>, \<origin\>) \<source\> is a value expression of type `timestamp` or `timestamp with time zone`. (Values of type `date` are cast automatically to `timestamp`.) \<stride\> is a value expression of type `interval`. The return value is likewise of type `timestamp` or `timestamp with time zone`, and it marks the beginning of the bin into which the \<source\> is placed.

Examples:

    SELECT date_bin('15 minutes', TIMESTAMP '2020-02-11 15:44:17', TIMESTAMP '2001-01-01');
    Result: 2020-02-11 15:30:00
    SELECT date_bin('15 minutes', TIMESTAMP '2020-02-11 15:44:17', TIMESTAMP '2001-01-01 00:02:30');
    Result: 2020-02-11 15:32:30

In the case of full units (1 minute, 1 hour, etc.), it gives the same result as the analogous `date_trunc` call, but the difference is that `date_bin` can truncate to an arbitrary interval.

The `stride` interval must be greater than zero and cannot contain units of month or larger.

### `AT TIME ZONE` and `AT LOCAL`

time zone

conversion

AT TIME ZONE

AT LOCAL

The `AT TIME ZONE` operator converts time stamp *without* time zone to/from time stamp *with* time zone, and `time with time zone` values to different time zones. [ and Variants](#functions-datetime-zoneconvert-table) shows its variants.

<table id="functions-datetime-zoneconvert-table">
<caption><code>AT TIME ZONE</code> and <code>AT LOCAL</code> Variants</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>timestamp without time zone</code> <code>AT TIME ZONE</code> &lt;zone&gt; timestamp with time zone</p>
<p>Converts given time stamp <em>without</em> time zone to time stamp <em>with</em> time zone, assuming the given value is in the named time zone.</p>
<p><code>timestamp '2001-02-16 20:38:40' at time zone 'America/Denver'</code> 2001-02-17 03:38:40+00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>timestamp without time zone</code> <code>AT LOCAL</code> timestamp with time zone</p>
<p>Converts given time stamp <em>without</em> time zone to time stamp <em>with</em> the session's <code>TimeZone</code> value as time zone.</p>
<p><code>timestamp '2001-02-16 20:38:40' at local</code> 2001-02-17 03:38:40+00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>timestamp with time zone</code> <code>AT TIME ZONE</code> &lt;zone&gt; timestamp without time zone</p>
<p>Converts given time stamp <em>with</em> time zone to time stamp <em>without</em> time zone, as the time would appear in that zone.</p>
<p><code>timestamp with time zone '2001-02-16 20:38:40-05' at time zone 'America/Denver'</code> 2001-02-16 18:38:40</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>timestamp with time zone</code> <code>AT LOCAL</code> timestamp without time zone</p>
<p>Converts given time stamp <em>with</em> time zone to time stamp <em>without</em> time zone, as the time would appear with the session's <code>TimeZone</code> value as time zone.</p>
<p><code>timestamp with time zone '2001-02-16 20:38:40-05' at local</code> 2001-02-16 18:38:40</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>time with time zone</code> <code>AT TIME ZONE</code> &lt;zone&gt; time with time zone</p>
<p>Converts given time <em>with</em> time zone to a new time zone. Since no date is supplied, this uses the currently active UTC offset for the named destination zone.</p>
<p><code>time with time zone '05:34:17-05' at time zone 'UTC'</code> 10:34:17+00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>time with time zone</code> <code>AT LOCAL</code> time with time zone</p>
<p>Converts given time <em>with</em> time zone to a new time zone. Since no date is supplied, this uses the currently active UTC offset for the session's <code>TimeZone</code> value.</p>
<p>Assuming the session's <code>TimeZone</code> is set to <code>UTC</code>:</p>
<p><code>time with time zone '05:34:17-05' at local</code> 10:34:17+00</p></td>
</tr>
</tbody>
</table>

In these expressions, the desired time zone \<zone\> can be specified either as a text value (e.g., `'America/Los_Angeles'`) or as an interval (e.g., `INTERVAL '-08:00'`). In the text case, a time zone name can be specified in any of the ways described in [???](#datatype-timezones). The interval case is only useful for zones that have fixed offsets from UTC, so it is not very common in practice.

The syntax `AT LOCAL` may be used as shorthand for `AT TIME ZONE local`, where \<local\> is the session's `TimeZone` value.

Examples (assuming the current [???](#guc-timezone) setting is `America/Los_Angeles`):

    SELECT TIMESTAMP '2001-02-16 20:38:40' AT TIME ZONE 'America/Denver';
    Result: 2001-02-16 19:38:40-08
    SELECT TIMESTAMP WITH TIME ZONE '2001-02-16 20:38:40-05' AT TIME ZONE 'America/Denver';
    Result: 2001-02-16 18:38:40
    SELECT TIMESTAMP '2001-02-16 20:38:40' AT TIME ZONE 'Asia/Tokyo' AT TIME ZONE 'America/Chicago';
    Result: 2001-02-16 05:38:40
    SELECT TIMESTAMP WITH TIME ZONE '2001-02-16 20:38:40-05' AT LOCAL;
    Result: 2001-02-16 17:38:40
    SELECT TIME WITH TIME ZONE '20:38:40-05' AT LOCAL;
    Result: 17:38:40

The first example adds a time zone to a value that lacks it, and displays the value using the current `TimeZone` setting. The second example shifts the time stamp with time zone value to the specified time zone, and returns the value without a time zone. This allows storage and display of values different from the current `TimeZone` setting. The third example converts Tokyo time to Chicago time. The fourth example shifts the time stamp with time zone value to the time zone currently specified by the `TimeZone` setting and returns the value without a time zone.

The fifth example is a cautionary tale. Due to the fact that there is no date associated with the input value, the conversion is made using the current date of the session. Therefore, this static example may show a wrong result depending on the time of the year it is viewed because `'America/Los_Angeles'` observes Daylight Savings Time.

The function `timezone(zone, timestamp)` is equivalent to the SQL-conforming construct `timestamp AT TIME ZONE zone`.

The function `timezone(zone, time)` is equivalent to the SQL-conforming construct `time AT TIME ZONE zone`.

The function `timezone(timestamp)` is equivalent to the SQL-conforming construct `timestamp AT LOCAL`.

The function `timezone(time)` is equivalent to the SQL-conforming construct `time AT LOCAL`.

### Current Date/Time

date

current

time

current

PostgreSQL provides a number of functions that return values related to the current date and time. These SQL-standard functions all return values based on the start time of the current transaction: CURRENT_DATE CURRENT_TIME CURRENT_TIMESTAMP CURRENT_TIME(\<precision\>) CURRENT_TIMESTAMP(\<precision\>) LOCALTIME LOCALTIMESTAMP LOCALTIME(\<precision\>) LOCALTIMESTAMP(\<precision\>)

`CURRENT_TIME` and `CURRENT_TIMESTAMP` deliver values with time zone; `LOCALTIME` and `LOCALTIMESTAMP` deliver values without time zone.

`CURRENT_TIME`, `CURRENT_TIMESTAMP`, `LOCALTIME`, and `LOCALTIMESTAMP` can optionally take a precision parameter, which causes the result to be rounded to that many fractional digits in the seconds field. Without a precision parameter, the result is given to the full available precision.

Some examples:

    SELECT CURRENT_TIME;
    Result: 14:39:53.662522-05
    SELECT CURRENT_DATE;
    Result: 2019-12-23
    SELECT CURRENT_TIMESTAMP;
    Result: 2019-12-23 14:39:53.662522-05
    SELECT CURRENT_TIMESTAMP(2);
    Result: 2019-12-23 14:39:53.66-05
    SELECT LOCALTIMESTAMP;
    Result: 2019-12-23 14:39:53.662522

Since these functions return the start time of the current transaction, their values do not change during the transaction. This is considered a feature: the intent is to allow a single transaction to have a consistent notion of the “current” time, so that multiple modifications within the same transaction bear the same time stamp.

> [!NOTE]
> Other database systems might advance these values more frequently.

PostgreSQL also provides functions that return the start time of the current statement, as well as the actual current time at the instant the function is called. The complete list of non-SQL-standard time functions is: transaction_timestamp() statement_timestamp() clock_timestamp() timeofday() now()

`transaction_timestamp()` is equivalent to `CURRENT_TIMESTAMP`, but is named to clearly reflect what it returns. `statement_timestamp()` returns the start time of the current statement (more specifically, the time of receipt of the latest command message from the client). `statement_timestamp()` and `transaction_timestamp()` return the same value during the first statement of a transaction, but might differ during subsequent statements. `clock_timestamp()` returns the actual current time, and therefore its value changes even within a single SQL statement. `timeofday()` is a historical PostgreSQL function. Like `clock_timestamp()`, it returns the actual current time, but as a formatted `text` string rather than a `timestamp with time zone` value. `now()` is a traditional PostgreSQL equivalent to `transaction_timestamp()`.

All the date/time data types also accept the special literal value `now` to specify the current date and time (again, interpreted as the transaction start time). Thus, the following three all return the same result:

    SELECT CURRENT_TIMESTAMP;
    SELECT now();
    SELECT TIMESTAMP 'now';  -- but see tip below

> [!TIP]
> Do not use the third form when specifying a value to be evaluated later, for example in a `DEFAULT` clause for a table column. The system will convert `now` to a `timestamp` as soon as the constant is parsed, so that when the default value is needed, the time of the table creation would be used! The first two forms will not be evaluated until the default value is used, because they are function calls. Thus they will give the desired behavior of defaulting to the time of row insertion. (See also [???](#datatype-datetime-special-values).)

### Delaying Execution

pg_sleep

pg_sleep_for

pg_sleep_until

sleep

delay

The following functions are available to delay execution of the server process: pg_sleep ( `double precision` ) pg_sleep_for ( `interval` ) pg_sleep_until ( `timestamp with time zone` ) `pg_sleep` makes the current session's process sleep until the given number of seconds have elapsed. Fractional-second delays can be specified. `pg_sleep_for` is a convenience function to allow the sleep time to be specified as an `interval`. `pg_sleep_until` is a convenience function for when a specific wake-up time is desired. For example:

    SELECT pg_sleep(1.5);
    SELECT pg_sleep_for('5 minutes');
    SELECT pg_sleep_until('tomorrow 03:00');

> [!NOTE]
> The effective resolution of the sleep interval is platform-specific; 0.01 seconds is a common value. The sleep delay will be at least as long as specified. It might be longer depending on factors such as server load. In particular, `pg_sleep_until` is not guaranteed to wake up exactly at the specified time, but it will not wake up any earlier.

> [!WARNING]
> Make sure that your session does not hold more locks than necessary when calling `pg_sleep` or its variants. Otherwise other sessions might have to wait for your sleeping process, slowing down the entire system.

## Enum Support Functions

For enum types (described in [???](#datatype-enum)), there are several functions that allow cleaner programming without hard-coding particular values of an enum type. These are listed in [Enum Support Functions](#functions-enum-table). The examples assume an enum type created as:

    CREATE TYPE rainbow AS ENUM ('red', 'orange', 'yellow', 'green', 'blue', 'purple');

<table id="functions-enum-table">
<caption>Enum Support Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>enum_first</code> ( <code>anyenum</code> ) anyenum</p>
<p>Returns the first value of the input enum type.</p>
<p><code>enum_first(null::rainbow)</code> red</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>enum_last</code> ( <code>anyenum</code> ) anyenum</p>
<p>Returns the last value of the input enum type.</p>
<p><code>enum_last(null::rainbow)</code> purple</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>enum_range</code> ( <code>anyenum</code> ) anyarray</p>
<p>Returns all values of the input enum type in an ordered array.</p>
<p><code>enum_range(null::rainbow)</code> {red,orange,yellow,​green,blue,purple}</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>enum_range</code> ( <code>anyenum</code>, <code>anyenum</code> ) anyarray</p>
<p>Returns the range between the two given enum values, as an ordered array. The values must be from the same enum type. If the first parameter is null, the result will start with the first value of the enum type. If the second parameter is null, the result will end with the last value of the enum type.</p>
<p><code>enum_range('orange'::rainbow, 'green'::rainbow)</code> {orange,yellow,green}</p>
<p><code>enum_range(NULL, 'green'::rainbow)</code> {red,orange,​yellow,green}</p>
<p><code>enum_range('orange'::rainbow, NULL)</code> {orange,yellow,green,​blue,purple}</p></td>
</tr>
</tbody>
</table>

Notice that except for the two-argument form of `enum_range`, these functions disregard the specific value passed to them; they care only about its declared data type. Either null or a specific value of the type can be passed, with the same result. It is more common to apply these functions to a table column or function argument than to a hardwired type name as used in the examples.

## Geometric Functions and Operators

The geometric types `point`, `box`, `lseg`, `line`, `path`, `polygon`, and `circle` have a large set of native support functions and operators, shown in [Geometric Operators](#functions-geometry-op-table), [Geometric Functions](#functions-geometry-func-table), and [Geometric Type Conversion Functions](#functions-geometry-conv-table).

<table id="functions-geometry-op-table">
<caption>Geometric Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>+</code> <code>point</code> &lt;geometric_type&gt;</p>
<p>Adds the coordinates of the second <code>point</code> to those of each point of the first argument, thus performing translation. Available for <code>point</code>, <code>box</code>, <code>path</code>, <code>circle</code>.</p>
<p><code>box '(1,1),(0,0)' + point '(2,0)'</code> (3,1),(2,0)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>path</code> <code>+</code> <code>path</code> path</p>
<p>Concatenates two open paths (returns NULL if either path is closed).</p>
<p><code>path '[(0,0),(1,1)]' + path '[(2,2),(3,3),(4,4)]'</code> [(0,0),(1,1),(2,2),(3,3),(4,4)]</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>-</code> <code>point</code> &lt;geometric_type&gt;</p>
<p>Subtracts the coordinates of the second <code>point</code> from those of each point of the first argument, thus performing translation. Available for <code>point</code>, <code>box</code>, <code>path</code>, <code>circle</code>.</p>
<p><code>box '(1,1),(0,0)' - point '(2,0)'</code> (-1,1),(-2,0)</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>*</code> <code>point</code> &lt;geometric_type&gt;</p>
<p>Multiplies each point of the first argument by the second <code>point</code> (treating a point as being a complex number represented by real and imaginary parts, and performing standard complex multiplication). If one interprets the second <code>point</code> as a vector, this is equivalent to scaling the object's size and distance from the origin by the length of the vector, and rotating it counterclockwise around the origin by the vector's angle from the &lt;x&gt; axis. Available for <code>point</code>, <code>box</code>,<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a> <code>path</code>, <code>circle</code>.</p>
<p><code>path '((0,0),(1,0),(1,1))' * point '(3.0,0)'</code> ((0,0),(3,0),(3,3))</p>
<p><code>path '((0,0),(1,0),(1,1))' * point(cosd(45), sind(45))</code> ((0,0),​(0.7071067811865475,0.7071067811865475),​(0,1.414213562373095))</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>/</code> <code>point</code> &lt;geometric_type&gt;</p>
<p>Divides each point of the first argument by the second <code>point</code> (treating a point as being a complex number represented by real and imaginary parts, and performing standard complex division). If one interprets the second <code>point</code> as a vector, this is equivalent to scaling the object's size and distance from the origin down by the length of the vector, and rotating it clockwise around the origin by the vector's angle from the &lt;x&gt; axis. Available for <code>point</code>, <code>box</code>, <code>path</code>, <code>circle</code>.</p>
<p><code>path '((0,0),(1,0),(1,1))' / point '(2.0,0)'</code> ((0,0),(0.5,0),(0.5,0.5))</p>
<p><code>path '((0,0),(1,0),(1,1))' / point(cosd(45), sind(45))</code> ((0,0),​(0.7071067811865476,-0.7071067811865476),​(1.4142135623730951,0))</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>@-@</code> &lt;geometric_type&gt; double precision</p>
<p>Computes the total length. Available for <code>lseg</code>, <code>path</code>.</p>
<p><code>@-@ path '[(0,0),(1,0),(1,1)]'</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>@@</code> &lt;geometric_type&gt; point</p>
<p>Computes the center point. Available for <code>box</code>, <code>lseg</code>, <code>polygon</code>, <code>circle</code>.</p>
<p><code>@@ box '(2,2),(0,0)'</code> (1,1)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>#</code> &lt;geometric_type&gt; integer</p>
<p>Returns the number of points. Available for <code>path</code>, <code>polygon</code>.</p>
<p><code># path '((1,0),(0,1),(-1,0))'</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>#</code> &lt;geometric_type&gt; point</p>
<p>Computes the point of intersection, or NULL if there is none. Available for <code>lseg</code>, <code>line</code>.</p>
<p><code>lseg '[(0,0),(1,1)]' # lseg '[(1,0),(0,1)]'</code> (0.5,0.5)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>box</code> <code>#</code> <code>box</code> box</p>
<p>Computes the intersection of two boxes, or NULL if there is none.</p>
<p><code>box '(2,2),(-1,-1)' # box '(1,1),(-2,-2)'</code> (1,1),(-1,-1)</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>##</code> &lt;geometric_type&gt; point</p>
<p>Computes the closest point to the first object on the second object. Available for these pairs of types: (<code>point</code>, <code>box</code>), (<code>point</code>, <code>lseg</code>), (<code>point</code>, <code>line</code>), (<code>lseg</code>, <code>box</code>), (<code>lseg</code>, <code>lseg</code>), (<code>line</code>, <code>lseg</code>).</p>
<p><code>point '(0,0)' ## lseg '[(2,0),(0,2)]'</code> (1,1)</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>&lt;-&gt;</code> &lt;geometric_type&gt; double precision</p>
<p>Computes the distance between the objects. Available for all seven geometric types, for all combinations of <code>point</code> with another geometric type, and for these additional pairs of types: (<code>box</code>, <code>lseg</code>), (<code>lseg</code>, <code>line</code>), (<code>polygon</code>, <code>circle</code>) (and the commutator cases).</p>
<p><code>circle '&lt;(0,0),1&gt;' &lt;-&gt; circle '&lt;(5,0),1&gt;'</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>@&gt;</code> &lt;geometric_type&gt; boolean</p>
<p>Does first object contain second? Available for these pairs of types: (<code>box</code>, <code>point</code>), (<code>box</code>, <code>box</code>), (<code>path</code>, <code>point</code>), (<code>polygon</code>, <code>point</code>), (<code>polygon</code>, <code>polygon</code>), (<code>circle</code>, <code>point</code>), (<code>circle</code>, <code>circle</code>).</p>
<p><code>circle '&lt;(0,0),2&gt;' @&gt; point '(1,1)'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>&lt;@</code> &lt;geometric_type&gt; boolean</p>
<p>Is first object contained in or on second? Available for these pairs of types: (<code>point</code>, <code>box</code>), (<code>point</code>, <code>lseg</code>), (<code>point</code>, <code>line</code>), (<code>point</code>, <code>path</code>), (<code>point</code>, <code>polygon</code>), (<code>point</code>, <code>circle</code>), (<code>box</code>, <code>box</code>), (<code>lseg</code>, <code>box</code>), (<code>lseg</code>, <code>line</code>), (<code>polygon</code>, <code>polygon</code>), (<code>circle</code>, <code>circle</code>).</p>
<p><code>point '(1,1)' &lt;@ circle '&lt;(0,0),2&gt;'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>&amp;&amp;</code> &lt;geometric_type&gt; boolean</p>
<p>Do these objects overlap? (One point in common makes this true.) Available for <code>box</code>, <code>polygon</code>, <code>circle</code>.</p>
<p><code>box '(1,1),(0,0)' &amp;&amp; box '(2,2),(0,0)'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>&lt;&lt;</code> &lt;geometric_type&gt; boolean</p>
<p>Is first object strictly left of second? Available for <code>point</code>, <code>box</code>, <code>polygon</code>, <code>circle</code>.</p>
<p><code>circle '&lt;(0,0),1&gt;' &lt;&lt; circle '&lt;(5,0),1&gt;'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>&gt;&gt;</code> &lt;geometric_type&gt; boolean</p>
<p>Is first object strictly right of second? Available for <code>point</code>, <code>box</code>, <code>polygon</code>, <code>circle</code>.</p>
<p><code>circle '&lt;(5,0),1&gt;' &gt;&gt; circle '&lt;(0,0),1&gt;'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>&amp;&lt;</code> &lt;geometric_type&gt; boolean</p>
<p>Does first object not extend to the right of second? Available for <code>box</code>, <code>polygon</code>, <code>circle</code>.</p>
<p><code>box '(1,1),(0,0)' &amp;&lt; box '(2,2),(0,0)'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>&amp;&gt;</code> &lt;geometric_type&gt; boolean</p>
<p>Does first object not extend to the left of second? Available for <code>box</code>, <code>polygon</code>, <code>circle</code>.</p>
<p><code>box '(3,3),(0,0)' &amp;&gt; box '(2,2),(0,0)'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>&lt;&lt;|</code> &lt;geometric_type&gt; boolean</p>
<p>Is first object strictly below second? Available for <code>point</code>, <code>box</code>, <code>polygon</code>, <code>circle</code>.</p>
<p><code>box '(3,3),(0,0)' &lt;&lt;| box '(5,5),(3,4)'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>|&gt;&gt;</code> &lt;geometric_type&gt; boolean</p>
<p>Is first object strictly above second? Available for <code>point</code>, <code>box</code>, <code>polygon</code>, <code>circle</code>.</p>
<p><code>box '(5,5),(3,4)' |&gt;&gt; box '(3,3),(0,0)'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>&amp;&lt;|</code> &lt;geometric_type&gt; boolean</p>
<p>Does first object not extend above second? Available for <code>box</code>, <code>polygon</code>, <code>circle</code>.</p>
<p><code>box '(1,1),(0,0)' &amp;&lt;| box '(2,2),(0,0)'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>|&amp;&gt;</code> &lt;geometric_type&gt; boolean</p>
<p>Does first object not extend below second? Available for <code>box</code>, <code>polygon</code>, <code>circle</code>.</p>
<p><code>box '(3,3),(0,0)' |&amp;&gt; box '(2,2),(0,0)'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>box</code> <code>&lt;^</code> <code>box</code> boolean</p>
<p>Is first object below second (allows edges to touch)?</p>
<p><code>box '((1,1),(0,0))' &lt;^ box '((2,2),(1,1))'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>box</code> <code>&gt;^</code> <code>box</code> boolean</p>
<p>Is first object above second (allows edges to touch)?</p>
<p><code>box '((2,2),(1,1))' &gt;^ box '((1,1),(0,0))'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>?#</code> &lt;geometric_type&gt; boolean</p>
<p>Do these objects intersect? Available for these pairs of types: (<code>box</code>, <code>box</code>), (<code>lseg</code>, <code>box</code>), (<code>lseg</code>, <code>lseg</code>), (<code>lseg</code>, <code>line</code>), (<code>line</code>, <code>box</code>), (<code>line</code>, <code>line</code>), (<code>path</code>, <code>path</code>).</p>
<p><code>lseg '[(-1,0),(1,0)]' ?# box '(2,2),(-2,-2)'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>?-</code> <code>line</code> boolean</p>
<p role="func_signature"><code>?-</code> <code>lseg</code> boolean</p>
<p>Is line horizontal?</p>
<p><code>?- lseg '[(-1,0),(1,0)]'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>point</code> <code>?-</code> <code>point</code> boolean</p>
<p>Are points horizontally aligned (that is, have same y coordinate)?</p>
<p><code>point '(1,0)' ?- point '(0,0)'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>?|</code> <code>line</code> boolean</p>
<p role="func_signature"><code>?|</code> <code>lseg</code> boolean</p>
<p>Is line vertical?</p>
<p><code>?| lseg '[(-1,0),(1,0)]'</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>point</code> <code>?|</code> <code>point</code> boolean</p>
<p>Are points vertically aligned (that is, have same x coordinate)?</p>
<p><code>point '(0,1)' ?| point '(0,0)'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>line</code> <code>?-|</code> <code>line</code> boolean</p>
<p role="func_signature"><code>lseg</code> <code>?-|</code> <code>lseg</code> boolean</p>
<p>Are lines perpendicular?</p>
<p><code>lseg '[(0,0),(0,1)]' ?-| lseg '[(0,0),(1,0)]'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>line</code> <code>?||</code> <code>line</code> boolean</p>
<p role="func_signature"><code>lseg</code> <code>?||</code> <code>lseg</code> boolean</p>
<p>Are lines parallel?</p>
<p><code>lseg '[(-1,0),(1,0)]' ?|| lseg '[(-1,2),(1,2)]'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;geometric_type&gt; <code>~=</code> &lt;geometric_type&gt; boolean</p>
<p>Are these objects the same? Available for <code>point</code>, <code>box</code>, <code>polygon</code>, <code>circle</code>.</p>
<p><code>polygon '((0,0),(1,1))' ~= polygon '((1,1),(0,0))'</code> t</p></td>
</tr>
</tbody>
</table>
<section id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>“Rotating” a box with these operators only moves its corner points: the box is still considered to have sides parallel to the axes. Hence the box's size is not preserved, as a true rotation would do.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</section>

> [!CAUTION]
> Note that the “same as” operator, `~=`, represents the usual notion of equality for the `point`, `box`, `polygon`, and `circle` types. Some of the geometric types also have an `=` operator, but `=` compares for equal *areas* only. The other scalar comparison operators (`<=` and so on), where available for these types, likewise compare areas.

> [!NOTE]
> Before PostgreSQL 14, the point is strictly below/above comparison operators `point` `<<|` `point` and `point` `|>>` `point` were respectively called `<^` and `>^`. These names are still available, but are deprecated and will eventually be removed.

<table id="functions-geometry-func-table">
<caption>Geometric Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>area</code> ( &lt;geometric_type&gt; ) double precision</p>
<p>Computes area. Available for <code>box</code>, <code>path</code>, <code>circle</code>. A <code>path</code> input must be closed, else NULL is returned. Also, if the <code>path</code> is self-intersecting, the result may be meaningless.</p>
<p><code>area(box '(2,2),(0,0)')</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>center</code> ( &lt;geometric_type&gt; ) point</p>
<p>Computes center point. Available for <code>box</code>, <code>circle</code>.</p>
<p><code>center(box '(1,2),(0,0)')</code> (0.5,1)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>diagonal</code> ( <code>box</code> ) lseg</p>
<p>Extracts box's diagonal as a line segment (same as <code>lseg(box)</code>).</p>
<p><code>diagonal(box '(1,2),(0,0)')</code> [(1,2),(0,0)]</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>diameter</code> ( <code>circle</code> ) double precision</p>
<p>Computes diameter of circle.</p>
<p><code>diameter(circle '&lt;(0,0),2&gt;')</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>height</code> ( <code>box</code> ) double precision</p>
<p>Computes vertical size of box.</p>
<p><code>height(box '(1,2),(0,0)')</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>isclosed</code> ( <code>path</code> ) boolean</p>
<p>Is path closed?</p>
<p><code>isclosed(path '((0,0),(1,1),(2,0))')</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>isopen</code> ( <code>path</code> ) boolean</p>
<p>Is path open?</p>
<p><code>isopen(path '[(0,0),(1,1),(2,0)]')</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>length</code> ( &lt;geometric_type&gt; ) double precision</p>
<p>Computes the total length. Available for <code>lseg</code>, <code>path</code>.</p>
<p><code>length(path '((-1,0),(1,0))')</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>npoints</code> ( &lt;geometric_type&gt; ) integer</p>
<p>Returns the number of points. Available for <code>path</code>, <code>polygon</code>.</p>
<p><code>npoints(path '[(0,0),(1,1),(2,0)]')</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pclose</code> ( <code>path</code> ) path</p>
<p>Converts path to closed form.</p>
<p><code>pclose(path '[(0,0),(1,1),(2,0)]')</code> ((0,0),(1,1),(2,0))</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>popen</code> ( <code>path</code> ) path</p>
<p>Converts path to open form.</p>
<p><code>popen(path '((0,0),(1,1),(2,0))')</code> [(0,0),(1,1),(2,0)]</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>radius</code> ( <code>circle</code> ) double precision</p>
<p>Computes radius of circle.</p>
<p><code>radius(circle '&lt;(0,0),2&gt;')</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>slope</code> ( <code>point</code>, <code>point</code> ) double precision</p>
<p>Computes slope of a line drawn through the two points.</p>
<p><code>slope(point '(0,0)', point '(2,1)')</code> 0.5</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>width</code> ( <code>box</code> ) double precision</p>
<p>Computes horizontal size of box.</p>
<p><code>width(box '(1,2),(0,0)')</code> 1</p></td>
</tr>
</tbody>
</table>

<table id="functions-geometry-conv-table">
<caption>Geometric Type Conversion Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>box</code> ( <code>circle</code> ) box</p>
<p>Computes box inscribed within the circle.</p>
<p><code>box(circle '&lt;(0,0),2&gt;')</code> (1.414213562373095,1.414213562373095),​(-1.414213562373095,-1.414213562373095)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>box</code> ( <code>point</code> ) box</p>
<p>Converts point to empty box.</p>
<p><code>box(point '(1,0)')</code> (1,0),(1,0)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>box</code> ( <code>point</code>, <code>point</code> ) box</p>
<p>Converts any two corner points to box.</p>
<p><code>box(point '(0,1)', point '(1,0)')</code> (1,1),(0,0)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>box</code> ( <code>polygon</code> ) box</p>
<p>Computes bounding box of polygon.</p>
<p><code>box(polygon '((0,0),(1,1),(2,0))')</code> (2,1),(0,0)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>bound_box</code> ( <code>box</code>, <code>box</code> ) box</p>
<p>Computes bounding box of two boxes.</p>
<p><code>bound_box(box '(1,1),(0,0)', box '(4,4),(3,3)')</code> (4,4),(0,0)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>circle</code> ( <code>box</code> ) circle</p>
<p>Computes smallest circle enclosing box.</p>
<p><code>circle(box '(1,1),(0,0)')</code> &lt;(0.5,0.5),0.7071067811865476&gt;</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>circle</code> ( <code>point</code>, <code>double precision</code> ) circle</p>
<p>Constructs circle from center and radius.</p>
<p><code>circle(point '(0,0)', 2.0)</code> &lt;(0,0),2&gt;</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>circle</code> ( <code>polygon</code> ) circle</p>
<p>Converts polygon to circle. The circle's center is the mean of the positions of the polygon's points, and the radius is the average distance of the polygon's points from that center.</p>
<p><code>circle(polygon '((0,0),(1,3),(2,0))')</code> &lt;(1,1),1.6094757082487299&gt;</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>line</code> ( <code>point</code>, <code>point</code> ) line</p>
<p>Converts two points to the line through them.</p>
<p><code>line(point '(-1,0)', point '(1,0)')</code> {0,-1,0}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lseg</code> ( <code>box</code> ) lseg</p>
<p>Extracts box's diagonal as a line segment.</p>
<p><code>lseg(box '(1,0),(-1,0)')</code> [(1,0),(-1,0)]</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>lseg</code> ( <code>point</code>, <code>point</code> ) lseg</p>
<p>Constructs line segment from two endpoints.</p>
<p><code>lseg(point '(-1,0)', point '(1,0)')</code> [(-1,0),(1,0)]</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>path</code> ( <code>polygon</code> ) path</p>
<p>Converts polygon to a closed path with the same list of points.</p>
<p><code>path(polygon '((0,0),(1,1),(2,0))')</code> ((0,0),(1,1),(2,0))</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>point</code> ( <code>double precision</code>, <code>double precision</code> ) point</p>
<p>Constructs point from its coordinates.</p>
<p><code>point(23.4, -44.5)</code> (23.4,-44.5)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>point</code> ( <code>box</code> ) point</p>
<p>Computes center of box.</p>
<p><code>point(box '(1,0),(-1,0)')</code> (0,0)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>point</code> ( <code>circle</code> ) point</p>
<p>Computes center of circle.</p>
<p><code>point(circle '&lt;(0,0),2&gt;')</code> (0,0)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>point</code> ( <code>lseg</code> ) point</p>
<p>Computes center of line segment.</p>
<p><code>point(lseg '[(-1,0),(1,0)]')</code> (0,0)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>point</code> ( <code>polygon</code> ) point</p>
<p>Computes center of polygon (the mean of the positions of the polygon's points).</p>
<p><code>point(polygon '((0,0),(1,1),(2,0))')</code> (1,0.3333333333333333)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>polygon</code> ( <code>box</code> ) polygon</p>
<p>Converts box to a 4-point polygon.</p>
<p><code>polygon(box '(1,1),(0,0)')</code> ((0,0),(0,1),(1,1),(1,0))</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>polygon</code> ( <code>circle</code> ) polygon</p>
<p>Converts circle to a 12-point polygon.</p>
<p><code>polygon(circle '&lt;(0,0),2&gt;')</code> ((-2,0),​(-1.7320508075688774,0.9999999999999999),​(-1.0000000000000002,1.7320508075688772),​(-1.2246063538223773e-16,2),​(0.9999999999999996,1.7320508075688774),​(1.732050807568877,1.0000000000000007),​(2,2.4492127076447545e-16),​(1.7320508075688776,-0.9999999999999994),​(1.0000000000000009,-1.7320508075688767),​(3.673819061467132e-16,-2),​(-0.9999999999999987,-1.732050807568878),​(-1.7320508075688767,-1.0000000000000009))</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>polygon</code> ( <code>integer</code>, <code>circle</code> ) polygon</p>
<p>Converts circle to an &lt;n&gt;-point polygon.</p>
<p><code>polygon(4, circle '&lt;(3,0),1&gt;')</code> ((2,0),​(3,1),​(4,1.2246063538223773e-16),​(3,-1))</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>polygon</code> ( <code>path</code> ) polygon</p>
<p>Converts closed path to a polygon with the same list of points.</p>
<p><code>polygon(path '((0,0),(1,1),(2,0))')</code> ((0,0),(1,1),(2,0))</p></td>
</tr>
</tbody>
</table>

It is possible to access the two component numbers of a `point` as though the point were an array with indexes 0 and 1. For example, if `t.p` is a `point` column then `SELECT p[0] FROM t` retrieves the X coordinate and `UPDATE t SET p[1] = ...` changes the Y coordinate. In the same way, a value of type `box` or `lseg` can be treated as an array of two `point` values.

## Network Address Functions and Operators

The IP network address types, `cidr` and `inet`, support the usual comparison operators shown in [Comparison Operators](#functions-comparison-op-table) as well as the specialized operators and functions shown in [IP Address Operators](#cidr-inet-operators-table) and [IP Address Functions](#cidr-inet-functions-table).

Any `cidr` value can be cast to `inet` implicitly; therefore, the operators and functions shown below as operating on `inet` also work on `cidr` values. (Where there are separate functions for `inet` and `cidr`, it is because the behavior should be different for the two cases.) Also, it is permitted to cast an `inet` value to `cidr`. When this is done, any bits to the right of the netmask are silently zeroed to create a valid `cidr` value.

<table id="cidr-inet-operators-table">
<caption>IP Address Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>inet</code> <code>&lt;&lt;</code> <code>inet</code> boolean</p>
<p>Is subnet strictly contained by subnet? This operator, and the next four, test for subnet inclusion. They consider only the network parts of the two addresses (ignoring any bits to the right of the netmasks) and determine whether one network is identical to or a subnet of the other.</p>
<p><code>inet '192.168.1.5' &lt;&lt; inet '192.168.1/24'</code> t</p>
<p><code>inet '192.168.0.5' &lt;&lt; inet '192.168.1/24'</code> f</p>
<p><code>inet '192.168.1/24' &lt;&lt; inet '192.168.1/24'</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>inet</code> <code>&lt;&lt;=</code> <code>inet</code> boolean</p>
<p>Is subnet contained by or equal to subnet?</p>
<p><code>inet '192.168.1/24' &lt;&lt;= inet '192.168.1/24'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>inet</code> <code>&gt;&gt;</code> <code>inet</code> boolean</p>
<p>Does subnet strictly contain subnet?</p>
<p><code>inet '192.168.1/24' &gt;&gt; inet '192.168.1.5'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>inet</code> <code>&gt;&gt;=</code> <code>inet</code> boolean</p>
<p>Does subnet contain or equal subnet?</p>
<p><code>inet '192.168.1/24' &gt;&gt;= inet '192.168.1/24'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>inet</code> <code>&amp;&amp;</code> <code>inet</code> boolean</p>
<p>Does either subnet contain or equal the other?</p>
<p><code>inet '192.168.1/24' &amp;&amp; inet '192.168.1.80/28'</code> t</p>
<p><code>inet '192.168.1/24' &amp;&amp; inet '192.168.2.0/28'</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>~</code> <code>inet</code> inet</p>
<p>Computes bitwise NOT.</p>
<p><code>~ inet '192.168.1.6'</code> 63.87.254.249</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>inet</code> <code>&amp;</code> <code>inet</code> inet</p>
<p>Computes bitwise AND.</p>
<p><code>inet '192.168.1.6' &amp; inet '0.0.0.255'</code> 0.0.0.6</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>inet</code> <code>|</code> <code>inet</code> inet</p>
<p>Computes bitwise OR.</p>
<p><code>inet '192.168.1.6' | inet '0.0.0.255'</code> 192.168.1.255</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>inet</code> <code>+</code> <code>bigint</code> inet</p>
<p>Adds an offset to an address.</p>
<p><code>inet '192.168.1.6' + 25</code> 192.168.1.31</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>bigint</code> <code>+</code> <code>inet</code> inet</p>
<p>Adds an offset to an address.</p>
<p><code>200 + inet '::ffff:fff0:1'</code> ::ffff:255.240.0.201</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>inet</code> <code>-</code> <code>bigint</code> inet</p>
<p>Subtracts an offset from an address.</p>
<p><code>inet '192.168.1.43' - 36</code> 192.168.1.7</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>inet</code> <code>-</code> <code>inet</code> bigint</p>
<p>Computes the difference of two addresses.</p>
<p><code>inet '192.168.1.43' - inet '192.168.1.19'</code> 24</p>
<p><code>inet '::1' - inet '::ffff:1'</code> -4294901760</p></td>
</tr>
</tbody>
</table>

<table id="cidr-inet-functions-table">
<caption>IP Address Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>abbrev</code> ( <code>inet</code> ) text</p>
<p>Creates an abbreviated display format as text. (The result is the same as the <code>inet</code> output function produces; it is “abbreviated” only in comparison to the result of an explicit cast to <code>text</code>, which for historical reasons will never suppress the netmask part.)</p>
<p><code>abbrev(inet '10.1.0.0/32')</code> 10.1.0.0</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>abbrev</code> ( <code>cidr</code> ) text</p>
<p>Creates an abbreviated display format as text. (The abbreviation consists of dropping all-zero octets to the right of the netmask; more examples are in <a href="#datatype-net-cidr-table">???</a>.)</p>
<p><code>abbrev(cidr '10.1.0.0/16')</code> 10.1/16</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>broadcast</code> ( <code>inet</code> ) inet</p>
<p>Computes the broadcast address for the address's network.</p>
<p><code>broadcast(inet '192.168.1.5/24')</code> 192.168.1.255/24</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>family</code> ( <code>inet</code> ) integer</p>
<p>Returns the address's family: <code>4</code> for IPv4, <code>6</code> for IPv6.</p>
<p><code>family(inet '::1')</code> 6</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>host</code> ( <code>inet</code> ) text</p>
<p>Returns the IP address as text, ignoring the netmask.</p>
<p><code>host(inet '192.168.1.0/24')</code> 192.168.1.0</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>hostmask</code> ( <code>inet</code> ) inet</p>
<p>Computes the host mask for the address's network.</p>
<p><code>hostmask(inet '192.168.23.20/30')</code> 0.0.0.3</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>inet_merge</code> ( <code>inet</code>, <code>inet</code> ) cidr</p>
<p>Computes the smallest network that includes both of the given networks.</p>
<p><code>inet_merge(inet '192.168.1.5/24', inet '192.168.2.5/24')</code> 192.168.0.0/22</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>inet_same_family</code> ( <code>inet</code>, <code>inet</code> ) boolean</p>
<p>Tests whether the addresses belong to the same IP family.</p>
<p><code>inet_same_family(inet '192.168.1.5/24', inet '::1')</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>masklen</code> ( <code>inet</code> ) integer</p>
<p>Returns the netmask length in bits.</p>
<p><code>masklen(inet '192.168.1.5/24')</code> 24</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>netmask</code> ( <code>inet</code> ) inet</p>
<p>Computes the network mask for the address's network.</p>
<p><code>netmask(inet '192.168.1.5/24')</code> 255.255.255.0</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>network</code> ( <code>inet</code> ) cidr</p>
<p>Returns the network part of the address, zeroing out whatever is to the right of the netmask. (This is equivalent to casting the value to <code>cidr</code>.)</p>
<p><code>network(inet '192.168.1.5/24')</code> 192.168.1.0/24</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>set_masklen</code> ( <code>inet</code>, <code>integer</code> ) inet</p>
<p>Sets the netmask length for an <code>inet</code> value. The address part does not change.</p>
<p><code>set_masklen(inet '192.168.1.5/24', 16)</code> 192.168.1.5/16</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>set_masklen</code> ( <code>cidr</code>, <code>integer</code> ) cidr</p>
<p>Sets the netmask length for a <code>cidr</code> value. Address bits to the right of the new netmask are set to zero.</p>
<p><code>set_masklen(cidr '192.168.1.0/24', 16)</code> 192.168.0.0/16</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>text</code> ( <code>inet</code> ) text</p>
<p>Returns the unabbreviated IP address and netmask length as text. (This has the same result as an explicit cast to <code>text</code>.)</p>
<p><code>text(inet '192.168.1.5')</code> 192.168.1.5/32</p></td>
</tr>
</tbody>
</table>

> [!TIP]
> The `abbrev`, `host`, and `text` functions are primarily intended to offer alternative display formats for IP addresses.

The MAC address types, `macaddr` and `macaddr8`, support the usual comparison operators shown in [Comparison Operators](#functions-comparison-op-table) as well as the specialized functions shown in [MAC Address Functions](#macaddr-functions-table). In addition, they support the bitwise logical operators `~`, `&` and `|` (NOT, AND and OR), just as shown above for IP addresses.

<table id="macaddr-functions-table">
<caption>MAC Address Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>trunc</code> ( <code>macaddr</code> ) macaddr</p>
<p>Sets the last 3 bytes of the address to zero. The remaining prefix can be associated with a particular manufacturer (using data not included in PostgreSQL).</p>
<p><code>trunc(macaddr '12:34:56:78:90:ab')</code> 12:34:56:00:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>trunc</code> ( <code>macaddr8</code> ) macaddr8</p>
<p>Sets the last 5 bytes of the address to zero. The remaining prefix can be associated with a particular manufacturer (using data not included in PostgreSQL).</p>
<p><code>trunc(macaddr8 '12:34:56:78:90:ab:cd:ef')</code> 12:34:56:00:00:00:00:00</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>macaddr8_set7bit</code> ( <code>macaddr8</code> ) macaddr8</p>
<p>Sets the 7th bit of the address to one, creating what is known as modified EUI-64, for inclusion in an IPv6 address.</p>
<p><code>macaddr8_set7bit(macaddr8 '00:34:56:ab:cd:ef')</code> 02:34:56:ff:fe:ab:cd:ef</p></td>
</tr>
</tbody>
</table>

## Text Search Functions and Operators

full text search

functions and operators

text search

functions and operators

[Text Search Operators](#textsearch-operators-table), [Text Search Functions](#textsearch-functions-table) and [Text Search Debugging Functions](#textsearch-functions-debug-table) summarize the functions and operators that are provided for full text searching. See [???](#textsearch) for a detailed explanation of PostgreSQL's text search facility.

<table id="textsearch-operators-table">
<caption>Text Search Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>tsvector</code> <code>@@</code> <code>tsquery</code> boolean</p>
<p role="func_signature"><code>tsquery</code> <code>@@</code> <code>tsvector</code> boolean</p>
<p>Does <code>tsvector</code> match <code>tsquery</code>? (The arguments can be given in either order.)</p>
<p><code>to_tsvector('fat cats ate rats') @@ to_tsquery('cat &amp; rat')</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>text</code> <code>@@</code> <code>tsquery</code> boolean</p>
<p>Does text string, after implicit invocation of <code>to_tsvector()</code>, match <code>tsquery</code>?</p>
<p><code>'fat cats ate rats' @@ to_tsquery('cat &amp; rat')</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>tsvector</code> <code>||</code> <code>tsvector</code> tsvector</p>
<p>Concatenates two <code>tsvector</code>s. If both inputs contain lexeme positions, the second input's positions are adjusted accordingly.</p>
<p><code>'a:1 b:2'::tsvector || 'c:1 d:2 b:3'::tsvector</code> 'a':1 'b':2,5 'c':3 'd':4</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>tsquery</code> <code>&amp;&amp;</code> <code>tsquery</code> tsquery</p>
<p>ANDs two <code>tsquery</code>s together, producing a query that matches documents that match both input queries.</p>
<p><code>'fat | rat'::tsquery &amp;&amp; 'cat'::tsquery</code> ( 'fat' | 'rat' ) &amp; 'cat'</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>tsquery</code> <code>||</code> <code>tsquery</code> tsquery</p>
<p>ORs two <code>tsquery</code>s together, producing a query that matches documents that match either input query.</p>
<p><code>'fat | rat'::tsquery || 'cat'::tsquery</code> 'fat' | 'rat' | 'cat'</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>!!</code> <code>tsquery</code> tsquery</p>
<p>Negates a <code>tsquery</code>, producing a query that matches documents that do not match the input query.</p>
<p><code>!! 'cat'::tsquery</code> !'cat'</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>tsquery</code> <code>&lt;-&gt;</code> <code>tsquery</code> tsquery</p>
<p>Constructs a phrase query, which matches if the two input queries match at successive lexemes.</p>
<p><code>to_tsquery('fat') &lt;-&gt; to_tsquery('rat')</code> 'fat' &lt;-&gt; 'rat'</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>tsquery</code> <code>@&gt;</code> <code>tsquery</code> boolean</p>
<p>Does first <code>tsquery</code> contain the second? (This considers only whether all the lexemes appearing in one query appear in the other, ignoring the combining operators.)</p>
<p><code>'cat'::tsquery @&gt; 'cat &amp; rat'::tsquery</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>tsquery</code> <code>&lt;@</code> <code>tsquery</code> boolean</p>
<p>Is first <code>tsquery</code> contained in the second? (This considers only whether all the lexemes appearing in one query appear in the other, ignoring the combining operators.)</p>
<p><code>'cat'::tsquery &lt;@ 'cat &amp; rat'::tsquery</code> t</p>
<p><code>'cat'::tsquery &lt;@ '!cat &amp; rat'::tsquery</code> t</p></td>
</tr>
</tbody>
</table>

In addition to these specialized operators, the usual comparison operators shown in [Comparison Operators](#functions-comparison-op-table) are available for types `tsvector` and `tsquery`. These are not very useful for text searching but allow, for example, unique indexes to be built on columns of these types.

<table id="textsearch-functions-table">
<caption>Text Search Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_to_tsvector</code> ( <code>text[]</code> ) tsvector</p>
<p>Converts an array of text strings to a <code>tsvector</code>. The given strings are used as lexemes as-is, without further processing. Array elements must not be empty strings or <code>NULL</code>.</p>
<p><code>array_to_tsvector('{fat,cat,rat}'::text[])</code> 'cat' 'fat' 'rat'</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>get_current_ts_config</code> ( ) regconfig</p>
<p>Returns the OID of the current default text search configuration (as set by <a href="#guc-default-text-search-config">???</a>).</p>
<p><code>get_current_ts_config()</code> english</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>length</code> ( <code>tsvector</code> ) integer</p>
<p>Returns the number of lexemes in the <code>tsvector</code>.</p>
<p><code>length('fat:2,4 cat:3 rat:5A'::tsvector)</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>numnode</code> ( <code>tsquery</code> ) integer</p>
<p>Returns the number of lexemes plus operators in the <code>tsquery</code>.</p>
<p><code>numnode('(fat &amp; rat) | cat'::tsquery)</code> 5</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>plainto_tsquery</code> ( [<code>config</code> <code>regconfig</code>,] <code>query</code> <code>text</code> ) tsquery</p>
<p>Converts text to a <code>tsquery</code>, normalizing words according to the specified or default configuration. Any punctuation in the string is ignored (it does not determine query operators). The resulting query matches documents containing all non-stopwords in the text.</p>
<p><code>plainto_tsquery('english', 'The Fat Rats')</code> 'fat' &amp; 'rat'</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>phraseto_tsquery</code> ( [<code>config</code> <code>regconfig</code>,] <code>query</code> <code>text</code> ) tsquery</p>
<p>Converts text to a <code>tsquery</code>, normalizing words according to the specified or default configuration. Any punctuation in the string is ignored (it does not determine query operators). The resulting query matches phrases containing all non-stopwords in the text.</p>
<p><code>phraseto_tsquery('english', 'The Fat Rats')</code> 'fat' &lt;-&gt; 'rat'</p>
<p><code>phraseto_tsquery('english', 'The Cat and Rats')</code> 'cat' &lt;2&gt; 'rat'</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>websearch_to_tsquery</code> ( [<code>config</code> <code>regconfig</code>,] <code>query</code> <code>text</code> ) tsquery</p>
<p>Converts text to a <code>tsquery</code>, normalizing words according to the specified or default configuration. Quoted word sequences are converted to phrase tests. The word “or” is understood as producing an OR operator, and a dash produces a NOT operator; other punctuation is ignored. This approximates the behavior of some common web search tools.</p>
<p><code>websearch_to_tsquery('english', '"fat rat" or cat dog')</code> 'fat' &lt;-&gt; 'rat' | 'cat' &amp; 'dog'</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>querytree</code> ( <code>tsquery</code> ) text</p>
<p>Produces a representation of the indexable portion of a <code>tsquery</code>. A result that is empty or just <code>T</code> indicates a non-indexable query.</p>
<p><code>querytree('foo &amp; ! bar'::tsquery)</code> 'foo'</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>setweight</code> ( <code>vector</code> <code>tsvector</code>, <code>weight</code> <code>"char"</code> ) tsvector</p>
<p>Assigns the specified <code>weight</code> to each element of the <code>vector</code>.</p>
<p><code>setweight('fat:2,4 cat:3 rat:5B'::tsvector, 'A')</code> 'cat':3A 'fat':2A,4A 'rat':5A</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>setweight</code> ( <code>vector</code> <code>tsvector</code>, <code>weight</code> <code>"char"</code>, <code>lexemes</code> <code>text[]</code> ) tsvector</p>
<p>Assigns the specified <code>weight</code> to elements of the <code>vector</code> that are listed in <code>lexemes</code>. The strings in <code>lexemes</code> are taken as lexemes as-is, without further processing. Strings that do not match any lexeme in <code>vector</code> are ignored.</p>
<p><code>setweight('fat:2,4 cat:3 rat:5,6B'::tsvector, 'A', '{cat,rat}')</code> 'cat':3A 'fat':2,4 'rat':5A,6A</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>strip</code> ( <code>tsvector</code> ) tsvector</p>
<p>Removes positions and weights from the <code>tsvector</code>.</p>
<p><code>strip('fat:2,4 cat:3 rat:5A'::tsvector)</code> 'cat' 'fat' 'rat'</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_tsquery</code> ( [<code>config</code> <code>regconfig</code>,] <code>query</code> <code>text</code> ) tsquery</p>
<p>Converts text to a <code>tsquery</code>, normalizing words according to the specified or default configuration. The words must be combined by valid <code>tsquery</code> operators.</p>
<p><code>to_tsquery('english', 'The &amp; Fat &amp; Rats')</code> 'fat' &amp; 'rat'</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_tsvector</code> ( [<code>config</code> <code>regconfig</code>,] <code>document</code> <code>text</code> ) tsvector</p>
<p>Converts text to a <code>tsvector</code>, normalizing words according to the specified or default configuration. Position information is included in the result.</p>
<p><code>to_tsvector('english', 'The Fat Rats')</code> 'fat':2 'rat':3</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>to_tsvector</code> ( [<code>config</code> <code>regconfig</code>,] <code>document</code> <code>json</code> ) tsvector</p>
<p role="func_signature"><code>to_tsvector</code> ( [<code>config</code> <code>regconfig</code>,] <code>document</code> <code>jsonb</code> ) tsvector</p>
<p>Converts each string value in the JSON document to a <code>tsvector</code>, normalizing words according to the specified or default configuration. The results are then concatenated in document order to produce the output. Position information is generated as though one stopword exists between each pair of string values. (Beware that “document order” of the fields of a JSON object is implementation-dependent when the input is <code>jsonb</code>; observe the difference in the examples.)</p>
<p><code>to_tsvector('english', '{"aa": "The Fat Rats", "b": "dog"}'::json)</code> 'dog':5 'fat':2 'rat':3</p>
<p><code>to_tsvector('english', '{"aa": "The Fat Rats", "b": "dog"}'::jsonb)</code> 'dog':1 'fat':4 'rat':5</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_to_tsvector</code> ( [<code>config</code> <code>regconfig</code>,] <code>document</code> <code>json</code>, <code>filter</code> <code>jsonb</code> ) tsvector</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_to_tsvector</code> ( [<code>config</code> <code>regconfig</code>,] <code>document</code> <code>jsonb</code>, <code>filter</code> <code>jsonb</code> ) tsvector</p>
<p>Selects each item in the JSON document that is requested by the <code>filter</code> and converts each one to a <code>tsvector</code>, normalizing words according to the specified or default configuration. The results are then concatenated in document order to produce the output. Position information is generated as though one stopword exists between each pair of selected items. (Beware that “document order” of the fields of a JSON object is implementation-dependent when the input is <code>jsonb</code>.) The <code>filter</code> must be a <code>jsonb</code> array containing zero or more of these keywords: <code>"string"</code> (to include all string values), <code>"numeric"</code> (to include all numeric values), <code>"boolean"</code> (to include all boolean values), <code>"key"</code> (to include all keys), or <code>"all"</code> (to include all the above). As a special case, the <code>filter</code> can also be a simple JSON value that is one of these keywords.</p>
<p><code>json_to_tsvector('english', '{"a": "The Fat Rats", "b": 123}'::json, '["string", "numeric"]')</code> '123':5 'fat':2 'rat':3</p>
<p><code>json_to_tsvector('english', '{"cat": "The Fat Rats", "dog": 123}'::json, '"all"')</code> '123':9 'cat':1 'dog':7 'fat':4 'rat':5</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ts_delete</code> ( <code>vector</code> <code>tsvector</code>, <code>lexeme</code> <code>text</code> ) tsvector</p>
<p>Removes any occurrence of the given <code>lexeme</code> from the <code>vector</code>. The <code>lexeme</code> string is treated as a lexeme as-is, without further processing.</p>
<p><code>ts_delete('fat:2,4 cat:3 rat:5A'::tsvector, 'fat')</code> 'cat':3 'rat':5A</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>ts_delete</code> ( <code>vector</code> <code>tsvector</code>, <code>lexemes</code> <code>text[]</code> ) tsvector</p>
<p>Removes any occurrences of the lexemes in <code>lexemes</code> from the <code>vector</code>. The strings in <code>lexemes</code> are taken as lexemes as-is, without further processing. Strings that do not match any lexeme in <code>vector</code> are ignored.</p>
<p><code>ts_delete('fat:2,4 cat:3 rat:5A'::tsvector, ARRAY['fat','rat'])</code> 'cat':3</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ts_filter</code> ( <code>vector</code> <code>tsvector</code>, <code>weights</code> <code>"char"[]</code> ) tsvector</p>
<p>Selects only elements with the given <code>weights</code> from the <code>vector</code>.</p>
<p><code>ts_filter('fat:2,4 cat:3b,7c rat:5A'::tsvector, '{a,b}')</code> 'cat':3B 'rat':5A</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ts_headline</code> ( [<code>config</code> <code>regconfig</code>,] <code>document</code> <code>text</code>, <code>query</code> <code>tsquery</code> [, <code>options</code> <code>text</code>] ) text</p>
<p>Displays, in an abbreviated form, the match(es) for the <code>query</code> in the <code>document</code>, which must be raw text not a <code>tsvector</code>. Words in the document are normalized according to the specified or default configuration before matching to the query. Use of this function is discussed in <a href="#textsearch-headline">???</a>, which also describes the available <code>options</code>.</p>
<p><code>ts_headline('The fat cat ate the rat.', 'cat')</code> The fat &lt;b&gt;cat&lt;/b&gt; ate the rat.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>ts_headline</code> ( [<code>config</code> <code>regconfig</code>,] <code>document</code> <code>json</code>, <code>query</code> <code>tsquery</code> [, <code>options</code> <code>text</code>] ) text</p>
<p role="func_signature"><code>ts_headline</code> ( [<code>config</code> <code>regconfig</code>,] <code>document</code> <code>jsonb</code>, <code>query</code> <code>tsquery</code> [, <code>options</code> <code>text</code>] ) text</p>
<p>Displays, in an abbreviated form, match(es) for the <code>query</code> that occur in string values within the JSON <code>document</code>. See <a href="#textsearch-headline">???</a> for more details.</p>
<p><code>ts_headline('{"cat":"raining cats and dogs"}'::jsonb, 'cat')</code> {"cat": "raining &lt;b&gt;cats&lt;/b&gt; and dogs"}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ts_rank</code> ( [<code>weights</code> <code>real[]</code>,] <code>vector</code> <code>tsvector</code>, <code>query</code> <code>tsquery</code> [, <code>normalization</code> <code>integer</code>] ) real</p>
<p>Computes a score showing how well the <code>vector</code> matches the <code>query</code>. See <a href="#textsearch-ranking">???</a> for details.</p>
<p><code>ts_rank(to_tsvector('raining cats and dogs'), 'cat')</code> 0.06079271</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ts_rank_cd</code> ( [<code>weights</code> <code>real[]</code>,] <code>vector</code> <code>tsvector</code>, <code>query</code> <code>tsquery</code> [, <code>normalization</code> <code>integer</code>] ) real</p>
<p>Computes a score showing how well the <code>vector</code> matches the <code>query</code>, using a cover density algorithm. See <a href="#textsearch-ranking">???</a> for details.</p>
<p><code>ts_rank_cd(to_tsvector('raining cats and dogs'), 'cat')</code> 0.1</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ts_rewrite</code> ( <code>query</code> <code>tsquery</code>, <code>target</code> <code>tsquery</code>, <code>substitute</code> <code>tsquery</code> ) tsquery</p>
<p>Replaces occurrences of <code>target</code> with <code>substitute</code> within the <code>query</code>. See <a href="#textsearch-query-rewriting">???</a> for details.</p>
<p><code>ts_rewrite('a &amp; b'::tsquery, 'a'::tsquery, 'foo|bar'::tsquery)</code> 'b' &amp; ( 'foo' | 'bar' )</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>ts_rewrite</code> ( <code>query</code> <code>tsquery</code>, <code>select</code> <code>text</code> ) tsquery</p>
<p>Replaces portions of the <code>query</code> according to target(s) and substitute(s) obtained by executing a <code>SELECT</code> command. See <a href="#textsearch-query-rewriting">???</a> for details.</p>
<p><code>SELECT ts_rewrite('a &amp; b'::tsquery, 'SELECT t,s FROM aliases')</code> 'b' &amp; ( 'foo' | 'bar' )</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>tsquery_phrase</code> ( <code>query1</code> <code>tsquery</code>, <code>query2</code> <code>tsquery</code> ) tsquery</p>
<p>Constructs a phrase query that searches for matches of <code>query1</code> and <code>query2</code> at successive lexemes (same as <code>&lt;-&gt;</code> operator).</p>
<p><code>tsquery_phrase(to_tsquery('fat'), to_tsquery('cat'))</code> 'fat' &lt;-&gt; 'cat'</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>tsquery_phrase</code> ( <code>query1</code> <code>tsquery</code>, <code>query2</code> <code>tsquery</code>, <code>distance</code> <code>integer</code> ) tsquery</p>
<p>Constructs a phrase query that searches for matches of <code>query1</code> and <code>query2</code> that occur exactly <code>distance</code> lexemes apart.</p>
<p><code>tsquery_phrase(to_tsquery('fat'), to_tsquery('cat'), 10)</code> 'fat' &lt;10&gt; 'cat'</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>tsvector_to_array</code> ( <code>tsvector</code> ) text[]</p>
<p>Converts a <code>tsvector</code> to an array of lexemes.</p>
<p><code>tsvector_to_array('fat:2,4 cat:3 rat:5A'::tsvector)</code> {cat,fat,rat}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>unnest</code> ( <code>tsvector</code> ) setof record ( <code>lexeme</code> <code>text</code>, <code>positions</code> <code>smallint[]</code>, <code>weights</code> <code>text</code> )</p>
<p>Expands a <code>tsvector</code> into a set of rows, one per lexeme.</p>
<p><code>select * from unnest('cat:3 fat:2,4 rat:5A'::tsvector)</code></p>
<pre><code> lexeme | positions | weights
--------+-----------+---------
 cat    | {3}       | {D}
 fat    | {2,4}     | {D,D}
 rat    | {5}       | {A}</code></pre></td>
</tr>
</tbody>
</table>

> [!NOTE]
> All the text search functions that accept an optional `regconfig` argument will use the configuration specified by [???](#guc-default-text-search-config) when that argument is omitted.

The functions in [Text Search Debugging Functions](#textsearch-functions-debug-table) are listed separately because they are not usually used in everyday text searching operations. They are primarily helpful for development and debugging of new text search configurations.

<table id="textsearch-functions-debug-table">
<caption>Text Search Debugging Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ts_debug</code> ( [<code>config</code> <code>regconfig</code>,] <code>document</code> <code>text</code> ) setof record ( <code>alias</code> <code>text</code>, <code>description</code> <code>text</code>, <code>token</code> <code>text</code>, <code>dictionaries</code> <code>regdictionary[]</code>, <code>dictionary</code> <code>regdictionary</code>, <code>lexemes</code> <code>text[]</code> )</p>
<p>Extracts and normalizes tokens from the <code>document</code> according to the specified or default text search configuration, and returns information about how each token was processed. See <a href="#textsearch-configuration-testing">???</a> for details.</p>
<p><code>ts_debug('english', 'The Brightest supernovaes')</code> (asciiword,"Word, all ASCII",The,{english_stem},english_stem,{}) ...</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ts_lexize</code> ( <code>dict</code> <code>regdictionary</code>, <code>token</code> <code>text</code> ) text[]</p>
<p>Returns an array of replacement lexemes if the input token is known to the dictionary, or an empty array if the token is known to the dictionary but it is a stop word, or NULL if it is not a known word. See <a href="#textsearch-dictionary-testing">???</a> for details.</p>
<p><code>ts_lexize('english_stem', 'stars')</code> {star}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ts_parse</code> ( <code>parser_name</code> <code>text</code>, <code>document</code> <code>text</code> ) setof record ( <code>tokid</code> <code>integer</code>, <code>token</code> <code>text</code> )</p>
<p>Extracts tokens from the <code>document</code> using the named parser. See <a href="#textsearch-parser-testing">???</a> for details.</p>
<p><code>ts_parse('default', 'foo - bar')</code> (1,foo) ...</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>ts_parse</code> ( <code>parser_oid</code> <code>oid</code>, <code>document</code> <code>text</code> ) setof record ( <code>tokid</code> <code>integer</code>, <code>token</code> <code>text</code> )</p>
<p>Extracts tokens from the <code>document</code> using a parser specified by OID. See <a href="#textsearch-parser-testing">???</a> for details.</p>
<p><code>ts_parse(3722, 'foo - bar')</code> (1,foo) ...</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ts_token_type</code> ( <code>parser_name</code> <code>text</code> ) setof record ( <code>tokid</code> <code>integer</code>, <code>alias</code> <code>text</code>, <code>description</code> <code>text</code> )</p>
<p>Returns a table that describes each type of token the named parser can recognize. See <a href="#textsearch-parser-testing">???</a> for details.</p>
<p><code>ts_token_type('default')</code> (1,asciiword,"Word, all ASCII") ...</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>ts_token_type</code> ( <code>parser_oid</code> <code>oid</code> ) setof record ( <code>tokid</code> <code>integer</code>, <code>alias</code> <code>text</code>, <code>description</code> <code>text</code> )</p>
<p>Returns a table that describes each type of token a parser specified by OID can recognize. See <a href="#textsearch-parser-testing">???</a> for details.</p>
<p><code>ts_token_type(3722)</code> (1,asciiword,"Word, all ASCII") ...</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ts_stat</code> ( <code>sqlquery</code> <code>text</code> [, <code>weights</code> <code>text</code>] ) setof record ( <code>word</code> <code>text</code>, <code>ndoc</code> <code>integer</code>, <code>nentry</code> <code>integer</code> )</p>
<p>Executes the <code>sqlquery</code>, which must return a single <code>tsvector</code> column, and returns statistics about each distinct lexeme contained in the data. See <a href="#textsearch-statistics">???</a> for details.</p>
<p><code>ts_stat('SELECT vector FROM apod')</code> (foo,10,15) ...</p></td>
</tr>
</tbody>
</table>

## UUID Functions

UUID

generating

gen_random_uuid

uuid_extract_timestamp

uuid_extract_version

PostgreSQL includes one function to generate a UUID: `gen_random_uuid` () uuid This function returns a version 4 (random) UUID. This is the most commonly used type of UUID and is appropriate for most applications.

The [???](#uuid-ossp) module provides additional functions that implement other standard algorithms for generating UUIDs.

There are also functions to extract data from UUIDs: `uuid_extract_timestamp` (uuid) timestamp with time zone This function extracts a `timestamp with time zone` from UUID version 1. For other versions, this function returns null. Note that the extracted timestamp is not necessarily exactly equal to the time the UUID was generated; this depends on the implementation that generated the UUID.

`uuid_extract_version` (uuid) smallint This function extracts the version from a UUID of the variant described by [RFC 4122](https://datatracker.ietf.org/doc/html/rfc4122). For other variants, this function returns null. For example, for a UUID generated by `gen_random_uuid`, this function will return 4.

PostgreSQL also provides the usual comparison operators shown in [Comparison Operators](#functions-comparison-op-table) for UUIDs.

## XML Functions

XML Functions

The functions and function-like expressions described in this section operate on values of type `xml`. See [???](#datatype-xml) for information about the `xml` type. The function-like expressions `xmlparse` and `xmlserialize` for converting to and from type `xml` are documented there, not in this section.

Use of most of these functions requires PostgreSQL to have been built with `configure --with-libxml`.

### Producing XML Content

A set of functions and function-like expressions is available for producing XML content from SQL data. As such, they are particularly suitable for formatting query results into XML documents for processing in client applications.

#### `xmltext`

xmltext

xmltext

(

text

)

xml

The function `xmltext` returns an XML value with a single text node containing the input argument as its content. Predefined entities like ampersand (`&`), left and right angle brackets (`< >`), and quotation marks (`""`) are escaped.

Example:

    SELECT xmltext('< foo & bar >');
             xmltext
    -------------------------
     &lt; foo &amp; bar &gt;

#### `xmlcomment`

xmlcomment

xmlcomment

(

text

)

xml

The function `xmlcomment` creates an XML value containing an XML comment with the specified text as content. The text cannot contain “`--`” or end with a “`-`”, otherwise the resulting construct would not be a valid XML comment. If the argument is null, the result is null.

Example:

    SELECT xmlcomment('hello');

      xmlcomment
    --------------
     <!--hello-->

#### `xmlconcat`

xmlconcat

xmlconcat

(

xml

, ...

)

xml

The function `xmlconcat` concatenates a list of individual XML values to create a single value containing an XML content fragment. Null values are omitted; the result is only null if there are no nonnull arguments.

Example:

    SELECT xmlconcat('<abc/>', '<bar>foo</bar>');

          xmlconcat
    ----------------------
     <abc/><bar>foo</bar>

XML declarations, if present, are combined as follows. If all argument values have the same XML version declaration, that version is used in the result, else no version is used. If all argument values have the standalone declaration value “yes”, then that value is used in the result. If all argument values have a standalone declaration value and at least one is “no”, then that is used in the result. Else the result will have no standalone declaration. If the result is determined to require a standalone declaration but no version declaration, a version declaration with version 1.0 will be used because XML requires an XML declaration to contain a version declaration. Encoding declarations are ignored and removed in all cases.

Example:

    SELECT xmlconcat('<foo/>', '<bar/>');

                 xmlconcat
    -----------------------------------
     <foo/><bar/>

#### `xmlelement`

xmlelement

xmlelement

(

NAME

name

,

XMLATTRIBUTES

(

attvalue

AS

attname

, ...

)

,

content

, ...

)

xml

The `xmlelement` expression produces an XML element with the given name, attributes, and content. The \<name\> and \<attname\> items shown in the syntax are simple identifiers, not values. The \<attvalue\> and \<content\> items are expressions, which can yield any PostgreSQL data type. The argument(s) within `XMLATTRIBUTES` generate attributes of the XML element; the \<content\> value(s) are concatenated to form its content.

Examples:

    SELECT xmlelement(name foo);

     xmlelement
    ------------
     <foo/>

    SELECT xmlelement(name foo, xmlattributes('xyz' as bar));

        xmlelement
    ------------------
     <foo bar="xyz"/>

    SELECT xmlelement(name foo, xmlattributes(current_date as bar), 'cont', 'ent');

                 xmlelement
    -------------------------------------
     <foo bar="2007-01-26">content</foo>

Element and attribute names that are not valid XML names are escaped by replacing the offending characters by the sequence `_xHHHH_`, where \<HHHH\> is the character's Unicode codepoint in hexadecimal notation. For example:

    SELECT xmlelement(name "foo$bar", xmlattributes('xyz' as "a&b"));

                xmlelement
    ----------------------------------
     <foo_x0024_bar a_x0026_b="xyz"/>

An explicit attribute name need not be specified if the attribute value is a column reference, in which case the column's name will be used as the attribute name by default. In other cases, the attribute must be given an explicit name. So this example is valid:

    CREATE TABLE test (a xml, b xml);
    SELECT xmlelement(name test, xmlattributes(a, b)) FROM test;

But these are not:

    SELECT xmlelement(name test, xmlattributes('constant'), a, b) FROM test;
    SELECT xmlelement(name test, xmlattributes(func(a, b))) FROM test;

Element content, if specified, will be formatted according to its data type. If the content is itself of type `xml`, complex XML documents can be constructed. For example:

    SELECT xmlelement(name foo, xmlattributes('xyz' as bar),
                                xmlelement(name abc),
                                xmlcomment('test'),
                                xmlelement(name xyz));

                      xmlelement
    ----------------------------------------------
     <foo bar="xyz"><abc/><!--test--><xyz/></foo>

Content of other types will be formatted into valid XML character data. This means in particular that the characters \<, \>, and & will be converted to entities. Binary data (data type `bytea`) will be represented in base64 or hex encoding, depending on the setting of the configuration parameter [???](#guc-xmlbinary). The particular behavior for individual data types is expected to evolve in order to align the PostgreSQL mappings with those specified in SQL:2006 and later, as discussed in [???](#functions-xml-limits-casts).

#### `xmlforest`

xmlforest

xmlforest

(

content

AS

name

, ...

)

xml

The `xmlforest` expression produces an XML forest (sequence) of elements using the given names and content. As for `xmlelement`, each \<name\> must be a simple identifier, while the \<content\> expressions can have any data type.

Examples:

    SELECT xmlforest('abc' AS foo, 123 AS bar);

              xmlforest
    ------------------------------
     <foo>abc</foo><bar>123</bar>

    SELECT xmlforest(table_name, column_name)
    FROM information_schema.columns
    WHERE table_schema = 'pg_catalog';

                                    xmlforest
    ------------------------------------​-----------------------------------
     <table_name>pg_authid</table_name>​<column_name>rolname</column_name>
     <table_name>pg_authid</table_name>​<column_name>rolsuper</column_name>
     ...

As seen in the second example, the element name can be omitted if the content value is a column reference, in which case the column name is used by default. Otherwise, a name must be specified.

Element names that are not valid XML names are escaped as shown for `xmlelement` above. Similarly, content data is escaped to make valid XML content, unless it is already of type `xml`.

Note that XML forests are not valid XML documents if they consist of more than one element, so it might be useful to wrap `xmlforest` expressions in `xmlelement`.

#### `xmlpi`

xmlpi

xmlpi

(

NAME

name

,

content

)

xml

The `xmlpi` expression creates an XML processing instruction. As for `xmlelement`, the \<name\> must be a simple identifier, while the \<content\> expression can have any data type. The \<content\>, if present, must not contain the character sequence `?>`.

Example:

    SELECT xmlpi(name php, 'echo "hello world";');

                xmlpi
    -----------------------------
     <?php echo "hello world";?>

#### `xmlroot`

xmlroot

xmlroot

(

xml

,

VERSION

{

text

\|

NO VALUE

}

,

STANDALONE

{

YES

\|

NO

\|

NO VALUE

}

)

xml

The `xmlroot` expression alters the properties of the root node of an XML value. If a version is specified, it replaces the value in the root node's version declaration; if a standalone setting is specified, it replaces the value in the root node's standalone declaration.

    SELECT xmlroot(xmlparse(document '<content>abc</content>'),
                   version '1.0', standalone yes);

                    xmlroot
    ----------------------------------------
     
     <content>abc</content>

#### `xmlagg`

xmlagg

xmlagg

(

xml

)

xml

The function `xmlagg` is, unlike the other functions described here, an aggregate function. It concatenates the input values to the aggregate function call, much like `xmlconcat` does, except that concatenation occurs across rows rather than across expressions in a single row. See [Aggregate Functions](#functions-aggregate) for additional information about aggregate functions.

Example:

    CREATE TABLE test (y int, x xml);
    INSERT INTO test VALUES (1, '<foo>abc</foo>');
    INSERT INTO test VALUES (2, '<bar/>');
    SELECT xmlagg(x) FROM test;
            xmlagg
    ----------------------
     <foo>abc</foo><bar/>

To determine the order of the concatenation, an `ORDER BY` clause may be added to the aggregate call as described in [???](#syntax-aggregates). For example:

    SELECT xmlagg(x ORDER BY y DESC) FROM test;
            xmlagg
    ----------------------
     <bar/><foo>abc</foo>

The following non-standard approach used to be recommended in previous versions, and may still be useful in specific cases:

    SELECT xmlagg(x) FROM (SELECT * FROM test ORDER BY y DESC) AS tab;
            xmlagg
    ----------------------
     <bar/><foo>abc</foo>

### XML Predicates

The expressions described in this section check properties of `xml` values.

#### `IS DOCUMENT`

IS DOCUMENT

xml

IS DOCUMENT

boolean

The expression `IS DOCUMENT` returns true if the argument XML value is a proper XML document, false if it is not (that is, it is a content fragment), or null if the argument is null. See [???](#datatype-xml) about the difference between documents and content fragments.

#### `IS NOT DOCUMENT`

IS NOT DOCUMENT

xml

IS NOT DOCUMENT

boolean

The expression `IS NOT DOCUMENT` returns false if the argument XML value is a proper XML document, true if it is not (that is, it is a content fragment), or null if the argument is null.

#### `XMLEXISTS`

XMLEXISTS

XMLEXISTS

(

text

PASSING

BY

{

REF

\|

VALUE

}

xml

BY

{

REF

\|

VALUE

}

)

boolean

The function `xmlexists` evaluates an XPath 1.0 expression (the first argument), with the passed XML value as its context item. The function returns false if the result of that evaluation yields an empty node-set, true if it yields any other value. The function returns null if any argument is null. A nonnull value passed as the context item must be an XML document, not a content fragment or any non-XML value.

Example:

    SELECT xmlexists('//town[text() = ''Toronto'']' PASSING BY VALUE '<towns><town>Toronto</town><town>Ottawa</town></towns>');

     xmlexists
    ------------
     t
    (1 row)

The `BY REF` and `BY VALUE` clauses are accepted in PostgreSQL, but are ignored, as discussed in [???](#functions-xml-limits-postgresql).

In the SQL standard, the `xmlexists` function evaluates an expression in the XML Query language, but PostgreSQL allows only an XPath 1.0 expression, as discussed in [???](#functions-xml-limits-xpath1).

#### `xml_is_well_formed`

xml_is_well_formed

xml_is_well_formed_document

xml_is_well_formed_content

xml_is_well_formed

(

text

)

boolean

xml_is_well_formed_document

(

text

)

boolean

xml_is_well_formed_content

(

text

)

boolean

These functions check whether a `text` string represents well-formed XML, returning a Boolean result. `xml_is_well_formed_document` checks for a well-formed document, while `xml_is_well_formed_content` checks for well-formed content. `xml_is_well_formed` does the former if the [???](#guc-xmloption) configuration parameter is set to `DOCUMENT`, or the latter if it is set to `CONTENT`. This means that `xml_is_well_formed` is useful for seeing whether a simple cast to type `xml` will succeed, whereas the other two functions are useful for seeing whether the corresponding variants of `XMLPARSE` will succeed.

Examples:

    SET xmloption TO DOCUMENT;
    SELECT xml_is_well_formed('<>');
     xml_is_well_formed
    --------------------
     f
    (1 row)

    SELECT xml_is_well_formed('<abc/>');
     xml_is_well_formed
    --------------------
     t
    (1 row)

    SET xmloption TO CONTENT;
    SELECT xml_is_well_formed('abc');
     xml_is_well_formed
    --------------------
     t
    (1 row)

    SELECT xml_is_well_formed_document('<pg:foo xmlns:pg="http://postgresql.org/stuff">bar</pg:foo>');
     xml_is_well_formed_document
    -----------------------------
     t
    (1 row)

    SELECT xml_is_well_formed_document('<pg:foo xmlns:pg="http://postgresql.org/stuff">bar</my:foo>');
     xml_is_well_formed_document
    -----------------------------
     f
    (1 row)

The last example shows that the checks include whether namespaces are correctly matched.

### Processing XML

To process values of data type `xml`, PostgreSQL offers the functions `xpath` and `xpath_exists`, which evaluate XPath 1.0 expressions, and the `XMLTABLE` table function.

#### `xpath`

XPath

xpath

(

xpath

text

,

xml

xml

,

nsarray

text\[\]

)

xml\[\]

The function `xpath` evaluates the XPath 1.0 expression `xpath` (given as text) against the XML value `xml`. It returns an array of XML values corresponding to the node-set produced by the XPath expression. If the XPath expression returns a scalar value rather than a node-set, a single-element array is returned.

The second argument must be a well formed XML document. In particular, it must have a single root node element.

The optional third argument of the function is an array of namespace mappings. This array should be a two-dimensional `text` array with the length of the second axis being equal to 2 (i.e., it should be an array of arrays, each of which consists of exactly 2 elements). The first element of each array entry is the namespace name (alias), the second the namespace URI. It is not required that aliases provided in this array be the same as those being used in the XML document itself (in other words, both in the XML document and in the `xpath` function context, aliases are *local*).

Example:

    SELECT xpath('/my:a/text()', '<my:a xmlns:my="http://example.com">test</my:a>',
                 ARRAY[ARRAY['my', 'http://example.com']]);

     xpath
    --------
     {test}
    (1 row)

To deal with default (anonymous) namespaces, do something like this:

    SELECT xpath('//mydefns:b/text()', '<a xmlns="http://example.com"><b>test</b></a>',
                 ARRAY[ARRAY['mydefns', 'http://example.com']]);

     xpath
    --------
     {test}
    (1 row)

#### `xpath_exists`

xpath_exists

xpath_exists

(

xpath

text

,

xml

xml

,

nsarray

text\[\]

)

boolean

The function `xpath_exists` is a specialized form of the `xpath` function. Instead of returning the individual XML values that satisfy the XPath 1.0 expression, this function returns a Boolean indicating whether the query was satisfied or not (specifically, whether it produced any value other than an empty node-set). This function is equivalent to the `XMLEXISTS` predicate, except that it also offers support for a namespace mapping argument.

Example:

    SELECT xpath_exists('/my:a/text()', '<my:a xmlns:my="http://example.com">test</my:a>',
                         ARRAY[ARRAY['my', 'http://example.com']]);

     xpath_exists
    --------------
     t
    (1 row)

#### `xmltable`

xmltable

table function

XMLTABLE

XMLTABLE

(

XMLNAMESPACES

(

namespace_uri

AS

namespace_name

, ...

),

row_expression

PASSING

BY

{

REF

\|

VALUE

}

document_expression

BY

{

REF

\|

VALUE

}

COLUMNS

name

{

type

PATH

column_expression

DEFAULT

default_expression

NOT NULL

\|

NULL

\|

FOR ORDINALITY

}

, ...

)

setof record

The `xmltable` expression produces a table based on an XML value, an XPath filter to extract rows, and a set of column definitions. Although it syntactically resembles a function, it can only appear as a table in a query's `FROM` clause.

The optional `XMLNAMESPACES` clause gives a comma-separated list of namespace definitions, where each \<namespace_uri\> is a `text` expression and each \<namespace_name\> is a simple identifier. It specifies the XML namespaces used in the document and their aliases. A default namespace specification is not currently supported.

The required \<row_expression\> argument is an XPath 1.0 expression (given as `text`) that is evaluated, passing the XML value \<document_expression\> as its context item, to obtain a set of XML nodes. These nodes are what `xmltable` transforms into output rows. No rows will be produced if the \<document_expression\> is null, nor if the \<row_expression\> produces an empty node-set or any value other than a node-set.

\<document_expression\> provides the context item for the \<row_expression\>. It must be a well-formed XML document; fragments/forests are not accepted. The `BY REF` and `BY VALUE` clauses are accepted but ignored, as discussed in [???](#functions-xml-limits-postgresql).

In the SQL standard, the `xmltable` function evaluates expressions in the XML Query language, but PostgreSQL allows only XPath 1.0 expressions, as discussed in [???](#functions-xml-limits-xpath1).

The required `COLUMNS` clause specifies the column(s) that will be produced in the output table. See the syntax summary above for the format. A name is required for each column, as is a data type (unless `FOR ORDINALITY` is specified, in which case type `integer` is implicit). The path, default and nullability clauses are optional.

A column marked `FOR ORDINALITY` will be populated with row numbers, starting with 1, in the order of nodes retrieved from the \<row_expression\>'s result node-set. At most one column may be marked `FOR ORDINALITY`.

> [!NOTE]
> XPath 1.0 does not specify an order for nodes in a node-set, so code that relies on a particular order of the results will be implementation-dependent. Details can be found in [???](#xml-xpath-1-specifics).

The \<column_expression\> for a column is an XPath 1.0 expression that is evaluated for each row, with the current node from the \<row_expression\> result as its context item, to find the value of the column. If no \<column_expression\> is given, then the column name is used as an implicit path.

If a column's XPath expression returns a non-XML value (which is limited to string, boolean, or double in XPath 1.0) and the column has a PostgreSQL type other than `xml`, the column will be set as if by assigning the value's string representation to the PostgreSQL type. (If the value is a boolean, its string representation is taken to be `1` or `0` if the output column's type category is numeric, otherwise `true` or `false`.)

If a column's XPath expression returns a non-empty set of XML nodes and the column's PostgreSQL type is `xml`, the column will be assigned the expression result exactly, if it is of document or content form. [^1]

A non-XML result assigned to an `xml` output column produces content, a single text node with the string value of the result. An XML result assigned to a column of any other type may not have more than one node, or an error is raised. If there is exactly one node, the column will be set as if by assigning the node's string value (as defined for the XPath 1.0 `string` function) to the PostgreSQL type.

The string value of an XML element is the concatenation, in document order, of all text nodes contained in that element and its descendants. The string value of an element with no descendant text nodes is an empty string (not `NULL`). Any `xsi:nil` attributes are ignored. Note that the whitespace-only `text()` node between two non-text elements is preserved, and that leading whitespace on a `text()` node is not flattened. The XPath 1.0 `string` function may be consulted for the rules defining the string value of other XML node types and non-XML values.

The conversion rules presented here are not exactly those of the SQL standard, as discussed in [???](#functions-xml-limits-casts).

If the path expression returns an empty node-set (typically, when it does not match) for a given row, the column will be set to `NULL`, unless a \<default_expression\> is specified; then the value resulting from evaluating that expression is used.

A \<default_expression\>, rather than being evaluated immediately when `xmltable` is called, is evaluated each time a default is needed for the column. If the expression qualifies as stable or immutable, the repeat evaluation may be skipped. This means that you can usefully use volatile functions like `nextval` in \<default_expression\>.

Columns may be marked `NOT NULL`. If the \<column_expression\> for a `NOT NULL` column does not match anything and there is no `DEFAULT` or the \<default_expression\> also evaluates to null, an error is reported.

Examples:

    CREATE TABLE xmldata AS SELECT
    xml $$
    <ROWS>
      <ROW id="1">
        <COUNTRY_ID>AU</COUNTRY_ID>
        <COUNTRY_NAME>Australia</COUNTRY_NAME>
      </ROW>
      <ROW id="5">
        <COUNTRY_ID>JP</COUNTRY_ID>
        <COUNTRY_NAME>Japan</COUNTRY_NAME>
        <PREMIER_NAME>Shinzo Abe</PREMIER_NAME>
        <SIZE unit="sq_mi">145935</SIZE>
      </ROW>
      <ROW id="6">
        <COUNTRY_ID>SG</COUNTRY_ID>
        <COUNTRY_NAME>Singapore</COUNTRY_NAME>
        <SIZE unit="sq_km">697</SIZE>
      </ROW>
    </ROWS>
    $$ AS data;

    SELECT xmltable.*
      FROM xmldata,
           XMLTABLE('//ROWS/ROW'
                    PASSING data
                    COLUMNS id int PATH '@id',
                            ordinality FOR ORDINALITY,
                            "COUNTRY_NAME" text,
                            country_id text PATH 'COUNTRY_ID',
                            size_sq_km float PATH 'SIZE[@unit = "sq_km"]',
                            size_other text PATH
                                 'concat(SIZE[@unit!="sq_km"], " ", SIZE[@unit!="sq_km"]/@unit)',
                            premier_name text PATH 'PREMIER_NAME' DEFAULT 'not specified');

     id | ordinality | COUNTRY_NAME | country_id | size_sq_km |  size_other  | premier_name
    ----+------------+--------------+------------+------------+--------------+---------------
      1 |          1 | Australia    | AU         |            |              | not specified
      5 |          2 | Japan        | JP         |            | 145935 sq_mi | Shinzo Abe
      6 |          3 | Singapore    | SG         |        697 |              | not specified

The following example shows concatenation of multiple text() nodes, usage of the column name as XPath filter, and the treatment of whitespace, XML comments and processing instructions:

    CREATE TABLE xmlelements AS SELECT
    xml $$
      <root>
       <element>  Hello<!-- xyxxz -->2a2<?aaaaa?> <!--x-->  bbb<x>xxx</x>CC  </element>
      </root>
    $$ AS data;

    SELECT xmltable.*
      FROM xmlelements, XMLTABLE('/root' PASSING data COLUMNS element text);
             element
    -------------------------
       Hello2a2   bbbxxxCC

The following example illustrates how the `XMLNAMESPACES` clause can be used to specify a list of namespaces used in the XML document as well as in the XPath expressions:

    WITH xmldata(data) AS (VALUES ('
    <example xmlns="http://example.com/myns" xmlns:B="http://example.com/b">
     <item foo="1" B:bar="2"/>
     <item foo="3" B:bar="4"/>
     <item foo="4" B:bar="5"/>
    </example>'::xml)
    )
    SELECT xmltable.*
      FROM XMLTABLE(XMLNAMESPACES('http://example.com/myns' AS x,
                                  'http://example.com/b' AS "B"),
                 '/x:example/x:item'
                    PASSING (SELECT data FROM xmldata)
                    COLUMNS foo int PATH '@foo',
                      bar int PATH '@B:bar');
     foo | bar
    -----+-----
       1 |   2
       3 |   4
       4 |   5
    (3 rows)

### Mapping Tables to XML

XML export

The following functions map the contents of relational tables to XML values. They can be thought of as XML export functionality: `table_to_xml` ( `table` `regclass`, `nulls` `boolean`, `tableforest` `boolean`, `targetns` `text` ) xml `query_to_xml` ( `query` `text`, `nulls` `boolean`, `tableforest` `boolean`, `targetns` `text` ) xml `cursor_to_xml` ( `cursor` `refcursor`, `count` `integer`, `nulls` `boolean`, `tableforest` `boolean`, `targetns` `text` ) xml

`table_to_xml` maps the content of the named table, passed as parameter `table`. The `regclass` type accepts strings identifying tables using the usual notation, including optional schema qualification and double quotes (see [???](#datatype-oid) for details). `query_to_xml` executes the query whose text is passed as parameter `query` and maps the result set. `cursor_to_xml` fetches the indicated number of rows from the cursor specified by the parameter `cursor`. This variant is recommended if large tables have to be mapped, because the result value is built up in memory by each function.

If `tableforest` is false, then the resulting XML document looks like this:

    <tablename>
      <row>
        <columnname1>data</columnname1>
        <columnname2>data</columnname2>
      </row>

      <row>
        ...
      </row>

      ...
    </tablename>

If `tableforest` is true, the result is an XML content fragment that looks like this:

    <tablename>
      <columnname1>data</columnname1>
      <columnname2>data</columnname2>
    </tablename>

    <tablename>
      ...
    </tablename>

    ...

If no table name is available, that is, when mapping a query or a cursor, the string `table` is used in the first format, `row` in the second format.

The choice between these formats is up to the user. The first format is a proper XML document, which will be important in many applications. The second format tends to be more useful in the `cursor_to_xml` function if the result values are to be reassembled into one document later on. The functions for producing XML content discussed above, in particular `xmlelement`, can be used to alter the results to taste.

The data values are mapped in the same way as described for the function `xmlelement` above.

The parameter `nulls` determines whether null values should be included in the output. If true, null values in columns are represented as:

    <columnname xsi:nil="true"/>

where `xsi` is the XML namespace prefix for XML Schema Instance. An appropriate namespace declaration will be added to the result value. If false, columns containing null values are simply omitted from the output.

The parameter `targetns` specifies the desired XML namespace of the result. If no particular namespace is wanted, an empty string should be passed.

The following functions return XML Schema documents describing the mappings performed by the corresponding functions above: `table_to_xmlschema` ( `table` `regclass`, `nulls` `boolean`, `tableforest` `boolean`, `targetns` `text` ) xml `query_to_xmlschema` ( `query` `text`, `nulls` `boolean`, `tableforest` `boolean`, `targetns` `text` ) xml `cursor_to_xmlschema` ( `cursor` `refcursor`, `nulls` `boolean`, `tableforest` `boolean`, `targetns` `text` ) xml It is essential that the same parameters are passed in order to obtain matching XML data mappings and XML Schema documents.

The following functions produce XML data mappings and the corresponding XML Schema in one document (or forest), linked together. They can be useful where self-contained and self-describing results are wanted: `table_to_xml_and_xmlschema` ( `table` `regclass`, `nulls` `boolean`, `tableforest` `boolean`, `targetns` `text` ) xml `query_to_xml_and_xmlschema` ( `query` `text`, `nulls` `boolean`, `tableforest` `boolean`, `targetns` `text` ) xml

In addition, the following functions are available to produce analogous mappings of entire schemas or the entire current database: `schema_to_xml` ( `schema` `name`, `nulls` `boolean`, `tableforest` `boolean`, `targetns` `text` ) xml `schema_to_xmlschema` ( `schema` `name`, `nulls` `boolean`, `tableforest` `boolean`, `targetns` `text` ) xml `schema_to_xml_and_xmlschema` ( `schema` `name`, `nulls` `boolean`, `tableforest` `boolean`, `targetns` `text` ) xml `database_to_xml` ( `nulls` `boolean`, `tableforest` `boolean`, `targetns` `text` ) xml `database_to_xmlschema` ( `nulls` `boolean`, `tableforest` `boolean`, `targetns` `text` ) xml `database_to_xml_and_xmlschema` ( `nulls` `boolean`, `tableforest` `boolean`, `targetns` `text` ) xml These functions ignore tables that are not readable by the current user. The database-wide functions additionally ignore schemas that the current user does not have `USAGE` (lookup) privilege for.

Note that these potentially produce a lot of data, which needs to be built up in memory. When requesting content mappings of large schemas or databases, it might be worthwhile to consider mapping the tables separately instead, possibly even through a cursor.

The result of a schema content mapping looks like this:

    <schemaname>

    table1-mapping

    table2-mapping

    ...

    </schemaname>

where the format of a table mapping depends on the `tableforest` parameter as explained above.

The result of a database content mapping looks like this:

    <dbname>

    <schema1name>
      ...
    </schema1name>

    <schema2name>
      ...
    </schema2name>

    ...

    </dbname>

where the schema mapping is as above.

As an example of using the output produced by these functions, [example_title](#xslt-xml-html) shows an XSLT stylesheet that converts the output of `table_to_xml_and_xmlschema` to an HTML document containing a tabular rendition of the table data. In a similar manner, the results from these functions can be converted into other XML-based formats.

XSLT Stylesheet for Converting SQL/XML Output to HTML

    <xsl:stylesheet version="1.0"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns="http://www.w3.org/1999/xhtml"
    >

      <xsl:output method="xml"
          doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
          doctype-public="-//W3C/DTD XHTML 1.0 Strict//EN"
          indent="yes"/>

      <xsl:template match="/*">
        <xsl:variable name="schema" select="//xsd:schema"/>
        <xsl:variable name="tabletypename"
                      select="$schema/xsd:element[@name=name(current())]/@type"/>
        <xsl:variable name="rowtypename"
                      select="$schema/xsd:complexType[@name=$tabletypename]/xsd:sequence/xsd:element[@name='row']/@type"/>

        <html>
          <head>
            <title><xsl:value-of select="name(current())"/></title>
          </head>
          <body>
            <table>
              <tr>
                <xsl:for-each select="$schema/xsd:complexType[@name=$rowtypename]/xsd:sequence/xsd:element/@name">
                  <th><xsl:value-of select="."/></th>
                </xsl:for-each>
              </tr>

              <xsl:for-each select="row">
                <tr>
                  <xsl:for-each select="*">
                    <td><xsl:value-of select="."/></td>
                  </xsl:for-each>
                </tr>
              </xsl:for-each>
            </table>
          </body>
        </html>
      </xsl:template>

    </xsl:stylesheet>

## JSON Functions and Operators

JSON

functions and operators

SQL/JSON

functions and expressions

This section describes:

- functions and operators for processing and creating JSON data

- the SQL/JSON path language

- the SQL/JSON query functions

To provide native support for JSON data types within the SQL environment, PostgreSQL implements the SQL/JSON data model. This model comprises sequences of items. Each item can hold SQL scalar values, with an additional SQL/JSON null value, and composite data structures that use JSON arrays and objects. The model is a formalization of the implied data model in the JSON specification [RFC 7159](https://datatracker.ietf.org/doc/html/rfc7159).

SQL/JSON allows you to handle JSON data alongside regular SQL data, with transaction support, including:

- Uploading JSON data into the database and storing it in regular SQL columns as character or binary strings.

- Generating JSON objects and arrays from relational data.

- Querying JSON data using SQL/JSON query functions and SQL/JSON path language expressions.

To learn more about the SQL/JSON standard, see [???](#sqltr-19075-6). For details on JSON types supported in PostgreSQL, see [???](#datatype-json).

### Processing and Creating JSON Data

[ and Operators](#functions-json-op-table) shows the operators that are available for use with JSON data types (see [???](#datatype-json)). In addition, the usual comparison operators shown in [Comparison Operators](#functions-comparison-op-table) are available for `jsonb`, though not for `json`. The comparison operators follow the ordering rules for B-tree operations outlined in [???](#json-indexing). See also [Aggregate Functions](#functions-aggregate) for the aggregate function `json_agg` which aggregates record values as JSON, the aggregate function `json_object_agg` which aggregates pairs of values into a JSON object, and their `jsonb` equivalents, `jsonb_agg` and `jsonb_object_agg`.

<table id="functions-json-op-table">
<caption><code>json</code> and <code>jsonb</code> Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>json</code> <code>-&gt;</code> <code>integer</code> json</p>
<p role="func_signature"><code>jsonb</code> <code>-&gt;</code> <code>integer</code> jsonb</p>
<p>Extracts <code>n</code>'th element of JSON array (array elements are indexed from zero, but negative integers count from the end).</p>
<p><code>'[{"a":"foo"},{"b":"bar"},{"c":"baz"}]'::json -&gt; 2</code> {"c":"baz"}</p>
<p><code>'[{"a":"foo"},{"b":"bar"},{"c":"baz"}]'::json -&gt; -3</code> {"a":"foo"}</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>json</code> <code>-&gt;</code> <code>text</code> json</p>
<p role="func_signature"><code>jsonb</code> <code>-&gt;</code> <code>text</code> jsonb</p>
<p>Extracts JSON object field with the given key.</p>
<p><code>'{"a": {"b":"foo"}}'::json -&gt; 'a'</code> {"b":"foo"}</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>json</code> <code>-&gt;&gt;</code> <code>integer</code> text</p>
<p role="func_signature"><code>jsonb</code> <code>-&gt;&gt;</code> <code>integer</code> text</p>
<p>Extracts <code>n</code>'th element of JSON array, as <code>text</code>.</p>
<p><code>'[1,2,3]'::json -&gt;&gt; 2</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>json</code> <code>-&gt;&gt;</code> <code>text</code> text</p>
<p role="func_signature"><code>jsonb</code> <code>-&gt;&gt;</code> <code>text</code> text</p>
<p>Extracts JSON object field with the given key, as <code>text</code>.</p>
<p><code>'{"a":1,"b":2}'::json -&gt;&gt; 'b'</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>json</code> <code>#&gt;</code> <code>text[]</code> json</p>
<p role="func_signature"><code>jsonb</code> <code>#&gt;</code> <code>text[]</code> jsonb</p>
<p>Extracts JSON sub-object at the specified path, where path elements can be either field keys or array indexes.</p>
<p><code>'{"a": {"b": ["foo","bar"]}}'::json #&gt; '{a,b,1}'</code> "bar"</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>json</code> <code>#&gt;&gt;</code> <code>text[]</code> text</p>
<p role="func_signature"><code>jsonb</code> <code>#&gt;&gt;</code> <code>text[]</code> text</p>
<p>Extracts JSON sub-object at the specified path as <code>text</code>.</p>
<p><code>'{"a": {"b": ["foo","bar"]}}'::json #&gt;&gt; '{a,b,1}'</code> bar</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> The field/element/path extraction operators return NULL, rather than failing, if the JSON input does not have the right structure to match the request; for example if no such key or array element exists.

Some further operators exist only for `jsonb`, as shown in [Additional Operators](#functions-jsonb-op-table). [???](#json-indexing) describes how these operators can be used to effectively search indexed `jsonb` data.

<table id="functions-jsonb-op-table">
<caption>Additional <code>jsonb</code> Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>jsonb</code> <code>@&gt;</code> <code>jsonb</code> boolean</p>
<p>Does the first JSON value contain the second? (See <a href="#json-containment">???</a> for details about containment.)</p>
<p><code>'{"a":1, "b":2}'::jsonb @&gt; '{"b":2}'::jsonb</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>jsonb</code> <code>&lt;@</code> <code>jsonb</code> boolean</p>
<p>Is the first JSON value contained in the second?</p>
<p><code>'{"b":2}'::jsonb &lt;@ '{"a":1, "b":2}'::jsonb</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>jsonb</code> <code>?</code> <code>text</code> boolean</p>
<p>Does the text string exist as a top-level key or array element within the JSON value?</p>
<p><code>'{"a":1, "b":2}'::jsonb ? 'b'</code> t</p>
<p><code>'["a", "b", "c"]'::jsonb ? 'b'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>jsonb</code> <code>?|</code> <code>text[]</code> boolean</p>
<p>Do any of the strings in the text array exist as top-level keys or array elements?</p>
<p><code>'{"a":1, "b":2, "c":3}'::jsonb ?| array['b', 'd']</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>jsonb</code> <code>?&amp;</code> <code>text[]</code> boolean</p>
<p>Do all of the strings in the text array exist as top-level keys or array elements?</p>
<p><code>'["a", "b", "c"]'::jsonb ?&amp; array['a', 'b']</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>jsonb</code> <code>||</code> <code>jsonb</code> jsonb</p>
<p>Concatenates two <code>jsonb</code> values. Concatenating two arrays generates an array containing all the elements of each input. Concatenating two objects generates an object containing the union of their keys, taking the second object's value when there are duplicate keys. All other cases are treated by converting a non-array input into a single-element array, and then proceeding as for two arrays. Does not operate recursively: only the top-level array or object structure is merged.</p>
<p><code>'["a", "b"]'::jsonb || '["a", "d"]'::jsonb</code> ["a", "b", "a", "d"]</p>
<p><code>'{"a": "b"}'::jsonb || '{"c": "d"}'::jsonb</code> {"a": "b", "c": "d"}</p>
<p><code>'[1, 2]'::jsonb || '3'::jsonb</code> [1, 2, 3]</p>
<p><code>'{"a": "b"}'::jsonb || '42'::jsonb</code> [{"a": "b"}, 42]</p>
<p>To append an array to another array as a single entry, wrap it in an additional layer of array, for example:</p>
<p><code>'[1, 2]'::jsonb || jsonb_build_array('[3, 4]'::jsonb)</code> [1, 2, [3, 4]]</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>jsonb</code> <code>-</code> <code>text</code> jsonb</p>
<p>Deletes a key (and its value) from a JSON object, or matching string value(s) from a JSON array.</p>
<p><code>'{"a": "b", "c": "d"}'::jsonb - 'a'</code> {"c": "d"}</p>
<p><code>'["a", "b", "c", "b"]'::jsonb - 'b'</code> ["a", "c"]</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>jsonb</code> <code>-</code> <code>text[]</code> jsonb</p>
<p>Deletes all matching keys or array elements from the left operand.</p>
<p><code>'{"a": "b", "c": "d"}'::jsonb - '{a,c}'::text[]</code> {}</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>jsonb</code> <code>-</code> <code>integer</code> jsonb</p>
<p>Deletes the array element with specified index (negative integers count from the end). Throws an error if JSON value is not an array.</p>
<p><code>'["a", "b"]'::jsonb - 1</code> ["a"]</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>jsonb</code> <code>#-</code> <code>text[]</code> jsonb</p>
<p>Deletes the field or array element at the specified path, where path elements can be either field keys or array indexes.</p>
<p><code>'["a", {"b":1}]'::jsonb #- '{1,b}'</code> ["a", {}]</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>jsonb</code> <code>@?</code> <code>jsonpath</code> boolean</p>
<p>Does JSON path return any item for the specified JSON value? (This is useful only with SQL-standard JSON path expressions, not <a href="#functions-sqljson-check-expressions">predicate check expressions</a>, since those always return a value.)</p>
<p><code>'{"a":[1,2,3,4,5]}'::jsonb @? '$.a[*] ? (@ &gt; 2)'</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>jsonb</code> <code>@@</code> <code>jsonpath</code> boolean</p>
<p>Returns the result of a JSON path predicate check for the specified JSON value. (This is useful only with <a href="#functions-sqljson-check-expressions">predicate check expressions</a>, not SQL-standard JSON path expressions, since it will return <code>NULL</code> if the path result is not a single boolean value.)</p>
<p><code>'{"a":[1,2,3,4,5]}'::jsonb @@ '$.a[*] &gt; 2'</code> t</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> The `jsonpath` operators `@?` and `@@` suppress the following errors: missing object field or array element, unexpected JSON item type, datetime and numeric errors. The `jsonpath`-related functions described below can also be told to suppress these types of errors. This behavior might be helpful when searching JSON document collections of varying structure.

[JSON Creation Functions](#functions-json-creation-table) shows the functions that are available for constructing `json` and `jsonb` values. Some functions in this table have a `RETURNING` clause, which specifies the data type returned. It must be one of `json`, `jsonb`, `bytea`, a character string type (`text`, `char`, or `varchar`), or a type that can be cast to `json`. By default, the `json` type is returned.

<table id="functions-json-creation-table">
<caption>JSON Creation Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_json</code> ( <code>anyelement</code> ) json</p>
<p role="func_signature"><span class="indexterm"></span> <code>to_jsonb</code> ( <code>anyelement</code> ) jsonb</p>
<p>Converts any SQL value to <code>json</code> or <code>jsonb</code>. Arrays and composites are converted recursively to arrays and objects (multidimensional arrays become arrays of arrays in JSON). Otherwise, if there is a cast from the SQL data type to <code>json</code>, the cast function will be used to perform the conversion;<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a> otherwise, a scalar JSON value is produced. For any scalar other than a number, a Boolean, or a null value, the text representation will be used, with escaping as necessary to make it a valid JSON string value.</p>
<p><code>to_json('Fred said "Hi."'::text)</code> "Fred said \"Hi.\""</p>
<p><code>to_jsonb(row(42, 'Fred said "Hi."'::text))</code> {"f1": 42, "f2": "Fred said \"Hi.\""}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_to_json</code> ( <code>anyarray</code> [, <code>boolean</code>] ) json</p>
<p>Converts an SQL array to a JSON array. The behavior is the same as <code>to_json</code> except that line feeds will be added between top-level array elements if the optional boolean parameter is true.</p>
<p><code>array_to_json('{{1,5},{99,100}}'::int[])</code> [[1,5],[99,100]]</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_array</code> ( [{ &lt;value_expression&gt; [<code>FORMAT JSON</code>] } [, ...]] [{ <code>NULL</code> | <code>ABSENT</code> } <code>ON NULL</code>] [<code>RETURNING</code> &lt;data_type&gt; [<code>FORMAT JSON</code> [<code>ENCODING UTF8</code>]]])</p>
<p role="func_signature"><code>json_array</code> ( [&lt;query_expression&gt;] [<code>RETURNING</code> &lt;data_type&gt; [<code>FORMAT JSON</code> [<code>ENCODING UTF8</code>]]])</p>
<p>Constructs a JSON array from either a series of &lt;value_expression&gt; parameters or from the results of &lt;query_expression&gt;, which must be a SELECT query returning a single column. If <code>ABSENT ON NULL</code> is specified, NULL values are ignored. This is always the case if a &lt;query_expression&gt; is used.</p>
<p><code>json_array(1,true,json '{"a":null}')</code> [1, true, {"a":null}]</p>
<p><code>json_array(SELECT * FROM (VALUES(1),(2)) t)</code> [1, 2]</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>row_to_json</code> ( <code>record</code> [, <code>boolean</code>] ) json</p>
<p>Converts an SQL composite value to a JSON object. The behavior is the same as <code>to_json</code> except that line feeds will be added between top-level elements if the optional boolean parameter is true.</p>
<p><code>row_to_json(row(1,'foo'))</code> {"f1":1,"f2":"foo"}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_build_array</code> ( <code>VARIADIC</code> <code>"any"</code> ) json</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_build_array</code> ( <code>VARIADIC</code> <code>"any"</code> ) jsonb</p>
<p>Builds a possibly-heterogeneously-typed JSON array out of a variadic argument list. Each argument is converted as per <code>to_json</code> or <code>to_jsonb</code>.</p>
<p><code>json_build_array(1, 2, 'foo', 4, 5)</code> [1, 2, "foo", 4, 5]</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_build_object</code> ( <code>VARIADIC</code> <code>"any"</code> ) json</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_build_object</code> ( <code>VARIADIC</code> <code>"any"</code> ) jsonb</p>
<p>Builds a JSON object out of a variadic argument list. By convention, the argument list consists of alternating keys and values. Key arguments are coerced to text; value arguments are converted as per <code>to_json</code> or <code>to_jsonb</code>.</p>
<p><code>json_build_object('foo', 1, 2, row(3,'bar'))</code> {"foo" : 1, "2" : {"f1":3,"f2":"bar"}}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_object</code> ( [{ &lt;key_expression&gt; { <code>VALUE</code> | ':' } &lt;value_expression&gt; [<code>FORMAT JSON</code> [<code>ENCODING UTF8</code>]] }[, ...]] [{ <code>NULL</code> | <code>ABSENT</code> } <code>ON NULL</code>] [{ <code>WITH</code> | <code>WITHOUT</code> } <code>UNIQUE</code> [<code>KEYS</code>]] [<code>RETURNING</code> &lt;data_type&gt; [<code>FORMAT JSON</code> [<code>ENCODING UTF8</code>]]])</p>
<p>Constructs a JSON object of all the key/value pairs given, or an empty object if none are given. &lt;key_expression&gt; is a scalar expression defining the JSON key, which is converted to the <code>text</code> type. It cannot be <code>NULL</code> nor can it belong to a type that has a cast to the <code>json</code> type. If <code>WITH UNIQUE KEYS</code> is specified, there must not be any duplicate &lt;key_expression&gt;. Any pair for which the &lt;value_expression&gt; evaluates to <code>NULL</code> is omitted from the output if <code>ABSENT ON NULL</code> is specified; if <code>NULL ON NULL</code> is specified or the clause omitted, the key is included with value <code>NULL</code>.</p>
<p><code>json_object('code' VALUE 'P123', 'title': 'Jaws')</code> {"code" : "P123", "title" : "Jaws"}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_object</code> ( <code>text[]</code> ) json</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_object</code> ( <code>text[]</code> ) jsonb</p>
<p>Builds a JSON object out of a text array. The array must have either exactly one dimension with an even number of members, in which case they are taken as alternating key/value pairs, or two dimensions such that each inner array has exactly two elements, which are taken as a key/value pair. All values are converted to JSON strings.</p>
<p><code>json_object('{a, 1, b, "def", c, 3.5}')</code> {"a" : "1", "b" : "def", "c" : "3.5"}</p>
<p><code>json_object('{{a, 1}, {b, "def"}, {c, 3.5}}')</code> {"a" : "1", "b" : "def", "c" : "3.5"}</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>json_object</code> ( <code>keys</code> <code>text[]</code>, <code>values</code> <code>text[]</code> ) json</p>
<p role="func_signature"><code>jsonb_object</code> ( <code>keys</code> <code>text[]</code>, <code>values</code> <code>text[]</code> ) jsonb</p>
<p>This form of <code>json_object</code> takes keys and values pairwise from separate text arrays. Otherwise it is identical to the one-argument form.</p>
<p><code>json_object('{a,b}', '{1,2}')</code> {"a": "1", "b": "2"}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json</code> ( &lt;expression&gt; [<code>FORMAT JSON</code> [<code>ENCODING UTF8</code>]] [{ <code>WITH</code> | <code>WITHOUT</code> } <code>UNIQUE</code> [<code>KEYS</code>]] ) json</p>
<p>Converts a given expression specified as <code>text</code> or <code>bytea</code> string (in UTF8 encoding) into a JSON value. If &lt;expression&gt; is NULL, an SQL null value is returned. If <code>WITH UNIQUE</code> is specified, the &lt;expression&gt; must not contain any duplicate object keys.</p>
<p><code>json('{"a":123, "b":[true,"foo"], "a":"bar"}')</code> {"a":123, "b":[true,"foo"], "a":"bar"}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_scalar</code> ( &lt;expression&gt; )</p>
<p>Converts a given SQL scalar value into a JSON scalar value. If the input is NULL, an SQL null is returned. If the input is number or a boolean value, a corresponding JSON number or boolean value is returned. For any other value, a JSON string is returned.</p>
<p><code>json_scalar(123.45)</code> 123.45</p>
<p><code>json_scalar(CURRENT_TIMESTAMP)</code> "2022-05-10T10:51:04.62128-04:00"</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>json_serialize</code> ( &lt;expression&gt; [<code>FORMAT JSON</code> [<code>ENCODING UTF8</code>]] [<code>RETURNING</code> &lt;data_type&gt; [<code>FORMAT JSON</code> [<code>ENCODING UTF8</code>]]] )</p>
<p>Converts an SQL/JSON expression into a character or binary string. The &lt;expression&gt; can be of any JSON type, any character string type, or <code>bytea</code> in UTF8 encoding. The returned type used in <code>RETURNING</code> can be any character string type or <code>bytea</code>. The default is <code>text</code>.</p>
<p><code>json_serialize('{ "a" : 1 } ' RETURNING bytea)</code> \x7b20226122203a2031207d20</p></td>
</tr>
</tbody>
</table>
<section id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>For example, the <a href="#hstore">???</a> extension has a cast from <code>hstore</code> to <code>json</code>, so that <code>hstore</code> values converted via the JSON creation functions will be represented as JSON objects, not as primitive string values.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</section>

[SQL/JSON Testing Functions](#functions-sqljson-misc) details SQL/JSON facilities for testing JSON.

<table id="functions-sqljson-misc">
<caption>SQL/JSON Testing Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function signature</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> &lt;expression&gt; <code>IS</code> [<code>NOT</code>] <code>JSON</code> [{ <code>VALUE</code> | <code>SCALAR</code> | <code>ARRAY</code> | <code>OBJECT</code> }] [{ <code>WITH</code> | <code>WITHOUT</code> } <code>UNIQUE</code> [<code>KEYS</code>]]</p>
<p>This predicate tests whether &lt;expression&gt; can be parsed as JSON, possibly of a specified type. If <code>SCALAR</code> or <code>ARRAY</code> or <code>OBJECT</code> is specified, the test is whether or not the JSON is of that particular type. If <code>WITH UNIQUE KEYS</code> is specified, then any object in the &lt;expression&gt; is also tested to see if it has duplicate keys.</p>
<pre><code>SELECT js,
  js IS JSON &quot;json?&quot;,
  js IS JSON SCALAR &quot;scalar?&quot;,
  js IS JSON OBJECT &quot;object?&quot;,
  js IS JSON ARRAY &quot;array?&quot;
FROM (VALUES
      (&#39;123&#39;), (&#39;&quot;abc&quot;&#39;), (&#39;{&quot;a&quot;: &quot;b&quot;}&#39;), (&#39;[1,2]&#39;),(&#39;abc&#39;)) foo(js);
     js     | json? | scalar? | object? | array?
------------+-------+---------+---------+--------
 123        | t     | t       | f       | f
 &quot;abc&quot;      | t     | t       | f       | f
 {&quot;a&quot;: &quot;b&quot;} | t     | f       | t       | f
 [1,2]      | t     | f       | f       | t
 abc        | f     | f       | f       | f</code></pre>
<pre><code>SELECT js,
  js IS JSON OBJECT &quot;object?&quot;,
  js IS JSON ARRAY &quot;array?&quot;,
  js IS JSON ARRAY WITH UNIQUE KEYS &quot;array w. UK?&quot;,
  js IS JSON ARRAY WITHOUT UNIQUE KEYS &quot;array w/o UK?&quot;
FROM (VALUES (&#39;[{&quot;a&quot;:&quot;1&quot;},
 {&quot;b&quot;:&quot;2&quot;,&quot;b&quot;:&quot;3&quot;}]&#39;)) foo(js);
-[ RECORD 1 ]-+--------------------
js            | [{&quot;a&quot;:&quot;1&quot;},        +
              |  {&quot;b&quot;:&quot;2&quot;,&quot;b&quot;:&quot;3&quot;}]
object?       | f
array?        | t
array w. UK?  | f
array w/o UK? | t</code></pre></td>
</tr>
</tbody>
</table>

[JSON Processing Functions](#functions-json-processing-table) shows the functions that are available for processing `json` and `jsonb` values.

<table id="functions-json-processing-table">
<caption>JSON Processing Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_array_elements</code> ( <code>json</code> ) setof json</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_array_elements</code> ( <code>jsonb</code> ) setof jsonb</p>
<p>Expands the top-level JSON array into a set of JSON values.</p>
<p><code>select * from json_array_elements('[1,true, [2,false]]')</code></p>
<pre><code>   value
-----------
 1
 true
 [2,false]</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_array_elements_text</code> ( <code>json</code> ) setof text</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_array_elements_text</code> ( <code>jsonb</code> ) setof text</p>
<p>Expands the top-level JSON array into a set of <code>text</code> values.</p>
<p><code>select * from json_array_elements_text('["foo", "bar"]')</code></p>
<pre><code>   value
-----------
 foo
 bar</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_array_length</code> ( <code>json</code> ) integer</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_array_length</code> ( <code>jsonb</code> ) integer</p>
<p>Returns the number of elements in the top-level JSON array.</p>
<p><code>json_array_length('[1,2,3,{"f1":1,"f2":[5,6]},4]')</code> 5</p>
<p><code>jsonb_array_length('[]')</code> 0</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_each</code> ( <code>json</code> ) setof record ( <code>key</code> <code>text</code>, <code>value</code> <code>json</code> )</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_each</code> ( <code>jsonb</code> ) setof record ( <code>key</code> <code>text</code>, <code>value</code> <code>jsonb</code> )</p>
<p>Expands the top-level JSON object into a set of key/value pairs.</p>
<p><code>select * from json_each('{"a":"foo", "b":"bar"}')</code></p>
<pre><code> key | value
-----+-------
 a   | &quot;foo&quot;
 b   | &quot;bar&quot;</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_each_text</code> ( <code>json</code> ) setof record ( <code>key</code> <code>text</code>, <code>value</code> <code>text</code> )</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_each_text</code> ( <code>jsonb</code> ) setof record ( <code>key</code> <code>text</code>, <code>value</code> <code>text</code> )</p>
<p>Expands the top-level JSON object into a set of key/value pairs. The returned <code>value</code>s will be of type <code>text</code>.</p>
<p><code>select * from json_each_text('{"a":"foo", "b":"bar"}')</code></p>
<pre><code> key | value
-----+-------
 a   | foo
 b   | bar</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_extract_path</code> ( <code>from_json</code> <code>json</code>, <code>VARIADIC</code> <code>path_elems</code> <code>text[]</code> ) json</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_extract_path</code> ( <code>from_json</code> <code>jsonb</code>, <code>VARIADIC</code> <code>path_elems</code> <code>text[]</code> ) jsonb</p>
<p>Extracts JSON sub-object at the specified path. (This is functionally equivalent to the <code>#&gt;</code> operator, but writing the path out as a variadic list can be more convenient in some cases.)</p>
<p><code>json_extract_path('{"f2":{"f3":1},"f4":{"f5":99,"f6":"foo"}}', 'f4', 'f6')</code> "foo"</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_extract_path_text</code> ( <code>from_json</code> <code>json</code>, <code>VARIADIC</code> <code>path_elems</code> <code>text[]</code> ) text</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_extract_path_text</code> ( <code>from_json</code> <code>jsonb</code>, <code>VARIADIC</code> <code>path_elems</code> <code>text[]</code> ) text</p>
<p>Extracts JSON sub-object at the specified path as <code>text</code>. (This is functionally equivalent to the <code>#&gt;&gt;</code> operator.)</p>
<p><code>json_extract_path_text('{"f2":{"f3":1},"f4":{"f5":99,"f6":"foo"}}', 'f4', 'f6')</code> foo</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_object_keys</code> ( <code>json</code> ) setof text</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_object_keys</code> ( <code>jsonb</code> ) setof text</p>
<p>Returns the set of keys in the top-level JSON object.</p>
<p><code>select * from json_object_keys('{"f1":"abc","f2":{"f3":"a", "f4":"b"}}')</code></p>
<pre><code> json_object_keys
------------------
 f1
 f2</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_populate_record</code> ( <code>base</code> <code>anyelement</code>, <code>from_json</code> <code>json</code> ) anyelement</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_populate_record</code> ( <code>base</code> <code>anyelement</code>, <code>from_json</code> <code>jsonb</code> ) anyelement</p>
<p>Expands the top-level JSON object to a row having the composite type of the <code>base</code> argument. The JSON object is scanned for fields whose names match column names of the output row type, and their values are inserted into those columns of the output. (Fields that do not correspond to any output column name are ignored.) In typical use, the value of <code>base</code> is just <code>NULL</code>, which means that any output columns that do not match any object field will be filled with nulls. However, if <code>base</code> isn't <code>NULL</code> then the values it contains will be used for unmatched columns.</p>
<p>To convert a JSON value to the SQL type of an output column, the following rules are applied in sequence:</p>
<ul>
<li>A JSON null value is converted to an SQL null in all cases.</li>
<li>If the output column is of type <code>json</code> or <code>jsonb</code>, the JSON value is just reproduced exactly.</li>
<li>If the output column is a composite (row) type, and the JSON value is a JSON object, the fields of the object are converted to columns of the output row type by recursive application of these rules.</li>
<li>Likewise, if the output column is an array type and the JSON value is a JSON array, the elements of the JSON array are converted to elements of the output array by recursive application of these rules.</li>
<li>Otherwise, if the JSON value is a string, the contents of the string are fed to the input conversion function for the column's data type.</li>
<li>Otherwise, the ordinary text representation of the JSON value is fed to the input conversion function for the column's data type.</li>
</ul>
<p>While the example below uses a constant JSON value, typical use would be to reference a <code>json</code> or <code>jsonb</code> column laterally from another table in the query's <code>FROM</code> clause. Writing <code>json_populate_record</code> in the <code>FROM</code> clause is good practice, since all of the extracted columns are available for use without duplicate function calls.</p>
<p><code>create type subrowtype as (d int, e text);</code> <code>create type myrowtype as (a int, b text[], c subrowtype);</code></p>
<p><code>select * from json_populate_record(null::myrowtype, '{"a": 1, "b": ["2", "a b"], "c": {"d": 4, "e": "a b c"}, "x": "foo"}')</code></p>
<pre><code> a |   b       |      c
---+-----------+-------------
 1 | {2,&quot;a b&quot;} | (4,&quot;a b c&quot;)</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>jsonb_populate_record_valid</code> ( <code>base</code> <code>anyelement</code>, <code>from_json</code> <code>json</code> ) boolean</p>
<p>Function for testing <code>jsonb_populate_record</code>. Returns <code>true</code> if the input <code>jsonb_populate_record</code> would finish without an error for the given input JSON object; that is, it's valid input, <code>false</code> otherwise.</p>
<p><code>create type jsb_char2 as (a char(2));</code></p>
<p><code>select jsonb_populate_record_valid(NULL::jsb_char2, '{"a": "aaa"}');</code></p>
<pre><code> jsonb_populate_record_valid
-----------------------------
 f
(1 row)</code></pre>
<p><code>select * from jsonb_populate_record(NULL::jsb_char2, '{"a": "aaa"}') q;</code></p>
<pre><code>ERROR:  value too long for type character(2)</code></pre>
<p><code>select jsonb_populate_record_valid(NULL::jsb_char2, '{"a": "aa"}');</code></p>
<pre><code> jsonb_populate_record_valid
-----------------------------
 t
(1 row)</code></pre>
<p><code>select * from jsonb_populate_record(NULL::jsb_char2, '{"a": "aa"}') q;</code></p>
<pre><code> a
----
 aa
(1 row)</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_populate_recordset</code> ( <code>base</code> <code>anyelement</code>, <code>from_json</code> <code>json</code> ) setof anyelement</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_populate_recordset</code> ( <code>base</code> <code>anyelement</code>, <code>from_json</code> <code>jsonb</code> ) setof anyelement</p>
<p>Expands the top-level JSON array of objects to a set of rows having the composite type of the <code>base</code> argument. Each element of the JSON array is processed as described above for <code>json[b]_populate_record</code>.</p>
<p><code>create type twoints as (a int, b int);</code></p>
<p><code>select * from json_populate_recordset(null::twoints, '[{"a":1,"b":2}, {"a":3,"b":4}]')</code></p>
<pre><code> a | b
---+---
 1 | 2
 3 | 4</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_to_record</code> ( <code>json</code> ) record</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_to_record</code> ( <code>jsonb</code> ) record</p>
<p>Expands the top-level JSON object to a row having the composite type defined by an <code>AS</code> clause. (As with all functions returning <code>record</code>, the calling query must explicitly define the structure of the record with an <code>AS</code> clause.) The output record is filled from fields of the JSON object, in the same way as described above for <code>json[b]_populate_record</code>. Since there is no input record value, unmatched columns are always filled with nulls.</p>
<p><code>create type myrowtype as (a int, b text);</code></p>
<p><code>select * from json_to_record('{"a":1,"b":[1,2,3],"c":[1,2,3],"e":"bar","r": {"a": 123, "b": "a b c"}}') as x(a int, b text, c int[], d text, r myrowtype)</code></p>
<pre><code> a |    b    |    c    | d |       r
---+---------+---------+---+---------------
 1 | [1,2,3] | {1,2,3} |   | (123,&quot;a b c&quot;)</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_to_recordset</code> ( <code>json</code> ) setof record</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_to_recordset</code> ( <code>jsonb</code> ) setof record</p>
<p>Expands the top-level JSON array of objects to a set of rows having the composite type defined by an <code>AS</code> clause. (As with all functions returning <code>record</code>, the calling query must explicitly define the structure of the record with an <code>AS</code> clause.) Each element of the JSON array is processed as described above for <code>json[b]_populate_record</code>.</p>
<p><code>select * from json_to_recordset('[{"a":1,"b":"foo"}, {"a":"2","c":"bar"}]') as x(a int, b text)</code></p>
<pre><code> a |  b
---+-----
 1 | foo
 2 |</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>jsonb_set</code> ( <code>target</code> <code>jsonb</code>, <code>path</code> <code>text[]</code>, <code>new_value</code> <code>jsonb</code> [, <code>create_if_missing</code> <code>boolean</code>] ) jsonb</p>
<p>Returns <code>target</code> with the item designated by <code>path</code> replaced by <code>new_value</code>, or with <code>new_value</code> added if <code>create_if_missing</code> is true (which is the default) and the item designated by <code>path</code> does not exist. All earlier steps in the path must exist, or the <code>target</code> is returned unchanged. As with the path oriented operators, negative integers that appear in the <code>path</code> count from the end of JSON arrays. If the last path step is an array index that is out of range, and <code>create_if_missing</code> is true, the new value is added at the beginning of the array if the index is negative, or at the end of the array if it is positive.</p>
<p><code>jsonb_set('[{"f1":1,"f2":null},2,null,3]', '{0,f1}', '[2,3,4]', false)</code> [{"f1": [2, 3, 4], "f2": null}, 2, null, 3]</p>
<p><code>jsonb_set('[{"f1":1,"f2":null},2]', '{0,f3}', '[2,3,4]')</code> [{"f1": 1, "f2": null, "f3": [2, 3, 4]}, 2]</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>jsonb_set_lax</code> ( <code>target</code> <code>jsonb</code>, <code>path</code> <code>text[]</code>, <code>new_value</code> <code>jsonb</code> [, <code>create_if_missing</code> <code>boolean</code> [, <code>null_value_treatment</code> <code>text</code>]] ) jsonb</p>
<p>If <code>new_value</code> is not <code>NULL</code>, behaves identically to <code>jsonb_set</code>. Otherwise behaves according to the value of <code>null_value_treatment</code> which must be one of <code>'raise_exception'</code>, <code>'use_json_null'</code>, <code>'delete_key'</code>, or <code>'return_target'</code>. The default is <code>'use_json_null'</code>.</p>
<p><code>jsonb_set_lax('[{"f1":1,"f2":null},2,null,3]', '{0,f1}', null)</code> [{"f1": null, "f2": null}, 2, null, 3]</p>
<p><code>jsonb_set_lax('[{"f1":99,"f2":null},2]', '{0,f3}', null, true, 'return_target')</code> [{"f1": 99, "f2": null}, 2]</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>jsonb_insert</code> ( <code>target</code> <code>jsonb</code>, <code>path</code> <code>text[]</code>, <code>new_value</code> <code>jsonb</code> [, <code>insert_after</code> <code>boolean</code>] ) jsonb</p>
<p>Returns <code>target</code> with <code>new_value</code> inserted. If the item designated by the <code>path</code> is an array element, <code>new_value</code> will be inserted before that item if <code>insert_after</code> is false (which is the default), or after it if <code>insert_after</code> is true. If the item designated by the <code>path</code> is an object field, <code>new_value</code> will be inserted only if the object does not already contain that key. All earlier steps in the path must exist, or the <code>target</code> is returned unchanged. As with the path oriented operators, negative integers that appear in the <code>path</code> count from the end of JSON arrays. If the last path step is an array index that is out of range, the new value is added at the beginning of the array if the index is negative, or at the end of the array if it is positive.</p>
<p><code>jsonb_insert('{"a": [0,1,2]}', '{a, 1}', '"new_value"')</code> {"a": [0, "new_value", 1, 2]}</p>
<p><code>jsonb_insert('{"a": [0,1,2]}', '{a, 1}', '"new_value"', true)</code> {"a": [0, 1, "new_value", 2]}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_strip_nulls</code> ( <code>json</code> ) json</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_strip_nulls</code> ( <code>jsonb</code> ) jsonb</p>
<p>Deletes all object fields that have null values from the given JSON value, recursively. Null values that are not object fields are untouched.</p>
<p><code>json_strip_nulls('[{"f1":1, "f2":null}, 2, null, 3]')</code> [{"f1":1},2,null,3]</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>jsonb_path_exists</code> ( <code>target</code> <code>jsonb</code>, <code>path</code> <code>jsonpath</code> [, <code>vars</code> <code>jsonb</code> [, <code>silent</code> <code>boolean</code>]] ) boolean</p>
<p>Checks whether the JSON path returns any item for the specified JSON value. (This is useful only with SQL-standard JSON path expressions, not <a href="#functions-sqljson-check-expressions">predicate check expressions</a>, since those always return a value.) If the <code>vars</code> argument is specified, it must be a JSON object, and its fields provide named values to be substituted into the <code>jsonpath</code> expression. If the <code>silent</code> argument is specified and is <code>true</code>, the function suppresses the same errors as the <code>@?</code> and <code>@@</code> operators do.</p>
<p><code>jsonb_path_exists('{"a":[1,2,3,4,5]}', '$.a[*] ? (@ &gt;= $min &amp;&amp; @ &lt;= $max)', '{"min":2, "max":4}')</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>jsonb_path_match</code> ( <code>target</code> <code>jsonb</code>, <code>path</code> <code>jsonpath</code> [, <code>vars</code> <code>jsonb</code> [, <code>silent</code> <code>boolean</code>]] ) boolean</p>
<p>Returns the SQL boolean result of a JSON path predicate check for the specified JSON value. (This is useful only with <a href="#functions-sqljson-check-expressions">predicate check expressions</a>, not SQL-standard JSON path expressions, since it will either fail or return <code>NULL</code> if the path result is not a single boolean value.) The optional <code>vars</code> and <code>silent</code> arguments act the same as for <code>jsonb_path_exists</code>.</p>
<p><code>jsonb_path_match('{"a":[1,2,3,4,5]}', 'exists($.a[*] ? (@ &gt;= $min &amp;&amp; @ &lt;= $max))', '{"min":2, "max":4}')</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>jsonb_path_query</code> ( <code>target</code> <code>jsonb</code>, <code>path</code> <code>jsonpath</code> [, <code>vars</code> <code>jsonb</code> [, <code>silent</code> <code>boolean</code>]] ) setof jsonb</p>
<p>Returns all JSON items returned by the JSON path for the specified JSON value. For SQL-standard JSON path expressions it returns the JSON values selected from <code>target</code>. For <a href="#functions-sqljson-check-expressions">predicate check expressions</a> it returns the result of the predicate check: <code>true</code>, <code>false</code>, or <code>null</code>. The optional <code>vars</code> and <code>silent</code> arguments act the same as for <code>jsonb_path_exists</code>.</p>
<p><code>select * from jsonb_path_query('{"a":[1,2,3,4,5]}', '$.a[*] ? (@ &gt;= $min &amp;&amp; @ &lt;= $max)', '{"min":2, "max":4}')</code></p>
<pre><code> jsonb_path_query
------------------
 2
 3
 4</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>jsonb_path_query_array</code> ( <code>target</code> <code>jsonb</code>, <code>path</code> <code>jsonpath</code> [, <code>vars</code> <code>jsonb</code> [, <code>silent</code> <code>boolean</code>]] ) jsonb</p>
<p>Returns all JSON items returned by the JSON path for the specified JSON value, as a JSON array. The parameters are the same as for <code>jsonb_path_query</code>.</p>
<p><code>jsonb_path_query_array('{"a":[1,2,3,4,5]}', '$.a[*] ? (@ &gt;= $min &amp;&amp; @ &lt;= $max)', '{"min":2, "max":4}')</code> [2, 3, 4]</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>jsonb_path_query_first</code> ( <code>target</code> <code>jsonb</code>, <code>path</code> <code>jsonpath</code> [, <code>vars</code> <code>jsonb</code> [, <code>silent</code> <code>boolean</code>]] ) jsonb</p>
<p>Returns the first JSON item returned by the JSON path for the specified JSON value, or <code>NULL</code> if there are no results. The parameters are the same as for <code>jsonb_path_query</code>.</p>
<p><code>jsonb_path_query_first('{"a":[1,2,3,4,5]}', '$.a[*] ? (@ &gt;= $min &amp;&amp; @ &lt;= $max)', '{"min":2, "max":4}')</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>jsonb_path_exists_tz</code> ( <code>target</code> <code>jsonb</code>, <code>path</code> <code>jsonpath</code> [, <code>vars</code> <code>jsonb</code> [, <code>silent</code> <code>boolean</code>]] ) boolean</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_path_match_tz</code> ( <code>target</code> <code>jsonb</code>, <code>path</code> <code>jsonpath</code> [, <code>vars</code> <code>jsonb</code> [, <code>silent</code> <code>boolean</code>]] ) boolean</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_path_query_tz</code> ( <code>target</code> <code>jsonb</code>, <code>path</code> <code>jsonpath</code> [, <code>vars</code> <code>jsonb</code> [, <code>silent</code> <code>boolean</code>]] ) setof jsonb</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_path_query_array_tz</code> ( <code>target</code> <code>jsonb</code>, <code>path</code> <code>jsonpath</code> [, <code>vars</code> <code>jsonb</code> [, <code>silent</code> <code>boolean</code>]] ) jsonb</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_path_query_first_tz</code> ( <code>target</code> <code>jsonb</code>, <code>path</code> <code>jsonpath</code> [, <code>vars</code> <code>jsonb</code> [, <code>silent</code> <code>boolean</code>]] ) jsonb</p>
<p>These functions act like their counterparts described above without the <code>_tz</code> suffix, except that these functions support comparisons of date/time values that require timezone-aware conversions. The example below requires interpretation of the date-only value <code>2015-08-02</code> as a timestamp with time zone, so the result depends on the current <a href="#guc-timezone">???</a> setting. Due to this dependency, these functions are marked as stable, which means these functions cannot be used in indexes. Their counterparts are immutable, and so can be used in indexes; but they will throw errors if asked to make such comparisons.</p>
<p><code>jsonb_path_exists_tz('["2015-08-01 12:00:00-05"]', '$[*] ? (@.datetime() &lt; "2015-08-02".datetime())')</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>jsonb_pretty</code> ( <code>jsonb</code> ) text</p>
<p>Converts the given JSON value to pretty-printed, indented text.</p>
<p><code>jsonb_pretty('[{"f1":1,"f2":null}, 2]')</code></p>
<pre><code>[
    {
        &quot;f1&quot;: 1,
        &quot;f2&quot;: null
    },
    2
]</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_typeof</code> ( <code>json</code> ) text</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_typeof</code> ( <code>jsonb</code> ) text</p>
<p>Returns the type of the top-level JSON value as a text string. Possible types are <code>object</code>, <code>array</code>, <code>string</code>, <code>number</code>, <code>boolean</code>, and <code>null</code>. (The <code>null</code> result should not be confused with an SQL NULL; see the examples.)</p>
<p><code>json_typeof('-123.4')</code> number</p>
<p><code>json_typeof('null'::json)</code> null</p>
<p><code>json_typeof(NULL::json) IS NULL</code> t</p></td>
</tr>
</tbody>
</table>

### The SQL/JSON Path Language

SQL/JSON path language

SQL/JSON path expressions specify item(s) to be retrieved from a JSON value, similarly to XPath expressions used for access to XML content. In PostgreSQL, path expressions are implemented as the `jsonpath` data type and can use any elements described in [???](#datatype-jsonpath).

JSON query functions and operators pass the provided path expression to the path engine for evaluation. If the expression matches the queried JSON data, the corresponding JSON item, or set of items, is returned. If there is no match, the result will be `NULL`, `false`, or an error, depending on the function. Path expressions are written in the SQL/JSON path language and can include arithmetic expressions and functions.

A path expression consists of a sequence of elements allowed by the `jsonpath` data type. The path expression is normally evaluated from left to right, but you can use parentheses to change the order of operations. If the evaluation is successful, a sequence of JSON items is produced, and the evaluation result is returned to the JSON query function that completes the specified computation.

To refer to the JSON value being queried (the context item), use the `$` variable in the path expression. The first element of a path must always be `$`. It can be followed by one or more [accessor operators](#type-jsonpath-accessors), which go down the JSON structure level by level to retrieve sub-items of the context item. Each accessor operator acts on the result(s) of the previous evaluation step, producing zero, one, or more output items from each input item.

For example, suppose you have some JSON data from a GPS tracker that you would like to parse, such as:

    SELECT '{
      "track": {
        "segments": [
          {
            "location":   [ 47.763, 13.4034 ],
            "start time": "2018-10-14 10:05:14",
            "HR": 73
          },
          {
            "location":   [ 47.706, 13.2635 ],
            "start time": "2018-10-14 10:39:21",
            "HR": 135
          }
        ]
      }
    }' AS json \gset

(The above example can be copied-and-pasted into psql to set things up for the following examples. Then psql will expand `:'json'` into a suitably-quoted string constant containing the JSON value.)

To retrieve the available track segments, you need to use the `.key` accessor operator to descend through surrounding JSON objects, for example:

    => select jsonb_path_query(:'json', '$.track.segments');
                                                                             jsonb_path_query
    -----------------------------------------------------------​-----------------------------------------------------------​---------------------------------------------
     [{"HR": 73, "location": [47.763, 13.4034], "start time": "2018-10-14 10:05:14"}, {"HR": 135, "location": [47.706, 13.2635], "start time": "2018-10-14 10:39:21"}]

To retrieve the contents of an array, you typically use the `[*]` operator. The following example will return the location coordinates for all the available track segments:

    => select jsonb_path_query(:'json', '$.track.segments[*].location');
     jsonb_path_query
    -------------------
     [47.763, 13.4034]
     [47.706, 13.2635]

Here we started with the whole JSON input value (`$`), then the `.track` accessor selected the JSON object associated with the `"track"` object key, then the `.segments` accessor selected the JSON array associated with the `"segments"` key within that object, then the `[*]` accessor selected each element of that array (producing a series of items), then the `.location` accessor selected the JSON array associated with the `"location"` key within each of those objects. In this example, each of those objects had a `"location"` key; but if any of them did not, the `.location` accessor would have simply produced no output for that input item.

To return the coordinates of the first segment only, you can specify the corresponding subscript in the `[]` accessor operator. Recall that JSON array indexes are 0-relative:

    => select jsonb_path_query(:'json', '$.track.segments[0].location');
     jsonb_path_query
    -------------------
     [47.763, 13.4034]

The result of each path evaluation step can be processed by one or more of the `jsonpath` operators and methods listed in [SQL/JSON Path Operators and Methods](#functions-sqljson-path-operators). Each method name must be preceded by a dot. For example, you can get the size of an array:

    => select jsonb_path_query(:'json', '$.track.segments.size()');
     jsonb_path_query
    ------------------
     2

More examples of using `jsonpath` operators and methods within path expressions appear below in [SQL/JSON Path Operators and Methods](#functions-sqljson-path-operators).

A path can also contain filter expressions that work similarly to the `WHERE` clause in SQL. A filter expression begins with a question mark and provides a condition in parentheses: ? (\<condition\>)

Filter expressions must be written just after the path evaluation step to which they should apply. The result of that step is filtered to include only those items that satisfy the provided condition. SQL/JSON defines three-valued logic, so the condition can produce `true`, `false`, or `unknown`. The `unknown` value plays the same role as SQL `NULL` and can be tested for with the `is unknown` predicate. Further path evaluation steps use only those items for which the filter expression returned `true`.

The functions and operators that can be used in filter expressions are listed in [ Filter Expression Elements](#functions-sqljson-filter-ex-table). Within a filter expression, the `@` variable denotes the value being considered (i.e., one result of the preceding path step). You can write accessor operators after `@` to retrieve component items.

For example, suppose you would like to retrieve all heart rate values higher than 130. You can achieve this as follows:

    => select jsonb_path_query(:'json', '$.track.segments[*].HR ? (@ > 130)');
     jsonb_path_query
    ------------------
     135

To get the start times of segments with such values, you have to filter out irrelevant segments before selecting the start times, so the filter expression is applied to the previous step, and the path used in the condition is different:

    => select jsonb_path_query(:'json', '$.track.segments[*] ? (@.HR > 130)."start time"');
       jsonb_path_query
    -----------------------
     "2018-10-14 10:39:21"

You can use several filter expressions in sequence, if required. The following example selects start times of all segments that contain locations with relevant coordinates and high heart rate values:

    => select jsonb_path_query(:'json', '$.track.segments[*] ? (@.location[1] < 13.4) ? (@.HR > 130)."start time"');
       jsonb_path_query
    -----------------------
     "2018-10-14 10:39:21"

Using filter expressions at different nesting levels is also allowed. The following example first filters all segments by location, and then returns high heart rate values for these segments, if available:

    => select jsonb_path_query(:'json', '$.track.segments[*] ? (@.location[1] < 13.4).HR ? (@ > 130)');
     jsonb_path_query
    ------------------
     135

You can also nest filter expressions within each other. This example returns the size of the track if it contains any segments with high heart rate values, or an empty sequence otherwise:

    => select jsonb_path_query(:'json', '$.track ? (exists(@.segments[*] ? (@.HR > 130))).segments.size()');
     jsonb_path_query
    ------------------
     2

#### Deviations from the SQL Standard

PostgreSQL's implementation of the SQL/JSON path language has the following deviations from the SQL/JSON standard.

##### Boolean Predicate Check Expressions

As an extension to the SQL standard, a PostgreSQL path expression can be a Boolean predicate, whereas the SQL standard allows predicates only within filters. While SQL-standard path expressions return the relevant element(s) of the queried JSON value, predicate check expressions return the single three-valued `jsonb` result of the predicate: `true`, `false`, or `null`. For example, we could write this SQL-standard filter expression:

    => select jsonb_path_query(:'json', '$.track.segments ?(@[*].HR > 130)');
                                    jsonb_path_query
    -----------------------------------------------------------​----------------------
     {"HR": 135, "location": [47.706, 13.2635], "start time": "2018-10-14 10:39:21"}

The similar predicate check expression simply returns `true`, indicating that a match exists:

    => select jsonb_path_query(:'json', '$.track.segments[*].HR > 130');
     jsonb_path_query
    ------------------
     true

> [!NOTE]
> Predicate check expressions are required in the `@@` operator (and the `jsonb_path_match` function), and should not be used with the `@?` operator (or the `jsonb_path_exists` function).

##### Regular Expression Interpretation

There are minor differences in the interpretation of regular expression patterns used in `like_regex` filters, as described in [SQL/JSON Regular Expressions](#jsonpath-regular-expressions).

#### Strict and Lax Modes

When you query JSON data, the path expression may not match the actual JSON data structure. An attempt to access a non-existent member of an object or element of an array is defined as a structural error. SQL/JSON path expressions have two modes of handling structural errors:

- lax (default) the path engine implicitly adapts the queried data to the specified path. Any structural errors that cannot be fixed as described below are suppressed, producing no match.

- strict if a structural error occurs, an error is raised.

Lax mode facilitates matching of a JSON document and path expression when the JSON data does not conform to the expected schema. If an operand does not match the requirements of a particular operation, it can be automatically wrapped as an SQL/JSON array, or unwrapped by converting its elements into an SQL/JSON sequence before performing the operation. Also, comparison operators automatically unwrap their operands in lax mode, so you can compare SQL/JSON arrays out-of-the-box. An array of size 1 is considered equal to its sole element. Automatic unwrapping is not performed when:

- The path expression contains `type()` or `size()` methods that return the type and the number of elements in the array, respectively.

- The queried JSON data contain nested arrays. In this case, only the outermost array is unwrapped, while all the inner arrays remain unchanged. Thus, implicit unwrapping can only go one level down within each path evaluation step.

For example, when querying the GPS data listed above, you can abstract from the fact that it stores an array of segments when using lax mode:

    => select jsonb_path_query(:'json', 'lax $.track.segments.location');
     jsonb_path_query
    -------------------
     [47.763, 13.4034]
     [47.706, 13.2635]

In strict mode, the specified path must exactly match the structure of the queried JSON document, so using this path expression will cause an error:

    => select jsonb_path_query(:'json', 'strict $.track.segments.location');
    ERROR:  jsonpath member accessor can only be applied to an object

To get the same result as in lax mode, you have to explicitly unwrap the `segments` array:

    => select jsonb_path_query(:'json', 'strict $.track.segments[*].location');
     jsonb_path_query
    -------------------
     [47.763, 13.4034]
     [47.706, 13.2635]

The unwrapping behavior of lax mode can lead to surprising results. For instance, the following query using the `.**` accessor selects every `HR` value twice:

    => select jsonb_path_query(:'json', 'lax $.**.HR');
     jsonb_path_query
    ------------------
     73
     135
     73
     135

This happens because the `.**` accessor selects both the `segments` array and each of its elements, while the `.HR` accessor automatically unwraps arrays when using lax mode. To avoid surprising results, we recommend using the `.**` accessor only in strict mode. The following query selects each `HR` value just once:

    => select jsonb_path_query(:'json', 'strict $.**.HR');
     jsonb_path_query
    ------------------
     73
     135

The unwrapping of arrays can also lead to unexpected results. Consider this example, which selects all the `location` arrays:

    => select jsonb_path_query(:'json', 'lax $.track.segments[*].location');
     jsonb_path_query
    -------------------
     [47.763, 13.4034]
     [47.706, 13.2635]
    (2 rows)

As expected it returns the full arrays. But applying a filter expression causes the arrays to be unwrapped to evaluate each item, returning only the items that match the expression:

    => select jsonb_path_query(:'json', 'lax $.track.segments[*].location ?(@[*] > 15)');
     jsonb_path_query
    ------------------
     47.763
     47.706
    (2 rows)

This despite the fact that the full arrays are selected by the path expression. Use strict mode to restore selecting the arrays:

    => select jsonb_path_query(:'json', 'strict $.track.segments[*].location ?(@[*] > 15)');
     jsonb_path_query
    -------------------
     [47.763, 13.4034]
     [47.706, 13.2635]
    (2 rows)

#### SQL/JSON Path Operators and Methods

[ Operators and Methods](#functions-sqljson-op-table) shows the operators and methods available in `jsonpath`. Note that while the unary operators and methods can be applied to multiple values resulting from a preceding path step, the binary operators (addition etc.) can only be applied to single values. In lax mode, methods applied to an array will be executed for each value in the array. The exceptions are `.type()` and `.size()`, which apply to the array itself.

<table id="functions-sqljson-op-table">
<caption><code>jsonpath</code> Operators and Methods</caption>
<thead>
<tr>
<th><p role="func_signature">Operator/Method</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature">&lt;number&gt; <code>+</code> &lt;number&gt; &lt;number&gt;</p>
<p>Addition</p>
<p><code>jsonb_path_query('[2]', '$[0] + 3')</code> 5</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>+</code> &lt;number&gt; &lt;number&gt;</p>
<p>Unary plus (no operation); unlike addition, this can iterate over multiple values</p>
<p><code>jsonb_path_query_array('{"x": [2,3,4]}', '+ $.x')</code> [2, 3, 4]</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;number&gt; <code>-</code> &lt;number&gt; &lt;number&gt;</p>
<p>Subtraction</p>
<p><code>jsonb_path_query('[2]', '7 - $[0]')</code> 5</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>-</code> &lt;number&gt; &lt;number&gt;</p>
<p>Negation; unlike subtraction, this can iterate over multiple values</p>
<p><code>jsonb_path_query_array('{"x": [2,3,4]}', '- $.x')</code> [-2, -3, -4]</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;number&gt; <code>*</code> &lt;number&gt; &lt;number&gt;</p>
<p>Multiplication</p>
<p><code>jsonb_path_query('[4]', '2 * $[0]')</code> 8</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;number&gt; <code>/</code> &lt;number&gt; &lt;number&gt;</p>
<p>Division</p>
<p><code>jsonb_path_query('[8.5]', '$[0] / 2')</code> 4.2500000000000000</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;number&gt; <code>%</code> &lt;number&gt; &lt;number&gt;</p>
<p>Modulo (remainder)</p>
<p><code>jsonb_path_query('[32]', '$[0] % 10')</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>.</code> <code>type()</code> &lt;string&gt;</p>
<p>Type of the JSON item (see <code>json_typeof</code>)</p>
<p><code>jsonb_path_query_array('[1, "2", {}]', '$[*].type()')</code> ["number", "string", "object"]</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>.</code> <code>size()</code> &lt;number&gt;</p>
<p>Size of the JSON item (number of array elements, or 1 if not an array)</p>
<p><code>jsonb_path_query('{"m": [11, 15]}', '$.m.size()')</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>.</code> <code>boolean()</code> &lt;boolean&gt;</p>
<p>Boolean value converted from a JSON boolean, number, or string</p>
<p><code>jsonb_path_query_array('[1, "yes", false]', '$[*].boolean()')</code> [true, true, false]</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>.</code> <code>string()</code> &lt;string&gt;</p>
<p>String value converted from a JSON boolean, number, string, or datetime</p>
<p><code>jsonb_path_query_array('[1.23, "xyz", false]', '$[*].string()')</code> ["1.23", "xyz", "false"]</p>
<p><code>jsonb_path_query('"2023-08-15 12:34:56"', '$.timestamp().string()')</code> "2023-08-15T12:34:56"</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>.</code> <code>double()</code> &lt;number&gt;</p>
<p>Approximate floating-point number converted from a JSON number or string</p>
<p><code>jsonb_path_query('{"len": "1.9"}', '$.len.double() * 2')</code> 3.8</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;number&gt; <code>.</code> <code>ceiling()</code> &lt;number&gt;</p>
<p>Nearest integer greater than or equal to the given number</p>
<p><code>jsonb_path_query('{"h": 1.3}', '$.h.ceiling()')</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;number&gt; <code>.</code> <code>floor()</code> &lt;number&gt;</p>
<p>Nearest integer less than or equal to the given number</p>
<p><code>jsonb_path_query('{"h": 1.7}', '$.h.floor()')</code> 1</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;number&gt; <code>.</code> <code>abs()</code> &lt;number&gt;</p>
<p>Absolute value of the given number</p>
<p><code>jsonb_path_query('{"z": -0.3}', '$.z.abs()')</code> 0.3</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>.</code> <code>bigint()</code> &lt;bigint&gt;</p>
<p>Big integer value converted from a JSON number or string</p>
<p><code>jsonb_path_query('{"len": "9876543219"}', '$.len.bigint()')</code> 9876543219</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>.</code> <code>decimal( [ precision [ , scale ] ] )</code> &lt;decimal&gt;</p>
<p>Rounded decimal value converted from a JSON number or string (<code>precision</code> and <code>scale</code> must be integer values)</p>
<p><code>jsonb_path_query('1234.5678', '$.decimal(6, 2)')</code> 1234.57</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>.</code> <code>integer()</code> &lt;integer&gt;</p>
<p>Integer value converted from a JSON number or string</p>
<p><code>jsonb_path_query('{"len": "12345"}', '$.len.integer()')</code> 12345</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>.</code> <code>number()</code> &lt;numeric&gt;</p>
<p>Numeric value converted from a JSON number or string</p>
<p><code>jsonb_path_query('{"len": "123.45"}', '$.len.number()')</code> 123.45</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;string&gt; <code>.</code> <code>datetime()</code> &lt;datetime_type&gt; (see note)</p>
<p>Date/time value converted from a string</p>
<p><code>jsonb_path_query('["2015-8-1", "2015-08-12"]', '$[*] ? (@.datetime() &lt; "2015-08-2".datetime())')</code> "2015-8-1"</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;string&gt; <code>.</code> <code>datetime(template)</code> &lt;datetime_type&gt; (see note)</p>
<p>Date/time value converted from a string using the specified <code>to_timestamp</code> template</p>
<p><code>jsonb_path_query_array('["12:30", "18:40"]', '$[*].datetime("HH24:MI")')</code> ["12:30:00", "18:40:00"]</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;string&gt; <code>.</code> <code>date()</code> &lt;date&gt;</p>
<p>Date value converted from a string</p>
<p><code>jsonb_path_query('"2023-08-15"', '$.date()')</code> "2023-08-15"</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;string&gt; <code>.</code> <code>time()</code> &lt;time without time zone&gt;</p>
<p>Time without time zone value converted from a string</p>
<p><code>jsonb_path_query('"12:34:56"', '$.time()')</code> "12:34:56"</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;string&gt; <code>.</code> <code>time(precision)</code> &lt;time without time zone&gt;</p>
<p>Time without time zone value converted from a string, with fractional seconds adjusted to the given precision</p>
<p><code>jsonb_path_query('"12:34:56.789"', '$.time(2)')</code> "12:34:56.79"</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;string&gt; <code>.</code> <code>time_tz()</code> &lt;time with time zone&gt;</p>
<p>Time with time zone value converted from a string</p>
<p><code>jsonb_path_query('"12:34:56 +05:30"', '$.time_tz()')</code> "12:34:56+05:30"</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;string&gt; <code>.</code> <code>time_tz(precision)</code> &lt;time with time zone&gt;</p>
<p>Time with time zone value converted from a string, with fractional seconds adjusted to the given precision</p>
<p><code>jsonb_path_query('"12:34:56.789 +05:30"', '$.time_tz(2)')</code> "12:34:56.79+05:30"</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;string&gt; <code>.</code> <code>timestamp()</code> &lt;timestamp without time zone&gt;</p>
<p>Timestamp without time zone value converted from a string</p>
<p><code>jsonb_path_query('"2023-08-15 12:34:56"', '$.timestamp()')</code> "2023-08-15T12:34:56"</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;string&gt; <code>.</code> <code>timestamp(precision)</code> &lt;timestamp without time zone&gt;</p>
<p>Timestamp without time zone value converted from a string, with fractional seconds adjusted to the given precision</p>
<p><code>jsonb_path_query('"2023-08-15 12:34:56.789"', '$.timestamp(2)')</code> "2023-08-15T12:34:56.79"</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;string&gt; <code>.</code> <code>timestamp_tz()</code> &lt;timestamp with time zone&gt;</p>
<p>Timestamp with time zone value converted from a string</p>
<p><code>jsonb_path_query('"2023-08-15 12:34:56 +05:30"', '$.timestamp_tz()')</code> "2023-08-15T12:34:56+05:30"</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;string&gt; <code>.</code> <code>timestamp_tz(precision)</code> &lt;timestamp with time zone&gt;</p>
<p>Timestamp with time zone value converted from a string, with fractional seconds adjusted to the given precision</p>
<p><code>jsonb_path_query('"2023-08-15 12:34:56.789 +05:30"', '$.timestamp_tz(2)')</code> "2023-08-15T12:34:56.79+05:30"</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;object&gt; <code>.</code> <code>keyvalue()</code> &lt;array&gt;</p>
<p>The object's key-value pairs, represented as an array of objects containing three fields: <code>"key"</code>, <code>"value"</code>, and <code>"id"</code>; <code>"id"</code> is a unique identifier of the object the key-value pair belongs to</p>
<p><code>jsonb_path_query_array('{"x": "20", "y": 32}', '$.keyvalue()')</code> [{"id": 0, "key": "x", "value": "20"}, {"id": 0, "key": "y", "value": 32}]</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> The result type of the `datetime()` and `datetime(template)` methods can be `date`, `timetz`, `time`, `timestamptz`, or `timestamp`. Both methods determine their result type dynamically.
>
> The `datetime()` method sequentially tries to match its input string to the ISO formats for `date`, `timetz`, `time`, `timestamptz`, and `timestamp`. It stops on the first matching format and emits the corresponding data type.
>
> The `datetime(template)` method determines the result type according to the fields used in the provided template string.
>
> The `datetime()` and `datetime(template)` methods use the same parsing rules as the `to_timestamp` SQL function does (see [Data Type Formatting Functions](#functions-formatting)), with three exceptions. First, these methods don't allow unmatched template patterns. Second, only the following separators are allowed in the template string: minus sign, period, solidus (slash), comma, apostrophe, semicolon, colon and space. Third, separators in the template string must exactly match the input string.
>
> If different date/time types need to be compared, an implicit cast is applied. A `date` value can be cast to `timestamp` or `timestamptz`, `timestamp` can be cast to `timestamptz`, and `time` to `timetz`. However, all but the first of these conversions depend on the current [???](#guc-timezone) setting, and thus can only be performed within timezone-aware `jsonpath` functions. Similarly, other date/time-related methods that convert strings to date/time types also do this casting, which may involve the current [???](#guc-timezone) setting. Therefore, these conversions can also only be performed within timezone-aware `jsonpath` functions.

[ Filter Expression Elements](#functions-sqljson-filter-ex-table) shows the available filter expression elements.

<table id="functions-sqljson-filter-ex-table">
<caption><code>jsonpath</code> Filter Expression Elements</caption>
<thead>
<tr>
<th><p role="func_signature">Predicate/Value</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>==</code> &lt;value&gt; boolean</p>
<p>Equality comparison (this, and the other comparison operators, work on all JSON scalar values)</p>
<p><code>jsonb_path_query_array('[1, "a", 1, 3]', '$[*] ? (@ == 1)')</code> [1, 1]</p>
<p><code>jsonb_path_query_array('[1, "a", 1, 3]', '$[*] ? (@ == "a")')</code> ["a"]</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>!=</code> &lt;value&gt; boolean</p>
<p role="func_signature">&lt;value&gt; <code>&lt;&gt;</code> &lt;value&gt; boolean</p>
<p>Non-equality comparison</p>
<p><code>jsonb_path_query_array('[1, 2, 1, 3]', '$[*] ? (@ != 1)')</code> [2, 3]</p>
<p><code>jsonb_path_query_array('["a", "b", "c"]', '$[*] ? (@ &lt;&gt; "b")')</code> ["a", "c"]</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>&lt;</code> &lt;value&gt; boolean</p>
<p>Less-than comparison</p>
<p><code>jsonb_path_query_array('[1, 2, 3]', '$[*] ? (@ &lt; 2)')</code> [1]</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>&lt;=</code> &lt;value&gt; boolean</p>
<p>Less-than-or-equal-to comparison</p>
<p><code>jsonb_path_query_array('["a", "b", "c"]', '$[*] ? (@ &lt;= "b")')</code> ["a", "b"]</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>&gt;</code> &lt;value&gt; boolean</p>
<p>Greater-than comparison</p>
<p><code>jsonb_path_query_array('[1, 2, 3]', '$[*] ? (@ &gt; 2)')</code> [3]</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;value&gt; <code>&gt;=</code> &lt;value&gt; boolean</p>
<p>Greater-than-or-equal-to comparison</p>
<p><code>jsonb_path_query_array('[1, 2, 3]', '$[*] ? (@ &gt;= 2)')</code> [2, 3]</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>true</code> boolean</p>
<p>JSON constant <code>true</code></p>
<p><code>jsonb_path_query('[{"name": "John", "parent": false}, {"name": "Chris", "parent": true}]', '$[*] ? (@.parent == true)')</code> {"name": "Chris", "parent": true}</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>false</code> boolean</p>
<p>JSON constant <code>false</code></p>
<p><code>jsonb_path_query('[{"name": "John", "parent": false}, {"name": "Chris", "parent": true}]', '$[*] ? (@.parent == false)')</code> {"name": "John", "parent": false}</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>null</code> &lt;value&gt;</p>
<p>JSON constant <code>null</code> (note that, unlike in SQL, comparison to <code>null</code> works normally)</p>
<p><code>jsonb_path_query('[{"name": "Mary", "job": null}, {"name": "Michael", "job": "driver"}]', '$[*] ? (@.job == null) .name')</code> "Mary"</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;boolean&gt; <code>&amp;&amp;</code> &lt;boolean&gt; boolean</p>
<p>Boolean AND</p>
<p><code>jsonb_path_query('[1, 3, 7]', '$[*] ? (@ &gt; 1 &amp;&amp; @ &lt; 5)')</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;boolean&gt; <code>||</code> &lt;boolean&gt; boolean</p>
<p>Boolean OR</p>
<p><code>jsonb_path_query('[1, 3, 7]', '$[*] ? (@ &lt; 1 || @ &gt; 5)')</code> 7</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>!</code> &lt;boolean&gt; boolean</p>
<p>Boolean NOT</p>
<p><code>jsonb_path_query('[1, 3, 7]', '$[*] ? (!(@ &lt; 5))')</code> 7</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;boolean&gt; <code>is unknown</code> boolean</p>
<p>Tests whether a Boolean condition is <code>unknown</code>.</p>
<p><code>jsonb_path_query('[-1, 2, 7, "foo"]', '$[*] ? ((@ &gt; 0) is unknown)')</code> "foo"</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;string&gt; <code>like_regex</code> &lt;string&gt; [<code>flag</code> &lt;string&gt;] boolean</p>
<p>Tests whether the first operand matches the regular expression given by the second operand, optionally with modifications described by a string of <code>flag</code> characters (see <a href="#jsonpath-regular-expressions">SQL/JSON Regular Expressions</a>).</p>
<p><code>jsonb_path_query_array('["abc", "abd", "aBdC", "abdacb", "babc"]', '$[*] ? (@ like_regex "^ab.*c")')</code> ["abc", "abdacb"]</p>
<p><code>jsonb_path_query_array('["abc", "abd", "aBdC", "abdacb", "babc"]', '$[*] ? (@ like_regex "^ab.*c" flag "i")')</code> ["abc", "aBdC", "abdacb"]</p></td>
</tr>
<tr>
<td><p role="func_signature">&lt;string&gt; <code>starts with</code> &lt;string&gt; boolean</p>
<p>Tests whether the second operand is an initial substring of the first operand.</p>
<p><code>jsonb_path_query('["John Smith", "Mary Stone", "Bob Johnson"]', '$[*] ? (@ starts with "John")')</code> "John Smith"</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>exists</code> <code>(</code> &lt;path_expression&gt; <code>)</code> boolean</p>
<p>Tests whether a path expression matches at least one SQL/JSON item. Returns <code>unknown</code> if the path expression would result in an error; the second example uses this to avoid a no-such-key error in strict mode.</p>
<p><code>jsonb_path_query('{"x": [1, 2], "y": [2, 4]}', 'strict $.* ? (exists (@ ? (@[*] &gt; 2)))')</code> [2, 4]</p>
<p><code>jsonb_path_query_array('{"value": 41}', 'strict $ ? (exists (@.name)) .name')</code> []</p></td>
</tr>
</tbody>
</table>

#### SQL/JSON Regular Expressions

LIKE_REGEX

in SQL/JSON

SQL/JSON path expressions allow matching text to a regular expression with the `like_regex` filter. For example, the following SQL/JSON path query would case-insensitively match all strings in an array that start with an English vowel:

    $[*] ? (@ like_regex "^[aeiou]" flag "i")

The optional `flag` string may include one or more of the characters `i` for case-insensitive match, `m` to allow `^` and `$` to match at newlines, `s` to allow `.` to match a newline, and `q` to quote the whole pattern (reducing the behavior to a simple substring match).

The SQL/JSON standard borrows its definition for regular expressions from the `LIKE_REGEX` operator, which in turn uses the XQuery standard. PostgreSQL does not currently support the `LIKE_REGEX` operator. Therefore, the `like_regex` filter is implemented using the POSIX regular expression engine described in [ Regular Expressions](#functions-posix-regexp). This leads to various minor discrepancies from standard SQL/JSON behavior, which are cataloged in [Differences from SQL Standard and XQuery](#posix-vs-xquery). Note, however, that the flag-letter incompatibilities described there do not apply to SQL/JSON, as it translates the XQuery flag letters to match what the POSIX engine expects.

Keep in mind that the pattern argument of `like_regex` is a JSON path string literal, written according to the rules given in [???](#datatype-jsonpath). This means in particular that any backslashes you want to use in the regular expression must be doubled. For example, to match string values of the root document that contain only digits:

    $.* ? (@ like_regex "^\\d+$")

### SQL/JSON Query Functions

SQL/JSON functions `JSON_EXISTS()`, `JSON_QUERY()`, and `JSON_VALUE()` described in [SQL/JSON Query Functions](#functions-sqljson-querying) can be used to query JSON documents. Each of these functions apply a \<path_expression\> (an SQL/JSON path query) to a \<context_item\> (the document). See [The SQL/JSON Path Language](#functions-sqljson-path) for more details on what the \<path_expression\> can contain. The \<path_expression\> can also reference variables, whose values are specified with their respective names in the `PASSING` clause that is supported by each function. \<context_item\> can be a `jsonb` value or a character string that can be successfully cast to `jsonb`.

<table id="functions-sqljson-querying">
<caption>SQL/JSON Query Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function signature</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>JSON_EXISTS</code> ( &lt;context_item&gt;, &lt;path_expression&gt; [<code>PASSING</code> { &lt;value&gt; <code>AS</code> &lt;varname&gt; } [, ...]] [{ <code>TRUE</code> | <code>FALSE</code> |<code>UNKNOWN</code> | <code>ERROR</code> } <code>ON ERROR</code>]) boolean</p>
<ul>
<li><p>Returns true if the SQL/JSON &lt;path_expression&gt; applied to the &lt;context_item&gt; yields any items, false otherwise.</p></li>
<li><p>The <code>ON ERROR</code> clause specifies the behavior if an error occurs during &lt;path_expression&gt; evaluation. Specifying <code>ERROR</code> will cause an error to be thrown with the appropriate message. Other options include returning <code>boolean</code> values <code>FALSE</code> or <code>TRUE</code> or the value <code>UNKNOWN</code> which is actually an SQL NULL. The default when no <code>ON ERROR</code> clause is specified is to return the <code>boolean</code> value <code>FALSE</code>.</p></li>
</ul>
<p>Examples:</p>
<p><code>JSON_EXISTS(jsonb '{"key1": [1,2,3]}', 'strict $.key1[*] ? (@ &gt; $x)' PASSING 2 AS x)</code> t</p>
<p><code>JSON_EXISTS(jsonb '{"a": [1,2,3]}', 'lax $.a[5]' ERROR ON ERROR)</code> f</p>
<p><code>JSON_EXISTS(jsonb '{"a": [1,2,3]}', 'strict $.a[5]' ERROR ON ERROR)</code></p>
<pre><code>ERROR:  jsonpath array subscript is out of bounds</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>JSON_QUERY</code> ( &lt;context_item&gt;, &lt;path_expression&gt; [<code>PASSING</code> { &lt;value&gt; <code>AS</code> &lt;varname&gt; } [, ...]] [<code>RETURNING</code> &lt;data_type&gt; [<code>FORMAT JSON</code> [<code>ENCODING UTF8</code>]]] [{ <code>WITHOUT</code> | <code>WITH</code> { <code>CONDITIONAL</code> | [<code>UNCONDITIONAL</code>] } } [<code>ARRAY</code>] <code>WRAPPER</code>] [{ <code>KEEP</code> | <code>OMIT</code> } <code>QUOTES</code> [<code>ON SCALAR STRING</code>]] [{ <code>ERROR</code> | <code>NULL</code> | <code>EMPTY</code> { [<code>ARRAY</code>] | <code>OBJECT</code> } | <code>DEFAULT</code> &lt;expression&gt; } <code>ON EMPTY</code>] [{ <code>ERROR</code> | <code>NULL</code> | <code>EMPTY</code> { [<code>ARRAY</code>] | <code>OBJECT</code> } | <code>DEFAULT</code> &lt;expression&gt; } <code>ON ERROR</code>]) jsonb</p>
<ul>
<li><p>Returns the result of applying the SQL/JSON &lt;path_expression&gt; to the &lt;context_item&gt;.</p></li>
<li><p>By default, the result is returned as a value of type <code>jsonb</code>, though the <code>RETURNING</code> clause can be used to return as some other type to which it can be successfully coerced.</p></li>
<li><p>If the path expression may return multiple values, it might be necessary to wrap those values using the <code>WITH WRAPPER</code> clause to make it a valid JSON string, because the default behavior is to not wrap them, as if <code>WITHOUT WRAPPER</code> were specified. The <code>WITH WRAPPER</code> clause is by default taken to mean <code>WITH UNCONDITIONAL WRAPPER</code>, which means that even a single result value will be wrapped. To apply the wrapper only when multiple values are present, specify <code>WITH CONDITIONAL WRAPPER</code>. Getting multiple values in result will be treated as an error if <code>WITHOUT WRAPPER</code> is specified.</p></li>
<li><p>If the result is a scalar string, by default, the returned value will be surrounded by quotes, making it a valid JSON value. It can be made explicit by specifying <code>KEEP QUOTES</code>. Conversely, quotes can be omitted by specifying <code>OMIT QUOTES</code>. To ensure that the result is a valid JSON value, <code>OMIT QUOTES</code> cannot be specified when <code>WITH WRAPPER</code> is also specified.</p></li>
<li><p>The <code>ON EMPTY</code> clause specifies the behavior if evaluating &lt;path_expression&gt; yields an empty set. The <code>ON ERROR</code> clause specifies the behavior if an error occurs when evaluating &lt;path_expression&gt;, when coercing the result value to the <code>RETURNING</code> type, or when evaluating the <code>ON EMPTY</code> expression if the &lt;path_expression&gt; evaluation returns an empty set.</p></li>
<li><p>For both <code>ON EMPTY</code> and <code>ON ERROR</code>, specifying <code>ERROR</code> will cause an error to be thrown with the appropriate message. Other options include returning an SQL NULL, an empty array (<code>EMPTY ARRAY</code>), an empty object (<code>EMPTY OBJECT</code>), or a user-specified expression (<code>DEFAULT</code> &lt;expression&gt;) that can be coerced to jsonb or the type specified in <code>RETURNING</code>. The default when <code>ON EMPTY</code> or <code>ON ERROR</code> is not specified is to return an SQL NULL value.</p></li>
</ul>
<p>Examples:</p>
<p><code>JSON_QUERY(jsonb '[1,[2,3],null]', 'lax $[*][$off]' PASSING 1 AS off WITH CONDITIONAL WRAPPER)</code> 3</p>
<p><code>JSON_QUERY(jsonb '{"a": "[1, 2]"}', 'lax $.a' OMIT QUOTES)</code> [1, 2]</p>
<p><code>JSON_QUERY(jsonb '{"a": "[1, 2]"}', 'lax $.a' RETURNING int[] OMIT QUOTES ERROR ON ERROR)</code></p>
<pre><code>ERROR:  malformed array literal: &quot;[1, 2]&quot;
DETAIL:  Missing &quot;]&quot; after array dimensions.</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>JSON_VALUE</code> ( &lt;context_item&gt;, &lt;path_expression&gt; [<code>PASSING</code> { &lt;value&gt; <code>AS</code> &lt;varname&gt; } [, ...]] [<code>RETURNING</code> &lt;data_type&gt;] [{ <code>ERROR</code> | <code>NULL</code> | <code>DEFAULT</code> &lt;expression&gt; } <code>ON EMPTY</code>] [{ <code>ERROR</code> | <code>NULL</code> | <code>DEFAULT</code> &lt;expression&gt; } <code>ON ERROR</code>]) text</p>
<ul>
<li><p>Returns the result of applying the SQL/JSON &lt;path_expression&gt; to the &lt;context_item&gt;.</p></li>
<li><p>Only use <code>JSON_VALUE()</code> if the extracted value is expected to be a single SQL/JSON scalar item; getting multiple values will be treated as an error. If you expect that extracted value might be an object or an array, use the <code>JSON_QUERY</code> function instead.</p></li>
<li><p>By default, the result, which must be a single scalar value, is returned as a value of type <code>text</code>, though the <code>RETURNING</code> clause can be used to return as some other type to which it can be successfully coerced.</p></li>
<li><p>The <code>ON ERROR</code> and <code>ON EMPTY</code> clauses have similar semantics as mentioned in the description of <code>JSON_QUERY</code>, except the set of values returned in lieu of throwing an error is different.</p></li>
<li><p>Note that scalar strings returned by <code>JSON_VALUE</code> always have their quotes removed, equivalent to specifying <code>OMIT QUOTES</code> in <code>JSON_QUERY</code>.</p></li>
</ul>
<p>Examples:</p>
<p><code>JSON_VALUE(jsonb '"123.45"', '$' RETURNING float)</code> 123.45</p>
<p><code>JSON_VALUE(jsonb '"03:04 2015-02-01"', '$.datetime("HH24:MIYYYY-MM-DD")' RETURNING date)</code> 2015-02-01</p>
<p><code>JSON_VALUE(jsonb '[1,2]', 'strict $[$off]' PASSING 1 as off)</code> 2</p>
<p><code>JSON_VALUE(jsonb '[1,2]', 'strict $[*]' DEFAULT 9 ON ERROR)</code> 9</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> The \<context_item\> expression is converted to `jsonb` by an implicit cast if the expression is not already of type `jsonb`. Note, however, that any parsing errors that occur during that conversion are thrown unconditionally, that is, are not handled according to the (specified or implicit) `ON ERROR` clause.

> [!NOTE]
> `JSON_VALUE()` returns an SQL NULL if \<path_expression\> returns a JSON `null`, whereas `JSON_QUERY()` returns the JSON `null` as is.

### JSON_TABLE

json_table

`JSON_TABLE` is an SQL/JSON function which queries JSON data and presents the results as a relational view, which can be accessed as a regular SQL table. You can use `JSON_TABLE` inside the `FROM` clause of a `SELECT`, `UPDATE`, or `DELETE` and as data source in a `MERGE` statement.

Taking JSON data as input, `JSON_TABLE` uses a JSON path expression to extract a part of the provided data to use as a row pattern for the constructed view. Each SQL/JSON value given by the row pattern serves as source for a separate row in the constructed view.

To split the row pattern into columns, `JSON_TABLE` provides the `COLUMNS` clause that defines the schema of the created view. For each column, a separate JSON path expression can be specified to be evaluated against the row pattern to get an SQL/JSON value that will become the value for the specified column in a given output row.

JSON data stored at a nested level of the row pattern can be extracted using the `NESTED PATH` clause. Each `NESTED PATH` clause can be used to generate one or more columns using the data from a nested level of the row pattern. Those columns can be specified using a `COLUMNS` clause that looks similar to the top-level COLUMNS clause. Rows constructed from NESTED COLUMNS are called child rows and are joined against the row constructed from the columns specified in the parent `COLUMNS` clause to get the row in the final view. Child columns themselves may contain a `NESTED PATH` specification thus allowing to extract data located at arbitrary nesting levels. Columns produced by multiple `NESTED PATH`s at the same level are considered to be siblings of each other and their rows after joining with the parent row are combined using UNION.

The rows produced by `JSON_TABLE` are laterally joined to the row that generated them, so you do not have to explicitly join the constructed view with the original table holding JSON data.

The syntax is:

JSON_TABLE (

context_item

,

path_expression

AS

json_path_name

PASSING {

value

AS

varname

}

, ...

COLUMNS (

json_table_column

, ...

)

{

ERROR

\|

EMPTY

ARRAY

}

ON ERROR

)

where

json_table_column

is:

name

FOR ORDINALITY \|

name

type

FORMAT JSON

ENCODING

UTF8

PATH

path_expression

{ WITHOUT \| WITH { CONDITIONAL \|

UNCONDITIONAL

} }

ARRAY

WRAPPER

{ KEEP \| OMIT } QUOTES

ON SCALAR STRING

{ ERROR \| NULL \| EMPTY {

ARRAY

\| OBJECT } \| DEFAULT

expression

} ON EMPTY

{ ERROR \| NULL \| EMPTY {

ARRAY

\| OBJECT } \| DEFAULT

expression

} ON ERROR

\|

name

type

EXISTS

PATH

path_expression

{ ERROR \| TRUE \| FALSE \| UNKNOWN } ON ERROR

\| NESTED

PATH

path_expression

AS

json_path_name

COLUMNS (

json_table_column

, ...

)

Each syntax element is described below in more detail.

`context_item, path_expression AS json_path_name PASSING { value AS varname } , ...`  
The \<context_item\> specifies the input document to query, the \<path_expression\> is an SQL/JSON path expression defining the query, and \<json_path_name\> is an optional name for the \<path_expression\>. The optional `PASSING` clause provides data values for the variables mentioned in the \<path_expression\>. The result of the input data evaluation using the aforementioned elements is called the row pattern, which is used as the source for row values in the constructed view.

`COLUMNS` ( \<json_table_column\> \[, ...\] )  
The `COLUMNS` clause defining the schema of the constructed view. In this clause, you can specify each column to be filled with an SQL/JSON value obtained by applying a JSON path expression against the row pattern. \<json_table_column\> has the following variants:

\<name\> `FOR ORDINALITY`  
Adds an ordinality column that provides sequential row numbering starting from 1. Each `NESTED PATH` (see below) gets its own counter for any nested ordinality columns.

`name type FORMAT JSON ENCODING UTF8 PATH path_expression`  
Inserts an SQL/JSON value obtained by applying \<path_expression\> against the row pattern into the view's output row after coercing it to specified \<type\>.

Specifying `FORMAT JSON` makes it explicit that you expect the value to be a valid `json` object. It only makes sense to specify `FORMAT JSON` if \<type\> is one of `bpchar`, `bytea`, `character varying`, `name`, `json`, `jsonb`, `text`, or a domain over these types.

Optionally, you can specify `WRAPPER` and `QUOTES` clauses to format the output. Note that specifying `OMIT QUOTES` overrides `FORMAT JSON` if also specified, because unquoted literals do not constitute valid `json` values.

Optionally, you can use `ON EMPTY` and `ON ERROR` clauses to specify whether to throw the error or return the specified value when the result of JSON path evaluation is empty and when an error occurs during JSON path evaluation or when coercing the SQL/JSON value to the specified type, respectively. The default for both is to return a `NULL` value.

> [!NOTE]
> This clause is internally turned into and has the same semantics as `JSON_VALUE` or `JSON_QUERY`. The latter if the specified type is not a scalar type or if either of `FORMAT JSON`, `WRAPPER`, or `QUOTES` clause is present.

\<name\> \<type\> `EXISTS` \[`PATH` \<path_expression\>\]  
Inserts a boolean value obtained by applying \<path_expression\> against the row pattern into the view's output row after coercing it to specified \<type\>.

The value corresponds to whether applying the `PATH` expression to the row pattern yields any values.

The specified \<type\> should have a cast from the `boolean` type.

Optionally, you can use `ON ERROR` to specify whether to throw the error or return the specified value when an error occurs during JSON path evaluation or when coercing SQL/JSON value to the specified type. The default is to return a boolean value `FALSE`.

> [!NOTE]
> This clause is internally turned into and has the same semantics as `JSON_EXISTS`.

`NESTED PATH` \<path_expression\> \[`AS` \<json_path_name\>\] `COLUMNS` ( \<json_table_column\> \[, ...\] )  
Extracts SQL/JSON values from nested levels of the row pattern, generates one or more columns as defined by the `COLUMNS` subclause, and inserts the extracted SQL/JSON values into those columns. The \<json_table_column\> expression in the `COLUMNS` subclause uses the same syntax as in the parent `COLUMNS` clause.

The `NESTED PATH` syntax is recursive, so you can go down multiple nested levels by specifying several `NESTED PATH` subclauses within each other. It allows to unnest the hierarchy of JSON objects and arrays in a single function invocation rather than chaining several `JSON_TABLE` expressions in an SQL statement.

> [!NOTE]
> In each variant of \<json_table_column\> described above, if the `PATH` clause is omitted, path expression `$.name` is used, where \<name\> is the provided column name.

`AS` \<json_path_name\>  
The optional \<json_path_name\> serves as an identifier of the provided \<path_expression\>. The name must be unique and distinct from the column names.

{ `ERROR` \| `EMPTY` } `ON ERROR`  
The optional `ON ERROR` can be used to specify how to handle errors when evaluating the top-level \<path_expression\>. Use `ERROR` if you want the errors to be thrown and `EMPTY` to return an empty table, that is, a table containing 0 rows. Note that this clause does not affect the errors that occur when evaluating columns, for which the behavior depends on whether the `ON ERROR` clause is specified against a given column.

Examples

In the examples that follow, the following table containing JSON data will be used:

    CREATE TABLE my_films ( js jsonb );

    INSERT INTO my_films VALUES (
    '{ "favorites" : [
       { "kind" : "comedy", "films" : [
         { "title" : "Bananas",
           "director" : "Woody Allen"},
         { "title" : "The Dinner Game",
           "director" : "Francis Veber" } ] },
       { "kind" : "horror", "films" : [
         { "title" : "Psycho",
           "director" : "Alfred Hitchcock" } ] },
       { "kind" : "thriller", "films" : [
         { "title" : "Vertigo",
           "director" : "Alfred Hitchcock" } ] },
       { "kind" : "drama", "films" : [
         { "title" : "Yojimbo",
           "director" : "Akira Kurosawa" } ] }
      ] }');

The following query shows how to use `JSON_TABLE` to turn the JSON objects in the my_films table to a view containing columns for the keys `kind`, `title`, and `director` contained in the original JSON along with an ordinality column:

    SELECT jt.* FROM
     my_films,
     JSON_TABLE (js, '$.favorites[*]' COLUMNS (
       id FOR ORDINALITY,
       kind text PATH '$.kind',
       title text PATH '$.films[*].title' WITH WRAPPER,
       director text PATH '$.films[*].director' WITH WRAPPER)) AS jt;

     id |   kind   |             title              |             director
    ----+----------+--------------------------------+----------------------------------
      1 | comedy   | ["Bananas", "The Dinner Game"] | ["Woody Allen", "Francis Veber"]
      2 | horror   | ["Psycho"]                     | ["Alfred Hitchcock"]
      3 | thriller | ["Vertigo"]                    | ["Alfred Hitchcock"]
      4 | drama    | ["Yojimbo"]                    | ["Akira Kurosawa"]
    (4 rows)

The following is a modified version of the above query to show the usage of `PASSING` arguments in the filter specified in the top-level JSON path expression and the various options for the individual columns:

    SELECT jt.* FROM
     my_films,
     JSON_TABLE (js, '$.favorites[*] ? (@.films[*].director == $filter)'
       PASSING 'Alfred Hitchcock' AS filter
         COLUMNS (
         id FOR ORDINALITY,
         kind text PATH '$.kind',
         title text FORMAT JSON PATH '$.films[*].title' OMIT QUOTES,
         director text PATH '$.films[*].director' KEEP QUOTES)) AS jt;

     id |   kind   |  title  |      director
    ----+----------+---------+--------------------
      1 | horror   | Psycho  | "Alfred Hitchcock"
      2 | thriller | Vertigo | "Alfred Hitchcock"
    (2 rows)

The following is a modified version of the above query to show the usage of `NESTED PATH` for populating title and director columns, illustrating how they are joined to the parent columns id and kind:

    SELECT jt.* FROM
     my_films,
     JSON_TABLE ( js, '$.favorites[*] ? (@.films[*].director == $filter)'
       PASSING 'Alfred Hitchcock' AS filter
       COLUMNS (
        id FOR ORDINALITY,
        kind text PATH '$.kind',
        NESTED PATH '$.films[*]' COLUMNS (
          title text FORMAT JSON PATH '$.title' OMIT QUOTES,
          director text PATH '$.director' KEEP QUOTES))) AS jt;

     id |   kind   |  title  |      director
    ----+----------+---------+--------------------
      1 | horror   | Psycho  | "Alfred Hitchcock"
      2 | thriller | Vertigo | "Alfred Hitchcock"
    (2 rows)

The following is the same query but without the filter in the root path:

    SELECT jt.* FROM
     my_films,
     JSON_TABLE ( js, '$.favorites[*]'
       COLUMNS (
        id FOR ORDINALITY,
        kind text PATH '$.kind',
        NESTED PATH '$.films[*]' COLUMNS (
          title text FORMAT JSON PATH '$.title' OMIT QUOTES,
          director text PATH '$.director' KEEP QUOTES))) AS jt;

     id |   kind   |      title      |      director
    ----+----------+-----------------+--------------------
      1 | comedy   | Bananas         | "Woody Allen"
      1 | comedy   | The Dinner Game | "Francis Veber"
      2 | horror   | Psycho          | "Alfred Hitchcock"
      3 | thriller | Vertigo         | "Alfred Hitchcock"
      4 | drama    | Yojimbo         | "Akira Kurosawa"
    (5 rows)

The following shows another query using a different `JSON` object as input. It shows the UNION "sibling join" between `NESTED` paths `$.movies[*]` and `$.books[*]` and also the usage of `FOR ORDINALITY` column at `NESTED` levels (columns `movie_id`, `book_id`, and `author_id`):

    SELECT * FROM JSON_TABLE (
    '{"favorites":
        [{"movies":
          [{"name": "One", "director": "John Doe"},
           {"name": "Two", "director": "Don Joe"}],
         "books":
          [{"name": "Mystery", "authors": [{"name": "Brown Dan"}]},
           {"name": "Wonder", "authors": [{"name": "Jun Murakami"}, {"name":"Craig Doe"}]}]
    }]}'::json, '$.favorites[*]'
    COLUMNS (
      user_id FOR ORDINALITY,
      NESTED '$.movies[*]'
        COLUMNS (
        movie_id FOR ORDINALITY,
        mname text PATH '$.name',
        director text),
      NESTED '$.books[*]'
        COLUMNS (
          book_id FOR ORDINALITY,
          bname text PATH '$.name',
          NESTED '$.authors[*]'
            COLUMNS (
              author_id FOR ORDINALITY,
              author_name text PATH '$.name'))));

     user_id | movie_id | mname | director | book_id |  bname  | author_id | author_name
    ---------+----------+-------+----------+---------+---------+-----------+--------------
           1 |        1 | One   | John Doe |         |         |           |
           1 |        2 | Two   | Don Joe  |         |         |           |
           1 |          |       |          |       1 | Mystery |         1 | Brown Dan
           1 |          |       |          |       2 | Wonder  |         1 | Jun Murakami
           1 |          |       |          |       2 | Wonder  |         2 | Craig Doe
    (5 rows)

## Sequence Manipulation Functions

sequence

This section describes functions for operating on sequence objects, also called sequence generators or just sequences. Sequence objects are special single-row tables created with [???](#sql-createsequence). Sequence objects are commonly used to generate unique identifiers for rows of a table. The sequence functions, listed in [Sequence Functions](#functions-sequence-table), provide simple, multiuser-safe methods for obtaining successive sequence values from sequence objects.

<table id="functions-sequence-table">
<caption>Sequence Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>nextval</code> ( <code>regclass</code> ) bigint</p>
<p>Advances the sequence object to its next value and returns that value. This is done atomically: even if multiple sessions execute <code>nextval</code> concurrently, each will safely receive a distinct sequence value. If the sequence object has been created with default parameters, successive <code>nextval</code> calls will return successive values beginning with 1. Other behaviors can be obtained by using appropriate parameters in the <a href="#sql-createsequence">???</a> command.</p>
<p>This function requires <code>USAGE</code> or <code>UPDATE</code> privilege on the sequence.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>setval</code> ( <code>regclass</code>, <code>bigint</code> [, <code>boolean</code>] ) bigint</p>
<p>Sets the sequence object's current value, and optionally its <code>is_called</code> flag. The two-parameter form sets the sequence's <code>last_value</code> field to the specified value and sets its <code>is_called</code> field to <code>true</code>, meaning that the next <code>nextval</code> will advance the sequence before returning a value. The value that will be reported by <code>currval</code> is also set to the specified value. In the three-parameter form, <code>is_called</code> can be set to either <code>true</code> or <code>false</code>. <code>true</code> has the same effect as the two-parameter form. If it is set to <code>false</code>, the next <code>nextval</code> will return exactly the specified value, and sequence advancement commences with the following <code>nextval</code>. Furthermore, the value reported by <code>currval</code> is not changed in this case. For example,</p>
<pre><code>SELECT setval(&#39;myseq&#39;, 42);           Next nextval will return 43
SELECT setval(&#39;myseq&#39;, 42, true);     Same as above
SELECT setval(&#39;myseq&#39;, 42, false);    Next nextval will return 42</code></pre>
<p>The result returned by <code>setval</code> is just the value of its second argument.</p>
<p>This function requires <code>UPDATE</code> privilege on the sequence.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>currval</code> ( <code>regclass</code> ) bigint</p>
<p>Returns the value most recently obtained by <code>nextval</code> for this sequence in the current session. (An error is reported if <code>nextval</code> has never been called for this sequence in this session.) Because this is returning a session-local value, it gives a predictable answer whether or not other sessions have executed <code>nextval</code> since the current session did.</p>
<p>This function requires <code>USAGE</code> or <code>SELECT</code> privilege on the sequence.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lastval</code> () bigint</p>
<p>Returns the value most recently returned by <code>nextval</code> in the current session. This function is identical to <code>currval</code>, except that instead of taking the sequence name as an argument it refers to whichever sequence <code>nextval</code> was most recently applied to in the current session. It is an error to call <code>lastval</code> if <code>nextval</code> has not yet been called in the current session.</p>
<p>This function requires <code>USAGE</code> or <code>SELECT</code> privilege on the last used sequence.</p></td>
</tr>
</tbody>
</table>

> [!CAUTION]
> To avoid blocking concurrent transactions that obtain numbers from the same sequence, the value obtained by `nextval` is not reclaimed for re-use if the calling transaction later aborts. This means that transaction aborts or database crashes can result in gaps in the sequence of assigned values. That can happen without a transaction abort, too. For example an `INSERT` with an `ON CONFLICT` clause will compute the to-be-inserted tuple, including doing any required `nextval` calls, before detecting any conflict that would cause it to follow the `ON CONFLICT` rule instead. Thus, PostgreSQL sequence objects *cannot be used to obtain “gapless” sequences*.
>
> Likewise, sequence state changes made by `setval` are immediately visible to other transactions, and are not undone if the calling transaction rolls back.
>
> If the database cluster crashes before committing a transaction containing a `nextval` or `setval` call, the sequence state change might not have made its way to persistent storage, so that it is uncertain whether the sequence will have its original or updated state after the cluster restarts. This is harmless for usage of the sequence within the database, since other effects of uncommitted transactions will not be visible either. However, if you wish to use a sequence value for persistent outside-the-database purposes, make sure that the `nextval` call has been committed before doing so.

The sequence to be operated on by a sequence function is specified by a `regclass` argument, which is simply the OID of the sequence in the pg_class system catalog. You do not have to look up the OID by hand, however, since the `regclass` data type's input converter will do the work for you. See [???](#datatype-oid) for details.

## Conditional Expressions

CASE

conditional expression

This section describes the SQL-compliant conditional expressions available in PostgreSQL.

> [!TIP]
> If your needs go beyond the capabilities of these conditional expressions, you might want to consider writing a server-side function in a more expressive programming language.

> [!NOTE]
> Although COALESCE, GREATEST, and LEAST are syntactically similar to functions, they are not ordinary functions, and thus cannot be used with explicit VARIADIC array arguments.

### `CASE`

The SQL CASE expression is a generic conditional expression, similar to if/else statements in other programming languages: CASE WHEN \<condition\> THEN \<result\> \[WHEN ...\] \[ELSE \<result\>\] END CASE clauses can be used wherever an expression is valid. Each \<condition\> is an expression that returns a `boolean` result. If the condition's result is true, the value of the CASE expression is the \<result\> that follows the condition, and the remainder of the CASE expression is not processed. If the condition's result is not true, any subsequent WHEN clauses are examined in the same manner. If no WHEN \<condition\> yields true, the value of the CASE expression is the \<result\> of the ELSE clause. If the ELSE clause is omitted and no condition is true, the result is null.

An example:

    SELECT * FROM test;

     a
    ---
     1
     2
     3

    SELECT a,
           CASE WHEN a=1 THEN 'one'
                WHEN a=2 THEN 'two'
                ELSE 'other'
           END
        FROM test;

     a | case
    ---+-------
     1 | one
     2 | two
     3 | other

The data types of all the \<result\> expressions must be convertible to a single output type. See [???](#typeconv-union-case) for more details.

There is a “simple” form of CASE expression that is a variant of the general form above: CASE \<expression\> WHEN \<value\> THEN \<result\> \[WHEN ...\] \[ELSE \<result\>\] END The first \<expression\> is computed, then compared to each of the \<value\> expressions in the WHEN clauses until one is found that is equal to it. If no match is found, the \<result\> of the ELSE clause (or a null value) is returned. This is similar to the `switch` statement in C.

The example above can be written using the simple CASE syntax:

    SELECT a,
           CASE a WHEN 1 THEN 'one'
                  WHEN 2 THEN 'two'
                  ELSE 'other'
           END
        FROM test;

     a | case
    ---+-------
     1 | one
     2 | two
     3 | other

A CASE expression does not evaluate any subexpressions that are not needed to determine the result. For example, this is a possible way of avoiding a division-by-zero failure:

    SELECT ... WHERE CASE WHEN x <> 0 THEN y/x > 1.5 ELSE false END;

> [!NOTE]
> As described in [???](#syntax-express-eval), there are various situations in which subexpressions of an expression are evaluated at different times, so that the principle that “CASE evaluates only necessary subexpressions” is not ironclad. For example a constant `1/0` subexpression will usually result in a division-by-zero failure at planning time, even if it's within a CASE arm that would never be entered at run time.

### `COALESCE`

COALESCE

NVL

IFNULL

COALESCE

(

value

, ...

)

The `COALESCE` function returns the first of its arguments that is not null. Null is returned only if all arguments are null. It is often used to substitute a default value for null values when data is retrieved for display, for example:

    SELECT COALESCE(description, short_description, '(none)') ...

This returns `description` if it is not null, otherwise `short_description` if it is not null, otherwise `(none)`.

The arguments must all be convertible to a common data type, which will be the type of the result (see [???](#typeconv-union-case) for details).

Like a CASE expression, `COALESCE` only evaluates the arguments that are needed to determine the result; that is, arguments to the right of the first non-null argument are not evaluated. This SQL-standard function provides capabilities similar to `NVL` and `IFNULL`, which are used in some other database systems.

### `NULLIF`

NULLIF

NULLIF

(

value1

,

value2

)

The `NULLIF` function returns a null value if \<value1\> equals \<value2\>; otherwise it returns \<value1\>. This can be used to perform the inverse operation of the `COALESCE` example given above:

    SELECT NULLIF(value, '(none)') ...

In this example, if `value` is `(none)`, null is returned, otherwise the value of `value` is returned.

The two arguments must be of comparable types. To be specific, they are compared exactly as if you had written `value1 = value2`, so there must be a suitable `=` operator available.

The result has the same type as the first argument but there is a subtlety. What is actually returned is the first argument of the implied `=` operator, and in some cases that will have been promoted to match the second argument's type. For example, `NULLIF(1, 2.2)` yields `numeric`, because there is no `integer` `=` `numeric` operator, only `numeric` `=` `numeric`.

### `GREATEST` and `LEAST`

GREATEST

LEAST

GREATEST

(

value

, ...

)

LEAST

(

value

, ...

)

The `GREATEST` and `LEAST` functions select the largest or smallest value from a list of any number of expressions. The expressions must all be convertible to a common data type, which will be the type of the result (see [???](#typeconv-union-case) for details).

NULL values in the argument list are ignored. The result will be NULL only if all the expressions evaluate to NULL. (This is a deviation from the SQL standard. According to the standard, the return value is NULL if any argument is NULL. Some other databases behave this way.)

## Array Functions and Operators

[Array Operators](#array-operators-table) shows the specialized operators available for array types. In addition to those, the usual comparison operators shown in [Comparison Operators](#functions-comparison-op-table) are available for arrays. The comparison operators compare the array contents element-by-element, using the default B-tree comparison function for the element data type, and sort based on the first difference. In multidimensional arrays the elements are visited in row-major order (last subscript varies most rapidly). If the contents of two arrays are equal but the dimensionality is different, the first difference in the dimensionality information determines the sort order.

<table id="array-operators-table">
<caption>Array Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>anyarray</code> <code>@&gt;</code> <code>anyarray</code> boolean</p>
<p>Does the first array contain the second, that is, does each element appearing in the second array equal some element of the first array? (Duplicates are not treated specially, thus <code>ARRAY[1]</code> and <code>ARRAY[1,1]</code> are each considered to contain the other.)</p>
<p><code>ARRAY[1,4,3] @&gt; ARRAY[3,1,3]</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyarray</code> <code>&lt;@</code> <code>anyarray</code> boolean</p>
<p>Is the first array contained by the second?</p>
<p><code>ARRAY[2,2,7] &lt;@ ARRAY[1,7,4,2,6]</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyarray</code> <code>&amp;&amp;</code> <code>anyarray</code> boolean</p>
<p>Do the arrays overlap, that is, have any elements in common?</p>
<p><code>ARRAY[1,4,3] &amp;&amp; ARRAY[2,1]</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anycompatiblearray</code> <code>||</code> <code>anycompatiblearray</code> anycompatiblearray</p>
<p>Concatenates the two arrays. Concatenating a null or empty array is a no-op; otherwise the arrays must have the same number of dimensions (as illustrated by the first example) or differ in number of dimensions by one (as illustrated by the second). If the arrays are not of identical element types, they will be coerced to a common type (see <a href="#typeconv-union-case">???</a>).</p>
<p><code>ARRAY[1,2,3] || ARRAY[4,5,6,7]</code> {1,2,3,4,5,6,7}</p>
<p><code>ARRAY[1,2,3] || ARRAY[[4,5,6],[7,8,9.9]]</code> {{1,2,3},{4,5,6},{7,8,9.9}}</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anycompatible</code> <code>||</code> <code>anycompatiblearray</code> anycompatiblearray</p>
<p>Concatenates an element onto the front of an array (which must be empty or one-dimensional).</p>
<p><code>3 || ARRAY[4,5,6]</code> {3,4,5,6}</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anycompatiblearray</code> <code>||</code> <code>anycompatible</code> anycompatiblearray</p>
<p>Concatenates an element onto the end of an array (which must be empty or one-dimensional).</p>
<p><code>ARRAY[4,5,6] || 7</code> {4,5,6,7}</p></td>
</tr>
</tbody>
</table>

See [???](#arrays) for more details about array operator behavior. See [???](#indexes-types) for more details about which operators support indexed operations.

[Array Functions](#array-functions-table) shows the functions available for use with array types. See [???](#arrays) for more information and examples of the use of these functions.

<table id="array-functions-table">
<caption>Array Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_append</code> ( <code>anycompatiblearray</code>, <code>anycompatible</code> ) anycompatiblearray</p>
<p>Appends an element to the end of an array (same as the <code>anycompatiblearray</code> <code>||</code> <code>anycompatible</code> operator).</p>
<p><code>array_append(ARRAY[1,2], 3)</code> {1,2,3}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_cat</code> ( <code>anycompatiblearray</code>, <code>anycompatiblearray</code> ) anycompatiblearray</p>
<p>Concatenates two arrays (same as the <code>anycompatiblearray</code> <code>||</code> <code>anycompatiblearray</code> operator).</p>
<p><code>array_cat(ARRAY[1,2,3], ARRAY[4,5])</code> {1,2,3,4,5}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_dims</code> ( <code>anyarray</code> ) text</p>
<p>Returns a text representation of the array's dimensions.</p>
<p><code>array_dims(ARRAY[[1,2,3], [4,5,6]])</code> [1:2][1:3]</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_fill</code> ( <code>anyelement</code>, <code>integer[]</code> [, <code>integer[]</code>] ) anyarray</p>
<p>Returns an array filled with copies of the given value, having dimensions of the lengths specified by the second argument. The optional third argument supplies lower-bound values for each dimension (which default to all <code>1</code>).</p>
<p><code>array_fill(11, ARRAY[2,3])</code> {{11,11,11},{11,11,11}}</p>
<p><code>array_fill(7, ARRAY[3], ARRAY[2])</code> [2:4]={7,7,7}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_length</code> ( <code>anyarray</code>, <code>integer</code> ) integer</p>
<p>Returns the length of the requested array dimension. (Produces NULL instead of 0 for empty or missing array dimensions.)</p>
<p><code>array_length(array[1,2,3], 1)</code> 3</p>
<p><code>array_length(array[]::int[], 1)</code> NULL</p>
<p><code>array_length(array['text'], 2)</code> NULL</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_lower</code> ( <code>anyarray</code>, <code>integer</code> ) integer</p>
<p>Returns the lower bound of the requested array dimension.</p>
<p><code>array_lower('[0:2]={1,2,3}'::integer[], 1)</code> 0</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_ndims</code> ( <code>anyarray</code> ) integer</p>
<p>Returns the number of dimensions of the array.</p>
<p><code>array_ndims(ARRAY[[1,2,3], [4,5,6]])</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_position</code> ( <code>anycompatiblearray</code>, <code>anycompatible</code> [, <code>integer</code>] ) integer</p>
<p>Returns the subscript of the first occurrence of the second argument in the array, or <code>NULL</code> if it's not present. If the third argument is given, the search begins at that subscript. The array must be one-dimensional. Comparisons are done using <code>IS NOT DISTINCT FROM</code> semantics, so it is possible to search for <code>NULL</code>.</p>
<p><code>array_position(ARRAY['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'], 'mon')</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_positions</code> ( <code>anycompatiblearray</code>, <code>anycompatible</code> ) integer[]</p>
<p>Returns an array of the subscripts of all occurrences of the second argument in the array given as first argument. The array must be one-dimensional. Comparisons are done using <code>IS NOT DISTINCT FROM</code> semantics, so it is possible to search for <code>NULL</code>. <code>NULL</code> is returned only if the array is <code>NULL</code>; if the value is not found in the array, an empty array is returned.</p>
<p><code>array_positions(ARRAY['A','A','B','A'], 'A')</code> {1,2,4}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_prepend</code> ( <code>anycompatible</code>, <code>anycompatiblearray</code> ) anycompatiblearray</p>
<p>Prepends an element to the beginning of an array (same as the <code>anycompatible</code> <code>||</code> <code>anycompatiblearray</code> operator).</p>
<p><code>array_prepend(1, ARRAY[2,3])</code> {1,2,3}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_remove</code> ( <code>anycompatiblearray</code>, <code>anycompatible</code> ) anycompatiblearray</p>
<p>Removes all elements equal to the given value from the array. The array must be one-dimensional. Comparisons are done using <code>IS NOT DISTINCT FROM</code> semantics, so it is possible to remove <code>NULL</code>s.</p>
<p><code>array_remove(ARRAY[1,2,3,2], 2)</code> {1,3}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_replace</code> ( <code>anycompatiblearray</code>, <code>anycompatible</code>, <code>anycompatible</code> ) anycompatiblearray</p>
<p>Replaces each array element equal to the second argument with the third argument.</p>
<p><code>array_replace(ARRAY[1,2,5,4], 5, 3)</code> {1,2,3,4}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_sample</code> ( <code>array</code> <code>anyarray</code>, <code>n</code> <code>integer</code> ) anyarray</p>
<p>Returns an array of <code>n</code> items randomly selected from <code>array</code>. <code>n</code> may not exceed the length of <code>array</code>'s first dimension. If <code>array</code> is multi-dimensional, an “item” is a slice having a given first subscript.</p>
<p><code>array_sample(ARRAY[1,2,3,4,5,6], 3)</code> {2,6,1}</p>
<p><code>array_sample(ARRAY[[1,2],[3,4],[5,6]], 2)</code> {{5,6},{1,2}}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_shuffle</code> ( <code>anyarray</code> ) anyarray</p>
<p>Randomly shuffles the first dimension of the array.</p>
<p><code>array_shuffle(ARRAY[[1,2],[3,4],[5,6]])</code> {{5,6},{1,2},{3,4}}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span id="function-array-to-string" class="indexterm"></span> <code>array_to_string</code> ( <code>array</code> <code>anyarray</code>, <code>delimiter</code> <code>text</code> [, <code>null_string</code> <code>text</code>] ) text</p>
<p>Converts each array element to its text representation, and concatenates those separated by the <code>delimiter</code> string. If <code>null_string</code> is given and is not <code>NULL</code>, then <code>NULL</code> array entries are represented by that string; otherwise, they are omitted. See also <a href="#function-string-to-array"><code>string_to_array</code></a>.</p>
<p><code>array_to_string(ARRAY[1, 2, 3, NULL, 5], ',', '*')</code> 1,2,3,*,5</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_upper</code> ( <code>anyarray</code>, <code>integer</code> ) integer</p>
<p>Returns the upper bound of the requested array dimension.</p>
<p><code>array_upper(ARRAY[1,8,3,7], 1)</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>cardinality</code> ( <code>anyarray</code> ) integer</p>
<p>Returns the total number of elements in the array, or 0 if the array is empty.</p>
<p><code>cardinality(ARRAY[[1,2],[3,4]])</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>trim_array</code> ( <code>array</code> <code>anyarray</code>, <code>n</code> <code>integer</code> ) anyarray</p>
<p>Trims an array by removing the last <code>n</code> elements. If the array is multidimensional, only the first dimension is trimmed.</p>
<p><code>trim_array(ARRAY[1,2,3,4,5,6], 2)</code> {1,2,3,4}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>unnest</code> ( <code>anyarray</code> ) setof anyelement</p>
<p>Expands an array into a set of rows. The array's elements are read out in storage order.</p>
<p><code>unnest(ARRAY[1,2])</code></p>
<pre><code> 1
 2</code></pre>
<p><code>unnest(ARRAY[['foo','bar'],['baz','quux']])</code></p>
<pre><code> foo
 bar
 baz
 quux</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><code>unnest</code> ( <code>anyarray</code>, <code>anyarray</code> [, ...] ) setof anyelement, anyelement [, ... ]</p>
<p>Expands multiple arrays (possibly of different data types) into a set of rows. If the arrays are not all the same length then the shorter ones are padded with <code>NULL</code>s. This form is only allowed in a query's FROM clause; see <a href="#queries-tablefunctions">???</a>.</p>
<p><code>select * from unnest(ARRAY[1,2], ARRAY['foo','bar','baz']) as x(a,b)</code></p>
<pre><code> a |  b
---+-----
 1 | foo
 2 | bar
   | baz</code></pre></td>
</tr>
</tbody>
</table>

See also [Aggregate Functions](#functions-aggregate) about the aggregate function `array_agg` for use with arrays.

## Range/Multirange Functions and Operators

See [???](#rangetypes) for an overview of range types.

[Range Operators](#range-operators-table) shows the specialized operators available for range types. [Multirange Operators](#multirange-operators-table) shows the specialized operators available for multirange types. In addition to those, the usual comparison operators shown in [Comparison Operators](#functions-comparison-op-table) are available for range and multirange types. The comparison operators order first by the range lower bounds, and only if those are equal do they compare the upper bounds. The multirange operators compare each range until one is unequal. This does not usually result in a useful overall ordering, but the operators are provided to allow unique indexes to be constructed on ranges.

<table id="range-operators-table">
<caption>Range Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>@&gt;</code> <code>anyrange</code> boolean</p>
<p>Does the first range contain the second?</p>
<p><code>int4range(2,4) @&gt; int4range(2,3)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>@&gt;</code> <code>anyelement</code> boolean</p>
<p>Does the range contain the element?</p>
<p><code>'[2011-01-01,2011-03-01)'::tsrange @&gt; '2011-01-10'::timestamp</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>&lt;@</code> <code>anyrange</code> boolean</p>
<p>Is the first range contained by the second?</p>
<p><code>int4range(2,4) &lt;@ int4range(1,7)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyelement</code> <code>&lt;@</code> <code>anyrange</code> boolean</p>
<p>Is the element contained in the range?</p>
<p><code>42 &lt;@ int4range(1,7)</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>&amp;&amp;</code> <code>anyrange</code> boolean</p>
<p>Do the ranges overlap, that is, have any elements in common?</p>
<p><code>int8range(3,7) &amp;&amp; int8range(4,12)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>&lt;&lt;</code> <code>anyrange</code> boolean</p>
<p>Is the first range strictly left of the second?</p>
<p><code>int8range(1,10) &lt;&lt; int8range(100,110)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>&gt;&gt;</code> <code>anyrange</code> boolean</p>
<p>Is the first range strictly right of the second?</p>
<p><code>int8range(50,60) &gt;&gt; int8range(20,30)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>&amp;&lt;</code> <code>anyrange</code> boolean</p>
<p>Does the first range not extend to the right of the second?</p>
<p><code>int8range(1,20) &amp;&lt; int8range(18,20)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>&amp;&gt;</code> <code>anyrange</code> boolean</p>
<p>Does the first range not extend to the left of the second?</p>
<p><code>int8range(7,20) &amp;&gt; int8range(5,10)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>-|-</code> <code>anyrange</code> boolean</p>
<p>Are the ranges adjacent?</p>
<p><code>numrange(1.1,2.2) -|- numrange(2.2,3.3)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>+</code> <code>anyrange</code> anyrange</p>
<p>Computes the union of the ranges. The ranges must overlap or be adjacent, so that the union is a single range (but see <code>range_merge()</code>).</p>
<p><code>numrange(5,15) + numrange(10,20)</code> [5,20)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>*</code> <code>anyrange</code> anyrange</p>
<p>Computes the intersection of the ranges.</p>
<p><code>int8range(5,15) * int8range(10,20)</code> [10,15)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>-</code> <code>anyrange</code> anyrange</p>
<p>Computes the difference of the ranges. The second range must not be contained in the first in such a way that the difference would not be a single range.</p>
<p><code>int8range(5,15) - int8range(10,20)</code> [5,10)</p></td>
</tr>
</tbody>
</table>

<table id="multirange-operators-table">
<caption>Multirange Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>@&gt;</code> <code>anymultirange</code> boolean</p>
<p>Does the first multirange contain the second?</p>
<p><code>'{[2,4)}'::int4multirange @&gt; '{[2,3)}'::int4multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>@&gt;</code> <code>anyrange</code> boolean</p>
<p>Does the multirange contain the range?</p>
<p><code>'{[2,4)}'::int4multirange @&gt; int4range(2,3)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>@&gt;</code> <code>anyelement</code> boolean</p>
<p>Does the multirange contain the element?</p>
<p><code>'{[2011-01-01,2011-03-01)}'::tsmultirange @&gt; '2011-01-10'::timestamp</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>@&gt;</code> <code>anymultirange</code> boolean</p>
<p>Does the range contain the multirange?</p>
<p><code>'[2,4)'::int4range @&gt; '{[2,3)}'::int4multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>&lt;@</code> <code>anymultirange</code> boolean</p>
<p>Is the first multirange contained by the second?</p>
<p><code>'{[2,4)}'::int4multirange &lt;@ '{[1,7)}'::int4multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>&lt;@</code> <code>anyrange</code> boolean</p>
<p>Is the multirange contained by the range?</p>
<p><code>'{[2,4)}'::int4multirange &lt;@ int4range(1,7)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>&lt;@</code> <code>anymultirange</code> boolean</p>
<p>Is the range contained by the multirange?</p>
<p><code>int4range(2,4) &lt;@ '{[1,7)}'::int4multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyelement</code> <code>&lt;@</code> <code>anymultirange</code> boolean</p>
<p>Is the element contained by the multirange?</p>
<p><code>4 &lt;@ '{[1,7)}'::int4multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>&amp;&amp;</code> <code>anymultirange</code> boolean</p>
<p>Do the multiranges overlap, that is, have any elements in common?</p>
<p><code>'{[3,7)}'::int8multirange &amp;&amp; '{[4,12)}'::int8multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>&amp;&amp;</code> <code>anyrange</code> boolean</p>
<p>Does the multirange overlap the range?</p>
<p><code>'{[3,7)}'::int8multirange &amp;&amp; int8range(4,12)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>&amp;&amp;</code> <code>anymultirange</code> boolean</p>
<p>Does the range overlap the multirange?</p>
<p><code>int8range(3,7) &amp;&amp; '{[4,12)}'::int8multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>&lt;&lt;</code> <code>anymultirange</code> boolean</p>
<p>Is the first multirange strictly left of the second?</p>
<p><code>'{[1,10)}'::int8multirange &lt;&lt; '{[100,110)}'::int8multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>&lt;&lt;</code> <code>anyrange</code> boolean</p>
<p>Is the multirange strictly left of the range?</p>
<p><code>'{[1,10)}'::int8multirange &lt;&lt; int8range(100,110)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>&lt;&lt;</code> <code>anymultirange</code> boolean</p>
<p>Is the range strictly left of the multirange?</p>
<p><code>int8range(1,10) &lt;&lt; '{[100,110)}'::int8multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>&gt;&gt;</code> <code>anymultirange</code> boolean</p>
<p>Is the first multirange strictly right of the second?</p>
<p><code>'{[50,60)}'::int8multirange &gt;&gt; '{[20,30)}'::int8multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>&gt;&gt;</code> <code>anyrange</code> boolean</p>
<p>Is the multirange strictly right of the range?</p>
<p><code>'{[50,60)}'::int8multirange &gt;&gt; int8range(20,30)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>&gt;&gt;</code> <code>anymultirange</code> boolean</p>
<p>Is the range strictly right of the multirange?</p>
<p><code>int8range(50,60) &gt;&gt; '{[20,30)}'::int8multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>&amp;&lt;</code> <code>anymultirange</code> boolean</p>
<p>Does the first multirange not extend to the right of the second?</p>
<p><code>'{[1,20)}'::int8multirange &amp;&lt; '{[18,20)}'::int8multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>&amp;&lt;</code> <code>anyrange</code> boolean</p>
<p>Does the multirange not extend to the right of the range?</p>
<p><code>'{[1,20)}'::int8multirange &amp;&lt; int8range(18,20)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>&amp;&lt;</code> <code>anymultirange</code> boolean</p>
<p>Does the range not extend to the right of the multirange?</p>
<p><code>int8range(1,20) &amp;&lt; '{[18,20)}'::int8multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>&amp;&gt;</code> <code>anymultirange</code> boolean</p>
<p>Does the first multirange not extend to the left of the second?</p>
<p><code>'{[7,20)}'::int8multirange &amp;&gt; '{[5,10)}'::int8multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>&amp;&gt;</code> <code>anyrange</code> boolean</p>
<p>Does the multirange not extend to the left of the range?</p>
<p><code>'{[7,20)}'::int8multirange &amp;&gt; int8range(5,10)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>&amp;&gt;</code> <code>anymultirange</code> boolean</p>
<p>Does the range not extend to the left of the multirange?</p>
<p><code>int8range(7,20) &amp;&gt; '{[5,10)}'::int8multirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>-|-</code> <code>anymultirange</code> boolean</p>
<p>Are the multiranges adjacent?</p>
<p><code>'{[1.1,2.2)}'::nummultirange -|- '{[2.2,3.3)}'::nummultirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>-|-</code> <code>anyrange</code> boolean</p>
<p>Is the multirange adjacent to the range?</p>
<p><code>'{[1.1,2.2)}'::nummultirange -|- numrange(2.2,3.3)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anyrange</code> <code>-|-</code> <code>anymultirange</code> boolean</p>
<p>Is the range adjacent to the multirange?</p>
<p><code>numrange(1.1,2.2) -|- '{[2.2,3.3)}'::nummultirange</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>+</code> <code>anymultirange</code> anymultirange</p>
<p>Computes the union of the multiranges. The multiranges need not overlap or be adjacent.</p>
<p><code>'{[5,10)}'::nummultirange + '{[15,20)}'::nummultirange</code> {[5,10), [15,20)}</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>*</code> <code>anymultirange</code> anymultirange</p>
<p>Computes the intersection of the multiranges.</p>
<p><code>'{[5,15)}'::int8multirange * '{[10,20)}'::int8multirange</code> {[10,15)}</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>anymultirange</code> <code>-</code> <code>anymultirange</code> anymultirange</p>
<p>Computes the difference of the multiranges.</p>
<p><code>'{[5,20)}'::int8multirange - '{[10,15)}'::int8multirange</code> {[5,10), [15,20)}</p></td>
</tr>
</tbody>
</table>

The left-of/right-of/adjacent operators always return false when an empty range or multirange is involved; that is, an empty range is not considered to be either before or after any other range.

Elsewhere empty ranges and multiranges are treated as the additive identity: anything unioned with an empty value is itself. Anything minus an empty value is itself. An empty multirange has exactly the same points as an empty range. Every range contains the empty range. Every multirange contains as many empty ranges as you like.

The range union and difference operators will fail if the resulting range would need to contain two disjoint sub-ranges, as such a range cannot be represented. There are separate operators for union and difference that take multirange parameters and return a multirange, and they do not fail even if their arguments are disjoint. So if you need a union or difference operation for ranges that may be disjoint, you can avoid errors by first casting your ranges to multiranges.

[Range Functions](#range-functions-table) shows the functions available for use with range types. [Multirange Functions](#multirange-functions-table) shows the functions available for use with multirange types.

<table id="range-functions-table">
<caption>Range Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lower</code> ( <code>anyrange</code> ) anyelement</p>
<p>Extracts the lower bound of the range (<code>NULL</code> if the range is empty or has no lower bound).</p>
<p><code>lower(numrange(1.1,2.2))</code> 1.1</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>upper</code> ( <code>anyrange</code> ) anyelement</p>
<p>Extracts the upper bound of the range (<code>NULL</code> if the range is empty or has no upper bound).</p>
<p><code>upper(numrange(1.1,2.2))</code> 2.2</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>isempty</code> ( <code>anyrange</code> ) boolean</p>
<p>Is the range empty?</p>
<p><code>isempty(numrange(1.1,2.2))</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lower_inc</code> ( <code>anyrange</code> ) boolean</p>
<p>Is the range's lower bound inclusive?</p>
<p><code>lower_inc(numrange(1.1,2.2))</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>upper_inc</code> ( <code>anyrange</code> ) boolean</p>
<p>Is the range's upper bound inclusive?</p>
<p><code>upper_inc(numrange(1.1,2.2))</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lower_inf</code> ( <code>anyrange</code> ) boolean</p>
<p>Does the range have no lower bound? (A lower bound of <code>-Infinity</code> returns false.)</p>
<p><code>lower_inf('(,)'::daterange)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>upper_inf</code> ( <code>anyrange</code> ) boolean</p>
<p>Does the range have no upper bound? (An upper bound of <code>Infinity</code> returns false.)</p>
<p><code>upper_inf('(,)'::daterange)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>range_merge</code> ( <code>anyrange</code>, <code>anyrange</code> ) anyrange</p>
<p>Computes the smallest range that includes both of the given ranges.</p>
<p><code>range_merge('[1,2)'::int4range, '[3,4)'::int4range)</code> [1,4)</p></td>
</tr>
</tbody>
</table>

<table id="multirange-functions-table">
<caption>Multirange Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lower</code> ( <code>anymultirange</code> ) anyelement</p>
<p>Extracts the lower bound of the multirange (<code>NULL</code> if the multirange is empty has no lower bound).</p>
<p><code>lower('{[1.1,2.2)}'::nummultirange)</code> 1.1</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>upper</code> ( <code>anymultirange</code> ) anyelement</p>
<p>Extracts the upper bound of the multirange (<code>NULL</code> if the multirange is empty or has no upper bound).</p>
<p><code>upper('{[1.1,2.2)}'::nummultirange)</code> 2.2</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>isempty</code> ( <code>anymultirange</code> ) boolean</p>
<p>Is the multirange empty?</p>
<p><code>isempty('{[1.1,2.2)}'::nummultirange)</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lower_inc</code> ( <code>anymultirange</code> ) boolean</p>
<p>Is the multirange's lower bound inclusive?</p>
<p><code>lower_inc('{[1.1,2.2)}'::nummultirange)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>upper_inc</code> ( <code>anymultirange</code> ) boolean</p>
<p>Is the multirange's upper bound inclusive?</p>
<p><code>upper_inc('{[1.1,2.2)}'::nummultirange)</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lower_inf</code> ( <code>anymultirange</code> ) boolean</p>
<p>Does the multirange have no lower bound? (A lower bound of <code>-Infinity</code> returns false.)</p>
<p><code>lower_inf('{(,)}'::datemultirange)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>upper_inf</code> ( <code>anymultirange</code> ) boolean</p>
<p>Does the multirange have no upper bound? (An upper bound of <code>Infinity</code> returns false.)</p>
<p><code>upper_inf('{(,)}'::datemultirange)</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>range_merge</code> ( <code>anymultirange</code> ) anyrange</p>
<p>Computes the smallest range that includes the entire multirange.</p>
<p><code>range_merge('{[1,2), [3,4)}'::int4multirange)</code> [1,4)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>multirange</code> ( <code>anyrange</code> ) anymultirange</p>
<p>Returns a multirange containing just the given range.</p>
<p><code>multirange('[1,2)'::int4range)</code> {[1,2)}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>unnest</code> ( <code>anymultirange</code> ) setof anyrange</p>
<p>Expands a multirange into a set of ranges in ascending order.</p>
<p><code>unnest('{[1,2), [3,4)}'::int4multirange)</code></p>
<pre><code> [1,2)
 [3,4)</code></pre></td>
</tr>
</tbody>
</table>

The `lower_inc`, `upper_inc`, `lower_inf`, and `upper_inf` functions all return false for an empty range or multirange.

## Aggregate Functions

aggregate function

built-in

Aggregate functions compute a single result from a set of input values. The built-in general-purpose aggregate functions are listed in [General-Purpose Aggregate Functions](#functions-aggregate-table) while statistical aggregates are in [Aggregate Functions for Statistics](#functions-aggregate-statistics-table). The built-in within-group ordered-set aggregate functions are listed in [Ordered-Set Aggregate Functions](#functions-orderedset-table) while the built-in within-group hypothetical-set ones are in [Hypothetical-Set Aggregate Functions](#functions-hypothetical-table). Grouping operations, which are closely related to aggregate functions, are listed in [Grouping Operations](#functions-grouping-table). The special syntax considerations for aggregate functions are explained in [???](#syntax-aggregates). Consult [???](#tutorial-agg) for additional introductory information.

Aggregate functions that support Partial Mode are eligible to participate in various optimizations, such as parallel aggregation.

While all aggregates below accept an optional `ORDER BY` clause (as outlined in [???](#syntax-aggregates)), the clause has only been added to aggregates whose output is affected by ordering.

<table id="functions-aggregate-table">
<caption>General-Purpose Aggregate Functions</caption>
<colgroup>
<col style="width: 90%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
<th>Partial Mode</th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>any_value</code> ( <code>anyelement</code> ) &lt;same as input type&gt;</p>
<p>Returns an arbitrary value from the non-null input values.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>array_agg</code> ( <code>anynonarray</code> <code>ORDER BY</code> <code>input_sort_columns</code> ) anyarray</p>
<p>Collects all the input values, including nulls, into an array.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><code>array_agg</code> ( <code>anyarray</code> <code>ORDER BY</code> <code>input_sort_columns</code> ) anyarray</p>
<p>Concatenates all the input arrays into an array of one higher dimension. (The inputs must all have the same dimensionality, and cannot be empty or null.)</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>avg</code> ( <code>smallint</code> ) numeric</p>
<p role="func_signature"><code>avg</code> ( <code>integer</code> ) numeric</p>
<p role="func_signature"><code>avg</code> ( <code>bigint</code> ) numeric</p>
<p role="func_signature"><code>avg</code> ( <code>numeric</code> ) numeric</p>
<p role="func_signature"><code>avg</code> ( <code>real</code> ) double precision</p>
<p role="func_signature"><code>avg</code> ( <code>double precision</code> ) double precision</p>
<p role="func_signature"><code>avg</code> ( <code>interval</code> ) interval</p>
<p>Computes the average (arithmetic mean) of all the non-null input values.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>bit_and</code> ( <code>smallint</code> ) smallint</p>
<p role="func_signature"><code>bit_and</code> ( <code>integer</code> ) integer</p>
<p role="func_signature"><code>bit_and</code> ( <code>bigint</code> ) bigint</p>
<p role="func_signature"><code>bit_and</code> ( <code>bit</code> ) bit</p>
<p>Computes the bitwise AND of all non-null input values.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>bit_or</code> ( <code>smallint</code> ) smallint</p>
<p role="func_signature"><code>bit_or</code> ( <code>integer</code> ) integer</p>
<p role="func_signature"><code>bit_or</code> ( <code>bigint</code> ) bigint</p>
<p role="func_signature"><code>bit_or</code> ( <code>bit</code> ) bit</p>
<p>Computes the bitwise OR of all non-null input values.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>bit_xor</code> ( <code>smallint</code> ) smallint</p>
<p role="func_signature"><code>bit_xor</code> ( <code>integer</code> ) integer</p>
<p role="func_signature"><code>bit_xor</code> ( <code>bigint</code> ) bigint</p>
<p role="func_signature"><code>bit_xor</code> ( <code>bit</code> ) bit</p>
<p>Computes the bitwise exclusive OR of all non-null input values. Can be useful as a checksum for an unordered set of values.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>bool_and</code> ( <code>boolean</code> ) boolean</p>
<p>Returns true if all non-null input values are true, otherwise false.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>bool_or</code> ( <code>boolean</code> ) boolean</p>
<p>Returns true if any non-null input value is true, otherwise false.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>count</code> ( <code>*</code> ) bigint</p>
<p>Computes the number of input rows.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><code>count</code> ( <code>"any"</code> ) bigint</p>
<p>Computes the number of input rows in which the input value is not null.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>every</code> ( <code>boolean</code> ) boolean</p>
<p>This is the SQL standard's equivalent to <code>bool_and</code>.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_agg</code> ( <code>anyelement</code> <code>ORDER BY</code> <code>input_sort_columns</code> ) json</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_agg</code> ( <code>anyelement</code> <code>ORDER BY</code> <code>input_sort_columns</code> ) jsonb</p>
<p>Collects all the input values, including nulls, into a JSON array. Values are converted to JSON as per <code>to_json</code> or <code>to_jsonb</code>.</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_agg_strict</code> ( <code>anyelement</code> ) json</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_agg_strict</code> ( <code>anyelement</code> ) jsonb</p>
<p>Collects all the input values, skipping nulls, into a JSON array. Values are converted to JSON as per <code>to_json</code> or <code>to_jsonb</code>.</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_arrayagg</code> ( [&lt;value_expression&gt;] [<code>ORDER BY</code> &lt;sort_expression&gt;] [{ <code>NULL</code> | <code>ABSENT</code> } <code>ON NULL</code>] [<code>RETURNING</code> &lt;data_type&gt; [<code>FORMAT JSON</code> [<code>ENCODING UTF8</code>]]])</p>
<p>Behaves in the same way as <code>json_array</code> but as an aggregate function so it only takes one &lt;value_expression&gt; parameter. If <code>ABSENT ON NULL</code> is specified, any NULL values are omitted. If <code>ORDER BY</code> is specified, the elements will appear in the array in that order rather than in the input order.</p>
<p><code>SELECT json_arrayagg(v) FROM (VALUES(2),(1)) t(v)</code> [2, 1]</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_objectagg</code> ( [{ &lt;key_expression&gt; { <code>VALUE</code> | ':' } &lt;value_expression&gt; }] [{ <code>NULL</code> | <code>ABSENT</code> } <code>ON NULL</code>] [{ <code>WITH</code> | <code>WITHOUT</code> } <code>UNIQUE</code> [<code>KEYS</code>]] [<code>RETURNING</code> &lt;data_type&gt; [<code>FORMAT JSON</code> [<code>ENCODING UTF8</code>]]])</p>
<p>Behaves like <code>json_object</code>, but as an aggregate function, so it only takes one &lt;key_expression&gt; and one &lt;value_expression&gt; parameter.</p>
<p><code>SELECT json_objectagg(k:v) FROM (VALUES ('a'::text,current_date),('b',current_date + 1)) AS t(k,v)</code> { "a" : "2022-05-10", "b" : "2022-05-11" }</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_object_agg</code> ( <code>key</code> <code>"any"</code>, <code>value</code> <code>"any"</code> <code>ORDER BY</code> <code>input_sort_columns</code> ) json</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_object_agg</code> ( <code>key</code> <code>"any"</code>, <code>value</code> <code>"any"</code> <code>ORDER BY</code> <code>input_sort_columns</code> ) jsonb</p>
<p>Collects all the key/value pairs into a JSON object. Key arguments are coerced to text; value arguments are converted as per <code>to_json</code> or <code>to_jsonb</code>. Values can be null, but keys cannot.</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_object_agg_strict</code> ( <code>key</code> <code>"any"</code>, <code>value</code> <code>"any"</code> ) json</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_object_agg_strict</code> ( <code>key</code> <code>"any"</code>, <code>value</code> <code>"any"</code> ) jsonb</p>
<p>Collects all the key/value pairs into a JSON object. Key arguments are coerced to text; value arguments are converted as per <code>to_json</code> or <code>to_jsonb</code>. The <code>key</code> can not be null. If the <code>value</code> is null then the entry is skipped,</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_object_agg_unique</code> ( <code>key</code> <code>"any"</code>, <code>value</code> <code>"any"</code> ) json</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_object_agg_unique</code> ( <code>key</code> <code>"any"</code>, <code>value</code> <code>"any"</code> ) jsonb</p>
<p>Collects all the key/value pairs into a JSON object. Key arguments are coerced to text; value arguments are converted as per <code>to_json</code> or <code>to_jsonb</code>. Values can be null, but keys cannot. If there is a duplicate key an error is thrown.</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>json_object_agg_unique_strict</code> ( <code>key</code> <code>"any"</code>, <code>value</code> <code>"any"</code> ) json</p>
<p role="func_signature"><span class="indexterm"></span> <code>jsonb_object_agg_unique_strict</code> ( <code>key</code> <code>"any"</code>, <code>value</code> <code>"any"</code> ) jsonb</p>
<p>Collects all the key/value pairs into a JSON object. Key arguments are coerced to text; value arguments are converted as per <code>to_json</code> or <code>to_jsonb</code>. The <code>key</code> can not be null. If the <code>value</code> is null then the entry is skipped. If there is a duplicate key an error is thrown.</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>max</code> ( &lt;see text&gt; ) &lt;same as input type&gt;</p>
<p>Computes the maximum of the non-null input values. Available for any numeric, string, date/time, or enum type, as well as <code>inet</code>, <code>interval</code>, <code>money</code>, <code>oid</code>, <code>pg_lsn</code>, <code>tid</code>, <code>xid8</code>, and arrays of any of these types.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>min</code> ( &lt;see text&gt; ) &lt;same as input type&gt;</p>
<p>Computes the minimum of the non-null input values. Available for any numeric, string, date/time, or enum type, as well as <code>inet</code>, <code>interval</code>, <code>money</code>, <code>oid</code>, <code>pg_lsn</code>, <code>tid</code>, <code>xid8</code>, and arrays of any of these types.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>range_agg</code> ( <code>value</code> <code>anyrange</code> ) anymultirange</p>
<p role="func_signature"><code>range_agg</code> ( <code>value</code> <code>anymultirange</code> ) anymultirange</p>
<p>Computes the union of the non-null input values.</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>range_intersect_agg</code> ( <code>value</code> <code>anyrange</code> ) anyrange</p>
<p role="func_signature"><code>range_intersect_agg</code> ( <code>value</code> <code>anymultirange</code> ) anymultirange</p>
<p>Computes the intersection of the non-null input values.</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>string_agg</code> ( <code>value</code> <code>text</code>, <code>delimiter</code> <code>text</code> ) text</p>
<p role="func_signature"><code>string_agg</code> ( <code>value</code> <code>bytea</code>, <code>delimiter</code> <code>bytea</code> <code>ORDER BY</code> <code>input_sort_columns</code> ) bytea</p>
<p>Concatenates the non-null input values into a string. Each value after the first is preceded by the corresponding <code>delimiter</code> (if it's not null).</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>sum</code> ( <code>smallint</code> ) bigint</p>
<p role="func_signature"><code>sum</code> ( <code>integer</code> ) bigint</p>
<p role="func_signature"><code>sum</code> ( <code>bigint</code> ) numeric</p>
<p role="func_signature"><code>sum</code> ( <code>numeric</code> ) numeric</p>
<p role="func_signature"><code>sum</code> ( <code>real</code> ) real</p>
<p role="func_signature"><code>sum</code> ( <code>double precision</code> ) double precision</p>
<p role="func_signature"><code>sum</code> ( <code>interval</code> ) interval</p>
<p role="func_signature"><code>sum</code> ( <code>money</code> ) money</p>
<p>Computes the sum of the non-null input values.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>xmlagg</code> ( <code>xml</code> <code>ORDER BY</code> <code>input_sort_columns</code> ) xml</p>
<p>Concatenates the non-null XML input values (see <a href="#functions-xml-xmlagg"></a>).</p></td>
<td>No</td>
</tr>
</tbody>
</table>

It should be noted that except for `count`, these functions return a null value when no rows are selected. In particular, `sum` of no rows returns null, not zero as one might expect, and `array_agg` returns null rather than an empty array when there are no input rows. The `coalesce` function can be used to substitute zero or an empty array for null when necessary.

The aggregate functions `array_agg`, `json_agg`, `jsonb_agg`, `json_agg_strict`, `jsonb_agg_strict`, `json_object_agg`, `jsonb_object_agg`, `json_object_agg_strict`, `jsonb_object_agg_strict`, `json_object_agg_unique`, `jsonb_object_agg_unique`, `json_object_agg_unique_strict`, `jsonb_object_agg_unique_strict`, `string_agg`, and `xmlagg`, as well as similar user-defined aggregate functions, produce meaningfully different result values depending on the order of the input values. This ordering is unspecified by default, but can be controlled by writing an `ORDER BY` clause within the aggregate call, as shown in [???](#syntax-aggregates). Alternatively, supplying the input values from a sorted subquery will usually work. For example:

    SELECT xmlagg(x) FROM (SELECT x FROM test ORDER BY y DESC) AS tab;

Beware that this approach can fail if the outer query level contains additional processing, such as a join, because that might cause the subquery's output to be reordered before the aggregate is computed.

> [!NOTE]
> ANY
>
> SOME
>
> The boolean aggregates `bool_and` and `bool_or` correspond to the standard SQL aggregates `every` and `any` or `some`. PostgreSQL supports `every`, but not `any` or `some`, because there is an ambiguity built into the standard syntax:
>
>     SELECT b1 = ANY((SELECT b2 FROM t2 ...)) FROM t1 ...;
>
> Here `ANY` can be considered either as introducing a subquery, or as being an aggregate function, if the subquery returns one row with a Boolean value. Thus the standard name cannot be given to these aggregates.

> [!NOTE]
> Users accustomed to working with other SQL database management systems might be disappointed by the performance of the `count` aggregate when it is applied to the entire table. A query like:
>
>     SELECT count(*) FROM sometable;
>
> will require effort proportional to the size of the table: PostgreSQL will need to scan either the entire table or the entirety of an index that includes all rows in the table.

[Aggregate Functions for Statistics](#functions-aggregate-statistics-table) shows aggregate functions typically used in statistical analysis. (These are separated out merely to avoid cluttering the listing of more-commonly-used aggregates.) Functions shown as accepting \<numeric_type\> are available for all the types `smallint`, `integer`, `bigint`, `numeric`, `real`, and `double precision`. Where the description mentions `N`, it means the number of input rows for which all the input expressions are non-null. In all cases, null is returned if the computation is meaningless, for example when `N` is zero.

statistics

linear regression

<table id="functions-aggregate-statistics-table">
<caption>Aggregate Functions for Statistics</caption>
<colgroup>
<col style="width: 90%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
<th>Partial Mode</th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>corr</code> ( <code>Y</code> <code>double precision</code>, <code>X</code> <code>double precision</code> ) double precision</p>
<p>Computes the correlation coefficient.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>covar_pop</code> ( <code>Y</code> <code>double precision</code>, <code>X</code> <code>double precision</code> ) double precision</p>
<p>Computes the population covariance.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>covar_samp</code> ( <code>Y</code> <code>double precision</code>, <code>X</code> <code>double precision</code> ) double precision</p>
<p>Computes the sample covariance.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regr_avgx</code> ( <code>Y</code> <code>double precision</code>, <code>X</code> <code>double precision</code> ) double precision</p>
<p>Computes the average of the independent variable, <code>sum(X)/N</code>.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regr_avgy</code> ( <code>Y</code> <code>double precision</code>, <code>X</code> <code>double precision</code> ) double precision</p>
<p>Computes the average of the dependent variable, <code>sum(Y)/N</code>.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regr_count</code> ( <code>Y</code> <code>double precision</code>, <code>X</code> <code>double precision</code> ) bigint</p>
<p>Computes the number of rows in which both inputs are non-null.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>regr_intercept</code> ( <code>Y</code> <code>double precision</code>, <code>X</code> <code>double precision</code> ) double precision</p>
<p>Computes the y-intercept of the least-squares-fit linear equation determined by the (<code>X</code>, <code>Y</code>) pairs.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regr_r2</code> ( <code>Y</code> <code>double precision</code>, <code>X</code> <code>double precision</code> ) double precision</p>
<p>Computes the square of the correlation coefficient.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>regr_slope</code> ( <code>Y</code> <code>double precision</code>, <code>X</code> <code>double precision</code> ) double precision</p>
<p>Computes the slope of the least-squares-fit linear equation determined by the (<code>X</code>, <code>Y</code>) pairs.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regr_sxx</code> ( <code>Y</code> <code>double precision</code>, <code>X</code> <code>double precision</code> ) double precision</p>
<p>Computes the “sum of squares” of the independent variable, <code>sum(X^2) - sum(X)^2/N</code>.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regr_sxy</code> ( <code>Y</code> <code>double precision</code>, <code>X</code> <code>double precision</code> ) double precision</p>
<p>Computes the “sum of products” of independent times dependent variables, <code>sum(X*Y) - sum(X) * sum(Y)/N</code>.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>regr_syy</code> ( <code>Y</code> <code>double precision</code>, <code>X</code> <code>double precision</code> ) double precision</p>
<p>Computes the “sum of squares” of the dependent variable, <code>sum(Y^2) - sum(Y)^2/N</code>.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>stddev</code> ( &lt;numeric_type&gt; ) <code>double precision</code> for <code>real</code> or <code>double precision</code>, otherwise <code>numeric</code></p>
<p>This is a historical alias for <code>stddev_samp</code>.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>stddev_pop</code> ( &lt;numeric_type&gt; ) <code>double precision</code> for <code>real</code> or <code>double precision</code>, otherwise <code>numeric</code></p>
<p>Computes the population standard deviation of the input values.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>stddev_samp</code> ( &lt;numeric_type&gt; ) <code>double precision</code> for <code>real</code> or <code>double precision</code>, otherwise <code>numeric</code></p>
<p>Computes the sample standard deviation of the input values.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>variance</code> ( &lt;numeric_type&gt; ) <code>double precision</code> for <code>real</code> or <code>double precision</code>, otherwise <code>numeric</code></p>
<p>This is a historical alias for <code>var_samp</code>.</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>var_pop</code> ( &lt;numeric_type&gt; ) <code>double precision</code> for <code>real</code> or <code>double precision</code>, otherwise <code>numeric</code></p>
<p>Computes the population variance of the input values (square of the population standard deviation).</p></td>
<td>Yes</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>var_samp</code> ( &lt;numeric_type&gt; ) <code>double precision</code> for <code>real</code> or <code>double precision</code>, otherwise <code>numeric</code></p>
<p>Computes the sample variance of the input values (square of the sample standard deviation).</p></td>
<td>Yes</td>
</tr>
</tbody>
</table>

[Ordered-Set Aggregate Functions](#functions-orderedset-table) shows some aggregate functions that use the ordered-set aggregate syntax. These functions are sometimes referred to as “inverse distribution” functions. Their aggregated input is introduced by `ORDER BY`, and they may also take a direct argument that is not aggregated, but is computed only once. All these functions ignore null values in their aggregated input. For those that take a `fraction` parameter, the fraction value must be between 0 and 1; an error is thrown if not. However, a null `fraction` value simply produces a null result.

ordered-set aggregate

built-in

inverse distribution

<table id="functions-orderedset-table">
<caption>Ordered-Set Aggregate Functions</caption>
<colgroup>
<col style="width: 90%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
<th>Partial Mode</th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>mode</code> () <code>WITHIN GROUP</code> ( <code>ORDER BY</code> <code>anyelement</code> ) anyelement</p>
<p>Computes the mode, the most frequent value of the aggregated argument (arbitrarily choosing the first one if there are multiple equally-frequent values). The aggregated argument must be of a sortable type.</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>percentile_cont</code> ( <code>fraction</code> <code>double precision</code> ) <code>WITHIN GROUP</code> ( <code>ORDER BY</code> <code>double precision</code> ) double precision</p>
<p role="func_signature"><code>percentile_cont</code> ( <code>fraction</code> <code>double precision</code> ) <code>WITHIN GROUP</code> ( <code>ORDER BY</code> <code>interval</code> ) interval</p>
<p>Computes the continuous percentile, a value corresponding to the specified <code>fraction</code> within the ordered set of aggregated argument values. This will interpolate between adjacent input items if needed.</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><code>percentile_cont</code> ( <code>fractions</code> <code>double precision[]</code> ) <code>WITHIN GROUP</code> ( <code>ORDER BY</code> <code>double precision</code> ) double precision[]</p>
<p role="func_signature"><code>percentile_cont</code> ( <code>fractions</code> <code>double precision[]</code> ) <code>WITHIN GROUP</code> ( <code>ORDER BY</code> <code>interval</code> ) interval[]</p>
<p>Computes multiple continuous percentiles. The result is an array of the same dimensions as the <code>fractions</code> parameter, with each non-null element replaced by the (possibly interpolated) value corresponding to that percentile.</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>percentile_disc</code> ( <code>fraction</code> <code>double precision</code> ) <code>WITHIN GROUP</code> ( <code>ORDER BY</code> <code>anyelement</code> ) anyelement</p>
<p>Computes the discrete percentile, the first value within the ordered set of aggregated argument values whose position in the ordering equals or exceeds the specified <code>fraction</code>. The aggregated argument must be of a sortable type.</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><code>percentile_disc</code> ( <code>fractions</code> <code>double precision[]</code> ) <code>WITHIN GROUP</code> ( <code>ORDER BY</code> <code>anyelement</code> ) anyarray</p>
<p>Computes multiple discrete percentiles. The result is an array of the same dimensions as the <code>fractions</code> parameter, with each non-null element replaced by the input value corresponding to that percentile. The aggregated argument must be of a sortable type.</p></td>
<td>No</td>
</tr>
</tbody>
</table>

hypothetical-set aggregate

built-in

Each of the “hypothetical-set” aggregates listed in [Hypothetical-Set Aggregate Functions](#functions-hypothetical-table) is associated with a window function of the same name defined in [Window Functions](#functions-window). In each case, the aggregate's result is the value that the associated window function would have returned for the “hypothetical” row constructed from \<args\>, if such a row had been added to the sorted group of rows represented by the \<sorted_args\>. For each of these functions, the list of direct arguments given in \<args\> must match the number and types of the aggregated arguments given in \<sorted_args\>. Unlike most built-in aggregates, these aggregates are not strict, that is they do not drop input rows containing nulls. Null values sort according to the rule specified in the `ORDER BY` clause.

<table id="functions-hypothetical-table">
<caption>Hypothetical-Set Aggregate Functions</caption>
<colgroup>
<col style="width: 90%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
<th>Partial Mode</th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>rank</code> ( &lt;args&gt; ) <code>WITHIN GROUP</code> ( <code>ORDER BY</code> &lt;sorted_args&gt; ) bigint</p>
<p>Computes the rank of the hypothetical row, with gaps; that is, the row number of the first row in its peer group.</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>dense_rank</code> ( &lt;args&gt; ) <code>WITHIN GROUP</code> ( <code>ORDER BY</code> &lt;sorted_args&gt; ) bigint</p>
<p>Computes the rank of the hypothetical row, without gaps; this function effectively counts peer groups.</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>percent_rank</code> ( &lt;args&gt; ) <code>WITHIN GROUP</code> ( <code>ORDER BY</code> &lt;sorted_args&gt; ) double precision</p>
<p>Computes the relative rank of the hypothetical row, that is (<code>rank</code> - 1) / (total rows - 1). The value thus ranges from 0 to 1 inclusive.</p></td>
<td>No</td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>cume_dist</code> ( &lt;args&gt; ) <code>WITHIN GROUP</code> ( <code>ORDER BY</code> &lt;sorted_args&gt; ) double precision</p>
<p>Computes the cumulative distribution, that is (number of rows preceding or peers with hypothetical row) / (total rows). The value thus ranges from 1/<code>N</code> to 1.</p></td>
<td>No</td>
</tr>
</tbody>
</table>

<table id="functions-grouping-table">
<caption>Grouping Operations</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>GROUPING</code> ( &lt;group_by_expression(s)&gt; ) integer</p>
<p>Returns a bit mask indicating which <code>GROUP BY</code> expressions are not included in the current grouping set. Bits are assigned with the rightmost argument corresponding to the least-significant bit; each bit is 0 if the corresponding expression is included in the grouping criteria of the grouping set generating the current result row, and 1 if it is not included.</p></td>
</tr>
</tbody>
</table>

The grouping operations shown in [Grouping Operations](#functions-grouping-table) are used in conjunction with grouping sets (see [???](#queries-grouping-sets)) to distinguish result rows. The arguments to the `GROUPING` function are not actually evaluated, but they must exactly match expressions given in the `GROUP BY` clause of the associated query level. For example:

    => SELECT * FROM items_sold;
     make  | model | sales
    -------+-------+-------
     Foo   | GT    |  10
     Foo   | Tour  |  20
     Bar   | City  |  15
     Bar   | Sport |  5
    (4 rows)

    => SELECT make, model, GROUPING(make,model), sum(sales) FROM items_sold GROUP BY ROLLUP(make,model);
     make  | model | grouping | sum
    -------+-------+----------+-----
     Foo   | GT    |        0 | 10
     Foo   | Tour  |        0 | 20
     Bar   | City  |        0 | 15
     Bar   | Sport |        0 | 5
     Foo   |       |        1 | 30
     Bar   |       |        1 | 20
           |       |        3 | 50
    (7 rows)

Here, the `grouping` value `0` in the first four rows shows that those have been grouped normally, over both the grouping columns. The value `1` indicates that `model` was not grouped by in the next-to-last two rows, and the value `3` indicates that neither `make` nor `model` was grouped by in the last row (which therefore is an aggregate over all the input rows).

## Window Functions

window function

built-in

Window functions provide the ability to perform calculations across sets of rows that are related to the current query row. See [???](#tutorial-window) for an introduction to this feature, and [???](#syntax-window-functions) for syntax details.

The built-in window functions are listed in [General-Purpose Window Functions](#functions-window-table). Note that these functions *must* be invoked using window function syntax, i.e., an `OVER` clause is required.

In addition to these functions, any built-in or user-defined ordinary aggregate (i.e., not ordered-set or hypothetical-set aggregates) can be used as a window function; see [Aggregate Functions](#functions-aggregate) for a list of the built-in aggregates. Aggregate functions act as window functions only when an `OVER` clause follows the call; otherwise they act as plain aggregates and return a single row for the entire set.

<table id="functions-window-table">
<caption>General-Purpose Window Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>row_number</code> () bigint</p>
<p>Returns the number of the current row within its partition, counting from 1.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>rank</code> () bigint</p>
<p>Returns the rank of the current row, with gaps; that is, the <code>row_number</code> of the first row in its peer group.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>dense_rank</code> () bigint</p>
<p>Returns the rank of the current row, without gaps; this function effectively counts peer groups.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>percent_rank</code> () double precision</p>
<p>Returns the relative rank of the current row, that is (<code>rank</code> - 1) / (total partition rows - 1). The value thus ranges from 0 to 1 inclusive.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>cume_dist</code> () double precision</p>
<p>Returns the cumulative distribution, that is (number of partition rows preceding or peers with current row) / (total partition rows). The value thus ranges from 1/<code>N</code> to 1.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ntile</code> ( <code>num_buckets</code> <code>integer</code> ) integer</p>
<p>Returns an integer ranging from 1 to the argument value, dividing the partition as equally as possible.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lag</code> ( <code>value</code> <code>anycompatible</code> [, <code>offset</code> <code>integer</code> [, <code>default</code> <code>anycompatible</code>]] ) anycompatible</p>
<p>Returns <code>value</code> evaluated at the row that is <code>offset</code> rows before the current row within the partition; if there is no such row, instead returns <code>default</code> (which must be of a type compatible with <code>value</code>). Both <code>offset</code> and <code>default</code> are evaluated with respect to the current row. If omitted, <code>offset</code> defaults to 1 and <code>default</code> to <code>NULL</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lead</code> ( <code>value</code> <code>anycompatible</code> [, <code>offset</code> <code>integer</code> [, <code>default</code> <code>anycompatible</code>]] ) anycompatible</p>
<p>Returns <code>value</code> evaluated at the row that is <code>offset</code> rows after the current row within the partition; if there is no such row, instead returns <code>default</code> (which must be of a type compatible with <code>value</code>). Both <code>offset</code> and <code>default</code> are evaluated with respect to the current row. If omitted, <code>offset</code> defaults to 1 and <code>default</code> to <code>NULL</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>first_value</code> ( <code>value</code> <code>anyelement</code> ) anyelement</p>
<p>Returns <code>value</code> evaluated at the row that is the first row of the window frame.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>last_value</code> ( <code>value</code> <code>anyelement</code> ) anyelement</p>
<p>Returns <code>value</code> evaluated at the row that is the last row of the window frame.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>nth_value</code> ( <code>value</code> <code>anyelement</code>, <code>n</code> <code>integer</code> ) anyelement</p>
<p>Returns <code>value</code> evaluated at the row that is the <code>n</code>'th row of the window frame (counting from 1); returns <code>NULL</code> if there is no such row.</p></td>
</tr>
</tbody>
</table>

All of the functions listed in [General-Purpose Window Functions](#functions-window-table) depend on the sort ordering specified by the `ORDER BY` clause of the associated window definition. Rows that are not distinct when considering only the `ORDER BY` columns are said to be peers. The four ranking functions (including `cume_dist`) are defined so that they give the same answer for all rows of a peer group.

Note that `first_value`, `last_value`, and `nth_value` consider only the rows within the “window frame”, which by default contains the rows from the start of the partition through the last peer of the current row. This is likely to give unhelpful results for `last_value` and sometimes also `nth_value`. You can redefine the frame by adding a suitable frame specification (`RANGE`, `ROWS` or `GROUPS`) to the `OVER` clause. See [???](#syntax-window-functions) for more information about frame specifications.

When an aggregate function is used as a window function, it aggregates over the rows within the current row's window frame. An aggregate used with `ORDER BY` and the default window frame definition produces a “running sum” type of behavior, which may or may not be what's wanted. To obtain aggregation over the whole partition, omit `ORDER BY` or use `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`. Other frame specifications can be used to obtain other effects.

> [!NOTE]
> The SQL standard defines a `RESPECT NULLS` or `IGNORE NULLS` option for `lead`, `lag`, `first_value`, `last_value`, and `nth_value`. This is not implemented in PostgreSQL: the behavior is always the same as the standard's default, namely `RESPECT NULLS`. Likewise, the standard's `FROM FIRST` or `FROM LAST` option for `nth_value` is not implemented: only the default `FROM FIRST` behavior is supported. (You can achieve the result of `FROM LAST` by reversing the `ORDER BY` ordering.)

## Merge Support Functions

MERGE

RETURNING

PostgreSQL includes one merge support function that may be used in the `RETURNING` list of a [???](#sql-merge) command to identify the action taken for each row; see [Merge Support Functions](#functions-merge-support-table).

<table id="functions-merge-support-table">
<caption>Merge Support Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>merge_action</code> ( ) text</p>
<p>Returns the merge action command executed for the current row. This will be <code>'INSERT'</code>, <code>'UPDATE'</code>, or <code>'DELETE'</code>.</p></td>
</tr>
</tbody>
</table>

Example:

    MERGE INTO products p
      USING stock s ON p.product_id = s.product_id
      WHEN MATCHED AND s.quantity > 0 THEN
        UPDATE SET in_stock = true, quantity = s.quantity
      WHEN MATCHED THEN
        UPDATE SET in_stock = false, quantity = 0
      WHEN NOT MATCHED THEN
        INSERT (product_id, in_stock, quantity)
          VALUES (s.product_id, true, s.quantity)
      RETURNING merge_action(), p.*;

     merge_action | product_id | in_stock | quantity
    --------------+------------+----------+----------
     UPDATE       |       1001 | t        |       50
     UPDATE       |       1002 | f        |        0
     INSERT       |       1003 | t        |       10

Note that this function can only be used in the `RETURNING` list of a `MERGE` command. It is an error to use it in any other part of a query.

## Subquery Expressions

EXISTS

IN

NOT IN

ANY

ALL

SOME

subquery

This section describes the SQL-compliant subquery expressions available in PostgreSQL. All of the expression forms documented in this section return Boolean (true/false) results.

### `EXISTS`

EXISTS (

subquery

)

The argument of EXISTS is an arbitrary `SELECT` statement, or subquery. The subquery is evaluated to determine whether it returns any rows. If it returns at least one row, the result of EXISTS is “true”; if the subquery returns no rows, the result of EXISTS is “false”.

The subquery can refer to variables from the surrounding query, which will act as constants during any one evaluation of the subquery.

The subquery will generally only be executed long enough to determine whether at least one row is returned, not all the way to completion. It is unwise to write a subquery that has side effects (such as calling sequence functions); whether the side effects occur might be unpredictable.

Since the result depends only on whether any rows are returned, and not on the contents of those rows, the output list of the subquery is normally unimportant. A common coding convention is to write all `EXISTS` tests in the form `EXISTS(SELECT 1 WHERE ...)`. There are exceptions to this rule however, such as subqueries that use INTERSECT.

This simple example is like an inner join on `col2`, but it produces at most one output row for each `tab1` row, even if there are several matching `tab2` rows:

    SELECT col1
    FROM tab1
    WHERE EXISTS (SELECT 1 FROM tab2 WHERE col2 = tab1.col2);

### `IN`

expression

IN (

subquery

)

The right-hand side is a parenthesized subquery, which must return exactly one column. The left-hand expression is evaluated and compared to each row of the subquery result. The result of IN is “true” if any equal subquery row is found. The result is “false” if no equal row is found (including the case where the subquery returns no rows).

Note that if the left-hand expression yields null, or if there are no equal right-hand values and at least one right-hand row yields null, the result of the IN construct will be null, not false. This is in accordance with SQL's normal rules for Boolean combinations of null values.

As with EXISTS, it's unwise to assume that the subquery will be evaluated completely.

row_constructor

IN (

subquery

)

The left-hand side of this form of IN is a row constructor, as described in [???](#sql-syntax-row-constructors). The right-hand side is a parenthesized subquery, which must return exactly as many columns as there are expressions in the left-hand row. The left-hand expressions are evaluated and compared row-wise to each row of the subquery result. The result of IN is “true” if any equal subquery row is found. The result is “false” if no equal row is found (including the case where the subquery returns no rows).

As usual, null values in the rows are combined per the normal rules of SQL Boolean expressions. Two rows are considered equal if all their corresponding members are non-null and equal; the rows are unequal if any corresponding members are non-null and unequal; otherwise the result of that row comparison is unknown (null). If all the per-row results are either unequal or null, with at least one null, then the result of IN is null.

### `NOT IN`

expression

NOT IN (

subquery

)

The right-hand side is a parenthesized subquery, which must return exactly one column. The left-hand expression is evaluated and compared to each row of the subquery result. The result of NOT IN is “true” if only unequal subquery rows are found (including the case where the subquery returns no rows). The result is “false” if any equal row is found.

Note that if the left-hand expression yields null, or if there are no equal right-hand values and at least one right-hand row yields null, the result of the NOT IN construct will be null, not true. This is in accordance with SQL's normal rules for Boolean combinations of null values.

As with EXISTS, it's unwise to assume that the subquery will be evaluated completely.

row_constructor

NOT IN (

subquery

)

The left-hand side of this form of NOT IN is a row constructor, as described in [???](#sql-syntax-row-constructors). The right-hand side is a parenthesized subquery, which must return exactly as many columns as there are expressions in the left-hand row. The left-hand expressions are evaluated and compared row-wise to each row of the subquery result. The result of NOT IN is “true” if only unequal subquery rows are found (including the case where the subquery returns no rows). The result is “false” if any equal row is found.

As usual, null values in the rows are combined per the normal rules of SQL Boolean expressions. Two rows are considered equal if all their corresponding members are non-null and equal; the rows are unequal if any corresponding members are non-null and unequal; otherwise the result of that row comparison is unknown (null). If all the per-row results are either unequal or null, with at least one null, then the result of NOT IN is null.

### `ANY`/`SOME`

expression

operator

ANY (

subquery

)

expression

operator

SOME (

subquery

)

The right-hand side is a parenthesized subquery, which must return exactly one column. The left-hand expression is evaluated and compared to each row of the subquery result using the given \<operator\>, which must yield a Boolean result. The result of ANY is “true” if any true result is obtained. The result is “false” if no true result is found (including the case where the subquery returns no rows).

SOME is a synonym for ANY. IN is equivalent to `= ANY`.

Note that if there are no successes and at least one right-hand row yields null for the operator's result, the result of the ANY construct will be null, not false. This is in accordance with SQL's normal rules for Boolean combinations of null values.

As with EXISTS, it's unwise to assume that the subquery will be evaluated completely.

row_constructor

operator

ANY (

subquery

)

row_constructor

operator

SOME (

subquery

)

The left-hand side of this form of ANY is a row constructor, as described in [???](#sql-syntax-row-constructors). The right-hand side is a parenthesized subquery, which must return exactly as many columns as there are expressions in the left-hand row. The left-hand expressions are evaluated and compared row-wise to each row of the subquery result, using the given \<operator\>. The result of ANY is “true” if the comparison returns true for any subquery row. The result is “false” if the comparison returns false for every subquery row (including the case where the subquery returns no rows). The result is NULL if no comparison with a subquery row returns true, and at least one comparison returns NULL.

See [Row Constructor Comparison](#row-wise-comparison) for details about the meaning of a row constructor comparison.

### `ALL`

expression

operator

ALL (

subquery

)

The right-hand side is a parenthesized subquery, which must return exactly one column. The left-hand expression is evaluated and compared to each row of the subquery result using the given \<operator\>, which must yield a Boolean result. The result of ALL is “true” if all rows yield true (including the case where the subquery returns no rows). The result is “false” if any false result is found. The result is NULL if no comparison with a subquery row returns false, and at least one comparison returns NULL.

NOT IN is equivalent to `<> ALL`.

As with EXISTS, it's unwise to assume that the subquery will be evaluated completely.

row_constructor

operator

ALL (

subquery

)

The left-hand side of this form of ALL is a row constructor, as described in [???](#sql-syntax-row-constructors). The right-hand side is a parenthesized subquery, which must return exactly as many columns as there are expressions in the left-hand row. The left-hand expressions are evaluated and compared row-wise to each row of the subquery result, using the given \<operator\>. The result of ALL is “true” if the comparison returns true for all subquery rows (including the case where the subquery returns no rows). The result is “false” if the comparison returns false for any subquery row. The result is NULL if no comparison with a subquery row returns false, and at least one comparison returns NULL.

See [Row Constructor Comparison](#row-wise-comparison) for details about the meaning of a row constructor comparison.

### Single-Row Comparison

comparison

subquery result row

row_constructor

operator

(

subquery

)

The left-hand side is a row constructor, as described in [???](#sql-syntax-row-constructors). The right-hand side is a parenthesized subquery, which must return exactly as many columns as there are expressions in the left-hand row. Furthermore, the subquery cannot return more than one row. (If it returns zero rows, the result is taken to be null.) The left-hand side is evaluated and compared row-wise to the single subquery result row.

See [Row Constructor Comparison](#row-wise-comparison) for details about the meaning of a row constructor comparison.

## Row and Array Comparisons

IN

NOT IN

ANY

ALL

SOME

composite type

comparison

row-wise comparison

comparison

composite type

comparison

row constructor

IS DISTINCT FROM

IS NOT DISTINCT FROM

This section describes several specialized constructs for making multiple comparisons between groups of values. These forms are syntactically related to the subquery forms of the previous section, but do not involve subqueries. The forms involving array subexpressions are PostgreSQL extensions; the rest are SQL-compliant. All of the expression forms documented in this section return Boolean (true/false) results.

### `IN`

expression

IN (

value

, ...

)

The right-hand side is a parenthesized list of expressions. The result is “true” if the left-hand expression's result is equal to any of the right-hand expressions. This is a shorthand notation for \<expression\> = \<value1\> OR \<expression\> = \<value2\> OR ...

Note that if the left-hand expression yields null, or if there are no equal right-hand values and at least one right-hand expression yields null, the result of the IN construct will be null, not false. This is in accordance with SQL's normal rules for Boolean combinations of null values.

### `NOT IN`

expression

NOT IN (

value

, ...

)

The right-hand side is a parenthesized list of expressions. The result is “true” if the left-hand expression's result is unequal to all of the right-hand expressions. This is a shorthand notation for \<expression\> \<\> \<value1\> AND \<expression\> \<\> \<value2\> AND ...

Note that if the left-hand expression yields null, or if there are no equal right-hand values and at least one right-hand expression yields null, the result of the NOT IN construct will be null, not true as one might naively expect. This is in accordance with SQL's normal rules for Boolean combinations of null values.

> [!TIP]
> `x NOT IN y` is equivalent to `NOT (x IN y)` in all cases. However, null values are much more likely to trip up the novice when working with NOT IN than when working with IN. It is best to express your condition positively if possible.

### `ANY`/`SOME` (array)

expression

operator

ANY (

array expression

)

expression

operator

SOME (

array expression

)

The right-hand side is a parenthesized expression, which must yield an array value. The left-hand expression is evaluated and compared to each element of the array using the given \<operator\>, which must yield a Boolean result. The result of ANY is “true” if any true result is obtained. The result is “false” if no true result is found (including the case where the array has zero elements).

If the array expression yields a null array, the result of ANY will be null. If the left-hand expression yields null, the result of ANY is ordinarily null (though a non-strict comparison operator could possibly yield a different result). Also, if the right-hand array contains any null elements and no true comparison result is obtained, the result of ANY will be null, not false (again, assuming a strict comparison operator). This is in accordance with SQL's normal rules for Boolean combinations of null values.

SOME is a synonym for ANY.

### `ALL` (array)

expression

operator

ALL (

array expression

)

The right-hand side is a parenthesized expression, which must yield an array value. The left-hand expression is evaluated and compared to each element of the array using the given \<operator\>, which must yield a Boolean result. The result of ALL is “true” if all comparisons yield true (including the case where the array has zero elements). The result is “false” if any false result is found.

If the array expression yields a null array, the result of ALL will be null. If the left-hand expression yields null, the result of ALL is ordinarily null (though a non-strict comparison operator could possibly yield a different result). Also, if the right-hand array contains any null elements and no false comparison result is obtained, the result of ALL will be null, not true (again, assuming a strict comparison operator). This is in accordance with SQL's normal rules for Boolean combinations of null values.

### Row Constructor Comparison

row_constructor

operator

row_constructor

Each side is a row constructor, as described in [???](#sql-syntax-row-constructors). The two row constructors must have the same number of fields. The given \<operator\> is applied to each pair of corresponding fields. (Since the fields could be of different types, this means that a different specific operator could be selected for each pair.) All the selected operators must be members of some B-tree operator class, or be the negator of an `=` member of a B-tree operator class, meaning that row constructor comparison is only possible when the \<operator\> is `=`, `<>`, `<`, `<=`, `>`, or `>=`, or has semantics similar to one of these.

The `=` and `<>` cases work slightly differently from the others. Two rows are considered equal if all their corresponding members are non-null and equal; the rows are unequal if any corresponding members are non-null and unequal; otherwise the result of the row comparison is unknown (null).

For the `<`, `<=`, `>` and `>=` cases, the row elements are compared left-to-right, stopping as soon as an unequal or null pair of elements is found. If either of this pair of elements is null, the result of the row comparison is unknown (null); otherwise comparison of this pair of elements determines the result. For example, `ROW(1,2,NULL) < ROW(1,3,0)` yields true, not null, because the third pair of elements are not considered.

row_constructor

IS DISTINCT FROM

row_constructor

This construct is similar to a `<>` row comparison, but it does not yield null for null inputs. Instead, any null value is considered unequal to (distinct from) any non-null value, and any two nulls are considered equal (not distinct). Thus the result will either be true or false, never null.

row_constructor

IS NOT DISTINCT FROM

row_constructor

This construct is similar to a `=` row comparison, but it does not yield null for null inputs. Instead, any null value is considered unequal to (distinct from) any non-null value, and any two nulls are considered equal (not distinct). Thus the result will always be either true or false, never null.

### Composite Type Comparison

record

operator

record

The SQL specification requires row-wise comparison to return NULL if the result depends on comparing two NULL values or a NULL and a non-NULL. PostgreSQL does this only when comparing the results of two row constructors (as in [Row Constructor Comparison](#row-wise-comparison)) or comparing a row constructor to the output of a subquery (as in [Subquery Expressions](#functions-subquery)). In other contexts where two composite-type values are compared, two NULL field values are considered equal, and a NULL is considered larger than a non-NULL. This is necessary in order to have consistent sorting and indexing behavior for composite types.

Each side is evaluated and they are compared row-wise. Composite type comparisons are allowed when the \<operator\> is `=`, `<>`, `<`, `<=`, `>` or `>=`, or has semantics similar to one of these. (To be specific, an operator can be a row comparison operator if it is a member of a B-tree operator class, or is the negator of the `=` member of a B-tree operator class.) The default behavior of the above operators is the same as for `IS [ NOT ] DISTINCT FROM` for row constructors (see [Row Constructor Comparison](#row-wise-comparison)).

To support matching of rows which include elements without a default B-tree operator class, the following operators are defined for composite type comparison: `*=`, `*<>`, `*<`, `*<=`, `*>`, and `*>=`. These operators compare the internal binary representation of the two rows. Two rows might have a different binary representation even though comparisons of the two rows with the equality operator is true. The ordering of rows under these comparison operators is deterministic but not otherwise meaningful. These operators are used internally for materialized views and might be useful for other specialized purposes such as replication and B-Tree deduplication (see [???](#btree-deduplication)). They are not intended to be generally useful for writing queries, though.

## Set Returning Functions

set returning functions

functions

This section describes functions that possibly return more than one row. The most widely used functions in this class are series generating functions, as detailed in [Series Generating Functions](#functions-srf-series) and [Subscript Generating Functions](#functions-srf-subscripts). Other, more specialized set-returning functions are described elsewhere in this manual. See [???](#queries-tablefunctions) for ways to combine multiple set-returning functions.

<table id="functions-srf-series">
<caption>Series Generating Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>generate_series</code> ( <code>start</code> <code>integer</code>, <code>stop</code> <code>integer</code> [, <code>step</code> <code>integer</code>] ) setof integer</p>
<p role="func_signature"><code>generate_series</code> ( <code>start</code> <code>bigint</code>, <code>stop</code> <code>bigint</code> [, <code>step</code> <code>bigint</code>] ) setof bigint</p>
<p role="func_signature"><code>generate_series</code> ( <code>start</code> <code>numeric</code>, <code>stop</code> <code>numeric</code> [, <code>step</code> <code>numeric</code>] ) setof numeric</p>
<p>Generates a series of values from <code>start</code> to <code>stop</code>, with a step size of <code>step</code>. <code>step</code> defaults to 1.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>generate_series</code> ( <code>start</code> <code>timestamp</code>, <code>stop</code> <code>timestamp</code>, <code>step</code> <code>interval</code> ) setof timestamp</p>
<p role="func_signature"><code>generate_series</code> ( <code>start</code> <code>timestamp with time zone</code>, <code>stop</code> <code>timestamp with time zone</code>, <code>step</code> <code>interval</code> [, <code>timezone</code> <code>text</code>] ) setof timestamp with time zone</p>
<p>Generates a series of values from <code>start</code> to <code>stop</code>, with a step size of <code>step</code>. In the timezone-aware form, times of day and daylight-savings adjustments are computed according to the time zone named by the <code>timezone</code> argument, or the current <a href="#guc-timezone">???</a> setting if that is omitted.</p></td>
</tr>
</tbody>
</table>

When `step` is positive, zero rows are returned if `start` is greater than `stop`. Conversely, when `step` is negative, zero rows are returned if `start` is less than `stop`. Zero rows are also returned if any input is `NULL`. It is an error for `step` to be zero. Some examples follow:

    SELECT * FROM generate_series(2,4);
     generate_series
    -----------------
                   2
                   3
                   4
    (3 rows)

    SELECT * FROM generate_series(5,1,-2);
     generate_series
    -----------------
                   5
                   3
                   1
    (3 rows)

    SELECT * FROM generate_series(4,3);
     generate_series
    -----------------
    (0 rows)

    SELECT generate_series(1.1, 4, 1.3);
     generate_series
    -----------------
                 1.1
                 2.4
                 3.7
    (3 rows)

    -- this example relies on the date-plus-integer operator:
    SELECT current_date + s.a AS dates FROM generate_series(0,14,7) AS s(a);
       dates
    ------------
     2004-02-05
     2004-02-12
     2004-02-19
    (3 rows)

    SELECT * FROM generate_series('2008-03-01 00:00'::timestamp,
                                  '2008-03-04 12:00', '10 hours');
       generate_series
    ---------------------
     2008-03-01 00:00:00
     2008-03-01 10:00:00
     2008-03-01 20:00:00
     2008-03-02 06:00:00
     2008-03-02 16:00:00
     2008-03-03 02:00:00
     2008-03-03 12:00:00
     2008-03-03 22:00:00
     2008-03-04 08:00:00
    (9 rows)

    -- this example assumes that TimeZone is set to UTC; note the DST transition:
    SELECT * FROM generate_series('2001-10-22 00:00 -04:00'::timestamptz,
                                  '2001-11-01 00:00 -05:00'::timestamptz,
                                  '1 day'::interval, 'America/New_York');
        generate_series
    ------------------------
     2001-10-22 04:00:00+00
     2001-10-23 04:00:00+00
     2001-10-24 04:00:00+00
     2001-10-25 04:00:00+00
     2001-10-26 04:00:00+00
     2001-10-27 04:00:00+00
     2001-10-28 04:00:00+00
     2001-10-29 05:00:00+00
     2001-10-30 05:00:00+00
     2001-10-31 05:00:00+00
     2001-11-01 05:00:00+00
    (11 rows)

<table id="functions-srf-subscripts">
<caption>Subscript Generating Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>generate_subscripts</code> ( <code>array</code> <code>anyarray</code>, <code>dim</code> <code>integer</code> ) setof integer</p>
<p>Generates a series comprising the valid subscripts of the <code>dim</code>'th dimension of the given array.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>generate_subscripts</code> ( <code>array</code> <code>anyarray</code>, <code>dim</code> <code>integer</code>, <code>reverse</code> <code>boolean</code> ) setof integer</p>
<p>Generates a series comprising the valid subscripts of the <code>dim</code>'th dimension of the given array. When <code>reverse</code> is true, returns the series in reverse order.</p></td>
</tr>
</tbody>
</table>

`generate_subscripts` is a convenience function that generates the set of valid subscripts for the specified dimension of the given array. Zero rows are returned for arrays that do not have the requested dimension, or if any input is `NULL`. Some examples follow:

    -- basic usage:
    SELECT generate_subscripts('{NULL,1,NULL,2}'::int[], 1) AS s;
     s
    ---
     1
     2
     3
     4
    (4 rows)

    -- presenting an array, the subscript and the subscripted
    -- value requires a subquery:
    SELECT * FROM arrays;
             a
    --------------------
     {-1,-2}
     {100,200,300}
    (2 rows)

    SELECT a AS array, s AS subscript, a[s] AS value
    FROM (SELECT generate_subscripts(a, 1) AS s, a FROM arrays) foo;
         array     | subscript | value
    ---------------+-----------+-------
     {-1,-2}       |         1 |    -1
     {-1,-2}       |         2 |    -2
     {100,200,300} |         1 |   100
     {100,200,300} |         2 |   200
     {100,200,300} |         3 |   300
    (5 rows)

    -- unnest a 2D array:
    CREATE OR REPLACE FUNCTION unnest2(anyarray)
    RETURNS SETOF anyelement AS $$
    select $1[i][j]
       from generate_subscripts($1,1) g1(i),
            generate_subscripts($1,2) g2(j);
    $$ LANGUAGE sql IMMUTABLE;
    CREATE FUNCTION
    SELECT * FROM unnest2(ARRAY[[1,2],[3,4]]);
     unnest2
    ---------
           1
           2
           3
           4
    (4 rows)

ordinality

When a function in the `FROM` clause is suffixed by `WITH ORDINALITY`, a `bigint` column is appended to the function's output column(s), which starts from 1 and increments by 1 for each row of the function's output. This is most useful in the case of set returning functions such as `unnest()`.

    -- set returning function WITH ORDINALITY:
    SELECT * FROM pg_ls_dir('.') WITH ORDINALITY AS t(ls,n);
           ls        | n
    -----------------+----
     pg_serial       |  1
     pg_twophase     |  2
     postmaster.opts |  3
     pg_notify       |  4
     postgresql.conf |  5
     pg_tblspc       |  6
     logfile         |  7
     base            |  8
     postmaster.pid  |  9
     pg_ident.conf   | 10
     global          | 11
     pg_xact         | 12
     pg_snapshots    | 13
     pg_multixact    | 14
     PG_VERSION      | 15
     pg_wal          | 16
     pg_hba.conf     | 17
     pg_stat_tmp     | 18
     pg_subtrans     | 19
    (19 rows)

## System Information Functions and Operators

The functions described in this section are used to obtain various information about a PostgreSQL installation.

### Session Information Functions

[Session Information Functions](#functions-info-session-table) shows several functions that extract session and system information.

In addition to the functions listed in this section, there are a number of functions related to the statistics system that also provide system information. See [???](#monitoring-stats-functions) for more information.

<table id="functions-info-session-table">
<caption>Session Information Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>current_catalog</code> name</p>
<p role="func_signature"><span class="indexterm"></span> <code>current_database</code> () name</p>
<p>Returns the name of the current database. (Databases are called “catalogs” in the SQL standard, so <code>current_catalog</code> is the standard's spelling.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>current_query</code> () text</p>
<p>Returns the text of the currently executing query, as submitted by the client (which might contain more than one statement).</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>current_role</code> name</p>
<p>This is equivalent to <code>current_user</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>current_schema</code> name</p>
<p role="func_signature"><code>current_schema</code> () name</p>
<p>Returns the name of the schema that is first in the search path (or a null value if the search path is empty). This is the schema that will be used for any tables or other named objects that are created without specifying a target schema.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>current_schemas</code> ( <code>include_implicit</code> <code>boolean</code> ) name[]</p>
<p>Returns an array of the names of all schemas presently in the effective search path, in their priority order. (Items in the current <a href="#guc-search-path">???</a> setting that do not correspond to existing, searchable schemas are omitted.) If the Boolean argument is <code>true</code>, then implicitly-searched system schemas such as <code>pg_catalog</code> are included in the result.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <code>current_user</code> name</p>
<p>Returns the user name of the current execution context.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>inet_client_addr</code> () inet</p>
<p>Returns the IP address of the current client, or <code>NULL</code> if the current connection is via a Unix-domain socket.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>inet_client_port</code> () integer</p>
<p>Returns the IP port number of the current client, or <code>NULL</code> if the current connection is via a Unix-domain socket.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>inet_server_addr</code> () inet</p>
<p>Returns the IP address on which the server accepted the current connection, or <code>NULL</code> if the current connection is via a Unix-domain socket.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>inet_server_port</code> () integer</p>
<p>Returns the IP port number on which the server accepted the current connection, or <code>NULL</code> if the current connection is via a Unix-domain socket.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_backend_pid</code> () integer</p>
<p>Returns the process ID of the server process attached to the current session.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_blocking_pids</code> ( <code>integer</code> ) integer[]</p>
<p>Returns an array of the process ID(s) of the sessions that are blocking the server process with the specified process ID from acquiring a lock, or an empty array if there is no such server process or it is not blocked.</p>
<p>One server process blocks another if it either holds a lock that conflicts with the blocked process's lock request (hard block), or is waiting for a lock that would conflict with the blocked process's lock request and is ahead of it in the wait queue (soft block). When using parallel queries the result always lists client-visible process IDs (that is, <code>pg_backend_pid</code> results) even if the actual lock is held or awaited by a child worker process. As a result of that, there may be duplicated PIDs in the result. Also note that when a prepared transaction holds a conflicting lock, it will be represented by a zero process ID.</p>
<p>Frequent calls to this function could have some impact on database performance, because it needs exclusive access to the lock manager's shared state for a short time.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_conf_load_time</code> () timestamp with time zone</p>
<p>Returns the time when the server configuration files were last loaded. If the current session was alive at the time, this will be the time when the session itself re-read the configuration files (so the reading will vary a little in different sessions). Otherwise it is the time when the postmaster process re-read the configuration files.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <span class="indexterm"></span> <span class="indexterm"></span> <span class="indexterm"></span> <code>pg_current_logfile</code> ( [<code>text</code>] ) text</p>
<p>Returns the path name of the log file currently in use by the logging collector. The path includes the <a href="#guc-log-directory">???</a> directory and the individual log file name. The result is <code>NULL</code> if the logging collector is disabled. When multiple log files exist, each in a different format, <code>pg_current_logfile</code> without an argument returns the path of the file having the first format found in the ordered list: <code>stderr</code>, <code>csvlog</code>, <code>jsonlog</code>. <code>NULL</code> is returned if no log file has any of these formats. To request information about a specific log file format, supply either <code>csvlog</code>, <code>jsonlog</code> or <code>stderr</code> as the value of the optional parameter. The result is <code>NULL</code> if the log format requested is not configured in <a href="#guc-log-destination">???</a>. The result reflects the contents of the <code>current_logfiles</code> file.</p>
<p>This function is restricted to superusers and roles with privileges of the <code>pg_monitor</code> role by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_my_temp_schema</code> () oid</p>
<p>Returns the OID of the current session's temporary schema, or zero if it has none (because it has not created any temporary tables).</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_is_other_temp_schema</code> ( <code>oid</code> ) boolean</p>
<p>Returns true if the given OID is the OID of another session's temporary schema. (This can be useful, for example, to exclude other sessions' temporary tables from a catalog display.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_jit_available</code> () boolean</p>
<p>Returns true if a JIT compiler extension is available (see <a href="#jit">???</a>) and the <a href="#guc-jit">???</a> configuration parameter is set to <code>on</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_listening_channels</code> () setof text</p>
<p>Returns the set of names of asynchronous notification channels that the current session is listening to.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_notification_queue_usage</code> () double precision</p>
<p>Returns the fraction (01) of the asynchronous notification queue's maximum size that is currently occupied by notifications that are waiting to be processed. See <a href="#sql-listen">???</a> and <a href="#sql-notify">???</a> for more information.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_postmaster_start_time</code> () timestamp with time zone</p>
<p>Returns the time when the server started.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_safe_snapshot_blocking_pids</code> ( <code>integer</code> ) integer[]</p>
<p>Returns an array of the process ID(s) of the sessions that are blocking the server process with the specified process ID from acquiring a safe snapshot, or an empty array if there is no such server process or it is not blocked.</p>
<p>A session running a <code>SERIALIZABLE</code> transaction blocks a <code>SERIALIZABLE READ ONLY DEFERRABLE</code> transaction from acquiring a snapshot until the latter determines that it is safe to avoid taking any predicate locks. See <a href="#xact-serializable">???</a> for more information about serializable and deferrable transactions.</p>
<p>Frequent calls to this function could have some impact on database performance, because it needs access to the predicate lock manager's shared state for a short time.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_trigger_depth</code> () integer</p>
<p>Returns the current nesting level of PostgreSQL triggers (0 if not called, directly or indirectly, from inside a trigger).</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>session_user</code> name</p>
<p>Returns the session user's name.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>system_user</code> text</p>
<p>Returns the authentication method and the identity (if any) that the user presented during the authentication cycle before they were assigned a database role. It is represented as <code>auth_method:identity</code> or <code>NULL</code> if the user has not been authenticated (for example if <a href="#auth-trust">Trust authentication</a> has been used).</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>user</code> name</p>
<p>This is equivalent to <code>current_user</code>.</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> `current_catalog`, `current_role`, `current_schema`, `current_user`, `session_user`, and `user` have special syntactic status in SQL: they must be called without trailing parentheses. In PostgreSQL, parentheses can optionally be used with `current_schema`, but not with the others.

The `session_user` is normally the user who initiated the current database connection; but superusers can change this setting with [???](#sql-set-session-authorization). The `current_user` is the user identifier that is applicable for permission checking. Normally it is equal to the session user, but it can be changed with [???](#sql-set-role). It also changes during the execution of functions with the attribute `SECURITY DEFINER`. In Unix parlance, the session user is the “real user” and the current user is the “effective user”. `current_role` and `user` are synonyms for `current_user`. (The SQL standard draws a distinction between `current_role` and `current_user`, but PostgreSQL does not, since it unifies users and roles into a single kind of entity.)

### Access Privilege Inquiry Functions

privilege

querying

[Access Privilege Inquiry Functions](#functions-info-access-table) lists functions that allow querying object access privileges programmatically. (See [???](#ddl-priv) for more information about privileges.) In these functions, the user whose privileges are being inquired about can be specified by name or by OID (pg_authid.oid), or if the name is given as `public` then the privileges of the PUBLIC pseudo-role are checked. Also, the `user` argument can be omitted entirely, in which case the `current_user` is assumed. The object that is being inquired about can be specified either by name or by OID, too. When specifying by name, a schema name can be included if relevant. The access privilege of interest is specified by a text string, which must evaluate to one of the appropriate privilege keywords for the object's type (e.g., `SELECT`). Optionally, `WITH GRANT OPTION` can be added to a privilege type to test whether the privilege is held with grant option. Also, multiple privilege types can be listed separated by commas, in which case the result will be true if any of the listed privileges is held. (Case of the privilege string is not significant, and extra whitespace is allowed between but not within privilege names.) Some examples:

    SELECT has_table_privilege('myschema.mytable', 'select');
    SELECT has_table_privilege('joe', 'mytable', 'INSERT, SELECT WITH GRANT OPTION');

<table id="functions-info-access-table">
<caption>Access Privilege Inquiry Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>has_any_column_privilege</code> ( [<code>user</code> <code>name</code> or <code>oid</code>,] <code>table</code> <code>text</code> or <code>oid</code>, <code>privilege</code> <code>text</code> ) boolean</p>
<p>Does user have privilege for any column of table? This succeeds either if the privilege is held for the whole table, or if there is a column-level grant of the privilege for at least one column. Allowable privilege types are <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, and <code>REFERENCES</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>has_column_privilege</code> ( [<code>user</code> <code>name</code> or <code>oid</code>,] <code>table</code> <code>text</code> or <code>oid</code>, <code>column</code> <code>text</code> or <code>smallint</code>, <code>privilege</code> <code>text</code> ) boolean</p>
<p>Does user have privilege for the specified table column? This succeeds either if the privilege is held for the whole table, or if there is a column-level grant of the privilege for the column. The column can be specified by name or by attribute number (pg_attribute.attnum). Allowable privilege types are <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, and <code>REFERENCES</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>has_database_privilege</code> ( [<code>user</code> <code>name</code> or <code>oid</code>,] <code>database</code> <code>text</code> or <code>oid</code>, <code>privilege</code> <code>text</code> ) boolean</p>
<p>Does user have privilege for database? Allowable privilege types are <code>CREATE</code>, <code>CONNECT</code>, <code>TEMPORARY</code>, and <code>TEMP</code> (which is equivalent to <code>TEMPORARY</code>).</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>has_foreign_data_wrapper_privilege</code> ( [<code>user</code> <code>name</code> or <code>oid</code>,] <code>fdw</code> <code>text</code> or <code>oid</code>, <code>privilege</code> <code>text</code> ) boolean</p>
<p>Does user have privilege for foreign-data wrapper? The only allowable privilege type is <code>USAGE</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>has_function_privilege</code> ( [<code>user</code> <code>name</code> or <code>oid</code>,] <code>function</code> <code>text</code> or <code>oid</code>, <code>privilege</code> <code>text</code> ) boolean</p>
<p>Does user have privilege for function? The only allowable privilege type is <code>EXECUTE</code>.</p>
<p>When specifying a function by name rather than by OID, the allowed input is the same as for the <code>regprocedure</code> data type (see <a href="#datatype-oid">???</a>). An example is:</p>
<pre><code>SELECT has_function_privilege(&#39;joeuser&#39;, &#39;myfunc(int, text)&#39;, &#39;execute&#39;);</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>has_language_privilege</code> ( [<code>user</code> <code>name</code> or <code>oid</code>,] <code>language</code> <code>text</code> or <code>oid</code>, <code>privilege</code> <code>text</code> ) boolean</p>
<p>Does user have privilege for language? The only allowable privilege type is <code>USAGE</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>has_parameter_privilege</code> ( [<code>user</code> <code>name</code> or <code>oid</code>,] <code>parameter</code> <code>text</code>, <code>privilege</code> <code>text</code> ) boolean</p>
<p>Does user have privilege for configuration parameter? The parameter name is case-insensitive. Allowable privilege types are <code>SET</code> and <code>ALTER SYSTEM</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>has_schema_privilege</code> ( [<code>user</code> <code>name</code> or <code>oid</code>,] <code>schema</code> <code>text</code> or <code>oid</code>, <code>privilege</code> <code>text</code> ) boolean</p>
<p>Does user have privilege for schema? Allowable privilege types are <code>CREATE</code> and <code>USAGE</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>has_sequence_privilege</code> ( [<code>user</code> <code>name</code> or <code>oid</code>,] <code>sequence</code> <code>text</code> or <code>oid</code>, <code>privilege</code> <code>text</code> ) boolean</p>
<p>Does user have privilege for sequence? Allowable privilege types are <code>USAGE</code>, <code>SELECT</code>, and <code>UPDATE</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>has_server_privilege</code> ( [<code>user</code> <code>name</code> or <code>oid</code>,] <code>server</code> <code>text</code> or <code>oid</code>, <code>privilege</code> <code>text</code> ) boolean</p>
<p>Does user have privilege for foreign server? The only allowable privilege type is <code>USAGE</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>has_table_privilege</code> ( [<code>user</code> <code>name</code> or <code>oid</code>,] <code>table</code> <code>text</code> or <code>oid</code>, <code>privilege</code> <code>text</code> ) boolean</p>
<p>Does user have privilege for table? Allowable privilege types are <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>, <code>TRUNCATE</code>, <code>REFERENCES</code>, <code>TRIGGER</code>, and <code>MAINTAIN</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>has_tablespace_privilege</code> ( [<code>user</code> <code>name</code> or <code>oid</code>,] <code>tablespace</code> <code>text</code> or <code>oid</code>, <code>privilege</code> <code>text</code> ) boolean</p>
<p>Does user have privilege for tablespace? The only allowable privilege type is <code>CREATE</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>has_type_privilege</code> ( [<code>user</code> <code>name</code> or <code>oid</code>,] <code>type</code> <code>text</code> or <code>oid</code>, <code>privilege</code> <code>text</code> ) boolean</p>
<p>Does user have privilege for data type? The only allowable privilege type is <code>USAGE</code>. When specifying a type by name rather than by OID, the allowed input is the same as for the <code>regtype</code> data type (see <a href="#datatype-oid">???</a>).</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_has_role</code> ( [<code>user</code> <code>name</code> or <code>oid</code>,] <code>role</code> <code>text</code> or <code>oid</code>, <code>privilege</code> <code>text</code> ) boolean</p>
<p>Does user have privilege for role? Allowable privilege types are <code>MEMBER</code>, <code>USAGE</code>, and <code>SET</code>. <code>MEMBER</code> denotes direct or indirect membership in the role without regard to what specific privileges may be conferred. <code>USAGE</code> denotes whether the privileges of the role are immediately available without doing <code>SET ROLE</code>, while <code>SET</code> denotes whether it is possible to change to the role using the <code>SET ROLE</code> command. <code>WITH ADMIN OPTION</code> or <code>WITH GRANT OPTION</code> can be added to any of these privilege types to test whether the <code>ADMIN</code> privilege is held (all six spellings test the same thing). This function does not allow the special case of setting <code>user</code> to <code>public</code>, because the PUBLIC pseudo-role can never be a member of real roles.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>row_security_active</code> ( <code>table</code> <code>text</code> or <code>oid</code> ) boolean</p>
<p>Is row-level security active for the specified table in the context of the current user and current environment?</p></td>
</tr>
</tbody>
</table>

[ Operators](#functions-aclitem-op-table) shows the operators available for the `aclitem` type, which is the catalog representation of access privileges. See [???](#ddl-priv) for information about how to read access privilege values.

<table id="functions-aclitem-op-table">
<caption><code>aclitem</code> Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>aclitem</code> <code>=</code> <code>aclitem</code> boolean</p>
<p>Are <code>aclitem</code>s equal? (Notice that type <code>aclitem</code> lacks the usual set of comparison operators; it has only equality. In turn, <code>aclitem</code> arrays can only be compared for equality.)</p>
<p><code>'calvin=r*w/hobbes'::aclitem = 'calvin=r*w*/hobbes'::aclitem</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>aclitem[]</code> <code>@&gt;</code> <code>aclitem</code> boolean</p>
<p>Does array contain the specified privileges? (This is true if there is an array entry that matches the <code>aclitem</code>'s grantee and grantor, and has at least the specified set of privileges.)</p>
<p><code>'{calvin=r*w/hobbes,hobbes=r*w*/postgres}'::aclitem[] @&gt; 'calvin=r*/hobbes'::aclitem</code> t</p></td>
</tr>
</tbody>
</table>

[ Functions](#functions-aclitem-fn-table) shows some additional functions to manage the `aclitem` type.

<table id="functions-aclitem-fn-table">
<caption><code>aclitem</code> Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>acldefault</code> ( <code>type</code> <code>"char"</code>, <code>ownerId</code> <code>oid</code> ) aclitem[]</p>
<p>Constructs an <code>aclitem</code> array holding the default access privileges for an object of type <code>type</code> belonging to the role with OID <code>ownerId</code>. This represents the access privileges that will be assumed when an object's ACL entry is null. (The default access privileges are described in <a href="#ddl-priv">???</a>.) The <code>type</code> parameter must be one of 'c' for <code>COLUMN</code>, 'r' for <code>TABLE</code> and table-like objects, 's' for <code>SEQUENCE</code>, 'd' for <code>DATABASE</code>, 'f' for <code>FUNCTION</code> or <code>PROCEDURE</code>, 'l' for <code>LANGUAGE</code>, 'L' for <code>LARGE OBJECT</code>, 'n' for <code>SCHEMA</code>, 'p' for <code>PARAMETER</code>, 't' for <code>TABLESPACE</code>, 'F' for <code>FOREIGN DATA WRAPPER</code>, 'S' for <code>FOREIGN SERVER</code>, or 'T' for <code>TYPE</code> or <code>DOMAIN</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>aclexplode</code> ( <code>aclitem[]</code> ) setof record ( <code>grantor</code> <code>oid</code>, <code>grantee</code> <code>oid</code>, <code>privilege_type</code> <code>text</code>, <code>is_grantable</code> <code>boolean</code> )</p>
<p>Returns the <code>aclitem</code> array as a set of rows. If the grantee is the pseudo-role PUBLIC, it is represented by zero in the <code>grantee</code> column. Each granted privilege is represented as <code>SELECT</code>, <code>INSERT</code>, etc (see <a href="#privilege-abbrevs-table">???</a> for a full list). Note that each privilege is broken out as a separate row, so only one keyword appears in the <code>privilege_type</code> column.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>makeaclitem</code> ( <code>grantee</code> <code>oid</code>, <code>grantor</code> <code>oid</code>, <code>privileges</code> <code>text</code>, <code>is_grantable</code> <code>boolean</code> ) aclitem</p>
<p>Constructs an <code>aclitem</code> with the given properties. <code>privileges</code> is a comma-separated list of privilege names such as <code>SELECT</code>, <code>INSERT</code>, etc, all of which are set in the result. (Case of the privilege string is not significant, and extra whitespace is allowed between but not within privilege names.)</p></td>
</tr>
</tbody>
</table>

### Schema Visibility Inquiry Functions

[Schema Visibility Inquiry Functions](#functions-info-schema-table) shows functions that determine whether a certain object is visible in the current schema search path. For example, a table is said to be visible if its containing schema is in the search path and no table of the same name appears earlier in the search path. This is equivalent to the statement that the table can be referenced by name without explicit schema qualification. Thus, to list the names of all visible tables:

    SELECT relname FROM pg_class WHERE pg_table_is_visible(oid);

For functions and operators, an object in the search path is said to be visible if there is no object of the same name *and argument data type(s)* earlier in the path. For operator classes and families, both the name and the associated index access method are considered.

search path

object visibility

<table id="functions-info-schema-table">
<caption>Schema Visibility Inquiry Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_collation_is_visible</code> ( <code>collation</code> <code>oid</code> ) boolean</p>
<p>Is collation visible in search path?</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_conversion_is_visible</code> ( <code>conversion</code> <code>oid</code> ) boolean</p>
<p>Is conversion visible in search path?</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_function_is_visible</code> ( <code>function</code> <code>oid</code> ) boolean</p>
<p>Is function visible in search path? (This also works for procedures and aggregates.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_opclass_is_visible</code> ( <code>opclass</code> <code>oid</code> ) boolean</p>
<p>Is operator class visible in search path?</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_operator_is_visible</code> ( <code>operator</code> <code>oid</code> ) boolean</p>
<p>Is operator visible in search path?</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_opfamily_is_visible</code> ( <code>opclass</code> <code>oid</code> ) boolean</p>
<p>Is operator family visible in search path?</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_statistics_obj_is_visible</code> ( <code>stat</code> <code>oid</code> ) boolean</p>
<p>Is statistics object visible in search path?</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_table_is_visible</code> ( <code>table</code> <code>oid</code> ) boolean</p>
<p>Is table visible in search path? (This works for all types of relations, including views, materialized views, indexes, sequences and foreign tables.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_ts_config_is_visible</code> ( <code>config</code> <code>oid</code> ) boolean</p>
<p>Is text search configuration visible in search path?</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_ts_dict_is_visible</code> ( <code>dict</code> <code>oid</code> ) boolean</p>
<p>Is text search dictionary visible in search path?</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_ts_parser_is_visible</code> ( <code>parser</code> <code>oid</code> ) boolean</p>
<p>Is text search parser visible in search path?</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_ts_template_is_visible</code> ( <code>template</code> <code>oid</code> ) boolean</p>
<p>Is text search template visible in search path?</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_type_is_visible</code> ( <code>type</code> <code>oid</code> ) boolean</p>
<p>Is type (or domain) visible in search path?</p></td>
</tr>
</tbody>
</table>

All these functions require object OIDs to identify the object to be checked. If you want to test an object by name, it is convenient to use the OID alias types (`regclass`, `regtype`, `regprocedure`, `regoperator`, `regconfig`, or `regdictionary`), for example:

    SELECT pg_type_is_visible('myschema.widget'::regtype);

Note that it would not make much sense to test a non-schema-qualified type name in this way if the name can be recognized at all, it must be visible.

### System Catalog Information Functions

[System Catalog Information Functions](#functions-info-catalog-table) lists functions that extract information from the system catalogs.

<table id="functions-info-catalog-table">
<caption>System Catalog Information Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>format_type</code> ( <code>type</code> <code>oid</code>, <code>typemod</code> <code>integer</code> ) text</p>
<p>Returns the SQL name for a data type that is identified by its type OID and possibly a type modifier. Pass NULL for the type modifier if no specific modifier is known.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_basetype</code> ( <code>regtype</code> ) regtype</p>
<p>Returns the OID of the base type of a domain identified by its type OID. If the argument is the OID of a non-domain type, returns the argument as-is. Returns NULL if the argument is not a valid type OID. If there's a chain of domain dependencies, it will recurse until finding the base type.</p>
<p>Assuming <code>CREATE DOMAIN mytext AS text</code>:</p>
<p><code>pg_basetype('mytext'::regtype)</code> text</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_char_to_encoding</code> ( <code>encoding</code> <code>name</code> ) integer</p>
<p>Converts the supplied encoding name into an integer representing the internal identifier used in some system catalog tables. Returns <code>-1</code> if an unknown encoding name is provided.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_encoding_to_char</code> ( <code>encoding</code> <code>integer</code> ) name</p>
<p>Converts the integer used as the internal identifier of an encoding in some system catalog tables into a human-readable string. Returns an empty string if an invalid encoding number is provided.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_catalog_foreign_keys</code> () setof record ( <code>fktable</code> <code>regclass</code>, <code>fkcols</code> <code>text[]</code>, <code>pktable</code> <code>regclass</code>, <code>pkcols</code> <code>text[]</code>, <code>is_array</code> <code>boolean</code>, <code>is_opt</code> <code>boolean</code> )</p>
<p>Returns a set of records describing the foreign key relationships that exist within the PostgreSQL system catalogs. The <code>fktable</code> column contains the name of the referencing catalog, and the <code>fkcols</code> column contains the name(s) of the referencing column(s). Similarly, the <code>pktable</code> column contains the name of the referenced catalog, and the <code>pkcols</code> column contains the name(s) of the referenced column(s). If <code>is_array</code> is true, the last referencing column is an array, each of whose elements should match some entry in the referenced catalog. If <code>is_opt</code> is true, the referencing column(s) are allowed to contain zeroes instead of a valid reference.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_constraintdef</code> ( <code>constraint</code> <code>oid</code> [, <code>pretty</code> <code>boolean</code>] ) text</p>
<p>Reconstructs the creating command for a constraint. (This is a decompiled reconstruction, not the original text of the command.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_expr</code> ( <code>expr</code> <code>pg_node_tree</code>, <code>relation</code> <code>oid</code> [, <code>pretty</code> <code>boolean</code>] ) text</p>
<p>Decompiles the internal form of an expression stored in the system catalogs, such as the default value for a column. If the expression might contain Vars, specify the OID of the relation they refer to as the second parameter; if no Vars are expected, passing zero is sufficient.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_functiondef</code> ( <code>func</code> <code>oid</code> ) text</p>
<p>Reconstructs the creating command for a function or procedure. (This is a decompiled reconstruction, not the original text of the command.) The result is a complete <code>CREATE OR REPLACE FUNCTION</code> or <code>CREATE OR REPLACE PROCEDURE</code> statement.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_function_arguments</code> ( <code>func</code> <code>oid</code> ) text</p>
<p>Reconstructs the argument list of a function or procedure, in the form it would need to appear in within <code>CREATE FUNCTION</code> (including default values).</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_function_identity_arguments</code> ( <code>func</code> <code>oid</code> ) text</p>
<p>Reconstructs the argument list necessary to identify a function or procedure, in the form it would need to appear in within commands such as <code>ALTER FUNCTION</code>. This form omits default values.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_function_result</code> ( <code>func</code> <code>oid</code> ) text</p>
<p>Reconstructs the <code>RETURNS</code> clause of a function, in the form it would need to appear in within <code>CREATE FUNCTION</code>. Returns <code>NULL</code> for a procedure.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_indexdef</code> ( <code>index</code> <code>oid</code> [, <code>column</code> <code>integer</code>, <code>pretty</code> <code>boolean</code>] ) text</p>
<p>Reconstructs the creating command for an index. (This is a decompiled reconstruction, not the original text of the command.) If <code>column</code> is supplied and is not zero, only the definition of that column is reconstructed.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_keywords</code> () setof record ( <code>word</code> <code>text</code>, <code>catcode</code> <code>"char"</code>, <code>barelabel</code> <code>boolean</code>, <code>catdesc</code> <code>text</code>, <code>baredesc</code> <code>text</code> )</p>
<p>Returns a set of records describing the SQL keywords recognized by the server. The <code>word</code> column contains the keyword. The <code>catcode</code> column contains a category code: <code>U</code> for an unreserved keyword, <code>C</code> for a keyword that can be a column name, <code>T</code> for a keyword that can be a type or function name, or <code>R</code> for a fully reserved keyword. The <code>barelabel</code> column contains <code>true</code> if the keyword can be used as a “bare” column label in <code>SELECT</code> lists, or <code>false</code> if it can only be used after <code>AS</code>. The <code>catdesc</code> column contains a possibly-localized string describing the keyword's category. The <code>baredesc</code> column contains a possibly-localized string describing the keyword's column label status.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_partition_constraintdef</code> ( <code>table</code> <code>oid</code> ) text</p>
<p>Reconstructs the definition of a partition constraint. (This is a decompiled reconstruction, not the original text of the command.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_partkeydef</code> ( <code>table</code> <code>oid</code> ) text</p>
<p>Reconstructs the definition of a partitioned table's partition key, in the form it would have in the <code>PARTITION BY</code> clause of <code>CREATE TABLE</code>. (This is a decompiled reconstruction, not the original text of the command.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_ruledef</code> ( <code>rule</code> <code>oid</code> [, <code>pretty</code> <code>boolean</code>] ) text</p>
<p>Reconstructs the creating command for a rule. (This is a decompiled reconstruction, not the original text of the command.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_serial_sequence</code> ( <code>table</code> <code>text</code>, <code>column</code> <code>text</code> ) text</p>
<p>Returns the name of the sequence associated with a column, or NULL if no sequence is associated with the column. If the column is an identity column, the associated sequence is the sequence internally created for that column. For columns created using one of the serial types (<code>serial</code>, <code>smallserial</code>, <code>bigserial</code>), it is the sequence created for that serial column definition. In the latter case, the association can be modified or removed with <code>ALTER SEQUENCE OWNED BY</code>. (This function probably should have been called <code>pg_get_owned_sequence</code>; its current name reflects the fact that it has historically been used with serial-type columns.) The first parameter is a table name with optional schema, and the second parameter is a column name. Because the first parameter potentially contains both schema and table names, it is parsed per usual SQL rules, meaning it is lower-cased by default. The second parameter, being just a column name, is treated literally and so has its case preserved. The result is suitably formatted for passing to the sequence functions (see <a href="#functions-sequence">Sequence Manipulation Functions</a>).</p>
<p>A typical use is in reading the current value of the sequence for an identity or serial column, for example:</p>
<pre><code>SELECT currval(pg_get_serial_sequence(&#39;sometable&#39;, &#39;id&#39;));</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_statisticsobjdef</code> ( <code>statobj</code> <code>oid</code> ) text</p>
<p>Reconstructs the creating command for an extended statistics object. (This is a decompiled reconstruction, not the original text of the command.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_triggerdef</code> ( <code>trigger</code> <code>oid</code> [, <code>pretty</code> <code>boolean</code>] ) text</p>
<p>Reconstructs the creating command for a trigger. (This is a decompiled reconstruction, not the original text of the command.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_userbyid</code> ( <code>role</code> <code>oid</code> ) name</p>
<p>Returns a role's name given its OID.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_viewdef</code> ( <code>view</code> <code>oid</code> [, <code>pretty</code> <code>boolean</code>] ) text</p>
<p>Reconstructs the underlying <code>SELECT</code> command for a view or materialized view. (This is a decompiled reconstruction, not the original text of the command.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>pg_get_viewdef</code> ( <code>view</code> <code>oid</code>, <code>wrap_column</code> <code>integer</code> ) text</p>
<p>Reconstructs the underlying <code>SELECT</code> command for a view or materialized view. (This is a decompiled reconstruction, not the original text of the command.) In this form of the function, pretty-printing is always enabled, and long lines are wrapped to try to keep them shorter than the specified number of columns.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>pg_get_viewdef</code> ( <code>view</code> <code>text</code> [, <code>pretty</code> <code>boolean</code>] ) text</p>
<p>Reconstructs the underlying <code>SELECT</code> command for a view or materialized view, working from a textual name for the view rather than its OID. (This is deprecated; use the OID variant instead.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_index_column_has_property</code> ( <code>index</code> <code>regclass</code>, <code>column</code> <code>integer</code>, <code>property</code> <code>text</code> ) boolean</p>
<p>Tests whether an index column has the named property. Common index column properties are listed in <a href="#functions-info-index-column-props">Index Column Properties</a>. (Note that extension access methods can define additional property names for their indexes.) <code>NULL</code> is returned if the property name is not known or does not apply to the particular object, or if the OID or column number does not identify a valid object.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_index_has_property</code> ( <code>index</code> <code>regclass</code>, <code>property</code> <code>text</code> ) boolean</p>
<p>Tests whether an index has the named property. Common index properties are listed in <a href="#functions-info-index-props">Index Properties</a>. (Note that extension access methods can define additional property names for their indexes.) <code>NULL</code> is returned if the property name is not known or does not apply to the particular object, or if the OID does not identify a valid object.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_indexam_has_property</code> ( <code>am</code> <code>oid</code>, <code>property</code> <code>text</code> ) boolean</p>
<p>Tests whether an index access method has the named property. Access method properties are listed in <a href="#functions-info-indexam-props">Index Access Method Properties</a>. <code>NULL</code> is returned if the property name is not known or does not apply to the particular object, or if the OID does not identify a valid object.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_options_to_table</code> ( <code>options_array</code> <code>text[]</code> ) setof record ( <code>option_name</code> <code>text</code>, <code>option_value</code> <code>text</code> )</p>
<p>Returns the set of storage options represented by a value from pg_class.reloptions or pg_attribute.attoptions.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_settings_get_flags</code> ( <code>guc</code> <code>text</code> ) text[]</p>
<p>Returns an array of the flags associated with the given GUC, or <code>NULL</code> if it does not exist. The result is an empty array if the GUC exists but there are no flags to show. Only the most useful flags listed in <a href="#functions-pg-settings-flags">GUC Flags</a> are exposed.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_tablespace_databases</code> ( <code>tablespace</code> <code>oid</code> ) setof oid</p>
<p>Returns the set of OIDs of databases that have objects stored in the specified tablespace. If this function returns any rows, the tablespace is not empty and cannot be dropped. To identify the specific objects populating the tablespace, you will need to connect to the database(s) identified by <code>pg_tablespace_databases</code> and query their pg_class catalogs.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_tablespace_location</code> ( <code>tablespace</code> <code>oid</code> ) text</p>
<p>Returns the file system path that this tablespace is located in.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_typeof</code> ( <code>"any"</code> ) regtype</p>
<p>Returns the OID of the data type of the value that is passed to it. This can be helpful for troubleshooting or dynamically constructing SQL queries. The function is declared as returning <code>regtype</code>, which is an OID alias type (see <a href="#datatype-oid">???</a>); this means that it is the same as an OID for comparison purposes but displays as a type name.</p>
<p><code>pg_typeof(33)</code> integer</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>COLLATION FOR</code> ( <code>"any"</code> ) text</p>
<p>Returns the name of the collation of the value that is passed to it. The value is quoted and schema-qualified if necessary. If no collation was derived for the argument expression, then <code>NULL</code> is returned. If the argument is not of a collatable data type, then an error is raised.</p>
<p><code>collation for ('foo'::text)</code> "default"</p>
<p><code>collation for ('foo' COLLATE "de_DE")</code> "de_DE"</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_regclass</code> ( <code>text</code> ) regclass</p>
<p>Translates a textual relation name to its OID. A similar result is obtained by casting the string to type <code>regclass</code> (see <a href="#datatype-oid">???</a>); however, this function will return <code>NULL</code> rather than throwing an error if the name is not found.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_regcollation</code> ( <code>text</code> ) regcollation</p>
<p>Translates a textual collation name to its OID. A similar result is obtained by casting the string to type <code>regcollation</code> (see <a href="#datatype-oid">???</a>); however, this function will return <code>NULL</code> rather than throwing an error if the name is not found.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_regnamespace</code> ( <code>text</code> ) regnamespace</p>
<p>Translates a textual schema name to its OID. A similar result is obtained by casting the string to type <code>regnamespace</code> (see <a href="#datatype-oid">???</a>); however, this function will return <code>NULL</code> rather than throwing an error if the name is not found.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_regoper</code> ( <code>text</code> ) regoper</p>
<p>Translates a textual operator name to its OID. A similar result is obtained by casting the string to type <code>regoper</code> (see <a href="#datatype-oid">???</a>); however, this function will return <code>NULL</code> rather than throwing an error if the name is not found or is ambiguous.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_regoperator</code> ( <code>text</code> ) regoperator</p>
<p>Translates a textual operator name (with parameter types) to its OID. A similar result is obtained by casting the string to type <code>regoperator</code> (see <a href="#datatype-oid">???</a>); however, this function will return <code>NULL</code> rather than throwing an error if the name is not found.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_regproc</code> ( <code>text</code> ) regproc</p>
<p>Translates a textual function or procedure name to its OID. A similar result is obtained by casting the string to type <code>regproc</code> (see <a href="#datatype-oid">???</a>); however, this function will return <code>NULL</code> rather than throwing an error if the name is not found or is ambiguous.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_regprocedure</code> ( <code>text</code> ) regprocedure</p>
<p>Translates a textual function or procedure name (with argument types) to its OID. A similar result is obtained by casting the string to type <code>regprocedure</code> (see <a href="#datatype-oid">???</a>); however, this function will return <code>NULL</code> rather than throwing an error if the name is not found.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_regrole</code> ( <code>text</code> ) regrole</p>
<p>Translates a textual role name to its OID. A similar result is obtained by casting the string to type <code>regrole</code> (see <a href="#datatype-oid">???</a>); however, this function will return <code>NULL</code> rather than throwing an error if the name is not found.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_regtype</code> ( <code>text</code> ) regtype</p>
<p>Parses a string of text, extracts a potential type name from it, and translates that name into a type OID. A syntax error in the string will result in an error; but if the string is a syntactically valid type name that happens not to be found in the catalogs, the result is <code>NULL</code>. A similar result is obtained by casting the string to type <code>regtype</code> (see <a href="#datatype-oid">???</a>), except that that will throw error for name not found.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>to_regtypemod</code> ( <code>text</code> ) integer</p>
<p>Parses a string of text, extracts a potential type name from it, and translates its type modifier, if any. A syntax error in the string will result in an error; but if the string is a syntactically valid type name that happens not to be found in the catalogs, the result is <code>NULL</code>. The result is <code>-1</code> if no type modifier is present.</p>
<p><code>to_regtypemod</code> can be combined with <a href="#to-regtype">to_regtype</a> to produce appropriate inputs for <a href="#format-type">format_type</a>, allowing a string representing a type name to be canonicalized.</p>
<p><code>format_type(to_regtype('varchar(32)'), to_regtypemod('varchar(32)'))</code> character varying(32)</p></td>
</tr>
</tbody>
</table>

Most of the functions that reconstruct (decompile) database objects have an optional `pretty` flag, which if `true` causes the result to be “pretty-printed”. Pretty-printing suppresses unnecessary parentheses and adds whitespace for legibility. The pretty-printed format is more readable, but the default format is more likely to be interpreted the same way by future versions of PostgreSQL; so avoid using pretty-printed output for dump purposes. Passing `false` for the `pretty` parameter yields the same result as omitting the parameter.

| Name | Description |
|----|----|
| `asc` | Does the column sort in ascending order on a forward scan? |
| `desc` | Does the column sort in descending order on a forward scan? |
| `nulls_first` | Does the column sort with nulls first on a forward scan? |
| `nulls_last` | Does the column sort with nulls last on a forward scan? |
| `orderable` | Does the column possess any defined sort ordering? |
| `distance_orderable` | Can the column be scanned in order by a “distance” operator, for example `ORDER BY col <-> constant` ? |
| `returnable` | Can the column value be returned by an index-only scan? |
| `search_array` | Does the column natively support `col = ANY(array)` searches? |
| `search_nulls` | Does the column support `IS NULL` and `IS NOT NULL` searches? |

Index Column Properties {#functions-info-index-column-props}

| Name | Description |
|----|----|
| `clusterable` | Can the index be used in a `CLUSTER` command? |
| `index_scan` | Does the index support plain (non-bitmap) scans? |
| `bitmap_scan` | Does the index support bitmap scans? |
| `backward_scan` | Can the scan direction be changed in mid-scan (to support `FETCH BACKWARD` on a cursor without needing materialization)? |

Index Properties {#functions-info-index-props}

| Name | Description |
|----|----|
| `can_order` | Does the access method support `ASC`, `DESC` and related keywords in `CREATE INDEX`? |
| `can_unique` | Does the access method support unique indexes? |
| `can_multi_col` | Does the access method support indexes with multiple columns? |
| `can_exclude` | Does the access method support exclusion constraints? |
| `can_include` | Does the access method support the `INCLUDE` clause of `CREATE INDEX`? |

Index Access Method Properties {#functions-info-indexam-props}

| Flag | Description |
|----|----|
| `EXPLAIN` | Parameters with this flag are included in `EXPLAIN (SETTINGS)` commands. |
| `NO_SHOW_ALL` | Parameters with this flag are excluded from `SHOW ALL` commands. |
| `NO_RESET` | Parameters with this flag do not support `RESET` commands. |
| `NO_RESET_ALL` | Parameters with this flag are excluded from `RESET ALL` commands. |
| `NOT_IN_SAMPLE` | Parameters with this flag are not included in `postgresql.conf` by default. |
| `RUNTIME_COMPUTED` | Parameters with this flag are runtime-computed ones. |

GUC Flags {#functions-pg-settings-flags}

### Object Information and Addressing Functions

[Object Information and Addressing Functions](#functions-info-object-table) lists functions related to database object identification and addressing.

<table id="functions-info-object-table">
<caption>Object Information and Addressing Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_describe_object</code> ( <code>classid</code> <code>oid</code>, <code>objid</code> <code>oid</code>, <code>objsubid</code> <code>integer</code> ) text</p>
<p>Returns a textual description of a database object identified by catalog OID, object OID, and sub-object ID (such as a column number within a table; the sub-object ID is zero when referring to a whole object). This description is intended to be human-readable, and might be translated, depending on server configuration. This is especially useful to determine the identity of an object referenced in the pg_depend catalog. This function returns <code>NULL</code> values for undefined objects.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_identify_object</code> ( <code>classid</code> <code>oid</code>, <code>objid</code> <code>oid</code>, <code>objsubid</code> <code>integer</code> ) record ( <code>type</code> <code>text</code>, <code>schema</code> <code>text</code>, <code>name</code> <code>text</code>, <code>identity</code> <code>text</code> )</p>
<p>Returns a row containing enough information to uniquely identify the database object specified by catalog OID, object OID and sub-object ID. This information is intended to be machine-readable, and is never translated. <code>type</code> identifies the type of database object; <code>schema</code> is the schema name that the object belongs in, or <code>NULL</code> for object types that do not belong to schemas; <code>name</code> is the name of the object, quoted if necessary, if the name (along with schema name, if pertinent) is sufficient to uniquely identify the object, otherwise <code>NULL</code>; <code>identity</code> is the complete object identity, with the precise format depending on object type, and each name within the format being schema-qualified and quoted as necessary. Undefined objects are identified with <code>NULL</code> values.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_identify_object_as_address</code> ( <code>classid</code> <code>oid</code>, <code>objid</code> <code>oid</code>, <code>objsubid</code> <code>integer</code> ) record ( <code>type</code> <code>text</code>, <code>object_names</code> <code>text[]</code>, <code>object_args</code> <code>text[]</code> )</p>
<p>Returns a row containing enough information to uniquely identify the database object specified by catalog OID, object OID and sub-object ID. The returned information is independent of the current server, that is, it could be used to identify an identically named object in another server. <code>type</code> identifies the type of database object; <code>object_names</code> and <code>object_args</code> are text arrays that together form a reference to the object. These three values can be passed to <code>pg_get_object_address</code> to obtain the internal address of the object.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_object_address</code> ( <code>type</code> <code>text</code>, <code>object_names</code> <code>text[]</code>, <code>object_args</code> <code>text[]</code> ) record ( <code>classid</code> <code>oid</code>, <code>objid</code> <code>oid</code>, <code>objsubid</code> <code>integer</code> )</p>
<p>Returns a row containing enough information to uniquely identify the database object specified by a type code and object name and argument arrays. The returned values are the ones that would be used in system catalogs such as pg_depend; they can be passed to other system functions such as <code>pg_describe_object</code> or <code>pg_identify_object</code>. <code>classid</code> is the OID of the system catalog containing the object; <code>objid</code> is the OID of the object itself, and <code>objsubid</code> is the sub-object ID, or zero if none. This function is the inverse of <code>pg_identify_object_as_address</code>. Undefined objects are identified with <code>NULL</code> values.</p></td>
</tr>
</tbody>
</table>

### Comment Information Functions

comment

about database objects

The functions shown in [Comment Information Functions](#functions-info-comment-table) extract comments previously stored with the [???](#sql-comment) command. A null value is returned if no comment could be found for the specified parameters.

<table id="functions-info-comment-table">
<caption>Comment Information Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>col_description</code> ( <code>table</code> <code>oid</code>, <code>column</code> <code>integer</code> ) text</p>
<p>Returns the comment for a table column, which is specified by the OID of its table and its column number. (<code>obj_description</code> cannot be used for table columns, since columns do not have OIDs of their own.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>obj_description</code> ( <code>object</code> <code>oid</code>, <code>catalog</code> <code>name</code> ) text</p>
<p>Returns the comment for a database object specified by its OID and the name of the containing system catalog. For example, <code>obj_description(123456, 'pg_class')</code> would retrieve the comment for the table with OID 123456.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>obj_description</code> ( <code>object</code> <code>oid</code> ) text</p>
<p>Returns the comment for a database object specified by its OID alone. This is <em>deprecated</em> since there is no guarantee that OIDs are unique across different system catalogs; therefore, the wrong comment might be returned.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>shobj_description</code> ( <code>object</code> <code>oid</code>, <code>catalog</code> <code>name</code> ) text</p>
<p>Returns the comment for a shared database object specified by its OID and the name of the containing system catalog. This is just like <code>obj_description</code> except that it is used for retrieving comments on shared objects (that is, databases, roles, and tablespaces). Some system catalogs are global to all databases within each cluster, and the descriptions for objects in them are stored globally as well.</p></td>
</tr>
</tbody>
</table>

### Data Validity Checking Functions

The functions shown in [Data Validity Checking Functions](#functions-info-validity-table) can be helpful for checking validity of proposed input data.

<table id="functions-info-validity-table">
<caption>Data Validity Checking Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_input_is_valid</code> ( <code>string</code> <code>text</code>, <code>type</code> <code>text</code> ) boolean</p>
<p>Tests whether the given <code>string</code> is valid input for the specified data type, returning true or false.</p>
<p>This function will only work as desired if the data type's input function has been updated to report invalid input as a “soft” error. Otherwise, invalid input will abort the transaction, just as if the string had been cast to the type directly.</p>
<p><code>pg_input_is_valid('42', 'integer')</code> t</p>
<p><code>pg_input_is_valid('42000000000', 'integer')</code> f</p>
<p><code>pg_input_is_valid('1234.567', 'numeric(7,4)')</code> f</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_input_error_info</code> ( <code>string</code> <code>text</code>, <code>type</code> <code>text</code> ) record ( <code>message</code> <code>text</code>, <code>detail</code> <code>text</code>, <code>hint</code> <code>text</code>, <code>sql_error_code</code> <code>text</code> )</p>
<p>Tests whether the given <code>string</code> is valid input for the specified data type; if not, return the details of the error that would have been thrown. If the input is valid, the results are NULL. The inputs are the same as for <code>pg_input_is_valid</code>.</p>
<p>This function will only work as desired if the data type's input function has been updated to report invalid input as a “soft” error. Otherwise, invalid input will abort the transaction, just as if the string had been cast to the type directly.</p>
<p><code>SELECT * FROM pg_input_error_info('42000000000', 'integer')</code></p>
<pre><code>                       message                        | detail | hint | sql_error_code
------------------------------------------------------+--------+------+----------------
 value &quot;42000000000&quot; is out of range for type integer |        |      | 22003</code></pre></td>
</tr>
</tbody>
</table>

### Transaction ID and Snapshot Information Functions

The functions shown in [Transaction ID and Snapshot Information Functions](#functions-pg-snapshot) provide server transaction information in an exportable form. The main use of these functions is to determine which transactions were committed between two snapshots.

<table id="functions-pg-snapshot">
<caption>Transaction ID and Snapshot Information Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>age</code> ( <code>xid</code> ) integer</p>
<p>Returns the number of transactions between the supplied transaction id and the current transaction counter.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>mxid_age</code> ( <code>xid</code> ) integer</p>
<p>Returns the number of multixacts IDs between the supplied multixact ID and the current multixacts counter.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_current_xact_id</code> () xid8</p>
<p>Returns the current transaction's ID. It will assign a new one if the current transaction does not have one already (because it has not performed any database updates); see <a href="#transaction-id">???</a> for details. If executed in a subtransaction, this will return the top-level transaction ID; see <a href="#subxacts">???</a> for details.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_current_xact_id_if_assigned</code> () xid8</p>
<p>Returns the current transaction's ID, or <code>NULL</code> if no ID is assigned yet. (It's best to use this variant if the transaction might otherwise be read-only, to avoid unnecessary consumption of an XID.) If executed in a subtransaction, this will return the top-level transaction ID.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_xact_status</code> ( <code>xid8</code> ) text</p>
<p>Reports the commit status of a recent transaction. The result is one of <code>in progress</code>, <code>committed</code>, or <code>aborted</code>, provided that the transaction is recent enough that the system retains the commit status of that transaction. If it is old enough that no references to the transaction survive in the system and the commit status information has been discarded, the result is <code>NULL</code>. Applications might use this function, for example, to determine whether their transaction committed or aborted after the application and database server become disconnected while a <code>COMMIT</code> is in progress. Note that prepared transactions are reported as <code>in progress</code>; applications must check <a href="#view-pg-prepared-xacts">pg_prepared_xacts</a> if they need to determine whether a transaction ID belongs to a prepared transaction.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_current_snapshot</code> () pg_snapshot</p>
<p>Returns a current snapshot, a data structure showing which transaction IDs are now in-progress. Only top-level transaction IDs are included in the snapshot; subtransaction IDs are not shown; see <a href="#subxacts">???</a> for details.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_snapshot_xip</code> ( <code>pg_snapshot</code> ) setof xid8</p>
<p>Returns the set of in-progress transaction IDs contained in a snapshot.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_snapshot_xmax</code> ( <code>pg_snapshot</code> ) xid8</p>
<p>Returns the xmax of a snapshot.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_snapshot_xmin</code> ( <code>pg_snapshot</code> ) xid8</p>
<p>Returns the xmin of a snapshot.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_visible_in_snapshot</code> ( <code>xid8</code>, <code>pg_snapshot</code> ) boolean</p>
<p>Is the given transaction ID visible according to this snapshot (that is, was it completed before the snapshot was taken)? Note that this function will not give the correct answer for a subtransaction ID (subxid); see <a href="#subxacts">???</a> for details.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_multixact_members</code> ( <code>multixid</code> <code>xid</code> ) setof record ( <code>xid</code> <code>xid</code>, <code>mode</code> <code>text</code> )</p>
<p>Returns the transaction ID and lock mode for each member of the specified multixact ID. The lock modes <code>forupd</code>, <code>fornokeyupd</code>, <code>sh</code>, and <code>keysh</code> correspond to the row-level locks <code>FOR UPDATE</code>, <code>FOR NO KEY UPDATE</code>, <code>FOR SHARE</code>, and <code>FOR KEY SHARE</code>, respectively, as described in <a href="#locking-rows">???</a>. Two additional modes are specific to multixacts: <code>nokeyupd</code>, used by updates that do not modify key columns, and <code>upd</code>, used by updates or deletes that modify key columns.</p></td>
</tr>
</tbody>
</table>

The internal transaction ID type `xid` is 32 bits wide and wraps around every 4 billion transactions. However, the functions shown in [Transaction ID and Snapshot Information Functions](#functions-pg-snapshot), except `age`, `mxid_age`, and `pg_get_multixact_members`, use a 64-bit type `xid8` that does not wrap around during the life of an installation and can be converted to `xid` by casting if required; see [???](#transaction-id) for details. The data type `pg_snapshot` stores information about transaction ID visibility at a particular moment in time. Its components are described in [Snapshot Components](#functions-pg-snapshot-parts). `pg_snapshot`'s textual representation is `xmin:xmax:xip_list`. For example `10:20:10,14,15` means `xmin=10, xmax=20, xip_list=10, 14, 15`.

| Name | Description |
|----|----|
| xmin | Lowest transaction ID that was still active. All transaction IDs less than xmin are either committed and visible, or rolled back and dead. |
| xmax | One past the highest completed transaction ID. All transaction IDs greater than or equal to xmax had not yet completed as of the time of the snapshot, and thus are invisible. |
| xip_list | Transactions in progress at the time of the snapshot. A transaction ID that is `xmin <= X < xmax` and not in this list was already completed at the time of the snapshot, and thus is either visible or dead according to its commit status. This list does not include the transaction IDs of subtransactions (subxids). |

Snapshot Components {#functions-pg-snapshot-parts}

In releases of PostgreSQL before 13 there was no `xid8` type, so variants of these functions were provided that used `bigint` to represent a 64-bit XID, with a correspondingly distinct snapshot data type `txid_snapshot`. These older functions have `txid` in their names. They are still supported for backward compatibility, but may be removed from a future release. See [Deprecated Transaction ID and Snapshot Information Functions](#functions-txid-snapshot).

<table id="functions-txid-snapshot">
<caption>Deprecated Transaction ID and Snapshot Information Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>txid_current</code> () bigint</p>
<p>See <code>pg_current_xact_id()</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>txid_current_if_assigned</code> () bigint</p>
<p>See <code>pg_current_xact_id_if_assigned()</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>txid_current_snapshot</code> () txid_snapshot</p>
<p>See <code>pg_current_snapshot()</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>txid_snapshot_xip</code> ( <code>txid_snapshot</code> ) setof bigint</p>
<p>See <code>pg_snapshot_xip()</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>txid_snapshot_xmax</code> ( <code>txid_snapshot</code> ) bigint</p>
<p>See <code>pg_snapshot_xmax()</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>txid_snapshot_xmin</code> ( <code>txid_snapshot</code> ) bigint</p>
<p>See <code>pg_snapshot_xmin()</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>txid_visible_in_snapshot</code> ( <code>bigint</code>, <code>txid_snapshot</code> ) boolean</p>
<p>See <code>pg_visible_in_snapshot()</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>txid_status</code> ( <code>bigint</code> ) text</p>
<p>See <code>pg_xact_status()</code>.</p></td>
</tr>
</tbody>
</table>

### Committed Transaction Information Functions

The functions shown in [Committed Transaction Information Functions](#functions-commit-timestamp) provide information about when past transactions were committed. They only provide useful data when the [???](#guc-track-commit-timestamp) configuration option is enabled, and only for transactions that were committed after it was enabled. Commit timestamp information is routinely removed during vacuum.

<table id="functions-commit-timestamp">
<caption>Committed Transaction Information Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_xact_commit_timestamp</code> ( <code>xid</code> ) timestamp with time zone</p>
<p>Returns the commit timestamp of a transaction.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_xact_commit_timestamp_origin</code> ( <code>xid</code> ) record ( <code>timestamp</code> <code>timestamp with time zone</code>, <code>roident</code> <code>oid</code>)</p>
<p>Returns the commit timestamp and replication origin of a transaction.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_last_committed_xact</code> () record ( <code>xid</code> <code>xid</code>, <code>timestamp</code> <code>timestamp with time zone</code>, <code>roident</code> <code>oid</code> )</p>
<p>Returns the transaction ID, commit timestamp and replication origin of the latest committed transaction.</p></td>
</tr>
</tbody>
</table>

### Control Data Functions

The functions shown in [Control Data Functions](#functions-controldata) print information initialized during `initdb`, such as the catalog version. They also show information about write-ahead logging and checkpoint processing. This information is cluster-wide, not specific to any one database. These functions provide most of the same information, from the same source, as the [???](#app-pgcontroldata) application.

<table id="functions-controldata">
<caption>Control Data Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_control_checkpoint</code> () record</p>
<p>Returns information about current checkpoint state, as shown in <a href="#functions-pg-control-checkpoint"> Output Columns</a>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_control_system</code> () record</p>
<p>Returns information about current control file state, as shown in <a href="#functions-pg-control-system"> Output Columns</a>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_control_init</code> () record</p>
<p>Returns information about cluster initialization state, as shown in <a href="#functions-pg-control-init"> Output Columns</a>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_control_recovery</code> () record</p>
<p>Returns information about recovery state, as shown in <a href="#functions-pg-control-recovery"> Output Columns</a>.</p></td>
</tr>
</tbody>
</table>

| Column Name          | Data Type                  |
|----------------------|----------------------------|
| checkpoint_lsn       | `pg_lsn`                   |
| redo_lsn             | `pg_lsn`                   |
| redo_wal_file        | `text`                     |
| timeline_id          | `integer`                  |
| prev_timeline_id     | `integer`                  |
| full_page_writes     | `boolean`                  |
| next_xid             | `text`                     |
| next_oid             | `oid`                      |
| next_multixact_id    | `xid`                      |
| next_multi_offset    | `xid`                      |
| oldest_xid           | `xid`                      |
| oldest_xid_dbid      | `oid`                      |
| oldest_active_xid    | `xid`                      |
| oldest_multi_xid     | `xid`                      |
| oldest_multi_dbid    | `oid`                      |
| oldest_commit_ts_xid | `xid`                      |
| newest_commit_ts_xid | `xid`                      |
| checkpoint_time      | `timestamp with time zone` |

`pg_control_checkpoint` Output Columns {#functions-pg-control-checkpoint}

| Column Name              | Data Type                  |
|--------------------------|----------------------------|
| pg_control_version       | `integer`                  |
| catalog_version_no       | `integer`                  |
| system_identifier        | `bigint`                   |
| pg_control_last_modified | `timestamp with time zone` |

`pg_control_system` Output Columns {#functions-pg-control-system}

| Column Name                | Data Type |
|----------------------------|-----------|
| max_data_alignment         | `integer` |
| database_block_size        | `integer` |
| blocks_per_segment         | `integer` |
| wal_block_size             | `integer` |
| bytes_per_wal_segment      | `integer` |
| max_identifier_length      | `integer` |
| max_index_columns          | `integer` |
| max_toast_chunk_size       | `integer` |
| large_object_chunk_size    | `integer` |
| float8_pass_by_value       | `boolean` |
| data_page_checksum_version | `integer` |

`pg_control_init` Output Columns {#functions-pg-control-init}

| Column Name                   | Data Type |
|-------------------------------|-----------|
| min_recovery_end_lsn          | `pg_lsn`  |
| min_recovery_end_timeline     | `integer` |
| backup_start_lsn              | `pg_lsn`  |
| backup_end_lsn                | `pg_lsn`  |
| end_of_backup_record_required | `boolean` |

`pg_control_recovery` Output Columns {#functions-pg-control-recovery}

### Version Information Functions

The functions shown in [Version Information Functions](#functions-version) print version information.

<table id="functions-version">
<caption>Version Information Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>version</code> () text</p>
<p>Returns a string describing the PostgreSQL server's version. You can also get this information from <a href="#guc-server-version">???</a>, or for a machine-readable version use <a href="#guc-server-version-num">???</a>. Software developers should use <code>server_version_num</code> (available since 8.2) or <a href="#libpq-PQserverVersion">???</a> instead of parsing the text version.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>unicode_version</code> () text</p>
<p>Returns a string representing the version of Unicode used by PostgreSQL.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>icu_unicode_version</code> () text</p>
<p>Returns a string representing the version of Unicode used by ICU, if the server was built with ICU support; otherwise returns <code>NULL</code></p></td>
</tr>
</tbody>
</table>

### WAL Summarization Information Functions

The functions shown in [WAL Summarization Information Functions](#functions-wal-summary) print information about the status of WAL summarization. See [???](#guc-summarize-wal).

<table id="functions-wal-summary">
<caption>WAL Summarization Information Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_available_wal_summaries</code> () setof record ( <code>tli</code> <code>bigint</code>, <code>start_lsn</code> <code>pg_lsn</code>, <code>end_lsn</code> <code>pg_lsn</code> )</p>
<p>Returns information about the WAL summary files present in the data directory, under <code>pg_wal/summaries</code>. One row will be returned per WAL summary file. Each file summarizes WAL on the indicated TLI within the indicated LSN range. This function might be useful to determine whether enough WAL summaries are present on the server to take an incremental backup based on some prior backup whose start LSN is known.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_wal_summary_contents</code> ( <code>tli</code> <code>bigint</code>, <code>start_lsn</code> <code>pg_lsn</code>, <code>end_lsn</code> <code>pg_lsn</code> ) setof record ( <code>relfilenode</code> <code>oid</code>, <code>reltablespace</code> <code>oid</code>, <code>reldatabase</code> <code>oid</code>, <code>relforknumber</code> <code>smallint</code>, <code>relblocknumber</code> <code>bigint</code>, <code>is_limit_block</code> <code>boolean</code> )</p>
<p>Returns one information about the contents of a single WAL summary file identified by TLI and starting and ending LSNs. Each row with <code>is_limit_block</code> false indicates that the block identified by the remaining output columns was modified by at least one WAL record within the range of records summarized by this file. Each row with <code>is_limit_block</code> true indicates either that (a) the relation fork was truncated to the length given by <code>relblocknumber</code> within the relevant range of WAL records or (b) that the relation fork was created or dropped within the relevant range of WAL records; in such cases, <code>relblocknumber</code> will be zero.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_wal_summarizer_state</code> () record ( <code>summarized_tli</code> <code>bigint</code>, <code>summarized_lsn</code> <code>pg_lsn</code>, <code>pending_lsn</code> <code>pg_lsn</code>, <code>summarizer_pid</code> <code>int</code> )</p>
<p>Returns information about the progress of the WAL summarizer. If the WAL summarizer has never run since the instance was started, then <code>summarized_tli</code> and <code>summarized_lsn</code> will be <code>0</code> and <code>0/0</code> respectively; otherwise, they will be the TLI and ending LSN of the last WAL summary file written to disk. If the WAL summarizer is currently running, <code>pending_lsn</code> will be the ending LSN of the last record that it has consumed, which must always be greater than or equal to <code>summarized_lsn</code>; if the WAL summarizer is not running, it will be equal to <code>summarized_lsn</code>. <code>summarizer_pid</code> is the PID of the WAL summarizer process, if it is running, and otherwise NULL.</p>
<p>As a special exception, the WAL summarizer will refuse to generate WAL summary files if run on WAL generated under <code>wal_level=minimal</code>, since such summaries would be unsafe to use as the basis for an incremental backup. In this case, the fields above will continue to advance as if summaries were being generated, but nothing will be written to disk. Once the summarizer reaches WAL generated while <code>wal_level</code> was set to <code>replica</code> or higher, it will resume writing summaries to disk.</p></td>
</tr>
</tbody>
</table>

## System Administration Functions

The functions described in this section are used to control and monitor a PostgreSQL installation.

### Configuration Settings Functions

SET

SHOW

configuration

of the server

functions

[Configuration Settings Functions](#functions-admin-set-table) shows the functions available to query and alter run-time configuration parameters.

<table id="functions-admin-set-table">
<caption>Configuration Settings Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>current_setting</code> ( <code>setting_name</code> <code>text</code> [, <code>missing_ok</code> <code>boolean</code>] ) text</p>
<p>Returns the current value of the setting <code>setting_name</code>. If there is no such setting, <code>current_setting</code> throws an error unless <code>missing_ok</code> is supplied and is <code>true</code> (in which case NULL is returned). This function corresponds to the SQL command <a href="#sql-show">???</a>.</p>
<p><code>current_setting('datestyle')</code> ISO, MDY</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>set_config</code> ( <code>setting_name</code> <code>text</code>, <code>new_value</code> <code>text</code>, <code>is_local</code> <code>boolean</code> ) text</p>
<p>Sets the parameter <code>setting_name</code> to <code>new_value</code>, and returns that value. If <code>is_local</code> is <code>true</code>, the new value will only apply during the current transaction. If you want the new value to apply for the rest of the current session, use <code>false</code> instead. This function corresponds to the SQL command <a href="#sql-set">???</a>.</p>
<p><code>set_config('log_statement_stats', 'off', false)</code> off</p></td>
</tr>
</tbody>
</table>

### Server Signaling Functions

signal

backend processes

The functions shown in [Server Signaling Functions](#functions-admin-signal-table) send control signals to other server processes. Use of these functions is restricted to superusers by default but access may be granted to others using `GRANT`, with noted exceptions.

Each of these functions returns `true` if the signal was successfully sent and `false` if sending the signal failed.

<table id="functions-admin-signal-table">
<caption>Server Signaling Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_cancel_backend</code> ( <code>pid</code> <code>integer</code> ) boolean</p>
<p>Cancels the current query of the session whose backend process has the specified process ID. This is also allowed if the calling role is a member of the role whose backend is being canceled or the calling role has privileges of <code>pg_signal_backend</code>, however only superusers can cancel superuser backends.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_log_backend_memory_contexts</code> ( <code>pid</code> <code>integer</code> ) boolean</p>
<p>Requests to log the memory contexts of the backend with the specified process ID. This function can send the request to backends and auxiliary processes except logger. These memory contexts will be logged at <code>LOG</code> message level. They will appear in the server log based on the log configuration set (see <a href="#runtime-config-logging">???</a> for more information), but will not be sent to the client regardless of <a href="#guc-client-min-messages">???</a>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_reload_conf</code> () boolean</p>
<p>Causes all processes of the PostgreSQL server to reload their configuration files. (This is initiated by sending a <code>SIGHUP</code> signal to the postmaster process, which in turn sends <code>SIGHUP</code> to each of its children.) You can use the <a href="#view-pg-file-settings">pg_file_settings</a>, <a href="#view-pg-hba-file-rules">pg_hba_file_rules</a> and <a href="#view-pg-ident-file-mappings">pg_ident_file_mappings</a> views to check the configuration files for possible errors, before reloading.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_rotate_logfile</code> () boolean</p>
<p>Signals the log-file manager to switch to a new output file immediately. This works only when the built-in log collector is running, since otherwise there is no log-file manager subprocess.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_terminate_backend</code> ( <code>pid</code> <code>integer</code>, <code>timeout</code> <code>bigint</code> <code>DEFAULT</code> <code>0</code> ) boolean</p>
<p>Terminates the session whose backend process has the specified process ID. This is also allowed if the calling role is a member of the role whose backend is being terminated or the calling role has privileges of <code>pg_signal_backend</code>, however only superusers can terminate superuser backends.</p>
<p>If <code>timeout</code> is not specified or zero, this function returns <code>true</code> whether the process actually terminates or not, indicating only that the sending of the signal was successful. If the <code>timeout</code> is specified (in milliseconds) and greater than zero, the function waits until the process is actually terminated or until the given time has passed. If the process is terminated, the function returns <code>true</code>. On timeout, a warning is emitted and <code>false</code> is returned.</p></td>
</tr>
</tbody>
</table>

`pg_cancel_backend` and `pg_terminate_backend` send signals (`SIGINT` or `SIGTERM` respectively) to backend processes identified by process ID. The process ID of an active backend can be found from the pid column of the pg_stat_activity view, or by listing the `postgres` processes on the server (using ps on Unix or the Task Manager on Windows). The role of an active backend can be found from the usename column of the pg_stat_activity view.

`pg_log_backend_memory_contexts` can be used to log the memory contexts of a backend process. For example:

    postgres=# SELECT pg_log_backend_memory_contexts(pg_backend_pid());
     pg_log_backend_memory_contexts
    --------------------------------
     t
    (1 row)

One message for each memory context will be logged. For example:

    LOG:  logging memory contexts of PID 10377
    STATEMENT:  SELECT pg_log_backend_memory_contexts(pg_backend_pid());
    LOG:  level: 0; TopMemoryContext: 80800 total in 6 blocks; 14432 free (5 chunks); 66368 used
    LOG:  level: 1; pgstat TabStatusArray lookup hash table: 8192 total in 1 blocks; 1408 free (0 chunks); 6784 used
    LOG:  level: 1; TopTransactionContext: 8192 total in 1 blocks; 7720 free (1 chunks); 472 used
    LOG:  level: 1; RowDescriptionContext: 8192 total in 1 blocks; 6880 free (0 chunks); 1312 used
    LOG:  level: 1; MessageContext: 16384 total in 2 blocks; 5152 free (0 chunks); 11232 used
    LOG:  level: 1; Operator class cache: 8192 total in 1 blocks; 512 free (0 chunks); 7680 used
    LOG:  level: 1; smgr relation table: 16384 total in 2 blocks; 4544 free (3 chunks); 11840 used
    LOG:  level: 1; TransactionAbortContext: 32768 total in 1 blocks; 32504 free (0 chunks); 264 used
    ...
    LOG:  level: 1; ErrorContext: 8192 total in 1 blocks; 7928 free (3 chunks); 264 used
    LOG:  Grand total: 1651920 bytes in 201 blocks; 622360 free (88 chunks); 1029560 used

If there are more than 100 child contexts under the same parent, the first 100 child contexts are logged, along with a summary of the remaining contexts. Note that frequent calls to this function could incur significant overhead, because it may generate a large number of log messages.

### Backup Control Functions

backup

The functions shown in [Backup Control Functions](#functions-admin-backup-table) assist in making on-line backups. These functions cannot be executed during recovery (except `pg_backup_start`, `pg_backup_stop`, and `pg_wal_lsn_diff`).

For details about proper usage of these functions, see [???](#continuous-archiving).

<table id="functions-admin-backup-table">
<caption>Backup Control Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_create_restore_point</code> ( <code>name</code> <code>text</code> ) pg_lsn</p>
<p>Creates a named marker record in the write-ahead log that can later be used as a recovery target, and returns the corresponding write-ahead log location. The given name can then be used with <a href="#guc-recovery-target-name">???</a> to specify the point up to which recovery will proceed. Avoid creating multiple restore points with the same name, since recovery will stop at the first one whose name matches the recovery target.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_current_wal_flush_lsn</code> () pg_lsn</p>
<p>Returns the current write-ahead log flush location (see notes below).</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_current_wal_insert_lsn</code> () pg_lsn</p>
<p>Returns the current write-ahead log insert location (see notes below).</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_current_wal_lsn</code> () pg_lsn</p>
<p>Returns the current write-ahead log write location (see notes below).</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_backup_start</code> ( <code>label</code> <code>text</code> [, <code>fast</code> <code>boolean</code>] ) pg_lsn</p>
<p>Prepares the server to begin an on-line backup. The only required parameter is an arbitrary user-defined label for the backup. (Typically this would be the name under which the backup dump file will be stored.) If the optional second parameter is given as <code>true</code>, it specifies executing <code>pg_backup_start</code> as quickly as possible. This forces an immediate checkpoint which will cause a spike in I/O operations, slowing any concurrently executing queries.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_backup_stop</code> ( [<code>wait_for_archive</code> <code>boolean</code>] ) record ( <code>lsn</code> <code>pg_lsn</code>, <code>labelfile</code> <code>text</code>, <code>spcmapfile</code> <code>text</code> )</p>
<p>Finishes performing an on-line backup. The desired contents of the backup label file and the tablespace map file are returned as part of the result of the function and must be written to files in the backup area. These files must not be written to the live data directory (doing so will cause PostgreSQL to fail to restart in the event of a crash).</p>
<p>There is an optional parameter of type <code>boolean</code>. If false, the function will return immediately after the backup is completed, without waiting for WAL to be archived. This behavior is only useful with backup software that independently monitors WAL archiving. Otherwise, WAL required to make the backup consistent might be missing and make the backup useless. By default or when this parameter is true, <code>pg_backup_stop</code> will wait for WAL to be archived when archiving is enabled. (On a standby, this means that it will wait only when <code>archive_mode</code> = <code>always</code>. If write activity on the primary is low, it may be useful to run <code>pg_switch_wal</code> on the primary in order to trigger an immediate segment switch.)</p>
<p>When executed on a primary, this function also creates a backup history file in the write-ahead log archive area. The history file includes the label given to <code>pg_backup_start</code>, the starting and ending write-ahead log locations for the backup, and the starting and ending times of the backup. After recording the ending location, the current write-ahead log insertion point is automatically advanced to the next write-ahead log file, so that the ending write-ahead log file can be archived immediately to complete the backup.</p>
<p>The result of the function is a single record. The <code>lsn</code> column holds the backup's ending write-ahead log location (which again can be ignored). The second column returns the contents of the backup label file, and the third column returns the contents of the tablespace map file. These must be stored as part of the backup and are required as part of the restore process.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_switch_wal</code> () pg_lsn</p>
<p>Forces the server to switch to a new write-ahead log file, which allows the current file to be archived (assuming you are using continuous archiving). The result is the ending write-ahead log location plus 1 within the just-completed write-ahead log file. If there has been no write-ahead log activity since the last write-ahead log switch, <code>pg_switch_wal</code> does nothing and returns the start location of the write-ahead log file currently in use.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_walfile_name</code> ( <code>lsn</code> <code>pg_lsn</code> ) text</p>
<p>Converts a write-ahead log location to the name of the WAL file holding that location.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_walfile_name_offset</code> ( <code>lsn</code> <code>pg_lsn</code> ) record ( <code>file_name</code> <code>text</code>, <code>file_offset</code> <code>integer</code> )</p>
<p>Converts a write-ahead log location to a WAL file name and byte offset within that file.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_split_walfile_name</code> ( <code>file_name</code> <code>text</code> ) record ( <code>segment_number</code> <code>numeric</code>, <code>timeline_id</code> <code>bigint</code> )</p>
<p>Extracts the sequence number and timeline ID from a WAL file name.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_wal_lsn_diff</code> ( <code>lsn1</code> <code>pg_lsn</code>, <code>lsn2</code> <code>pg_lsn</code> ) numeric</p>
<p>Calculates the difference in bytes (<code>lsn1</code> - <code>lsn2</code>) between two write-ahead log locations. This can be used with pg_stat_replication or some of the functions shown in <a href="#functions-admin-backup-table">Backup Control Functions</a> to get the replication lag.</p></td>
</tr>
</tbody>
</table>

`pg_current_wal_lsn` displays the current write-ahead log write location in the same format used by the above functions. Similarly, `pg_current_wal_insert_lsn` displays the current write-ahead log insertion location and `pg_current_wal_flush_lsn` displays the current write-ahead log flush location. The insertion location is the “logical” end of the write-ahead log at any instant, while the write location is the end of what has actually been written out from the server's internal buffers, and the flush location is the last location known to be written to durable storage. The write location is the end of what can be examined from outside the server, and is usually what you want if you are interested in archiving partially-complete write-ahead log files. The insertion and flush locations are made available primarily for server debugging purposes. These are all read-only operations and do not require superuser permissions.

You can use `pg_walfile_name_offset` to extract the corresponding write-ahead log file name and byte offset from a `pg_lsn` value. For example:

    postgres=# SELECT * FROM pg_walfile_name_offset((pg_backup_stop()).lsn);
            file_name         | file_offset
    --------------------------+-------------
     00000001000000000000000D |     4039624
    (1 row)

Similarly, `pg_walfile_name` extracts just the write-ahead log file name.

`pg_split_walfile_name` is useful to compute a LSN from a file offset and WAL file name, for example:

    postgres=# \set file_name '000000010000000100C000AB'
    postgres=# \set offset 256
    postgres=# SELECT '0/0'::pg_lsn + pd.segment_number * ps.setting::int + :offset AS lsn
      FROM pg_split_walfile_name(:'file_name') pd,
           pg_show_all_settings() ps
      WHERE ps.name = 'wal_segment_size';
          lsn
    ---------------
     C001/AB000100
    (1 row)

### Recovery Control Functions

The functions shown in [Recovery Information Functions](#functions-recovery-info-table) provide information about the current status of a standby server. These functions may be executed both during recovery and in normal running.

<table id="functions-recovery-info-table">
<caption>Recovery Information Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_is_in_recovery</code> () boolean</p>
<p>Returns true if recovery is still in progress.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_last_wal_receive_lsn</code> () pg_lsn</p>
<p>Returns the last write-ahead log location that has been received and synced to disk by streaming replication. While streaming replication is in progress this will increase monotonically. If recovery has completed then this will remain static at the location of the last WAL record received and synced to disk during recovery. If streaming replication is disabled, or if it has not yet started, the function returns <code>NULL</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_last_wal_replay_lsn</code> () pg_lsn</p>
<p>Returns the last write-ahead log location that has been replayed during recovery. If recovery is still in progress this will increase monotonically. If recovery has completed then this will remain static at the location of the last WAL record applied during recovery. When the server has been started normally without recovery, the function returns <code>NULL</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_last_xact_replay_timestamp</code> () timestamp with time zone</p>
<p>Returns the time stamp of the last transaction replayed during recovery. This is the time at which the commit or abort WAL record for that transaction was generated on the primary. If no transactions have been replayed during recovery, the function returns <code>NULL</code>. Otherwise, if recovery is still in progress this will increase monotonically. If recovery has completed then this will remain static at the time of the last transaction applied during recovery. When the server has been started normally without recovery, the function returns <code>NULL</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_wal_resource_managers</code> () setof record ( <code>rm_id</code> <code>integer</code>, <code>rm_name</code> <code>text</code>, <code>rm_builtin</code> <code>boolean</code> )</p>
<p>Returns the currently-loaded WAL resource managers in the system. The column <code>rm_builtin</code> indicates whether it's a built-in resource manager, or a custom resource manager loaded by an extension.</p></td>
</tr>
</tbody>
</table>

The functions shown in [Recovery Control Functions](#functions-recovery-control-table) control the progress of recovery. These functions may be executed only during recovery.

<table id="functions-recovery-control-table">
<caption>Recovery Control Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_is_wal_replay_paused</code> () boolean</p>
<p>Returns true if recovery pause is requested.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_get_wal_replay_pause_state</code> () text</p>
<p>Returns recovery pause state. The return values are <code>not paused</code> if pause is not requested, <code>pause requested</code> if pause is requested but recovery is not yet paused, and <code>paused</code> if the recovery is actually paused.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_promote</code> ( <code>wait</code> <code>boolean</code> <code>DEFAULT</code> <code>true</code>, <code>wait_seconds</code> <code>integer</code> <code>DEFAULT</code> <code>60</code> ) boolean</p>
<p>Promotes a standby server to primary status. With <code>wait</code> set to <code>true</code> (the default), the function waits until promotion is completed or <code>wait_seconds</code> seconds have passed, and returns <code>true</code> if promotion is successful and <code>false</code> otherwise. If <code>wait</code> is set to <code>false</code>, the function returns <code>true</code> immediately after sending a <code>SIGUSR1</code> signal to the postmaster to trigger promotion.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_wal_replay_pause</code> () void</p>
<p>Request to pause recovery. A request doesn't mean that recovery stops right away. If you want a guarantee that recovery is actually paused, you need to check for the recovery pause state returned by <code>pg_get_wal_replay_pause_state()</code>. Note that <code>pg_is_wal_replay_paused()</code> returns whether a request is made. While recovery is paused, no further database changes are applied. If hot standby is active, all new queries will see the same consistent snapshot of the database, and no further query conflicts will be generated until recovery is resumed.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_wal_replay_resume</code> () void</p>
<p>Restarts recovery if it was paused.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
</tbody>
</table>

`pg_wal_replay_pause` and `pg_wal_replay_resume` cannot be executed while a promotion is ongoing. If a promotion is triggered while recovery is paused, the paused state ends and promotion continues.

If streaming replication is disabled, the paused state may continue indefinitely without a problem. If streaming replication is in progress then WAL records will continue to be received, which will eventually fill available disk space, depending upon the duration of the pause, the rate of WAL generation and available disk space.

### Snapshot Synchronization Functions

PostgreSQL allows database sessions to synchronize their snapshots. A snapshot determines which data is visible to the transaction that is using the snapshot. Synchronized snapshots are necessary when two or more sessions need to see identical content in the database. If two sessions just start their transactions independently, there is always a possibility that some third transaction commits between the executions of the two `START TRANSACTION` commands, so that one session sees the effects of that transaction and the other does not.

To solve this problem, PostgreSQL allows a transaction to export the snapshot it is using. As long as the exporting transaction remains open, other transactions can import its snapshot, and thereby be guaranteed that they see exactly the same view of the database that the first transaction sees. But note that any database changes made by any one of these transactions remain invisible to the other transactions, as is usual for changes made by uncommitted transactions. So the transactions are synchronized with respect to pre-existing data, but act normally for changes they make themselves.

Snapshots are exported with the `pg_export_snapshot` function, shown in [Snapshot Synchronization Functions](#functions-snapshot-synchronization-table), and imported with the [???](#sql-set-transaction) command.

<table id="functions-snapshot-synchronization-table">
<caption>Snapshot Synchronization Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_export_snapshot</code> () text</p>
<p>Saves the transaction's current snapshot and returns a <code>text</code> string identifying the snapshot. This string must be passed (outside the database) to clients that want to import the snapshot. The snapshot is available for import only until the end of the transaction that exported it.</p>
<p>A transaction can export more than one snapshot, if needed. Note that doing so is only useful in <code>READ COMMITTED</code> transactions, since in <code>REPEATABLE READ</code> and higher isolation levels, transactions use the same snapshot throughout their lifetime. Once a transaction has exported any snapshots, it cannot be prepared with <a href="#sql-prepare-transaction">???</a>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_log_standby_snapshot</code> () pg_lsn</p>
<p>Take a snapshot of running transactions and write it to WAL, without having to wait for bgwriter or checkpointer to log one. This is useful for logical decoding on standby, as logical slot creation has to wait until such a record is replayed on the standby.</p></td>
</tr>
</tbody>
</table>

### Replication Management Functions

The functions shown in [Replication Management Functions](#functions-replication-table) are for controlling and interacting with replication features. See [???](#streaming-replication), [???](#streaming-replication-slots), and [???](#replication-origins) for information about the underlying features. Use of functions for replication origin is only allowed to the superuser by default, but may be allowed to other users by using the `GRANT` command. Use of functions for replication slots is restricted to superusers and users having `REPLICATION` privilege.

Many of these functions have equivalent commands in the replication protocol; see [???](#protocol-replication).

The functions described in [Backup Control Functions](#functions-admin-backup), [Recovery Control Functions](#functions-recovery-control), and [Snapshot Synchronization Functions](#functions-snapshot-synchronization) are also relevant for replication.

<table id="functions-replication-table">
<caption>Replication Management Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_create_physical_replication_slot</code> ( <code>slot_name</code> <code>name</code> [, <code>immediately_reserve</code> <code>boolean</code>, <code>temporary</code> <code>boolean</code>] ) record ( <code>slot_name</code> <code>name</code>, <code>lsn</code> <code>pg_lsn</code> )</p>
<p>Creates a new physical replication slot named <code>slot_name</code>. The optional second parameter, when <code>true</code>, specifies that the LSN for this replication slot be reserved immediately; otherwise the LSN is reserved on first connection from a streaming replication client. Streaming changes from a physical slot is only possible with the streaming-replication protocol see <a href="#protocol-replication">???</a>. The optional third parameter, <code>temporary</code>, when set to true, specifies that the slot should not be permanently stored to disk and is only meant for use by the current session. Temporary slots are also released upon any error. This function corresponds to the replication protocol command <code>CREATE_REPLICATION_SLOT ... PHYSICAL</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_drop_replication_slot</code> ( <code>slot_name</code> <code>name</code> ) void</p>
<p>Drops the physical or logical replication slot named <code>slot_name</code>. Same as replication protocol command <code>DROP_REPLICATION_SLOT</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_create_logical_replication_slot</code> ( <code>slot_name</code> <code>name</code>, <code>plugin</code> <code>name</code> [, <code>temporary</code> <code>boolean</code>, <code>twophase</code> <code>boolean</code>, <code>failover</code> <code>boolean</code>] ) record ( <code>slot_name</code> <code>name</code>, <code>lsn</code> <code>pg_lsn</code> )</p>
<p>Creates a new logical (decoding) replication slot named <code>slot_name</code> using the output plugin <code>plugin</code>. The optional third parameter, <code>temporary</code>, when set to true, specifies that the slot should not be permanently stored to disk and is only meant for use by the current session. Temporary slots are also released upon any error. The optional fourth parameter, <code>twophase</code>, when set to true, specifies that the decoding of prepared transactions is enabled for this slot. The optional fifth parameter, <code>failover</code>, when set to true, specifies that this slot is enabled to be synced to the standbys so that logical replication can be resumed after failover. A call to this function has the same effect as the replication protocol command <code>CREATE_REPLICATION_SLOT ... LOGICAL</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_copy_physical_replication_slot</code> ( <code>src_slot_name</code> <code>name</code>, <code>dst_slot_name</code> <code>name</code> [, <code>temporary</code> <code>boolean</code>] ) record ( <code>slot_name</code> <code>name</code>, <code>lsn</code> <code>pg_lsn</code> )</p>
<p>Copies an existing physical replication slot named <code>src_slot_name</code> to a physical replication slot named <code>dst_slot_name</code>. The copied physical slot starts to reserve WAL from the same LSN as the source slot. <code>temporary</code> is optional. If <code>temporary</code> is omitted, the same value as the source slot is used. Copy of an invalidated slot is not allowed.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_copy_logical_replication_slot</code> ( <code>src_slot_name</code> <code>name</code>, <code>dst_slot_name</code> <code>name</code> [, <code>temporary</code> <code>boolean</code> [, <code>plugin</code> <code>name</code>]] ) record ( <code>slot_name</code> <code>name</code>, <code>lsn</code> <code>pg_lsn</code> )</p>
<p>Copies an existing logical replication slot named <code>src_slot_name</code> to a logical replication slot named <code>dst_slot_name</code>, optionally changing the output plugin and persistence. The copied logical slot starts from the same LSN as the source logical slot. Both <code>temporary</code> and <code>plugin</code> are optional; if they are omitted, the values of the source slot are used. The <code>failover</code> option of the source logical slot is not copied and is set to <code>false</code> by default. This is to avoid the risk of being unable to continue logical replication after failover to standby where the slot is being synchronized. Copy of an invalidated slot is not allowed.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_logical_slot_get_changes</code> ( <code>slot_name</code> <code>name</code>, <code>upto_lsn</code> <code>pg_lsn</code>, <code>upto_nchanges</code> <code>integer</code>, <code>VARIADIC</code> <code>options</code> <code>text[]</code> ) setof record ( <code>lsn</code> <code>pg_lsn</code>, <code>xid</code> <code>xid</code>, <code>data</code> <code>text</code> )</p>
<p>Returns changes in the slot <code>slot_name</code>, starting from the point from which changes have been consumed last. If <code>upto_lsn</code> and <code>upto_nchanges</code> are NULL, logical decoding will continue until end of WAL. If <code>upto_lsn</code> is non-NULL, decoding will include only those transactions which commit prior to the specified LSN. If <code>upto_nchanges</code> is non-NULL, decoding will stop when the number of rows produced by decoding exceeds the specified value. Note, however, that the actual number of rows returned may be larger, since this limit is only checked after adding the rows produced when decoding each new transaction commit. If the specified slot is a logical failover slot then the function will not return until all physical slots specified in <a href="#guc-synchronized-standby-slots"><code>synchronized_standby_slots</code></a> have confirmed WAL receipt.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_logical_slot_peek_changes</code> ( <code>slot_name</code> <code>name</code>, <code>upto_lsn</code> <code>pg_lsn</code>, <code>upto_nchanges</code> <code>integer</code>, <code>VARIADIC</code> <code>options</code> <code>text[]</code> ) setof record ( <code>lsn</code> <code>pg_lsn</code>, <code>xid</code> <code>xid</code>, <code>data</code> <code>text</code> )</p>
<p>Behaves just like the <code>pg_logical_slot_get_changes()</code> function, except that changes are not consumed; that is, they will be returned again on future calls.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_logical_slot_get_binary_changes</code> ( <code>slot_name</code> <code>name</code>, <code>upto_lsn</code> <code>pg_lsn</code>, <code>upto_nchanges</code> <code>integer</code>, <code>VARIADIC</code> <code>options</code> <code>text[]</code> ) setof record ( <code>lsn</code> <code>pg_lsn</code>, <code>xid</code> <code>xid</code>, <code>data</code> <code>bytea</code> )</p>
<p>Behaves just like the <code>pg_logical_slot_get_changes()</code> function, except that changes are returned as <code>bytea</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_logical_slot_peek_binary_changes</code> ( <code>slot_name</code> <code>name</code>, <code>upto_lsn</code> <code>pg_lsn</code>, <code>upto_nchanges</code> <code>integer</code>, <code>VARIADIC</code> <code>options</code> <code>text[]</code> ) setof record ( <code>lsn</code> <code>pg_lsn</code>, <code>xid</code> <code>xid</code>, <code>data</code> <code>bytea</code> )</p>
<p>Behaves just like the <code>pg_logical_slot_peek_changes()</code> function, except that changes are returned as <code>bytea</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_replication_slot_advance</code> ( <code>slot_name</code> <code>name</code>, <code>upto_lsn</code> <code>pg_lsn</code> ) record ( <code>slot_name</code> <code>name</code>, <code>end_lsn</code> <code>pg_lsn</code> )</p>
<p>Advances the current confirmed position of a replication slot named <code>slot_name</code>. The slot will not be moved backwards, and it will not be moved beyond the current insert location. Returns the name of the slot and the actual position that it was advanced to. The updated slot position information is written out at the next checkpoint if any advancing is done. So in the event of a crash, the slot may return to an earlier position. If the specified slot is a logical failover slot then the function will not return until all physical slots specified in <a href="#guc-synchronized-standby-slots"><code>synchronized_standby_slots</code></a> have confirmed WAL receipt.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_replication_origin_create</code> ( <code>node_name</code> <code>text</code> ) oid</p>
<p>Creates a replication origin with the given external name, and returns the internal ID assigned to it.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_replication_origin_drop</code> ( <code>node_name</code> <code>text</code> ) void</p>
<p>Deletes a previously-created replication origin, including any associated replay progress.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_replication_origin_oid</code> ( <code>node_name</code> <code>text</code> ) oid</p>
<p>Looks up a replication origin by name and returns the internal ID. If no such replication origin is found, <code>NULL</code> is returned.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_replication_origin_session_setup</code> ( <code>node_name</code> <code>text</code> ) void</p>
<p>Marks the current session as replaying from the given origin, allowing replay progress to be tracked. Can only be used if no origin is currently selected. Use <code>pg_replication_origin_session_reset</code> to undo.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_replication_origin_session_reset</code> () void</p>
<p>Cancels the effects of <code>pg_replication_origin_session_setup()</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_replication_origin_session_is_setup</code> () boolean</p>
<p>Returns true if a replication origin has been selected in the current session.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_replication_origin_session_progress</code> ( <code>flush</code> <code>boolean</code> ) pg_lsn</p>
<p>Returns the replay location for the replication origin selected in the current session. The parameter <code>flush</code> determines whether the corresponding local transaction will be guaranteed to have been flushed to disk or not.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_replication_origin_xact_setup</code> ( <code>origin_lsn</code> <code>pg_lsn</code>, <code>origin_timestamp</code> <code>timestamp with time zone</code> ) void</p>
<p>Marks the current transaction as replaying a transaction that has committed at the given LSN and timestamp. Can only be called when a replication origin has been selected using <code>pg_replication_origin_session_setup</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_replication_origin_xact_reset</code> () void</p>
<p>Cancels the effects of <code>pg_replication_origin_xact_setup()</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_replication_origin_advance</code> ( <code>node_name</code> <code>text</code>, <code>lsn</code> <code>pg_lsn</code> ) void</p>
<p>Sets replication progress for the given node to the given location. This is primarily useful for setting up the initial location, or setting a new location after configuration changes and similar. Be aware that careless use of this function can lead to inconsistently replicated data.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_replication_origin_progress</code> ( <code>node_name</code> <code>text</code>, <code>flush</code> <code>boolean</code> ) pg_lsn</p>
<p>Returns the replay location for the given replication origin. The parameter <code>flush</code> determines whether the corresponding local transaction will be guaranteed to have been flushed to disk or not.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_logical_emit_message</code> ( <code>transactional</code> <code>boolean</code>, <code>prefix</code> <code>text</code>, <code>content</code> <code>text</code> [, <code>flush</code> <code>boolean</code> <code>DEFAULT</code> <code>false</code>] ) pg_lsn</p>
<p role="func_signature"><code>pg_logical_emit_message</code> ( <code>transactional</code> <code>boolean</code>, <code>prefix</code> <code>text</code>, <code>content</code> <code>bytea</code> [, <code>flush</code> <code>boolean</code> <code>DEFAULT</code> <code>false</code>] ) pg_lsn</p>
<p>Emits a logical decoding message. This can be used to pass generic messages to logical decoding plugins through WAL. The <code>transactional</code> parameter specifies if the message should be part of the current transaction, or if it should be written immediately and decoded as soon as the logical decoder reads the record. The <code>prefix</code> parameter is a textual prefix that can be used by logical decoding plugins to easily recognize messages that are interesting for them. The <code>content</code> parameter is the content of the message, given either in text or binary form. The <code>flush</code> parameter (default set to <code>false</code>) controls if the message is immediately flushed to WAL or not. <code>flush</code> has no effect with <code>transactional</code>, as the message's WAL record is flushed along with its transaction.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_sync_replication_slots</code> () void</p>
<p>Synchronize the logical failover replication slots from the primary server to the standby server. This function can only be executed on the standby server. Temporary synced slots, if any, cannot be used for logical decoding and must be dropped after promotion. See <a href="#logicaldecoding-replication-slots-synchronization">???</a> for details. Note that this function is primarily intended for testing and debugging purposes and should be used with caution. Additionally, this function cannot be executed if <a href="#guc-sync-replication-slots"><code>sync_replication_slots</code></a> is enabled and the slotsync worker is already running to perform the synchronization of slots.</p>

&#10;</div>
<p>If, after executing the function, <a href="#guc-hot-standby-feedback"> <code>hot_standby_feedback</code></a> is disabled on the standby or the physical slot configured in <a href="#guc-primary-slot-name"> <code>primary_slot_name</code></a> is removed, then it is possible that the necessary rows of the synchronized slot will be removed by the VACUUM process on the primary server, resulting in the synchronized slot becoming invalidated.</p>
</div></td>
</tr>
</tbody>
</table>

### Database Object Management Functions

The functions shown in [Database Object Size Functions](#functions-admin-dbsize) calculate the disk space usage of database objects, or assist in presentation or understanding of usage results. `bigint` results are measured in bytes. If an OID that does not represent an existing object is passed to one of these functions, `NULL` is returned.

<table id="functions-admin-dbsize">
<caption>Database Object Size Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_column_size</code> ( <code>"any"</code> ) integer</p>
<p>Shows the number of bytes used to store any individual data value. If applied directly to a table column value, this reflects any compression that was done.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_column_compression</code> ( <code>"any"</code> ) text</p>
<p>Shows the compression algorithm that was used to compress an individual variable-length value. Returns <code>NULL</code> if the value is not compressed.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_column_toast_chunk_id</code> ( <code>"any"</code> ) oid</p>
<p>Shows the chunk_id of an on-disk TOASTed value. Returns <code>NULL</code> if the value is un-TOASTed or not on-disk. See <a href="#storage-toast">???</a> for more information about TOAST.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_database_size</code> ( <code>name</code> ) bigint</p>
<p role="func_signature"><code>pg_database_size</code> ( <code>oid</code> ) bigint</p>
<p>Computes the total disk space used by the database with the specified name or OID. To use this function, you must have <code>CONNECT</code> privilege on the specified database (which is granted by default) or have privileges of the <code>pg_read_all_stats</code> role.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_indexes_size</code> ( <code>regclass</code> ) bigint</p>
<p>Computes the total disk space used by indexes attached to the specified table.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_relation_size</code> ( <code>relation</code> <code>regclass</code> [, <code>fork</code> <code>text</code>] ) bigint</p>
<p>Computes the disk space used by one “fork” of the specified relation. (Note that for most purposes it is more convenient to use the higher-level functions <code>pg_total_relation_size</code> or <code>pg_table_size</code>, which sum the sizes of all forks.) With one argument, this returns the size of the main data fork of the relation. The second argument can be provided to specify which fork to examine:</p>
<ul>
<li><code>main</code> returns the size of the main data fork of the relation.</li>
<li><code>fsm</code> returns the size of the Free Space Map (see <a href="#storage-fsm">???</a>) associated with the relation.</li>
<li><code>vm</code> returns the size of the Visibility Map (see <a href="#storage-vm">???</a>) associated with the relation.</li>
<li><code>init</code> returns the size of the initialization fork, if any, associated with the relation.</li>
</ul></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_size_bytes</code> ( <code>text</code> ) bigint</p>
<p>Converts a size in human-readable format (as returned by <code>pg_size_pretty</code>) into bytes. Valid units are <code>bytes</code>, <code>B</code>, <code>kB</code>, <code>MB</code>, <code>GB</code>, <code>TB</code>, and <code>PB</code>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_size_pretty</code> ( <code>bigint</code> ) text</p>
<p role="func_signature"><code>pg_size_pretty</code> ( <code>numeric</code> ) text</p>
<p>Converts a size in bytes into a more easily human-readable format with size units (bytes, kB, MB, GB, TB, or PB as appropriate). Note that the units are powers of 2 rather than powers of 10, so 1kB is 1024 bytes, 1MB is 1024<sup>2</sup> = 1048576 bytes, and so on.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_table_size</code> ( <code>regclass</code> ) bigint</p>
<p>Computes the disk space used by the specified table, excluding indexes (but including its TOAST table if any, free space map, and visibility map).</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_tablespace_size</code> ( <code>name</code> ) bigint</p>
<p role="func_signature"><code>pg_tablespace_size</code> ( <code>oid</code> ) bigint</p>
<p>Computes the total disk space used in the tablespace with the specified name or OID. To use this function, you must have <code>CREATE</code> privilege on the specified tablespace or have privileges of the <code>pg_read_all_stats</code> role, unless it is the default tablespace for the current database.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_total_relation_size</code> ( <code>regclass</code> ) bigint</p>
<p>Computes the total disk space used by the specified table, including all indexes and TOAST data. The result is equivalent to <code>pg_table_size</code> <code>+</code> <code>pg_indexes_size</code>.</p></td>
</tr>
</tbody>
</table>

The functions above that operate on tables or indexes accept a `regclass` argument, which is simply the OID of the table or index in the pg_class system catalog. You do not have to look up the OID by hand, however, since the `regclass` data type's input converter will do the work for you. See [???](#datatype-oid) for details.

The functions shown in [Database Object Location Functions](#functions-admin-dblocation) assist in identifying the specific disk files associated with database objects.

<table id="functions-admin-dblocation">
<caption>Database Object Location Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_relation_filenode</code> ( <code>relation</code> <code>regclass</code> ) oid</p>
<p>Returns the “filenode” number currently assigned to the specified relation. The filenode is the base component of the file name(s) used for the relation (see <a href="#storage-file-layout">???</a> for more information). For most relations the result is the same as pg_class.relfilenode, but for certain system catalogs relfilenode is zero and this function must be used to get the correct value. The function returns NULL if passed a relation that does not have storage, such as a view.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_relation_filepath</code> ( <code>relation</code> <code>regclass</code> ) text</p>
<p>Returns the entire file path name (relative to the database cluster's data directory, <code>PGDATA</code>) of the relation.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_filenode_relation</code> ( <code>tablespace</code> <code>oid</code>, <code>filenode</code> <code>oid</code> ) regclass</p>
<p>Returns a relation's OID given the tablespace OID and filenode it is stored under. This is essentially the inverse mapping of <code>pg_relation_filepath</code>. For a relation in the database's default tablespace, the tablespace can be specified as zero. Returns <code>NULL</code> if no relation in the current database is associated with the given values, or if dealing with a temporary relation.</p></td>
</tr>
</tbody>
</table>

[Collation Management Functions](#functions-admin-collation) lists functions used to manage collations.

<table id="functions-admin-collation">
<caption>Collation Management Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_collation_actual_version</code> ( <code>oid</code> ) text</p>
<p>Returns the actual version of the collation object as it is currently installed in the operating system. If this is different from the value in pg_collation.collversion, then objects depending on the collation might need to be rebuilt. See also <a href="#sql-altercollation">???</a>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_database_collation_actual_version</code> ( <code>oid</code> ) text</p>
<p>Returns the actual version of the database's collation as it is currently installed in the operating system. If this is different from the value in pg_database.datcollversion, then objects depending on the collation might need to be rebuilt. See also <a href="#sql-alterdatabase">???</a>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_import_system_collations</code> ( <code>schema</code> <code>regnamespace</code> ) integer</p>
<p>Adds collations to the system catalog pg_collation based on all the locales it finds in the operating system. This is what <code>initdb</code> uses; see <a href="#collation-managing">???</a> for more details. If additional locales are installed into the operating system later on, this function can be run again to add collations for the new locales. Locales that match existing entries in pg_collation will be skipped. (But collation objects based on locales that are no longer present in the operating system are not removed by this function.) The <code>schema</code> parameter would typically be <code>pg_catalog</code>, but that is not a requirement; the collations could be installed into some other schema as well. The function returns the number of new collation objects it created. Use of this function is restricted to superusers.</p></td>
</tr>
</tbody>
</table>

[Partitioning Information Functions](#functions-info-partition) lists functions that provide information about the structure of partitioned tables.

<table id="functions-info-partition">
<caption>Partitioning Information Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_partition_tree</code> ( <code>regclass</code> ) setof record ( <code>relid</code> <code>regclass</code>, <code>parentrelid</code> <code>regclass</code>, <code>isleaf</code> <code>boolean</code>, <code>level</code> <code>integer</code> )</p>
<p>Lists the tables or indexes in the partition tree of the given partitioned table or partitioned index, with one row for each partition. Information provided includes the OID of the partition, the OID of its immediate parent, a boolean value telling if the partition is a leaf, and an integer telling its level in the hierarchy. The level value is 0 for the input table or index, 1 for its immediate child partitions, 2 for their partitions, and so on. Returns no rows if the relation does not exist or is not a partition or partitioned table.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_partition_ancestors</code> ( <code>regclass</code> ) setof regclass</p>
<p>Lists the ancestor relations of the given partition, including the relation itself. Returns no rows if the relation does not exist or is not a partition or partitioned table.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_partition_root</code> ( <code>regclass</code> ) regclass</p>
<p>Returns the top-most parent of the partition tree to which the given relation belongs. Returns <code>NULL</code> if the relation does not exist or is not a partition or partitioned table.</p></td>
</tr>
</tbody>
</table>

For example, to check the total size of the data contained in a partitioned table measurement, one could use the following query:

    SELECT pg_size_pretty(sum(pg_relation_size(relid))) AS total_size
      FROM pg_partition_tree('measurement');

### Index Maintenance Functions

[Index Maintenance Functions](#functions-admin-index-table) shows the functions available for index maintenance tasks. (Note that these maintenance tasks are normally done automatically by autovacuum; use of these functions is only required in special cases.) These functions cannot be executed during recovery. Use of these functions is restricted to superusers and the owner of the given index.

<table id="functions-admin-index-table">
<caption>Index Maintenance Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>brin_summarize_new_values</code> ( <code>index</code> <code>regclass</code> ) integer</p>
<p>Scans the specified BRIN index to find page ranges in the base table that are not currently summarized by the index; for any such range it creates a new summary index tuple by scanning those table pages. Returns the number of new page range summaries that were inserted into the index.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>brin_summarize_range</code> ( <code>index</code> <code>regclass</code>, <code>blockNumber</code> <code>bigint</code> ) integer</p>
<p>Summarizes the page range covering the given block, if not already summarized. This is like <code>brin_summarize_new_values</code> except that it only processes the page range that covers the given table block number.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>brin_desummarize_range</code> ( <code>index</code> <code>regclass</code>, <code>blockNumber</code> <code>bigint</code> ) void</p>
<p>Removes the BRIN index tuple that summarizes the page range covering the given table block, if there is one.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>gin_clean_pending_list</code> ( <code>index</code> <code>regclass</code> ) bigint</p>
<p>Cleans up the “pending” list of the specified GIN index by moving entries in it, in bulk, to the main GIN data structure. Returns the number of pages removed from the pending list. If the argument is a GIN index built with the <code>fastupdate</code> option disabled, no cleanup happens and the result is zero, because the index doesn't have a pending list. See <a href="#gin-fast-update">???</a> and <a href="#gin-tips">???</a> for details about the pending list and <code>fastupdate</code> option.</p></td>
</tr>
</tbody>
</table>

### Generic File Access Functions

The functions shown in [Generic File Access Functions](#functions-admin-genfile-table) provide native access to files on the machine hosting the server. Only files within the database cluster directory and the `log_directory` can be accessed, unless the user is a superuser or is granted the role `pg_read_server_files`. Use a relative path for files in the cluster directory, and a path matching the `log_directory` configuration setting for log files.

Note that granting users the EXECUTE privilege on `pg_read_file()`, or related functions, allows them the ability to read any file on the server that the database server process can read; these functions bypass all in-database privilege checks. This means that, for example, a user with such access is able to read the contents of the pg_authid table where authentication information is stored, as well as read any table data in the database. Therefore, granting access to these functions should be carefully considered.

When granting privilege on these functions, note that the table entries showing optional parameters are mostly implemented as several physical functions with different parameter lists. Privilege must be granted separately on each such function, if it is to be used. psql's `\df` command can be useful to check what the actual function signatures are.

Some of these functions take an optional `missing_ok` parameter, which specifies the behavior when the file or directory does not exist. If `true`, the function returns `NULL` or an empty result set, as appropriate. If `false`, an error is raised. (Failure conditions other than “file not found” are reported as errors in any case.) The default is `false`.

<table id="functions-admin-genfile-table">
<caption>Generic File Access Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_ls_dir</code> ( <code>dirname</code> <code>text</code> [, <code>missing_ok</code> <code>boolean</code>, <code>include_dot_dirs</code> <code>boolean</code>] ) setof text</p>
<p>Returns the names of all files (and directories and other special files) in the specified directory. The <code>include_dot_dirs</code> parameter indicates whether “.” and “..” are to be included in the result set; the default is to exclude them. Including them can be useful when <code>missing_ok</code> is <code>true</code>, to distinguish an empty directory from a non-existent directory.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_ls_logdir</code> () setof record ( <code>name</code> <code>text</code>, <code>size</code> <code>bigint</code>, <code>modification</code> <code>timestamp with time zone</code> )</p>
<p>Returns the name, size, and last modification time (mtime) of each ordinary file in the server's log directory. Filenames beginning with a dot, directories, and other special files are excluded.</p>
<p>This function is restricted to superusers and roles with privileges of the <code>pg_monitor</code> role by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_ls_waldir</code> () setof record ( <code>name</code> <code>text</code>, <code>size</code> <code>bigint</code>, <code>modification</code> <code>timestamp with time zone</code> )</p>
<p>Returns the name, size, and last modification time (mtime) of each ordinary file in the server's write-ahead log (WAL) directory. Filenames beginning with a dot, directories, and other special files are excluded.</p>
<p>This function is restricted to superusers and roles with privileges of the <code>pg_monitor</code> role by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_ls_logicalmapdir</code> () setof record ( <code>name</code> <code>text</code>, <code>size</code> <code>bigint</code>, <code>modification</code> <code>timestamp with time zone</code> )</p>
<p>Returns the name, size, and last modification time (mtime) of each ordinary file in the server's <code>pg_logical/mappings</code> directory. Filenames beginning with a dot, directories, and other special files are excluded.</p>
<p>This function is restricted to superusers and members of the <code>pg_monitor</code> role by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_ls_logicalsnapdir</code> () setof record ( <code>name</code> <code>text</code>, <code>size</code> <code>bigint</code>, <code>modification</code> <code>timestamp with time zone</code> )</p>
<p>Returns the name, size, and last modification time (mtime) of each ordinary file in the server's <code>pg_logical/snapshots</code> directory. Filenames beginning with a dot, directories, and other special files are excluded.</p>
<p>This function is restricted to superusers and members of the <code>pg_monitor</code> role by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_ls_replslotdir</code> ( <code>slot_name</code> <code>text</code> ) setof record ( <code>name</code> <code>text</code>, <code>size</code> <code>bigint</code>, <code>modification</code> <code>timestamp with time zone</code> )</p>
<p>Returns the name, size, and last modification time (mtime) of each ordinary file in the server's <code>pg_replslot/slot_name</code> directory, where <code>slot_name</code> is the name of the replication slot provided as input of the function. Filenames beginning with a dot, directories, and other special files are excluded.</p>
<p>This function is restricted to superusers and members of the <code>pg_monitor</code> role by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_ls_archive_statusdir</code> () setof record ( <code>name</code> <code>text</code>, <code>size</code> <code>bigint</code>, <code>modification</code> <code>timestamp with time zone</code> )</p>
<p>Returns the name, size, and last modification time (mtime) of each ordinary file in the server's WAL archive status directory (<code>pg_wal/archive_status</code>). Filenames beginning with a dot, directories, and other special files are excluded.</p>
<p>This function is restricted to superusers and members of the <code>pg_monitor</code> role by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_ls_tmpdir</code> ( [<code>tablespace</code> <code>oid</code>] ) setof record ( <code>name</code> <code>text</code>, <code>size</code> <code>bigint</code>, <code>modification</code> <code>timestamp with time zone</code> )</p>
<p>Returns the name, size, and last modification time (mtime) of each ordinary file in the temporary file directory for the specified <code>tablespace</code>. If <code>tablespace</code> is not provided, the <code>pg_default</code> tablespace is examined. Filenames beginning with a dot, directories, and other special files are excluded.</p>
<p>This function is restricted to superusers and members of the <code>pg_monitor</code> role by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_read_file</code> ( <code>filename</code> <code>text</code> [, <code>offset</code> <code>bigint</code>, <code>length</code> <code>bigint</code>] [, <code>missing_ok</code> <code>boolean</code>] ) text</p>
<p>Returns all or part of a text file, starting at the given byte <code>offset</code>, returning at most <code>length</code> bytes (less if the end of file is reached first). If <code>offset</code> is negative, it is relative to the end of the file. If <code>offset</code> and <code>length</code> are omitted, the entire file is returned. The bytes read from the file are interpreted as a string in the database's encoding; an error is thrown if they are not valid in that encoding.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_read_binary_file</code> ( <code>filename</code> <code>text</code> [, <code>offset</code> <code>bigint</code>, <code>length</code> <code>bigint</code>] [, <code>missing_ok</code> <code>boolean</code>] ) bytea</p>
<p>Returns all or part of a file. This function is identical to <code>pg_read_file</code> except that it can read arbitrary binary data, returning the result as <code>bytea</code> not <code>text</code>; accordingly, no encoding checks are performed.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p>
<p>In combination with the <code>convert_from</code> function, this function can be used to read a text file in a specified encoding and convert to the database's encoding:</p>
<pre><code>SELECT convert_from(pg_read_binary_file(&#39;file_in_utf8.txt&#39;), &#39;UTF8&#39;);</code></pre></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_file</code> ( <code>filename</code> <code>text</code> [, <code>missing_ok</code> <code>boolean</code>] ) record ( <code>size</code> <code>bigint</code>, <code>access</code> <code>timestamp with time zone</code>, <code>modification</code> <code>timestamp with time zone</code>, <code>change</code> <code>timestamp with time zone</code>, <code>creation</code> <code>timestamp with time zone</code>, <code>isdir</code> <code>boolean</code> )</p>
<p>Returns a record containing the file's size, last access time stamp, last modification time stamp, last file status change time stamp (Unix platforms only), file creation time stamp (Windows only), and a flag indicating if it is a directory.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
</tbody>
</table>

### Advisory Lock Functions

The functions shown in [Advisory Lock Functions](#functions-advisory-locks-table) manage advisory locks. For details about proper use of these functions, see [???](#advisory-locks).

All these functions are intended to be used to lock application-defined resources, which can be identified either by a single 64-bit key value or two 32-bit key values (note that these two key spaces do not overlap). If another session already holds a conflicting lock on the same resource identifier, the functions will either wait until the resource becomes available, or return a `false` result, as appropriate for the function. Locks can be either shared or exclusive: a shared lock does not conflict with other shared locks on the same resource, only with exclusive locks. Locks can be taken at session level (so that they are held until released or the session ends) or at transaction level (so that they are held until the current transaction ends; there is no provision for manual release). Multiple session-level lock requests stack, so that if the same resource identifier is locked three times there must then be three unlock requests to release the resource in advance of session end.

<table id="functions-advisory-locks-table">
<caption>Advisory Lock Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_advisory_lock</code> ( <code>key</code> <code>bigint</code> ) void</p>
<p role="func_signature"><code>pg_advisory_lock</code> ( <code>key1</code> <code>integer</code>, <code>key2</code> <code>integer</code> ) void</p>
<p>Obtains an exclusive session-level advisory lock, waiting if necessary.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_advisory_lock_shared</code> ( <code>key</code> <code>bigint</code> ) void</p>
<p role="func_signature"><code>pg_advisory_lock_shared</code> ( <code>key1</code> <code>integer</code>, <code>key2</code> <code>integer</code> ) void</p>
<p>Obtains a shared session-level advisory lock, waiting if necessary.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_advisory_unlock</code> ( <code>key</code> <code>bigint</code> ) boolean</p>
<p role="func_signature"><code>pg_advisory_unlock</code> ( <code>key1</code> <code>integer</code>, <code>key2</code> <code>integer</code> ) boolean</p>
<p>Releases a previously-acquired exclusive session-level advisory lock. Returns <code>true</code> if the lock is successfully released. If the lock was not held, <code>false</code> is returned, and in addition, an SQL warning will be reported by the server.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_advisory_unlock_all</code> () void</p>
<p>Releases all session-level advisory locks held by the current session. (This function is implicitly invoked at session end, even if the client disconnects ungracefully.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_advisory_unlock_shared</code> ( <code>key</code> <code>bigint</code> ) boolean</p>
<p role="func_signature"><code>pg_advisory_unlock_shared</code> ( <code>key1</code> <code>integer</code>, <code>key2</code> <code>integer</code> ) boolean</p>
<p>Releases a previously-acquired shared session-level advisory lock. Returns <code>true</code> if the lock is successfully released. If the lock was not held, <code>false</code> is returned, and in addition, an SQL warning will be reported by the server.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_advisory_xact_lock</code> ( <code>key</code> <code>bigint</code> ) void</p>
<p role="func_signature"><code>pg_advisory_xact_lock</code> ( <code>key1</code> <code>integer</code>, <code>key2</code> <code>integer</code> ) void</p>
<p>Obtains an exclusive transaction-level advisory lock, waiting if necessary.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_advisory_xact_lock_shared</code> ( <code>key</code> <code>bigint</code> ) void</p>
<p role="func_signature"><code>pg_advisory_xact_lock_shared</code> ( <code>key1</code> <code>integer</code>, <code>key2</code> <code>integer</code> ) void</p>
<p>Obtains a shared transaction-level advisory lock, waiting if necessary.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_try_advisory_lock</code> ( <code>key</code> <code>bigint</code> ) boolean</p>
<p role="func_signature"><code>pg_try_advisory_lock</code> ( <code>key1</code> <code>integer</code>, <code>key2</code> <code>integer</code> ) boolean</p>
<p>Obtains an exclusive session-level advisory lock if available. This will either obtain the lock immediately and return <code>true</code>, or return <code>false</code> without waiting if the lock cannot be acquired immediately.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_try_advisory_lock_shared</code> ( <code>key</code> <code>bigint</code> ) boolean</p>
<p role="func_signature"><code>pg_try_advisory_lock_shared</code> ( <code>key1</code> <code>integer</code>, <code>key2</code> <code>integer</code> ) boolean</p>
<p>Obtains a shared session-level advisory lock if available. This will either obtain the lock immediately and return <code>true</code>, or return <code>false</code> without waiting if the lock cannot be acquired immediately.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_try_advisory_xact_lock</code> ( <code>key</code> <code>bigint</code> ) boolean</p>
<p role="func_signature"><code>pg_try_advisory_xact_lock</code> ( <code>key1</code> <code>integer</code>, <code>key2</code> <code>integer</code> ) boolean</p>
<p>Obtains an exclusive transaction-level advisory lock if available. This will either obtain the lock immediately and return <code>true</code>, or return <code>false</code> without waiting if the lock cannot be acquired immediately.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_try_advisory_xact_lock_shared</code> ( <code>key</code> <code>bigint</code> ) boolean</p>
<p role="func_signature"><code>pg_try_advisory_xact_lock_shared</code> ( <code>key1</code> <code>integer</code>, <code>key2</code> <code>integer</code> ) boolean</p>
<p>Obtains a shared transaction-level advisory lock if available. This will either obtain the lock immediately and return <code>true</code>, or return <code>false</code> without waiting if the lock cannot be acquired immediately.</p></td>
</tr>
</tbody>
</table>

## Trigger Functions

While many uses of triggers involve user-written trigger functions, PostgreSQL provides a few built-in trigger functions that can be used directly in user-defined triggers. These are summarized in [Built-In Trigger Functions](#builtin-triggers-table). (Additional built-in trigger functions exist, which implement foreign key constraints and deferred index constraints. Those are not documented here since users need not use them directly.)

For more information about creating triggers, see [???](#sql-createtrigger).

<table id="builtin-triggers-table">
<caption>Built-In Trigger Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example Usage</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>suppress_redundant_updates_trigger</code> ( ) trigger</p>
<p>Suppresses do-nothing update operations. See below for details.</p>
<p><code>CREATE TRIGGER ... suppress_redundant_updates_trigger()</code></p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>tsvector_update_trigger</code> ( ) trigger</p>
<p>Automatically updates a <code>tsvector</code> column from associated plain-text document column(s). The text search configuration to use is specified by name as a trigger argument. See <a href="#textsearch-update-triggers">???</a> for details.</p>
<p><code>CREATE TRIGGER ... tsvector_update_trigger(tsvcol, 'pg_catalog.swedish', title, body)</code></p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>tsvector_update_trigger_column</code> ( ) trigger</p>
<p>Automatically updates a <code>tsvector</code> column from associated plain-text document column(s). The text search configuration to use is taken from a <code>regconfig</code> column of the table. See <a href="#textsearch-update-triggers">???</a> for details.</p>
<p><code>CREATE TRIGGER ... tsvector_update_trigger_column(tsvcol, tsconfigcol, title, body)</code></p></td>
</tr>
</tbody>
</table>

The `suppress_redundant_updates_trigger` function, when applied as a row-level `BEFORE UPDATE` trigger, will prevent any update that does not actually change the data in the row from taking place. This overrides the normal behavior which always performs a physical row update regardless of whether or not the data has changed. (This normal behavior makes updates run faster, since no checking is required, and is also useful in certain cases.)

Ideally, you should avoid running updates that don't actually change the data in the record. Redundant updates can cost considerable unnecessary time, especially if there are lots of indexes to alter, and space in dead rows that will eventually have to be vacuumed. However, detecting such situations in client code is not always easy, or even possible, and writing expressions to detect them can be error-prone. An alternative is to use `suppress_redundant_updates_trigger`, which will skip updates that don't change the data. You should use this with care, however. The trigger takes a small but non-trivial time for each record, so if most of the records affected by updates do actually change, use of this trigger will make updates run slower on average.

The `suppress_redundant_updates_trigger` function can be added to a table like this:

    CREATE TRIGGER z_min_update
    BEFORE UPDATE ON tablename
    FOR EACH ROW EXECUTE FUNCTION suppress_redundant_updates_trigger();

In most cases, you need to fire this trigger last for each row, so that it does not override other triggers that might wish to alter the row. Bearing in mind that triggers fire in name order, you would therefore choose a trigger name that comes after the name of any other trigger you might have on the table. (Hence the “z” prefix in the example.)

## Event Trigger Functions

PostgreSQL provides these helper functions to retrieve information from event triggers.

For more information about event triggers, see [???](#event-triggers).

### Capturing Changes at Command End

pg_event_trigger_ddl_commands

pg_event_trigger_ddl_commands

()

setof record

`pg_event_trigger_ddl_commands` returns a list of DDL commands executed by each user action, when invoked in a function attached to a `ddl_command_end` event trigger. If called in any other context, an error is raised. `pg_event_trigger_ddl_commands` returns one row for each base command executed; some commands that are a single SQL sentence may return more than one row. This function returns the following columns:

| Name | Type | Description |
|----|----|----|
| `classid` | `oid` | OID of catalog the object belongs in |
| `objid` | `oid` | OID of the object itself |
| `objsubid` | `integer` | Sub-object ID (e.g., attribute number for a column) |
| `command_tag` | `text` | Command tag |
| `object_type` | `text` | Type of the object |
| `schema_name` | `text` | Name of the schema the object belongs in, if any; otherwise `NULL`. No quoting is applied. |
| `object_identity` | `text` | Text rendering of the object identity, schema-qualified. Each identifier included in the identity is quoted if necessary. |
| `in_extension` | `boolean` | True if the command is part of an extension script |
| `command` | `pg_ddl_command` | A complete representation of the command, in internal format. This cannot be output directly, but it can be passed to other functions to obtain different pieces of information about the command. |

### Processing Objects Dropped by a DDL Command

pg_event_trigger_dropped_objects

pg_event_trigger_dropped_objects

()

setof record

`pg_event_trigger_dropped_objects` returns a list of all objects dropped by the command in whose `sql_drop` event it is called. If called in any other context, an error is raised. This function returns the following columns:

| Name | Type | Description |
|----|----|----|
| `classid` | `oid` | OID of catalog the object belonged in |
| `objid` | `oid` | OID of the object itself |
| `objsubid` | `integer` | Sub-object ID (e.g., attribute number for a column) |
| `original` | `boolean` | True if this was one of the root object(s) of the deletion |
| `normal` | `boolean` | True if there was a normal dependency relationship in the dependency graph leading to this object |
| `is_temporary` | `boolean` | True if this was a temporary object |
| `object_type` | `text` | Type of the object |
| `schema_name` | `text` | Name of the schema the object belonged in, if any; otherwise `NULL`. No quoting is applied. |
| `object_name` | `text` | Name of the object, if the combination of schema and name can be used as a unique identifier for the object; otherwise `NULL`. No quoting is applied, and name is never schema-qualified. |
| `object_identity` | `text` | Text rendering of the object identity, schema-qualified. Each identifier included in the identity is quoted if necessary. |
| `address_names` | `text[]` | An array that, together with `object_type` and `address_args`, can be used by the `pg_get_object_address` function to recreate the object address in a remote server containing an identically named object of the same kind. |
| `address_args` | `text[]` | Complement for `address_names` |

The `pg_event_trigger_dropped_objects` function can be used in an event trigger like this:

    CREATE FUNCTION test_event_trigger_for_drops()
            RETURNS event_trigger LANGUAGE plpgsql AS $$
    DECLARE
        obj record;
    BEGIN
        FOR obj IN SELECT * FROM pg_event_trigger_dropped_objects()
        LOOP
            RAISE NOTICE '% dropped object: % %.% %',
                         tg_tag,
                         obj.object_type,
                         obj.schema_name,
                         obj.object_name,
                         obj.object_identity;
        END LOOP;
    END;
    $$;
    CREATE EVENT TRIGGER test_event_trigger_for_drops
       ON sql_drop
       EXECUTE FUNCTION test_event_trigger_for_drops();

### Handling a Table Rewrite Event

The functions shown in [Table Rewrite Information Functions](#functions-event-trigger-table-rewrite) provide information about a table for which a `table_rewrite` event has just been called. If called in any other context, an error is raised.

<table id="functions-event-trigger-table-rewrite">
<caption>Table Rewrite Information Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_event_trigger_table_rewrite_oid</code> () oid</p>
<p>Returns the OID of the table about to be rewritten.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_event_trigger_table_rewrite_reason</code> () integer</p>
<p>Returns a code explaining the reason(s) for rewriting. The value is a bitmap built from the following values: <code>1</code> (the table has changed its persistence), <code>2</code> (default value of a column has changed), <code>4</code> (a column has a new data type) and <code>8</code> (the table access method has changed).</p></td>
</tr>
</tbody>
</table>

These functions can be used in an event trigger like this:

    CREATE FUNCTION test_event_trigger_table_rewrite_oid()
     RETURNS event_trigger
     LANGUAGE plpgsql AS
    $$
    BEGIN
      RAISE NOTICE 'rewriting table % for reason %',
                    pg_event_trigger_table_rewrite_oid()::regclass,
                    pg_event_trigger_table_rewrite_reason();
    END;
    $$;

    CREATE EVENT TRIGGER test_table_rewrite_oid
                      ON table_rewrite
       EXECUTE FUNCTION test_event_trigger_table_rewrite_oid();

## Statistics Information Functions

function

statistics

PostgreSQL provides a function to inspect complex statistics defined using the `CREATE STATISTICS` command.

### Inspecting MCV Lists

pg_mcv_list_items

pg_mcv_list_items

(

pg_mcv_list

)

setof record

`pg_mcv_list_items` returns a set of records describing all items stored in a multi-column MCV list. It returns the following columns:

| Name             | Type               | Description                       |
|------------------|--------------------|-----------------------------------|
| `index`          | `integer`          | index of the item in the MCV list |
| `values`         | `text[]`           | values stored in the MCV item     |
| `nulls`          | `boolean[]`        | flags identifying `NULL` values   |
| `frequency`      | `double precision` | frequency of this MCV item        |
| `base_frequency` | `double precision` | base frequency of this MCV item   |

The `pg_mcv_list_items` function can be used like this:

    SELECT m.* FROM pg_statistic_ext join pg_statistic_ext_data on (oid = stxoid),
                    pg_mcv_list_items(stxdmcv) m WHERE stxname = 'stts';

Values of the `pg_mcv_list` type can be obtained only from the pg_statistic_ext_data.stxdmcv column.

[^1]: A result containing more than one element node at the top level, or non-whitespace text outside of an element, is an example of content form. An XPath result can be of neither form, for example if it returns an attribute node selected from the element that contains it. Such a result will be put into content form with each such disallowed node replaced by its string value, as defined for the XPath 1.0 `string` function.
