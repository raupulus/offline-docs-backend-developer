---
title: SQLite3::busyTimeout
description: Define el gestor de espera de la conexión
source_url: https://www.php.net/manual/es/sqlite3.busytimeout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/busyTimeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85630
---

SQLite3::busyTimeout

Define el gestor de espera de la conexión

## Descripción

```php
public SQLite3::busyTimeout(int $milliseconds): bool
```php

Define el gestor de espera que aguardará hasta que la base de datos no esté bloqueada o hasta que se alcance el tiempo límite.

## Parámetros

`milliseconds`  
Los milisegundos a esperar. Establecer este valor a cero o a un valor inferior desactivará un gestor de espera previamente definido.

## Valores devueltos

Devuelve `true` en caso de éxito, o `false` si ocurre un error.
