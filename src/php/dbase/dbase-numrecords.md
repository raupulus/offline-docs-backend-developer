---
title: dbase_numrecords
description: Cuenta el número de registros en una base dBase
source_url: https://www.php.net/manual/es/function.dbase-numrecords.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dbase/functions/dbase-numrecords.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dbase
translation_status: ready
translation_reviewed: false
translation_revision: 0545e305c
order: 11780
---

dbase_numrecords

Cuenta el número de registros en una base dBase

## Descripción

```php
dbase_numrecords(resource $database): int
```php

Recupera el número de registros (filas) en la base especificada.

> [!NOTE]
> Los registros marcados como eliminados también se cuentan.

> [!NOTE]
> Los números de campo están numerados de 0 a `dbase_numfields($db)-1`, mientras que los números de registros están numerados de 1 a `dbase_numrecords($db)`.

## Parámetros

`database`  
Un recurso de base de datos, devuelto por `dbase_open` o `dbase_create`.

## Valores devueltos

El número de registros en la base de datos o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL dbase 7.0.0 | El parámetro `database` es ahora un `resource` en lugar de un `int`. |

## Ejemplos

Lectura de todos los registros de la base de datos

```
<?php

// Apertura en modo de solo lectura
$db = dbase_open('/tmp/test.dbf', 0);

if ($db) {
    $record_numbers = dbase_numrecords($db);
    for ($i = 1; $i <= $record_numbers; $i++) {
        $record = dbase_get_record($db, $i);
        if (!$record['deleted']) {
            // hacer algo con el registro $record
        } else {
            // hacer algo con el registro eliminado $record o ignorarlo
        }
    }
}

?>

    
```php

## Véase también

`dbase_numfields`
