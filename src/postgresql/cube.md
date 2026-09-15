---
title: cube — a multi-dimensional cube data type
source_url: https://www.postgresql.org/docs/17/cube.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: cube.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 350
---

## cube a multi-dimensional cube data type

cube (extension)

This module implements a data type `cube` for representing multidimensional cubes.

This module is considered “trusted”, that is, it can be installed by non-superusers who have `CREATE` privilege on the current database.

## Syntax

[Cube External Representations](#cube-repr-table) shows the valid external representations for the `cube` type. \<x\>, \<y\>, etc. denote floating-point numbers.

| External Syntax | Meaning |
|----|----|
| `x` | A one-dimensional point (or, zero-length one-dimensional interval) |
| `(x)` | Same as above |
| `x1,x2,...,xn` | A point in n-dimensional space, represented internally as a zero-volume cube |
| `(x1,x2,...,xn)` | Same as above |
| `(x),(y)` | A one-dimensional interval starting at \<x\> and ending at \<y\> or vice versa; the order does not matter |
| `[(x),(y)]` | Same as above |
| `(x1,...,xn),(y1,...,yn)` | An n-dimensional cube represented by a pair of its diagonally opposite corners |
| `[(x1,...,xn),(y1,...,yn)]` | Same as above |

Cube External Representations {#cube-repr-table}

It does not matter which order the opposite corners of a cube are entered in. The `cube` functions automatically swap values if needed to create a uniform “lower left upper right” internal representation. When the corners coincide, `cube` stores only one corner along with an “is point” flag to avoid wasting space.

White space is ignored on input, so `[(x),(y)]` is the same as `[ ( x ), ( y ) ]`.

## Precision

Values are stored internally as 64-bit floating point numbers. This means that numbers with more than about 16 significant digits will be truncated.

## Usage

[Cube Operators](#cube-operators-table) shows the specialized operators provided for type `cube`.

<table id="cube-operators-table">
<caption>Cube Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>cube</code> <code>&amp;&amp;</code> <code>cube</code> boolean</p>
<p>Do the cubes overlap?</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube</code> <code>@&gt;</code> <code>cube</code> boolean</p>
<p>Does the first cube contain the second?</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube</code> <code>&lt;@</code> <code>cube</code> boolean</p>
<p>Is the first cube contained in the second?</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube</code> <code>-&gt;</code> <code>integer</code> float8</p>
<p>Extracts the <code>n</code>-th coordinate of the cube (counting from 1).</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube</code> <code>~&gt;</code> <code>integer</code> float8</p>
<p>Extracts the <code>n</code>-th coordinate of the cube, counting in the following way: <code>n</code> = 2 * <code>k</code> - 1 means lower bound of <code>k</code>-th dimension, <code>n</code> = 2 * <code>k</code> means upper bound of <code>k</code>-th dimension. Negative <code>n</code> denotes the inverse value of the corresponding positive coordinate. This operator is designed for KNN-GiST support.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube</code> <code>&lt;-&gt;</code> <code>cube</code> float8</p>
<p>Computes the Euclidean distance between the two cubes.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube</code> <code>&lt;#&gt;</code> <code>cube</code> float8</p>
<p>Computes the taxicab (L-1 metric) distance between the two cubes.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube</code> <code>&lt;=&gt;</code> <code>cube</code> float8</p>
<p>Computes the Chebyshev (L-inf metric) distance between the two cubes.</p></td>
</tr>
</tbody>
</table>

In addition to the above operators, the usual comparison operators shown in [???](#functions-comparison-op-table) are available for type `cube`. These operators first compare the first coordinates, and if those are equal, compare the second coordinates, etc. They exist mainly to support the b-tree index operator class for `cube`, which can be useful for example if you would like a UNIQUE constraint on a `cube` column. Otherwise, this ordering is not of much practical use.

The `cube` module also provides a GiST index operator class for `cube` values. A `cube` GiST index can be used to search for values using the `=`, `&&`, `@>`, and `<@` operators in `WHERE` clauses.

In addition, a `cube` GiST index can be used to find nearest neighbors using the metric operators `<->`, `<#>`, and `<=>` in `ORDER BY` clauses. For example, the nearest neighbor of the 3-D point (0.5, 0.5, 0.5) could be found efficiently with:

    SELECT c FROM test ORDER BY c <-> cube(array[0.5,0.5,0.5]) LIMIT 1;

The `~>` operator can also be used in this way to efficiently retrieve the first few values sorted by a selected coordinate. For example, to get the first few cubes ordered by the first coordinate (lower left corner) ascending one could use the following query:

    SELECT c FROM test ORDER BY c ~> 1 LIMIT 5;

And to get 2-D cubes ordered by the first coordinate of the upper right corner descending:

    SELECT c FROM test ORDER BY c ~> 3 DESC LIMIT 5;

[Cube Functions](#cube-functions-table) shows the available functions.

<table id="cube-functions-table">
<caption>Cube Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>cube</code> ( <code>float8</code> ) cube</p>
<p>Makes a one dimensional cube with both coordinates the same.</p>
<p><code>cube(1)</code> (1)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube</code> ( <code>float8</code>, <code>float8</code> ) cube</p>
<p>Makes a one dimensional cube.</p>
<p><code>cube(1, 2)</code> (1),(2)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube</code> ( <code>float8[]</code> ) cube</p>
<p>Makes a zero-volume cube using the coordinates defined by the array.</p>
<p><code>cube(ARRAY[1,2,3])</code> (1, 2, 3)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube</code> ( <code>float8[]</code>, <code>float8[]</code> ) cube</p>
<p>Makes a cube with upper right and lower left coordinates as defined by the two arrays, which must be of the same length.</p>
<p><code>cube(ARRAY[1,2], ARRAY[3,4])</code> (1, 2),(3, 4)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube</code> ( <code>cube</code>, <code>float8</code> ) cube</p>
<p>Makes a new cube by adding a dimension on to an existing cube, with the same values for both endpoints of the new coordinate. This is useful for building cubes piece by piece from calculated values.</p>
<p><code>cube('(1,2),(3,4)'::cube, 5)</code> (1, 2, 5),(3, 4, 5)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube</code> ( <code>cube</code>, <code>float8</code>, <code>float8</code> ) cube</p>
<p>Makes a new cube by adding a dimension on to an existing cube. This is useful for building cubes piece by piece from calculated values.</p>
<p><code>cube('(1,2),(3,4)'::cube, 5, 6)</code> (1, 2, 5),(3, 4, 6)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube_dim</code> ( <code>cube</code> ) integer</p>
<p>Returns the number of dimensions of the cube.</p>
<p><code>cube_dim('(1,2),(3,4)')</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube_ll_coord</code> ( <code>cube</code>, <code>integer</code> ) float8</p>
<p>Returns the <code>n</code>-th coordinate value for the lower left corner of the cube.</p>
<p><code>cube_ll_coord('(1,2),(3,4)', 2)</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube_ur_coord</code> ( <code>cube</code>, <code>integer</code> ) float8</p>
<p>Returns the <code>n</code>-th coordinate value for the upper right corner of the cube.</p>
<p><code>cube_ur_coord('(1,2),(3,4)', 2)</code> 4</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube_is_point</code> ( <code>cube</code> ) boolean</p>
<p>Returns true if the cube is a point, that is, the two defining corners are the same.</p>
<p><code>cube_is_point(cube(1,1))</code> t</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube_distance</code> ( <code>cube</code>, <code>cube</code> ) float8</p>
<p>Returns the distance between two cubes. If both cubes are points, this is the normal distance function.</p>
<p><code>cube_distance('(1,2)', '(3,4)')</code> 2.8284271247461903</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube_subset</code> ( <code>cube</code>, <code>integer[]</code> ) cube</p>
<p>Makes a new cube from an existing cube, using a list of dimension indexes from an array. Can be used to extract the endpoints of a single dimension, or to drop dimensions, or to reorder them as desired.</p>
<p><code>cube_subset(cube('(1,3,5),(6,7,8)'), ARRAY[2])</code> (3),(7)</p>
<p><code>cube_subset(cube('(1,3,5),(6,7,8)'), ARRAY[3,2,1,1])</code> (5, 3, 1, 1),(8, 7, 6, 6)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube_union</code> ( <code>cube</code>, <code>cube</code> ) cube</p>
<p>Produces the union of two cubes.</p>
<p><code>cube_union('(1,2)', '(3,4)')</code> (1, 2),(3, 4)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube_inter</code> ( <code>cube</code>, <code>cube</code> ) cube</p>
<p>Produces the intersection of two cubes.</p>
<p><code>cube_inter('(1,2)', '(3,4)')</code> (3, 4),(1, 2)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>cube_enlarge</code> ( <code>c</code> <code>cube</code>, <code>r</code> <code>double</code>, <code>n</code> <code>integer</code> ) cube</p>
<p>Increases the size of the cube by the specified radius <code>r</code> in at least <code>n</code> dimensions. If the radius is negative the cube is shrunk instead. All defined dimensions are changed by the radius <code>r</code>. Lower-left coordinates are decreased by <code>r</code> and upper-right coordinates are increased by <code>r</code>. If a lower-left coordinate is increased to more than the corresponding upper-right coordinate (this can only happen when <code>r</code> &lt; 0) than both coordinates are set to their average. If <code>n</code> is greater than the number of defined dimensions and the cube is being enlarged (<code>r</code> &gt; 0), then extra dimensions are added to make <code>n</code> altogether; 0 is used as the initial value for the extra coordinates. This function is useful for creating bounding boxes around a point for searching for nearby points.</p>
<p><code>cube_enlarge('(1,2),(3,4)', 0.5, 3)</code> (0.5, 1.5, -0.5),(3.5, 4.5, 0.5)</p></td>
</tr>
</tbody>
</table>

## Defaults

This union:

    select cube_union('(0,5,2),(2,3,1)', '0');
    cube_union
    -------------------
    (0, 0, 0),(2, 5, 2)
    (1 row)

does not contradict common sense, neither does the intersection:

    select cube_inter('(0,-1),(1,1)', '(-2),(2)');
    cube_inter
    -------------
    (0, 0),(1, 0)
    (1 row)

In all binary operations on differently-dimensioned cubes, the lower-dimensional one is assumed to be a Cartesian projection, i. e., having zeroes in place of coordinates omitted in the string representation. The above examples are equivalent to:

    cube_union('(0,5,2),(2,3,1)','(0,0,0),(0,0,0)');
    cube_inter('(0,-1),(1,1)','(-2,0),(2,0)');

The following containment predicate uses the point syntax, while in fact the second argument is internally represented by a box. This syntax makes it unnecessary to define a separate point type and functions for (box,point) predicates.

    select cube_contains('(0,0),(1,1)', '0.5,0.5');
    cube_contains
    --------------
    t
    (1 row)

## Notes

For examples of usage, see the regression test `sql/cube.sql`.

To make it harder for people to break things, there is a limit of 100 on the number of dimensions of cubes. This is set in `cubedata.h` if you need something bigger.

## Credits

Original author: Gene Selkov, Jr. <selkovjr@mcs.anl.gov>, Mathematics and Computer Science Division, Argonne National Laboratory.

My thanks are primarily to Prof. Joe Hellerstein ([](https://dsf.berkeley.edu/jmh/)) for elucidating the gist of the GiST ([](http://gist.cs.berkeley.edu/)), and to his former student Andy Dong for his example written for Illustra. I am also grateful to all Postgres developers, present and past, for enabling myself to create my own world and live undisturbed in it. And I would like to acknowledge my gratitude to Argonne Lab and to the U.S. Department of Energy for the years of faithful support of my database research.

Minor updates to this package were made by Bruno Wolff III <bruno@wolff.to> in August/September of 2002. These include changing the precision from single precision to double precision and adding some new functions.

Additional updates were made by Joshua Reich <josh@root.net> in July 2006. These include `cube(float8[], float8[])` and cleaning up the code to use the V1 call protocol instead of the deprecated V0 protocol.
