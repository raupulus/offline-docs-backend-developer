---
title: SQLite3Result::columnType
description: Devuelve el tipo de una columna
source_url: https://www.php.net/manual/es/sqlite3result.columntype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3result/columntype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: true
translation_revision: 855bfee2f
order: 85870
---

SQLite3Result::columnType

Devuelve el tipo de una columna

## Descripción

```php
public SQLite3Result::columnType(int $column): int
```php

Devuelve el tipo de la columna identificada por el argumento `column`.

## Parámetros

`column`  
El número de la columna, comenzando por 0.

## Valores devueltos

Devuelve el tipo de datos de la columna identificada por `column` (uno de `SQLITE3_INTEGER`, `SQLITE3_FLOAT`, `SQLITE3_TEXT`, `SQLITE3_BLOB`, o `SQLITE3_NULL`), o `false` si la columna no existe.
