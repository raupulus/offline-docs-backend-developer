---
title: Procedural Languages
source_url: https://www.postgresql.org/docs/17/xplang.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: xplang.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 3830
---

## Procedural Languages

procedural language

PostgreSQL allows user-defined functions to be written in other languages besides SQL and C. These other languages are generically called procedural languages (PLs). For a function written in a procedural language, the database server has no built-in knowledge about how to interpret the function's source text. Instead, the task is passed to a special handler that knows the details of the language. The handler could either do all the work of parsing, syntax analysis, execution, etc. itself, or it could serve as “glue” between PostgreSQL and an existing implementation of a programming language. The handler itself is a C language function compiled into a shared object and loaded on demand, just like any other C function.

There are currently four procedural languages available in the standard PostgreSQL distribution: PL/pgSQL ([???](#plpgsql)), PL/Tcl ([???](#pltcl)), PL/Perl ([???](#plperl)), and PL/Python ([???](#plpython)). There are additional procedural languages available that are not included in the core distribution. [???](#external-projects) has information about finding them. In addition other languages can be defined by users; the basics of developing a new procedural language are covered in [???](#plhandler).

## Installing Procedural Languages

A procedural language must be “installed” into each database where it is to be used. But procedural languages installed in the database `template1` are automatically available in all subsequently created databases, since their entries in `template1` will be copied by `CREATE DATABASE`. So the database administrator can decide which languages are available in which databases and can make some languages available by default if desired.

For the languages supplied with the standard distribution, it is only necessary to execute `CREATE EXTENSION` \<language_name\> to install the language into the current database. The manual procedure described below is only recommended for installing languages that have not been packaged as extensions.

1.  The shared object for the language handler must be compiled and installed into an appropriate library directory. This works in the same way as building and installing modules with regular user-defined C functions does; see [???](#dfunc). Often, the language handler will depend on an external library that provides the actual programming language engine; if so, that must be installed as well.

2.  The handler must be declared with the command CREATE FUNCTION \<handler_function_name\>() RETURNS language_handler AS '\<path-to-shared-object\>' LANGUAGE C; The special return type of `language_handler` tells the database system that this function does not return one of the defined SQL data types and is not directly usable in SQL statements.

3.  Optionally, the language handler can provide an “inline” handler function that executes anonymous code blocks ([`DO`](#sql-do) commands) written in this language. If an inline handler function is provided by the language, declare it with a command like CREATE FUNCTION \<inline_function_name\>(internal) RETURNS void AS '\<path-to-shared-object\>' LANGUAGE C;

4.  Optionally, the language handler can provide a “validator” function that checks a function definition for correctness without actually executing it. The validator function is called by `CREATE FUNCTION` if it exists. If a validator function is provided by the language, declare it with a command like CREATE FUNCTION \<validator_function_name\>(oid) RETURNS void AS '\<path-to-shared-object\>' LANGUAGE C STRICT;

5.  Finally, the PL must be declared with the command CREATE \[TRUSTED\] LANGUAGE \<language_name\> HANDLER \<handler_function_name\> \[INLINE \<inline_function_name\>\] \[VALIDATOR \<validator_function_name\>\] ; The optional key word `TRUSTED` specifies that the language does not grant access to data that the user would not otherwise have. Trusted languages are designed for ordinary database users (those without superuser privilege) and allows them to safely create functions and procedures. Since PL functions are executed inside the database server, the `TRUSTED` flag should only be given for languages that do not allow access to database server internals or the file system. The languages PL/pgSQL, PL/Tcl, and PL/Perl are considered trusted; the languages PL/TclU, PL/PerlU, and PL/PythonU are designed to provide unlimited functionality and should *not* be marked trusted.

[example_title](#xplang-install-example) shows how the manual installation procedure would work with the language PL/Perl.

Manual Installation of PL/Perl

The following command tells the database server where to find the shared object for the PL/Perl language's call handler function:

    CREATE FUNCTION plperl_call_handler() RETURNS language_handler AS
        '$libdir/plperl' LANGUAGE C;

PL/Perl has an inline handler function and a validator function, so we declare those too:

    CREATE FUNCTION plperl_inline_handler(internal) RETURNS void AS
        '$libdir/plperl' LANGUAGE C STRICT;

    CREATE FUNCTION plperl_validator(oid) RETURNS void AS
        '$libdir/plperl' LANGUAGE C STRICT;

The command:

    CREATE TRUSTED LANGUAGE plperl
        HANDLER plperl_call_handler
        INLINE plperl_inline_handler
        VALIDATOR plperl_validator;

then defines that the previously declared functions should be invoked for functions and procedures where the language attribute is `plperl`.

In a default PostgreSQL installation, the handler for the PL/pgSQL language is built and installed into the “library” directory; furthermore, the PL/pgSQL language itself is installed in all databases. If Tcl support is configured in, the handlers for PL/Tcl and PL/TclU are built and installed in the library directory, but the language itself is not installed in any database by default. Likewise, the PL/Perl and PL/PerlU handlers are built and installed if Perl support is configured, and the PL/PythonU handler is installed if Python support is configured, but these languages are not installed by default.
