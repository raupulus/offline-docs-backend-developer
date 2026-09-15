---
title: earthdistance — calculate great-circle distances
source_url: https://www.postgresql.org/docs/17/earthdistance.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: earthdistance.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 470
---

## earthdistance calculate great-circle distances

earthdistance

The `earthdistance` module provides two different approaches to calculating great circle distances on the surface of the Earth. The one described first depends on the `cube` module. The second one is based on the built-in `point` data type, using longitude and latitude for the coordinates.

In this module, the Earth is assumed to be perfectly spherical. (If that's too inaccurate for you, you might want to look at the [PostGIS](https://postgis.net/) project.)

The `cube` module must be installed before `earthdistance` can be installed (although you can use the `CASCADE` option of `CREATE EXTENSION` to install both in one command).

> [!CAUTION]
> It is strongly recommended that `earthdistance` and `cube` be installed in the same schema, and that that schema be one for which CREATE privilege has not been and will not be granted to any untrusted users. Otherwise there are installation-time security hazards if `earthdistance`'s schema contains objects defined by a hostile user. Furthermore, when using `earthdistance`'s functions after installation, the entire search path should contain only trusted schemas.

## Cube-Based Earth Distances

Data is stored in cubes that are points (both corners are the same) using 3 coordinates representing the x, y, and z distance from the center of the Earth. A domain `earth` over type `cube` is provided, which includes constraint checks that the value meets these restrictions and is reasonably close to the actual surface of the Earth.

The radius of the Earth is obtained from the `earth()` function. It is given in meters. But by changing this one function you can change the module to use some other units, or to use a different value of the radius that you feel is more appropriate.

This package has applications to astronomical databases as well. Astronomers will probably want to change `earth()` to return a radius of `180/pi()` so that distances are in degrees.

Functions are provided to support input in latitude and longitude (in degrees), to support output of latitude and longitude, to calculate the great circle distance between two points and to easily specify a bounding box usable for index searches.

The provided functions are shown in [Cube-Based Earthdistance Functions](#earthdistance-cube-functions).

<table id="earthdistance-cube-functions">
<caption>Cube-Based Earthdistance Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>earth</code> () float8</p>
<p>Returns the assumed radius of the Earth.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>sec_to_gc</code> ( <code>float8</code> ) float8</p>
<p>Converts the normal straight line (secant) distance between two points on the surface of the Earth to the great circle distance between them.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>gc_to_sec</code> ( <code>float8</code> ) float8</p>
<p>Converts the great circle distance between two points on the surface of the Earth to the normal straight line (secant) distance between them.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>ll_to_earth</code> ( <code>float8</code>, <code>float8</code> ) earth</p>
<p>Returns the location of a point on the surface of the Earth given its latitude (argument 1) and longitude (argument 2) in degrees.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>latitude</code> ( <code>earth</code> ) float8</p>
<p>Returns the latitude in degrees of a point on the surface of the Earth.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>longitude</code> ( <code>earth</code> ) float8</p>
<p>Returns the longitude in degrees of a point on the surface of the Earth.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>earth_distance</code> ( <code>earth</code>, <code>earth</code> ) float8</p>
<p>Returns the great circle distance between two points on the surface of the Earth.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>earth_box</code> ( <code>earth</code>, <code>float8</code> ) cube</p>
<p>Returns a box suitable for an indexed search using the <code>cube</code> <code>@&gt;</code> operator for points within a given great circle distance of a location. Some points in this box are further than the specified great circle distance from the location, so a second check using <code>earth_distance</code> should be included in the query.</p></td>
</tr>
</tbody>
</table>

## Point-Based Earth Distances

The second part of the module relies on representing Earth locations as values of type `point`, in which the first component is taken to represent longitude in degrees, and the second component is taken to represent latitude in degrees. Points are taken as (longitude, latitude) and not vice versa because longitude is closer to the intuitive idea of x-axis and latitude to y-axis.

A single operator is provided, shown in [Point-Based Earthdistance Operators](#earthdistance-point-operators).

<table id="earthdistance-point-operators">
<caption>Point-Based Earthdistance Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>point</code> <code>&lt;@&gt;</code> <code>point</code> float8</p>
<p>Computes the distance in statute miles between two points on the Earth's surface.</p></td>
</tr>
</tbody>
</table>

Note that unlike the `cube`-based part of the module, units are hardwired here: changing the `earth()` function will not affect the results of this operator.

One disadvantage of the longitude/latitude representation is that you need to be careful about the edge conditions near the poles and near +/- 180 degrees of longitude. The `cube`-based representation avoids these discontinuities.
