---
title: dbase_pack
description: Compacta una base dBase
source_url: https://www.php.net/manual/es/function.dbase-pack.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dbase/functions/dbase-pack.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dbase
translation_status: ready
translation_revision: 0545e305c
order: 11800
---

dbase_pack

Compacta una base dBase

## Descripción

```php
dbase_pack(resource $database): bool
```php

`dbase_pack` compacta la base de datos `dbase_identifier` (borrado definitivo de todos los registros marcados para el borrado utilizando la función `dbase_delete_record`). Téngase en cuenta que el fichero será truncado después de una compactación exitosa (a diferencia del comando PACK de dBASE III).

## Parámetros

`database`  
El recurso database, devuelto por `dbase_open` o `dbase_create`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión          | Descripción                                             |
|------------------|---------------------------------------------------------|
| PECL dbase 7.0.0 | `database` es ahora un `resource` en lugar de un `int`. |

## Ejemplos

Vacía una base de datos dBase

```
<?php

// Apertura en modo lectura-escritura
$db = dbase_open('/tmp/test.dbf', 2);

if ($db) {
  $record_numbers = dbase_numrecords($db);
  for ($i = 1; $i <= $record_numbers; $i++) {
    dbase_delete_record($db, $i);
  }
// Compacta la base de datos
dbase_pack($db);
}

?>

    
```php

## Véase también

`dbase_delete_record`
