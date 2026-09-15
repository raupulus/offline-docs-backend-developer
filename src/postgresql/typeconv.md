---
title: Type Conversion
source_url: https://www.postgresql.org/docs/17/typeconv.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: typeconv.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 3700
---

## Type Conversion

data type

conversion

SQL statements can, intentionally or not, require the mixing of different data types in the same expression. PostgreSQL has extensive facilities for evaluating mixed-type expressions.

In many cases a user does not need to understand the details of the type conversion mechanism. However, implicit conversions done by PostgreSQL can affect the results of a query. When necessary, these results can be tailored by using *explicit* type conversion.

This chapter introduces the PostgreSQL type conversion mechanisms and conventions. Refer to the relevant sections in [???](#datatype) and [???](#functions) for more information on specific data types and allowed functions and operators.

## Overview

SQL is a strongly typed language. That is, every data item has an associated data type which determines its behavior and allowed usage. PostgreSQL has an extensible type system that is more general and flexible than other SQL implementations. Hence, most type conversion behavior in PostgreSQL is governed by general rules rather than by ad hoc heuristics. This allows the use of mixed-type expressions even with user-defined types.

The PostgreSQL scanner/parser divides lexical elements into five fundamental categories: integers, non-integer numbers, strings, identifiers, and key words. Constants of most non-numeric types are first classified as strings. The SQL language definition allows specifying type names with strings, and this mechanism can be used in PostgreSQL to start the parser down the correct path. For example, the query:

    SELECT text 'Origin' AS "label", point '(0,0)' AS "value";

     label  | value
    --------+-------
     Origin | (0,0)
    (1 row)

has two literal constants, of type `text` and `point`. If a type is not specified for a string literal, then the placeholder type `unknown` is assigned initially, to be resolved in later stages as described below.

There are four fundamental SQL constructs requiring distinct type conversion rules in the PostgreSQL parser:

Function calls  
Much of the PostgreSQL type system is built around a rich set of functions. Functions can have one or more arguments. Since PostgreSQL permits function overloading, the function name alone does not uniquely identify the function to be called; the parser must select the right function based on the data types of the supplied arguments.

Operators  
PostgreSQL allows expressions with prefix (one-argument) operators, as well as infix (two-argument) operators. Like functions, operators can be overloaded, so the same problem of selecting the right operator exists.

Value Storage  
SQL `INSERT` and `UPDATE` statements place the results of expressions into a table. The expressions in the statement must be matched up with, and perhaps converted to, the types of the target columns.

`UNION`, `CASE`, and related constructs  
Since all query results from a unionized `SELECT` statement must appear in a single set of columns, the types of the results of each `SELECT` clause must be matched up and converted to a uniform set. Similarly, the result expressions of a `CASE` construct must be converted to a common type so that the `CASE` expression as a whole has a known output type. Some other constructs, such as `ARRAY[]` and the `GREATEST` and `LEAST` functions, likewise require determination of a common type for several subexpressions.

The system catalogs store information about which conversions, or casts, exist between which data types, and how to perform those conversions. Additional casts can be added by the user with the [???](#sql-createcast) command. (This is usually done in conjunction with defining new data types. The set of casts between built-in types has been carefully crafted and is best not altered.)

data type

category

An additional heuristic provided by the parser allows improved determination of the proper casting behavior among groups of types that have implicit casts. Data types are divided into several basic type categories, including `boolean`, `numeric`, `string`, `bitstring`, `datetime`, `timespan`, `geometric`, `network`, and user-defined. (For a list see [???](#catalog-typcategory-table); but note it is also possible to create custom type categories.) Within each category there can be one or more preferred types, which are preferred when there is a choice of possible types. With careful selection of preferred types and available implicit casts, it is possible to ensure that ambiguous expressions (those with multiple candidate parsing solutions) can be resolved in a useful way.

All type conversion rules are designed with several principles in mind:

- Implicit conversions should never have surprising or unpredictable outcomes.

- There should be no extra overhead in the parser or executor if a query does not need implicit type conversion. That is, if a query is well-formed and the types already match, then the query should execute without spending extra time in the parser and without introducing unnecessary implicit conversion calls in the query.

- Additionally, if a query usually requires an implicit conversion for a function, and if then the user defines a new function with the correct argument types, the parser should use this new function and no longer do implicit conversion to use the old function.

## Operators

operator

type resolution in an invocation

The specific operator that is referenced by an operator expression is determined using the following procedure. Note that this procedure is indirectly affected by the precedence of the operators involved, since that will determine which sub-expressions are taken to be the inputs of which operators. See [???](#sql-precedence) for more information.

1.  Select the operators to be considered from the `pg_operator` system catalog. If a non-schema-qualified operator name was used (the usual case), the operators considered are those with the matching name and argument count that are visible in the current search path (see [???](#ddl-schemas-path)). If a qualified operator name was given, only operators in the specified schema are considered.

    1.  If the search path finds multiple operators with identical argument types, only the one appearing earliest in the path is considered. Operators with different argument types are considered on an equal footing regardless of search path position.

2.  Check for an operator accepting exactly the input argument types. If one exists (there can be only one exact match in the set of operators considered), use it. Lack of an exact match creates a security hazard when calling, via qualified name [^1] (not typical), any operator found in a schema that permits untrusted users to create objects. In such situations, cast arguments to force an exact match.

    1.  If one argument of a binary operator invocation is of the `unknown` type, then assume it is the same type as the other argument for this check. Invocations involving two `unknown` inputs, or a prefix operator with an `unknown` input, will never find a match at this step.

    2.  If one argument of a binary operator invocation is of the `unknown` type and the other is of a domain type, next check to see if there is an operator accepting exactly the domain's base type on both sides; if so, use it.

3.  Look for the best match.

    1.  Discard candidate operators for which the input types do not match and cannot be converted (using an implicit conversion) to match. `unknown` literals are assumed to be convertible to anything for this purpose. If only one candidate remains, use it; else continue to the next step.

    2.  If any input argument is of a domain type, treat it as being of the domain's base type for all subsequent steps. This ensures that domains act like their base types for purposes of ambiguous-operator resolution.

    3.  Run through all candidates and keep those with the most exact matches on input types. Keep all candidates if none have exact matches. If only one candidate remains, use it; else continue to the next step.

    4.  Run through all candidates and keep those that accept preferred types (of the input data type's type category) at the most positions where type conversion will be required. Keep all candidates if none accept preferred types. If only one candidate remains, use it; else continue to the next step.

    5.  If any input arguments are `unknown`, check the type categories accepted at those argument positions by the remaining candidates. At each position, select the `string` category if any candidate accepts that category. (This bias towards string is appropriate since an unknown-type literal looks like a string.) Otherwise, if all the remaining candidates accept the same type category, select that category; otherwise fail because the correct choice cannot be deduced without more clues. Now discard candidates that do not accept the selected type category. Furthermore, if any candidate accepts a preferred type in that category, discard candidates that accept non-preferred types for that argument. Keep all candidates if none survive these tests. If only one candidate remains, use it; else continue to the next step.

    6.  If there are both `unknown` and known-type arguments, and all the known-type arguments have the same type, assume that the `unknown` arguments are also of that type, and check which candidates can accept that type at the `unknown`-argument positions. If exactly one candidate passes this test, use it. Otherwise, fail.

Some examples follow.

Square Root Operator Type Resolution

There is only one square root operator (prefix `|/`) defined in the standard catalog, and it takes an argument of type `double precision`. The scanner assigns an initial type of `integer` to the argument in this query expression:

    SELECT |/ 40 AS "square root of 40";
     square root of 40
    -------------------
     6.324555320336759
    (1 row)

So the parser does a type conversion on the operand and the query is equivalent to:

    SELECT |/ CAST(40 AS double precision) AS "square root of 40";

String Concatenation Operator Type Resolution

A string-like syntax is used for working with string types and for working with complex extension types. Strings with unspecified type are matched with likely operator candidates.

An example with one unspecified argument:

    SELECT text 'abc' || 'def' AS "text and unknown";

     text and unknown
    ------------------
     abcdef
    (1 row)

In this case the parser looks to see if there is an operator taking `text` for both arguments. Since there is, it assumes that the second argument should be interpreted as type `text`.

Here is a concatenation of two values of unspecified types:

    SELECT 'abc' || 'def' AS "unspecified";

     unspecified
    -------------
     abcdef
    (1 row)

In this case there is no initial hint for which type to use, since no types are specified in the query. So, the parser looks for all candidate operators and finds that there are candidates accepting both string-category and bit-string-category inputs. Since string category is preferred when available, that category is selected, and then the preferred type for strings, `text`, is used as the specific type to resolve the unknown-type literals as.

Absolute-Value and Negation Operator Type Resolution

The PostgreSQL operator catalog has several entries for the prefix operator `@`, all of which implement absolute-value operations for various numeric data types. One of these entries is for type `float8`, which is the preferred type in the numeric category. Therefore, PostgreSQL will use that entry when faced with an `unknown` input:

    SELECT @ '-4.5' AS "abs";
     abs
    -----
     4.5
    (1 row)

Here the system has implicitly resolved the unknown-type literal as type `float8` before applying the chosen operator. We can verify that `float8` and not some other type was used:

    SELECT @ '-4.5e500' AS "abs";

    ERROR:  "-4.5e500" is out of range for type double precision

On the other hand, the prefix operator `~` (bitwise negation) is defined only for integer data types, not for `float8`. So, if we try a similar case with `~`, we get:

    SELECT ~ '20' AS "negation";

    ERROR:  operator is not unique: ~ "unknown"
    HINT:  Could not choose a best candidate operator. You might need to add
    explicit type casts.

This happens because the system cannot decide which of the several possible `~` operators should be preferred. We can help it out with an explicit cast:

    SELECT ~ CAST('20' AS int8) AS "negation";

     negation
    ----------
          -21
    (1 row)

Array Inclusion Operator Type Resolution

Here is another example of resolving an operator with one known and one unknown input:

    SELECT array[1,2] <@ '{1,2,3}' as "is subset";

     is subset
    -----------
     t
    (1 row)

The PostgreSQL operator catalog has several entries for the infix operator `<@`, but the only two that could possibly accept an integer array on the left-hand side are array inclusion (`anyarray` `<@` `anyarray`) and range inclusion (`anyelement` `<@` `anyrange`). Since none of these polymorphic pseudo-types (see [???](#datatype-pseudo)) are considered preferred, the parser cannot resolve the ambiguity on that basis. However, [step_title](#op-resol-last-unknown) tells it to assume that the unknown-type literal is of the same type as the other input, that is, integer array. Now only one of the two operators can match, so array inclusion is selected. (Had range inclusion been selected, we would have gotten an error, because the string does not have the right format to be a range literal.)

Custom Operator on a Domain Type

Users sometimes try to declare operators applying just to a domain type. This is possible but is not nearly as useful as it might seem, because the operator resolution rules are designed to select operators applying to the domain's base type. As an example consider

    CREATE DOMAIN mytext AS text CHECK(...);
    CREATE FUNCTION mytext_eq_text (mytext, text) RETURNS boolean AS ...;
    CREATE OPERATOR = (procedure=mytext_eq_text, leftarg=mytext, rightarg=text);
    CREATE TABLE mytable (val mytext);

    SELECT * FROM mytable WHERE val = 'foo';

This query will not use the custom operator. The parser will first see if there is a `mytext` `=` `mytext` operator ([step_title](#op-resol-exact-unknown)), which there is not; then it will consider the domain's base type `text`, and see if there is a `text` `=` `text` operator ([step_title](#op-resol-exact-domain)), which there is; so it resolves the `unknown`-type literal as `text` and uses the `text` `=` `text` operator. The only way to get the custom operator to be used is to explicitly cast the literal:

    SELECT * FROM mytable WHERE val = text 'foo';

so that the `mytext` `=` `text` operator is found immediately according to the exact-match rule. If the best-match rules are reached, they actively discriminate against operators on domain types. If they did not, such an operator would create too many ambiguous-operator failures, because the casting rules always consider a domain as castable to or from its base type, and so the domain operator would be considered usable in all the same cases as a similarly-named operator on the base type.

## Functions

function

type resolution in an invocation

The specific function that is referenced by a function call is determined using the following procedure.

1.  Select the functions to be considered from the `pg_proc` system catalog. If a non-schema-qualified function name was used, the functions considered are those with the matching name and argument count that are visible in the current search path (see [???](#ddl-schemas-path)). If a qualified function name was given, only functions in the specified schema are considered.

    1.  If the search path finds multiple functions of identical argument types, only the one appearing earliest in the path is considered. Functions of different argument types are considered on an equal footing regardless of search path position.

    2.  If a function is declared with a `VARIADIC` array parameter, and the call does not use the `VARIADIC` keyword, then the function is treated as if the array parameter were replaced by one or more occurrences of its element type, as needed to match the call. After such expansion the function might have effective argument types identical to some non-variadic function. In that case the function appearing earlier in the search path is used, or if the two functions are in the same schema, the non-variadic one is preferred.

        This creates a security hazard when calling, via qualified name [^2], a variadic function found in a schema that permits untrusted users to create objects. A malicious user can take control and execute arbitrary SQL functions as though you executed them. Substitute a call bearing the `VARIADIC` keyword, which bypasses this hazard. Calls populating `VARIADIC "any"` parameters often have no equivalent formulation containing the `VARIADIC` keyword. To issue those calls safely, the function's schema must permit only trusted users to create objects.

    3.  Functions that have default values for parameters are considered to match any call that omits zero or more of the defaultable parameter positions. If more than one such function matches a call, the one appearing earliest in the search path is used. If there are two or more such functions in the same schema with identical parameter types in the non-defaulted positions (which is possible if they have different sets of defaultable parameters), the system will not be able to determine which to prefer, and so an “ambiguous function call” error will result if no better match to the call can be found.

        This creates an availability hazard when calling, via qualified name, any function found in a schema that permits untrusted users to create objects. A malicious user can create a function with the name of an existing function, replicating that function's parameters and appending novel parameters having default values. This precludes new calls to the original function. To forestall this hazard, place functions in schemas that permit only trusted users to create objects.

2.  Check for a function accepting exactly the input argument types. If one exists (there can be only one exact match in the set of functions considered), use it. Lack of an exact match creates a security hazard when calling, via qualified name, a function found in a schema that permits untrusted users to create objects. In such situations, cast arguments to force an exact match. (Cases involving `unknown` will never find a match at this step.)

3.  If no exact match is found, see if the function call appears to be a special type conversion request. This happens if the function call has just one argument and the function name is the same as the (internal) name of some data type. Furthermore, the function argument must be either an unknown-type literal, or a type that is binary-coercible to the named data type, or a type that could be converted to the named data type by applying that type's I/O functions (that is, the conversion is either to or from one of the standard string types). When these conditions are met, the function call is treated as a form of `CAST` specification. [^3]

4.  Look for the best match.

    1.  Discard candidate functions for which the input types do not match and cannot be converted (using an implicit conversion) to match. `unknown` literals are assumed to be convertible to anything for this purpose. If only one candidate remains, use it; else continue to the next step.

    2.  If any input argument is of a domain type, treat it as being of the domain's base type for all subsequent steps. This ensures that domains act like their base types for purposes of ambiguous-function resolution.

    3.  Run through all candidates and keep those with the most exact matches on input types. Keep all candidates if none have exact matches. If only one candidate remains, use it; else continue to the next step.

    4.  Run through all candidates and keep those that accept preferred types (of the input data type's type category) at the most positions where type conversion will be required. Keep all candidates if none accept preferred types. If only one candidate remains, use it; else continue to the next step.

    5.  If any input arguments are `unknown`, check the type categories accepted at those argument positions by the remaining candidates. At each position, select the `string` category if any candidate accepts that category. (This bias towards string is appropriate since an unknown-type literal looks like a string.) Otherwise, if all the remaining candidates accept the same type category, select that category; otherwise fail because the correct choice cannot be deduced without more clues. Now discard candidates that do not accept the selected type category. Furthermore, if any candidate accepts a preferred type in that category, discard candidates that accept non-preferred types for that argument. Keep all candidates if none survive these tests. If only one candidate remains, use it; else continue to the next step.

    6.  If there are both `unknown` and known-type arguments, and all the known-type arguments have the same type, assume that the `unknown` arguments are also of that type, and check which candidates can accept that type at the `unknown`-argument positions. If exactly one candidate passes this test, use it. Otherwise, fail.

Note that the “best match” rules are identical for operator and function type resolution. Some examples follow.

Rounding Function Argument Type Resolution

There is only one `round` function that takes two arguments; it takes a first argument of type `numeric` and a second argument of type `integer`. So the following query automatically converts the first argument of type `integer` to `numeric`:

    SELECT round(4, 4);

     round
    --------
     4.0000
    (1 row)

That query is actually transformed by the parser to:

    SELECT round(CAST (4 AS numeric), 4);

Since numeric constants with decimal points are initially assigned the type `numeric`, the following query will require no type conversion and therefore might be slightly more efficient:

    SELECT round(4.0, 4);

Variadic Function Resolution

    CREATE FUNCTION public.variadic_example(VARIADIC numeric[]) RETURNS int
      LANGUAGE sql AS 'SELECT 1';
    CREATE FUNCTION

This function accepts, but does not require, the VARIADIC keyword. It tolerates both integer and numeric arguments:

    SELECT public.variadic_example(0),
           public.variadic_example(0.0),
           public.variadic_example(VARIADIC array[0.0]);
     variadic_example | variadic_example | variadic_example
    ------------------+------------------+------------------
                    1 |                1 |                1
    (1 row)

However, the first and second calls will prefer more-specific functions, if available:

    CREATE FUNCTION public.variadic_example(numeric) RETURNS int
      LANGUAGE sql AS 'SELECT 2';
    CREATE FUNCTION

    CREATE FUNCTION public.variadic_example(int) RETURNS int
      LANGUAGE sql AS 'SELECT 3';
    CREATE FUNCTION

    SELECT public.variadic_example(0),
           public.variadic_example(0.0),
           public.variadic_example(VARIADIC array[0.0]);
     variadic_example | variadic_example | variadic_example
    ------------------+------------------+------------------
                    3 |                2 |                1
    (1 row)

Given the default configuration and only the first function existing, the first and second calls are insecure. Any user could intercept them by creating the second or third function. By matching the argument type exactly and using the `VARIADIC` keyword, the third call is secure.

Substring Function Type Resolution

There are several `substr` functions, one of which takes types `text` and `integer`. If called with a string constant of unspecified type, the system chooses the candidate function that accepts an argument of the preferred category `string` (namely of type `text`).

    SELECT substr('1234', 3);

     substr
    --------
         34
    (1 row)

If the string is declared to be of type `varchar`, as might be the case if it comes from a table, then the parser will try to convert it to become `text`:

    SELECT substr(varchar '1234', 3);

     substr
    --------
         34
    (1 row)

This is transformed by the parser to effectively become:

    SELECT substr(CAST (varchar '1234' AS text), 3);

> [!NOTE]
> The parser learns from the pg_cast catalog that `text` and `varchar` are binary-compatible, meaning that one can be passed to a function that accepts the other without doing any physical conversion. Therefore, no type conversion call is really inserted in this case.

And, if the function is called with an argument of type `integer`, the parser will try to convert that to `text`:

    SELECT substr(1234, 3);
    ERROR:  function substr(integer, integer) does not exist
    HINT:  No function matches the given name and argument types. You might need
    to add explicit type casts.

This does not work because `integer` does not have an implicit cast to `text`. An explicit cast will work, however:

    SELECT substr(CAST (1234 AS text), 3);

     substr
    --------
         34
    (1 row)

## Value Storage

Values to be inserted into a table are converted to the destination column's data type according to the following steps.

1.  Check for an exact match with the target.

2.  Otherwise, try to convert the expression to the target type. This is possible if an assignment cast between the two types is registered in the pg_cast catalog (see [???](#sql-createcast)). Alternatively, if the expression is an unknown-type literal, the contents of the literal string will be fed to the input conversion routine for the target type.

3.  Check to see if there is a sizing cast for the target type. A sizing cast is a cast from that type to itself. If one is found in the pg_cast catalog, apply it to the expression before storing into the destination column. The implementation function for such a cast always takes an extra parameter of type `integer`, which receives the destination column's atttypmod value (typically its declared length, although the interpretation of atttypmod varies for different data types), and it may take a third `boolean` parameter that says whether the cast is explicit or implicit. The cast function is responsible for applying any length-dependent semantics such as size checking or truncation.

`character` Storage Type Conversion

For a target column declared as `character(20)` the following statement shows that the stored value is sized correctly:

    CREATE TABLE vv (v character(20));
    INSERT INTO vv SELECT 'abc' || 'def';
    SELECT v, octet_length(v) FROM vv;

              v           | octet_length
    ----------------------+--------------
     abcdef               |           20
    (1 row)

What has really happened here is that the two unknown literals are resolved to `text` by default, allowing the `||` operator to be resolved as `text` concatenation. Then the `text` result of the operator is converted to `bpchar` (“blank-padded char”, the internal name of the `character` data type) to match the target column type. (Since the conversion from `text` to `bpchar` is binary-coercible, this conversion does not insert any real function call.) Finally, the sizing function `bpchar(bpchar, integer, boolean)` is found in the system catalog and applied to the operator's result and the stored column length. This type-specific function performs the required length check and addition of padding spaces.

## `UNION`, `CASE`, and Related Constructs

UNION

determination of result type

CASE

determination of result type

ARRAY

determination of result type

VALUES

determination of result type

GREATEST

determination of result type

LEAST

determination of result type

SQL `UNION` constructs must match up possibly dissimilar types to become a single result set. The resolution algorithm is applied separately to each output column of a union query. The `INTERSECT` and `EXCEPT` constructs resolve dissimilar types in the same way as `UNION`. Some other constructs, including `CASE`, `ARRAY`, `VALUES`, and the `GREATEST` and `LEAST` functions, use the identical algorithm to match up their component expressions and select a result data type.

1.  If all inputs are of the same type, and it is not `unknown`, resolve as that type.

2.  If any input is of a domain type, treat it as being of the domain's base type for all subsequent steps. [^4]

3.  If all inputs are of type `unknown`, resolve as type `text` (the preferred type of the string category). Otherwise, `unknown` inputs are ignored for the purposes of the remaining rules.

4.  If the non-unknown inputs are not all of the same type category, fail.

5.  Select the first non-unknown input type as the candidate type, then consider each other non-unknown input type, left to right. [^5] If the candidate type can be implicitly converted to the other type, but not vice-versa, select the other type as the new candidate type. Then continue considering the remaining inputs. If, at any stage of this process, a preferred type is selected, stop considering additional inputs.

6.  Convert all inputs to the final candidate type. Fail if there is not an implicit conversion from a given input type to the candidate type.

Some examples follow.

Type Resolution with Underspecified Types in a Union

    SELECT text 'a' AS "text" UNION SELECT 'b';

     text
    ------
     a
     b
    (2 rows)

Here, the unknown-type literal `'b'` will be resolved to type `text`.

Type Resolution in a Simple Union

    SELECT 1.2 AS "numeric" UNION SELECT 1;

     numeric
    ---------
           1
         1.2
    (2 rows)

The literal `1.2` is of type `numeric`, and the `integer` value `1` can be cast implicitly to `numeric`, so that type is used.

Type Resolution in a Transposed Union

    SELECT 1 AS "real" UNION SELECT CAST('2.2' AS REAL);

     real
    ------
        1
      2.2
    (2 rows)

Here, since type `real` cannot be implicitly cast to `integer`, but `integer` can be implicitly cast to `real`, the union result type is resolved as `real`.

Type Resolution in a Nested Union

    SELECT NULL UNION SELECT NULL UNION SELECT 1;

    ERROR:  UNION types text and integer cannot be matched

This failure occurs because PostgreSQL treats multiple `UNION`s as a nest of pairwise operations; that is, this input is the same as

    (SELECT NULL UNION SELECT NULL) UNION SELECT 1;

The inner `UNION` is resolved as emitting type `text`, according to the rules given above. Then the outer `UNION` has inputs of types `text` and `integer`, leading to the observed error. The problem can be fixed by ensuring that the leftmost `UNION` has at least one input of the desired result type.

`INTERSECT` and `EXCEPT` operations are likewise resolved pairwise. However, the other constructs described in this section consider all of their inputs in one resolution step.

## `SELECT` Output Columns

SELECT

determination of result type

The rules given in the preceding sections will result in assignment of non-`unknown` data types to all expressions in an SQL query, except for unspecified-type literals that appear as simple output columns of a `SELECT` command. For example, in

    SELECT 'Hello World';

there is nothing to identify what type the string literal should be taken as. In this situation PostgreSQL will fall back to resolving the literal's type as `text`.

When the `SELECT` is one arm of a `UNION` (or `INTERSECT` or `EXCEPT`) construct, or when it appears within `INSERT ... SELECT`, this rule is not applied since rules given in preceding sections take precedence. The type of an unspecified-type literal can be taken from the other `UNION` arm in the first case, or from the destination column in the second case.

`RETURNING` lists are treated the same as `SELECT` output lists for this purpose.

> [!NOTE]
> Prior to PostgreSQL 10, this rule did not exist, and unspecified-type literals in a `SELECT` output list were left as type `unknown`. That had assorted bad consequences, so it's been changed.

[^1]: The hazard does not arise with a non-schema-qualified name, because a search path containing schemas that permit untrusted users to create objects is not a [secure schema usage pattern](#ddl-schemas-patterns).

[^2]: The hazard does not arise with a non-schema-qualified name, because a search path containing schemas that permit untrusted users to create objects is not a [secure schema usage pattern](#ddl-schemas-patterns).

[^3]: The reason for this step is to support function-style cast specifications in cases where there is not an actual cast function. If there is a cast function, it is conventionally named after its output type, and so there is no need to have a special case. See [???](#sql-createcast) for additional commentary.

[^4]: Somewhat like the treatment of domain inputs for operators and functions, this behavior allows a domain type to be preserved through a `UNION` or similar construct, so long as the user is careful to ensure that all inputs are implicitly or explicitly of that exact type. Otherwise the domain's base type will be used.

[^5]: For historical reasons, `CASE` treats its `ELSE` clause (if any) as the “first” input, with the `THEN` clauses(s) considered after that. In all other cases, “left to right” means the order in which the expressions appear in the query text.
