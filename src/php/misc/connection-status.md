---
title: connection_status
description: Devuelve los bits de estado de la conexión HTTP
source_url: https://www.php.net/manual/es/function.connection-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/connection-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: d05c9017a
order: 47010
---

connection_status

Devuelve los bits de estado de la conexión HTTP

## Descripción

```php
connection_status(): int
```php

Devuelve los bits de estado de la conexión HTTP.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve los bits de estado de la conexión, que pueden ser utilizados con las constantes [`CONNECTION_*`](#misc.constants) para determinar el estado de la conexión.

## Véase también

`connection_aborted`, `ignore_user_abort`, [Gestor de conexión](#features.connection-handling) para una descripción completa del gestor de conexión en PHP.
