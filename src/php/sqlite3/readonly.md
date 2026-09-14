---
title: SQLite3Stmt::readOnly
description: Determina si una declaración es de solo lectura
source_url: https://www.php.net/manual/es/sqlite3stmt.readonly.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3stmt/readonly.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 86020
---

SQLite3Stmt::readOnly

Determina si una declaración es de solo lectura

## Descripción

```php
public SQLite3Stmt::readOnly(): bool
```php

Determina si una declaración es de solo lectura. Una declaración es considerada de solo lectura si no realiza ningún cambio *directo* al contenido del archivo de la base de datos. Notar que las funciones SQL definidas por el usuario pueden *indirectamente* cambiar la base de datos como efecto secundario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la declaración es de solo lectura, `false` en caso contrario.
