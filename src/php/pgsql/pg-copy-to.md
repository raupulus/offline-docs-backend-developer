---
title: pg_copy_to
description: Copia una tabla en un array
source_url: https://www.php.net/manual/es/function.pg-copy-to.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-copy-to.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 62980
---

pg_copy_to

Copia una tabla en un array

## Descripción

```php
pg_copy_to(PgSql\Connection $connection, string $table_name, [string $separator], [string $null_as]): array
```php

`pg_copy_to` copia la tabla `table_name` en un array. Esta función utiliza el comando interno SQL `COPY TO` para insertar los arrays.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`table_name`  
Nombre de la tabla a partir de la cual los datos en `rows` serán copiados.

`separator`  
El marcador que separa los valores para cada campo en cada elemento de `rows`. Por omisión `\t`.

`null_as`  
Cómo las valores `NULL` de SQL son representados en `rows`. Por omisión `\\N` (`"\\\\N"`).

## Valores devueltos

Un `array` con un elemento para cada línea de datos `COPY`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_copy_to`

```
<?php
   $db = pg_connect("dbname=publisher") or die("Conexión imposible");

   $rows = pg_copy_to($db, $table_name);

   pg_query($db, "DELETE FROM $table_name");

   pg_copy_from($db, $table_name, $rows);
?>

    
```php

## Véase también

`pg_copy_from`
