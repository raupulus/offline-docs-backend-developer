---
title: pg_field_size
description: Devuelve el tamaño interno de almacenamiento de un campo dado
source_url: https://www.php.net/manual/es/function.pg-field-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-field-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63180
---

pg_field_size

Devuelve el tamaño interno de almacenamiento de un campo dado

## Descripción

```php
pg_field_size(PgSql\Result $result, int $field): int
```php

`pg_field_size` devuelve el tamaño interno de almacenamiento de un campo dado, en bytes.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_fieldsize`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`field`  
Número del campo, comenzando en 0.

## Valores devueltos

El tamaño del almacenamiento interno de un campo (en bytes). -1 significa un campo de tamaño variable.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Recuperación de información de los campos

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  $res = pg_query($dbconn, "select * from autores where autor = 'Orwell'");
  $i = pg_num_fields($res);
  for ($j = 0; $j < $i; $j++) {
      echo "columna $j\n";
      $fieldname = pg_field_name($res, $j);
      echo "Nombre del campo: $fieldname\n";
      echo "Tamaño para la visualización: " . pg_field_prtlen($res, $fieldname) . " caracteres\n";
      echo "Tamaño para el almacenamiento: " . pg_field_size($res, $j) . " bytes\n";
      echo "Tipo del campo: " . pg_field_type($res, $j) . " \n\n";
  }
?>

    
```php

El ejemplo anterior mostrará:

    columna 0
    Nombre del campo: autor
    Tamaño para la visualización: 6 caracteres
    Tamaño para el almacenamiento: -1 bytes
    Tipo del campo: varchar

    columna 1
    Nombre del campo: año
    Tamaño para la visualización: 4 caracteres
    Tamaño para el almacenamiento: 2 bytes
    Tipo del campo: int2

    columna 2
    Nombre del campo: título
    Tamaño para la visualización: 24 caracteres
    Tamaño para el almacenamiento: -1 bytes
    Tipo del campo: varchar

## Véase también

`pg_field_prtlen`, `pg_field_type`
