---
title: Bridging Tcl and JSON with the SQLite Extension
source_url: https://www.sqlite.org/tcljson.html
source_path: tcljson.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 8090
---

# 1. Using SQLite to Bridge Tcl and JSON

[The Tcl SQLite extension](./tclsqlite.md) can act as a bridge to smooth over Tcl's impedance mismatch with JSON, shifting all of the parsing and escaping from Tcl to SQLite with very little effort. The sections below demonstrate techniques for consuming and emitting JSON via SQLite.

## 1.1. Consuming JSON

One of the simplest way to consume and break down a JSON payload is to feed it to SQLite and extract the results using Tcl's `lassign` function:

> \
> set json theJSON...\
> lassign \[db eval {\
>   with payload(j) as (select jsonb(\$json)) select\
>   -- A simple value:\
>   j-\>\>'foo',\
>   -- A sub-object or array:\
>   CASE WHEN json_valid(j-\>\>'bar') THEN j-\>\>'bar' ELSE NULL END\
>   -- Any other fields...\
>   from payload\
> }\] foo bar\

Arrays can be injested using `json_each()`:

> \
> set json {\[1, "two", 3.0, {"nested": true}, null\]}\
> set myList \[db eval {\
>   select value from json_each(\$json)\
> }\]\
> \
> \# Emits: 1 two 3.0 {{"nested":true}} {}\

Arrays of objects can be decomposed into a list of dict objects:

> \
> set json {\[{"id":1, "v":"A"}, {"id":2, "v":"B"}\]}\
> set myDictList \[db eval {\
>   select json_object('id', value-\>\>'id', 'v', value-\>\>'v')\
>   from json_each(\$json)\
> }\]\
> \
> \# Emits: {{"id":1,"v":"A"}} {{"id":2,"v":"B"}}\

Object entries in array objects can be decomposed using an approach like the first example shown above.

## 1.2. Emitting JSON: Db Table as a JSON Object

The approach described here uses an in-memory db to incrementally build up a JSON object, automatically smoothing over the edges between data types such as numbers and strings.

> \
> \#\
> \# Initialize, if needed, the sqlite3 connection for the JR temp db and\
> \# return its command name.\
> \#\
> \# JR = JSON Response (to an HTTP request)\
> \#\
> proc jr-db {} {\
>   if {"" eq \[info command ::\_\_jrdb\]} {\
>     sqlite3 ::\_\_jrdb ":memory:"\
>     ::\_\_jrdb eval {\
>       -- Holds a list of key/value pairs for a JSON response object\
>       create table jr(k TEXT UNIQUE ON CONFLICT REPLACE,v ANY);\
>     }\
>   }\
>   return ::\_\_jrdb\
> }\
> \
> \#\
> \# Remove all entries from the JR buffer.\
> \#\
> proc jr-reset {args} {\
>   \[jr-db\] eval {delete from jr}\
> }\
> \
> \#\
> \# Set one or more key/value pairs in the JR object.\
> \#\
> proc jr-set {args} {\
>   set db \[jr-db\]\
>   foreach {k v} \$args {\
>     \$db eval {insert into jr(k,v) values(\$k,\$v)}\
>   }\
> }\
> \
> \#\
> \# Returns a JSON-format object representing the current JR state.\
> \#\
> proc jr-get {} {\
>   \[jr-db\] onecolumn {\
>     select json_group_object(k,CASE WHEN json_valid(v,1)\
>                              THEN json(v) ELSE v END) from jr\
>   }\
> }\

Example usage:

> \
> jr-set message "This is a message."\
> jr-set aBool true isNull null anInt 37 aFloat 42.42\
> puts \[jr-get\]\

Results in:

> \
> {"message":"This is a message.","aBool":true,"isNull":null,"anInt":37,"aFloat":42.42}\

## 1.3. Emitting JSON: Incremental Build-up

The approach shown here uses a couple of routines to incrementally build up a nested object or array, faithfully navigating the type handling, such that integers, null, and boolean-looking values can be emitted as such instead of strings.

> \
> \#\
> \# Returns the command name of the shared SQLite3 instance used by the\
> \# X-to-JSON APIs, initializing it on demand.\
> \#\
> proc json-db {} {\
>   if {"" eq \[info command ::\_\_jsonDb\]} {\
>     sqlite3 ::\_\_jsonDb ":memory:"\
>   }\
>   return ::\_\_jsonDb\
> }\
> \
> \#\
> \# Given a dict-style object, this creates a JSON object representation.\
> \# It does not handle nested objects but each value may itself be the result\
> \# of its own call to this method, which has a similar effect.\
> \#\
> proc json-obj {kvps} {\
>   set q "select json_object("\
>   set n 0\
>   set nn 1\
>   foreach {k v} \$kvps {\
>     set \$n \$k\
>     set \$nn \$v\
>     if {\$n} {append q ","}\
>     append q "\\\$n, CASE WHEN json_valid(\\\$nn) THEN json(\\\$nn) ELSE \\\$nn END"\
>     # This may look like an SQL injection opportunity, but it's\
>     # injecting prepared statement placeholders, not values.\
>     incr n 2\
>     incr nn 2\
>   }\
>   append q ")"\
>   \[json-db\] onecolumn \$q\
> }\
> \
> \#\
> \# Returns a JSON-format array of the given arguments. See json-object\
> \# for notes about nesting.\
> \#\
> proc json-array {args} {\
>   set n 0\
>   set q "select json_array("\
>   foreach a \$args {\
>     set \$n \$a\
>     if {\$n} {append q ","}\
>     append q "CASE WHEN json_valid(\\\$n) THEN json(\\\$n) ELSE \\\$n END"\
>     incr n\
>   }\
>   append q ")"\
>   \[json-db\] onecolumn \$q\
> }\

Example usage:

> \
> proc json-pretty {arg {space "  "}} {\
>   \[json-db\] onecolumn {select json_pretty(\$arg,\$space)}\
> }\
> set o {\
>   hi world\
>   number 17.3\
>   truth true\
>   lies false\
>   nil null\
>   nada "null"\
>   notNull "Null"\
> }\
> lappend o list \[json-array hello there \[json-obj {nested true}\]\]\
> lappend o obj \[json-obj {name "Nested object"}\]\
> puts \[json-pretty \[json-obj \$o\]\]\

Results in:

> {\
>   "hi": "world",\
>   "number": 17.3,\
>   "truth": true,\
>   "lies": false,\
>   "nil": null,\
>   "nada": null,\
>   "notNull": "Null",\
>   "list": \[\
>     "hello",\
>     "there",\
>     {\
>       "nested": true\
>     }\
>   \],\
>   "obj": {\
>     "name": "Nested object"\
>   }\
> }\
