---
title: SQLite3Result::columnName
description: Devuelve el nombre de una columna
source_url: https://www.php.net/manual/es/sqlite3result.columnname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3result/columnname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85860
---

SQLite3Result::columnName

Devuelve el nombre de una columna

## Descripción

```php
public SQLite3Result::columnName(int $column): string
```php

Devuelve el nombre de la columna identificada por el argumento `column`. Cabe señalar que el nombre de la columna de resultado y el valor de la cláusula `AS` para esta columna, si existe una cláusula `AS`. Si no hay cláusula, el nombre de la columna es no especificado y puede cambiar de una versión de libsqlite3 a otra.

## Parámetros

`column`  
El número de la columna, comenzando desde 0.

## Valores devueltos

Devuelve el nombre de la columna identificada por el argumento `column`, o `false` si la columna no existe.
