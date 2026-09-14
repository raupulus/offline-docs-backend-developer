---
title: SQLite3Stmt::execute
description: Ejecuta una consulta preparada
source_url: https://www.php.net/manual/es/sqlite3stmt.execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3stmt/execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85990
---

SQLite3Stmt::execute

Ejecuta una consulta preparada

## Descripción

```php
public SQLite3Stmt::execute(): SQLite3Result
```php

Ejecuta una consulta preparada y devuelve un objeto que representa el conjunto de resultados.

> [!CAUTION]
> Los objetos de conjunto de resultados recuperados mediante la llamada a este método sobre el mismo objeto de instrucción no son independientes, sino que comparten más bien la misma estructura subyacente. Por lo tanto, se recomienda llamar SQLite3Result::finalize, antes de llamar de nuevo SQLite3Stmt::execute sobre el mismo objeto de instrucción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto `SQLite3Result` si la consulta preparada se ha ejecutado con éxito, o `false` si ocurre un error.

## Véase también

SQLite3::prepare

SQLite3Stmt::bindValue

SQLite3Stmt::bindParam
