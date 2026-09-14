---
title: SQLite3Stmt::clear
description: Elimina todos los parámetros actualmente vinculados
source_url: https://www.php.net/manual/es/sqlite3stmt.clear.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3stmt/clear.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85960
---

SQLite3Stmt::clear

Elimina todos los parámetros actualmente vinculados

## Descripción

```php
public SQLite3Stmt::clear(): bool
```php

Elimina todos los parámetros actualmente vinculados (los define como `null`).

> [!CAUTION]
> Este método debe ser utilizado con SQLite3Stmt::reset. Si se utiliza solo, cualquier llamada a SQLite3Stmt::bindValue o SQLite3Stmt::bindParam no tendrá efecto y todos los parámetros vinculados tendrán como valor `null`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si todos los parámetros actualmente vinculados han sido eliminados, `false` si ocurre un error.
