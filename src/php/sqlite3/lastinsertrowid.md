---
title: SQLite3::lastInsertRowID
description: Devuelve el identificador de la fila correspondiente a la última consulta
  de tipo INSERT
source_url: https://www.php.net/manual/es/sqlite3.lastinsertrowid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/lastinsertrowid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85750
---

SQLite3::lastInsertRowID

Devuelve el identificador de la fila correspondiente a la última consulta de tipo INSERT

## Descripción

```php
public SQLite3::lastInsertRowID(): int
```php

Devuelve el identificador de la fila correspondiente a la última consulta de tipo INSERT ejecutada en la base de datos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el identificador de la fila correspondiente a la última consulta de tipo INSERT ejecutada en la base de datos. Si ninguna consulta de tipo INSERT en las tablas rowid ha tenido éxito en esta conexión de base de datos, entonces SQLite3::lastInsertRowID devuelve `0`.
