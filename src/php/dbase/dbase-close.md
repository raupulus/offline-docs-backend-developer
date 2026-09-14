---
title: dbase_close
description: Cierra una base dBase
source_url: https://www.php.net/manual/es/function.dbase-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dbase/functions/dbase-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dbase
translation_status: ready
translation_revision: 0545e305c
order: 11710
---

dbase_close

Cierra una base dBase

## Descripción

```php
dbase_close(resource $database): bool
```php

`dbase_close` cierra la base de datos correspondiente al recurso `database`.

## Parámetros

`database`  
El recurso de base de datos, devuelto por `dbase_open` o `dbase_create`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión          | Descripción                                             |
|------------------|---------------------------------------------------------|
| PECL dbase 7.0.0 | `database` es ahora un `resource` en lugar de un `int`. |

## Ejemplos

Cierra un fichero de base de datos dBase

```
<?php

// Apertura en modo lectura-escritura
$db = dbase_open('/tmp/test.dbf', 0);

if ($db) {
// Lectura de datos ..

dbase_close($db);
}

?>

    
```php

## Véase también

`dbase_open`, `dbase_create`
