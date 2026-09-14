---
title: SQLite3Stmt::reset
description: Reinicia una consulta preparada
source_url: https://www.php.net/manual/es/sqlite3stmt.reset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3stmt/reset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 86030
---

SQLite3Stmt::reset

Reinicia una consulta preparada

## Descripción

```php
public SQLite3Stmt::reset(): bool
```php

Reinicia una consulta preparada, de tal manera que se recupera su estado inicial, antes de la ejecución. Todos los marcadores permanecerán intactos después de esta operación.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la consulta preparada ha sido correctamente reiniciada, o `false` si ocurre un error.
