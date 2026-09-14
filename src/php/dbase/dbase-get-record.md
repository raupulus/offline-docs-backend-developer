---
title: dbase_get_record
description: Lee un registro en una base dBase
source_url: https://www.php.net/manual/es/function.dbase-get-record.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dbase/functions/dbase-get-record.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dbase
translation_status: ready
translation_revision: 0545e305c
order: 11760
---

dbase_get_record

Lee un registro en una base dBase

## Descripción

```php
dbase_get_record(resource $database, int $number): array
```php

`dbase_get_record` devuelve los datos del registro `record` en un array.

## Parámetros

`database`  
El recurso de la base de datos, devuelto por `dbase_open` o `dbase_create`.

`number`  
El índice del registro entre `1` y `dbase_numrecords($dbase_identifier)`.

## Valores devueltos

Un array indexado con el registro. Este array incluye asimismo una clave asociada llamada `deleted` que se define a 1 si el registro ha sido marcado para eliminación (ver `dbase_delete_record`).

Cada campo se convierte al tipo PHP apropiado, excepto:

- Las fechas se mantienen como cadenas.

- Los valores DateTime se convierten en cadenas.

- Los enteros fuera del rango `PHP_INT_MIN`..`PHP_INT_MAX` se devuelven como cadenas.

- Antes de dbase 7.0.0, los booleanos (`L`) se convertían en `1` o `0`.

En caso de error, `dbase_get_record` devuelve `false`.

## Historial de cambios

| Versión          | Descripción                                             |
|------------------|---------------------------------------------------------|
| PECL dbase 7.0.0 | `database` es ahora un `resource` en lugar de un `int`. |

## Véase también

`dbase_get_record_with_names`
