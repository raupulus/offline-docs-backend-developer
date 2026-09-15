---
title: Preface
source_url: https://www.postgresql.org/docs/17/preface.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: intro.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 760
---

## Preface

This book is the official documentation of PostgreSQL. It has been written by the PostgreSQL developers and other volunteers in parallel to the development of the PostgreSQL software. It describes all the functionality that the current version of PostgreSQL officially supports.

To make the large amount of information about PostgreSQL manageable, this book has been organized in several parts. Each part is targeted at a different class of users, or at users in different stages of their PostgreSQL experience:

- [???](#tutorial) is an informal introduction for new users.

- [???](#sql) documents the SQL query language environment, including data types and functions, as well as user-level performance tuning. Every PostgreSQL user should read this.

- [???](#admin) describes the installation and administration of the server. Everyone who runs a PostgreSQL server, be it for private use or for others, should read this part.

- [???](#client-interfaces) describes the programming interfaces for PostgreSQL client programs.

- [???](#server-programming) contains information for advanced users about the extensibility capabilities of the server. Topics include user-defined data types and functions.

- [???](#reference) contains reference information about SQL commands, client and server programs. This part supports the other parts with structured information sorted by command or program.

- [???](#internals) contains assorted information that might be of use to PostgreSQL developers.

## What Is PostgreSQL?

PostgreSQL is an object-relational database management system (ORDBMS) based on [ POSTGRES, Version 4.2](https://dsf.berkeley.edu/postgres.html), developed at the University of California at Berkeley Computer Science Department. POSTGRES pioneered many concepts that only became available in some commercial database systems much later.

PostgreSQL is an open-source descendant of this original Berkeley code. It supports a large part of the SQL standard and offers many modern features:

- [complex queries](#sql)
- [foreign keys](#ddl-constraints-fk)
- [triggers](#triggers)
- [updatable views](#sql-createview-updatable-views)
- [transactional integrity](#transaction-iso)
- [multiversion concurrency control](#mvcc)

Also, PostgreSQL can be extended by the user in many ways, for example by adding new

- [data types](#datatype)
- [functions](#functions)
- [operators](#functions)
- [aggregate functions](#functions-aggregate)
- [index methods](#indexes)
- [procedural languages](#server-programming)

And because of the liberal license, PostgreSQL can be used, modified, and distributed by anyone free of charge for any purpose, be it private, commercial, or academic.
