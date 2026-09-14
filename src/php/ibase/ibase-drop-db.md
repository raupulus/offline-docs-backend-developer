---
title: ibase_drop_db
description: Elimina una base de datos iBase
source_url: https://www.php.net/manual/es/function.ibase-drop-db.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-drop-db.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30280
---

ibase_drop_db

Elimina una base de datos iBase

## Descripción

```php
ibase_drop_db([resource $connection]): bool
```php

`ibase_drop_db` elimina una base de datos que ha sido abierta por `ibase_connect` o `ibase_pconnect`. La base de datos es cerrada y eliminada del servidor.

## Parámetros

`connection`  
Un identificador de conexión a InterBase. Si se omite, se utilizará la última conexión abierta.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

ibase_connect

ibase_pconnect
