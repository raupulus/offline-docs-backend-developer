---
title: dbase_delete_record
description: Borra un registro en una base dBase
source_url: https://www.php.net/manual/es/function.dbase-delete-record.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dbase/functions/dbase-delete-record.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dbase
translation_status: ready
translation_revision: 0545e305c
order: 11730
---

dbase_delete_record

Borra un registro en una base dBase

## Descripción

```php
dbase_delete_record(resource $database, int $number): bool
```php

`dbase_delete_record` marca el registro `record` para el borrado, en la base `dbase_identifier`.

> [!NOTE]
> Para borrar realmente el registro de la base de datos, se debe llamar a la función `dbase_pack`.

## Parámetros

`database`  
El recurso de base de datos, devuelto por `dbase_open` o `dbase_create`.

`number`  
Un entero comprendido entre 1 y el número máximo de registros en la base de datos (tal como devuelto por la función `dbase_numrecords`).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión          | Descripción                                             |
|------------------|---------------------------------------------------------|
| PECL dbase 7.0.0 | `database` es ahora un `resource` en lugar de un `int`. |

## Véase también

`dbase_add_record`, `dbase_replace_record`
