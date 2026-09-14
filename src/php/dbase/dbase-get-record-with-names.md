---
title: dbase_get_record_with_names
description: Lee un registro en una base dBase, en forma de array asociativo
source_url: https://www.php.net/manual/es/function.dbase-get-record-with-names.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dbase/functions/dbase-get-record-with-names.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dbase
translation_status: ready
translation_revision: 0545e305c
order: 11750
---

dbase_get_record_with_names

Lee un registro en una base dBase, en forma de array asociativo

## Descripción

```php
dbase_get_record_with_names(resource $database, int $number): array
```php

Recupera un registro de una base de datos dBase como un array asociativo.

## Parámetros

`database`  
El recurso de base de datos, devuelto por `dbase_open` o `dbase_create`.

`number`  
El índice del registro entre `1` y `dbase_numrecords($dbase_identifier)`.

## Valores devueltos

El registro, en forma de array asociativo. Esto incluye también una clave llamada `deleted` que se define a 1 si el registro ha sido marcado para eliminación (ver la función `dbase_delete_record`). Por consiguiente, no es posible recuperar el valor de un campo llamado `deleted` con esta función.

Cada campo se convierte al tipo PHP apropiado, excepto:

- Las fechas se mantienen como cadenas.

- Los valores DateTime se convierten en cadenas.

- Los enteros fuera del rango `PHP_INT_MIN`..`PHP_INT_MAX` se devuelven como cadenas.

- Antes de dbase 7.0.0, los booleanos (`L`) se convertían en `1` o `0`.

En caso de error, `dbase_get_record_with_names` devuelve `false`.

## Historial de cambios

| Versión          | Descripción                                             |
|------------------|---------------------------------------------------------|
| PECl dbase 7.0.0 | `database` es ahora un `resource` en lugar de un `int`. |

## Ejemplos

Lista todos los miembros registrados en la base de datos

```
<?php
// Apertura en modo solo lectura
$db = dbase_open('/tmp/test.dbf', 0);

if ($db) {
  $record_numbers = dbase_numrecords($db);
  for ($i = 1; $i <= $record_numbers; $i++) {
    $row = dbase_get_record_with_names($db, $i);
    if ($row['ismember'] == 1) {
      echo "Miembro #$i: " . trim($row['name']) . "\n";
    }
  }
}
?>

    
```php

## Véase también

`dbase_get_record`
