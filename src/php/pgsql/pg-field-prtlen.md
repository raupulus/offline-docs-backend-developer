---
title: pg_field_prtlen
description: Devuelve el tamaño de impresión
source_url: https://www.php.net/manual/es/function.pg-field-prtlen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-field-prtlen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 39bb8a868
order: 63170
---

pg_field_prtlen

Devuelve el tamaño de impresión

## Descripción

```php
pg_field_prtlen(PgSql\Result $result, string $row, mixed $field_name_or_number): int
```php

```php
pg_field_prtlen(PgSql\Result $result, mixed $field_name_or_number): int
```

`pg_field_prtlen` devuelve el tamaño de impresión (número de caracteres) de un valor dado en un resultado PostgreSQL. La numeración de las líneas comienza en 0. `pg_field_prtlen` devuelve `false` en caso de error.

El parámetro `field_name_or_number` puede ser pasado ya sea como `int` o como `string`. Si es pasado como `int`, PHP lo identifica como el número de un campo, de lo contrario, como el nombre de un campo.

Ver el ejemplo dado en la página de la documentación de la función `pg_field_name`.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_fieldprtlen`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`row`  
Número de la línea en el resultado. Las líneas están numeradas a partir de 0 en adelante. Si este parámetro no es proporcionado, la línea en curso es recuperada.

## Valores devueltos

El número de caracteres impresos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | `row` es ahora nullable. |
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Recuperación de información acerca de los campos

```php
<?php
  $dbconn = pg_connect("dbname=editeur") or die("Conexión imposible");

  $res = pg_query($dbconn, "select * from autores where autor = 'Orwell'");
  $i = pg_num_fields($res);
  for ($j = 0; $j < $i; $j++) {
      echo "columna $j\n";
      $fieldname = pg_field_name($res, $j);
      echo "nombre campo: $fieldname\n";
      echo "tamaño visualización: " . pg_field_prtlen($res, $fieldname) . " caracteres\n";
      echo "tamaño registro: " . pg_field_size($res, $j) . " bytes\n";
      echo "tipo campo: " . pg_field_type($res, $j) . " \n\n";
  }
?>

    
```

El ejemplo anterior mostrará:

    columna 0
    nombre campo: autor
    tamaño visualización: 6 caracteres
    tamaño registro: -1 bytes
    tipo campo: varchar

    columna 1
    nombre campo: año
    tamaño visualización: 4 caracteres
    tamaño registro: 2 bytes
    tipo campo: int2

    columna 2
    nombre campo: título
    tamaño visualización: 24 caracteres
    tamaño registro: -1 bytes
    tipo campo: varchar

## Véase también

`pg_field_size`
