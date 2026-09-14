---
title: connection_aborted
description: Indica si el usuario ha abandonado la conexión HTTP
source_url: https://www.php.net/manual/es/function.connection-aborted.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/connection-aborted.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 4411b371d
order: 47000
---

connection_aborted

Indica si el usuario ha abandonado la conexión HTTP

## Descripción

```php
connection_aborted(): int
```php

Indica si el usuario ha abandonado la conexión HTTP.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve 1 si el cliente está desconectado, 0 en caso contrario.

## Véase también

`connection_status`, `ignore_user_abort`, [Gestor de conexión](#features.connection-handling) para una descripción completa del gestor de conexión en PHP.
