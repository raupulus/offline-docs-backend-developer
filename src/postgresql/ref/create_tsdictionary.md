---
title: CREATE TEXT SEARCH DICTIONARY
description: define a new text search dictionary
source_url: https://www.postgresql.org/docs/17/sql-createtsdictionary.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/create_tsdictionary.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2130
---

CREATE TEXT SEARCH DICTIONARY

CREATE TEXT SEARCH DICTIONARY

7

SQL - Language Statements

CREATE TEXT SEARCH DICTIONARY

define a new text search dictionary

CREATE TEXT SEARCH DICTIONARY

name

( TEMPLATE =

template

\[,

option

=

value

\[, ... \]\] )

## Description

`CREATE TEXT SEARCH DICTIONARY` creates a new text search dictionary. A text search dictionary specifies a way of recognizing interesting or uninteresting words for searching. A dictionary depends on a text search template, which specifies the functions that actually perform the work. Typically the dictionary provides some options that control the detailed behavior of the template's functions.

If a schema name is given then the text search dictionary is created in the specified schema. Otherwise it is created in the current schema.

The user who defines a text search dictionary becomes its owner.

Refer to [???](#textsearch) for further information.

## Parameters

\<name\>  
The name of the text search dictionary to be created. The name can be schema-qualified.

\<template\>  
The name of the text search template that will define the basic behavior of this dictionary.

\<option\>  
The name of a template-specific option to be set for this dictionary.

\<value\>  
The value to use for a template-specific option. If the value is not a simple identifier or number, it must be quoted (but you can always quote it, if you wish).

The options can appear in any order.

## Examples

The following example command creates a Snowball-based dictionary with a nonstandard list of stop words.

    CREATE TEXT SEARCH DICTIONARY my_russian (
        template = snowball,
        language = russian,
        stopwords = myrussian
    );

## Compatibility

There is no `CREATE TEXT SEARCH DICTIONARY` statement in the SQL standard.

## See Also
