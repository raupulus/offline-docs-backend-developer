---
title: dbase_add_record
description: Añade un registro en una base de datos dBase
source_url: https://www.php.net/manual/es/function.dbase-add-record.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dbase/functions/dbase-add-record.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dbase
translation_status: ready
translation_revision: 0545e305c
order: 11700
---

dbase_add_record

Añade un registro en una base de datos dBase

## Descripción

```php
dbase_add_record(resource $database, array $data): bool
```php

`dbase_add_record` añade los datos proporcionados en la base de datos dBase especificada.

## Parámetros

`database`  
El recurso de base de datos, devuelto por `dbase_open` o `dbase_create`.

`data`  
Un array de datos indexado. El número de elementos debe ser igual al número de campos en la base de datos, de lo contrario la función `dbase_add_record` fallará.

> [!NOTE]
> Si se utiliza `dbase_get_record` para devolver un valor para este argumento, no se olvide de reinicializar la clave nombrada `deleted`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión          | Descripción                                             |
|------------------|---------------------------------------------------------|
| PECL dbase 7.0.0 | `database` es ahora un `resource` en lugar de un `int`. |

## Ejemplos

Inserción de un registro en una base de datos dBase

```
<?php

// Apertura en modo lectura-escritura
$db = dbase_open('/tmp/test.dbf', 2);

if ($db) {
  dbase_add_record($db, array(
    date('Ymd'),
    'Maxim Topolov',
    '23',
    'max@example.com',
    'T'));
  dbase_close($db);
}

?>

    
```php

## Véase también

`dbase_delete_record`, `dbase_replace_record`
