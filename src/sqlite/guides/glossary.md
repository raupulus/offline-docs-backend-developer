---
title: Terms of Art Glossary
source_url: https://www.sqlite.org/glossary.html
source_path: glossary.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 2980
---

This page contains a glossary of terms of art which appear, but are not defined, throughout this project's documentation. This page is *not* a tutorial, just a summary, and many related terms of art are not listed here. Countless web-hosted resources exist which cover, in detail, all of the terminology listed here. Interested readers are encouraged to feed these terms to their internet search engine of choice.

In alphabetical order:

- **DDL: Data Definition Language** is the subset of SQL related to maintenance of database tables: `CREATE`, `DROP`, `ALTER`, etc.
- **DML: Data Manipulation Language** is the subset of SQL related to manipulating the contents of tables: `INSERT`, `UPDATE`, `DELETE`, etc.
- **DQL: Data Query Language** is the subset of SQL related to fetching results, i.e. `SELECT`. Whether `INSERT...RETURNING` also qualifies as DQL is a question left to those who define these terms formally.
- **TCL: Transaction Control Language** is the subset of SQL involving transactions: `BEGIN`, `COMMIT`, `ROLLBACK`, etc.
- **Relational Theory** is, in this context, the area of study from which SQL is derived. SQL does not, for reasons of practically, strictly conform to relational theory, but it's a close approximation.
- **SQL: Structured Query Language** is the primary interface between a database and its users. It encompasses DDL, DML, DQL, and TCL (see above).
