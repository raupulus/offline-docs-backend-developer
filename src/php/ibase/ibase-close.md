---
title: ibase_close
description: Cierra una conexión a una base de datos Interbase
source_url: https://www.php.net/manual/es/function.ibase-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30220
---

ibase_close

Cierra una conexión a una base de datos Interbase

## Descripción

```php
ibase_close([resource $connection_id]): bool
```php

Cierra una conexión a una base de datos Interbase. Esta función toma como argumento el identificador de conexión `connection_id` devuelto por `ibase_connect`. Las transacciones por omisión son validadas y las otras son anuladas.

## Parámetros

`connection_id`  
Un identificador de conexión a InterBase, devuelto por la función `ibase_connect`. Si es omitido, la última conexión abierta será utilizada.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

ibase_connect

ibase_pconnect
