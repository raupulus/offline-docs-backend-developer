---
title: SQLite3Stmt::__construct
description: Construye un objeto SQLite3Stmt
source_url: https://www.php.net/manual/es/sqlite3stmt.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3stmt/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85980
---

SQLite3Stmt::\_\_construct

Construye un objeto SQLite3Stmt

## Descripción

```php
private SQLite3Stmt::__construct(SQLite3 $sqlite3, string $query)
```php

Las instancias de `SQLite3Stmt` son creadas por SQLite3::prepare.

## Parámetros

`sqlite3`  
El objeto SQLite3 al que pertenece la consulta.

`query`  
La consulta SQL a preparar.
