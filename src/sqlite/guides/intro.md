---
title: Introduction
source_url: https://www.sqlite.org/session/intro.html
source_path: session/intro.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6710
---

These pages define the C-language interface for the SQLite [session extension](../sessionintro.md). This is not a tutorial. These pages are designed to be precise, not easy to read. A tutorial is [available separately](../sessionintro.md).

This version of the C-language interface reference is broken down into small pages for easy viewing. The same content is also available as a [single large HTML file](../session.md) for those who prefer that format.

The content on these pages is extracted from comments in the source code.

The interface is broken down into three categories:

1.  [**List Of Objects.**](../session/objlist.md) This is a list of the three abstract objects used by the SQLite session module.

2.  [**List Of Constants.**](../session/constlist.md) This is a list of numeric constants used by the SQLite session module and represented by \#defines in the sqlite3session.h header file. There are constants passed to conflict handler callbacks to indicate the type of conflict, and constants returned by the conflict handler to indicate how the conflict should be resolved.

3.  [**List Of Functions.**](../session/funclist.md) This is a list of all SQLite session module functions.
