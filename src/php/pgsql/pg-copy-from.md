---
title: pg_copy_from
description: Inserta filas en una tabla a partir de un array
source_url: https://www.php.net/manual/es/function.pg-copy-from.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-copy-from.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: aa120f36c
order: 62970
---

pg_copy_from

Inserta filas en una tabla a partir de un array

## Descripción

```php
pg_copy_from(PgSql\Connection $connection, string $table_name, array $rows, [string $separator], [string $null_as]): bool
```php

`pg_copy_from` inserta los elementos del array `rows` en una tabla. Esta función utiliza la orden SQL interna `COPY FROM`.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`table_name`  
Nombre de la tabla en la que `rows` será copiado.

`rows`  
Datos `iterable` a ser copiados dentro de `table_name`. Cada valor en `rows` se convierte en una fila en `table_name`. Cada valor en `rows` debería ser una cadena delimitada por valores a insertar dentro de cada campo. Los valores deben terminar con un salto de línea.

`separator`  
El marcador que separa los valores para cada campo en cada elemento de `rows`. Por omisión `\t`.

`null_as`  
Cómo se representan los valores `NULL` de SQL en `rows`. Por omisión `\\N` (`"\\\\N"`).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | `rows` es ahora de tipo `iterable`. Anteriormente, era de tipo `array`. |
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_copy_from`

```
<?php
   $db = pg_connect("dbname=publisher") or die("Conexión imposible");

   $rows = pg_copy_to($db, $table_name);

   pg_query($db, "DELETE FROM $table_name");

   pg_copy_from($db, $table_name, $rows);
?>

    
```php

## Véase también

`pg_copy_to`
