---
title: dbase_replace_record
description: Reemplaza un registro en una base dBase
source_url: https://www.php.net/manual/es/function.dbase-replace-record.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dbase/functions/dbase-replace-record.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dbase
translation_status: ready
translation_revision: 0545e305c
order: 11810
---

dbase_replace_record

Reemplaza un registro en una base dBase

## Descripción

```php
dbase_replace_record(resource $database, array $data, int $number): bool
```php

Reemplaza el registro pasado en la base de datos con los datos proporcionados.

## Parámetros

`database`  
El recurso de la base de datos, devuelto por `dbase_open` o `dbase_create`.

`data`  
Un array indexado de datos. El número de elementos debe ser igual al número de campos en la base de datos, de lo contrario la función `dbase_replace_record` fallará.

> [!NOTE]
> Si se utiliza `dbase_get_record` para devolver el valor de este argumento, no se olvide de reinicializar la clave nombrada `deleted`.

`number`  
Un entero entre 1 y el número total de registros en la base de datos (como devuelto por la función `dbase_numrecords`).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL dbase 7.0.0 | El argumento `database` es ahora una `resource` en lugar de un `int`. |

## Ejemplos

Actualización de un registro en una base de datos

```
<?php

// Apertura en modo lectura-escritura
$db = dbase_open('/tmp/test.dbf', 2);

if ($db) {
  // Recuperación de la antigua fila
  $row = dbase_get_record_with_names($db, 1);

  // Elimina la entrada borrada
  unset($row['deleted']);

  // Actualización de la fecha del campo con el timestamp actual
  $row['date'] = date('Ymd');

  // Reemplazar el registro
  dbase_replace_record($db, $row, 1);
  dbase_close($db);
}

?>

    
```php

## Notas

> [!NOTE]
> Los resultados de los campos `bool` son elementos de valor de tipo `int` (`0` o `1`) cuando se recuperan mediante `dbase_get_record` o `dbase_get_record_with_names`. Si se reescriben, esto hará que el valor se convierta en `0`, por lo que se deben tomar precauciones para ajustar correctamente los valores.

## Véase también

`dbase_add_record`, `dbase_delete_record`
