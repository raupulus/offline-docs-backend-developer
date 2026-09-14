---
title: pg_field_name
description: Devuelve el nombre de un campo PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-field-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-field-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63150
---

pg_field_name

Devuelve el nombre de un campo PostgreSQL

## Descripción

```php
pg_field_name(PgSql\Result $result, int $field): string
```php

`pg_field_name` devuelve el nombre del campo que ocupa la columna número `field` en el resultado `result`. La numeración de los campos comienza en 0.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_fieldname`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`field`  
Número del campo, comenzando en 0.

## Valores devueltos

El nombre del campo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Obtención de información de los campos

```
<?php
 $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

 $res = pg_query($dbconn, "select * from autores where autor = 'Orwell'");
 $i = pg_num_fields($res);
 for ($j = 0; $j < $i; $j++) {
     echo "columna $j\n";
     $fieldname = pg_field_name($res, $j);
     echo "Campo: $fieldname\n";
     echo "Tamaño mostrado: ".pg_field_prtlen($res, $fieldname)." caracteres\n";
     echo "Tamaño de almacenamiento: ".pg_field_size($res, $j)." bytes\n";
     echo "Tipo de campo: ".pg_field_type($res, $j)." \n\n";
 }
?>

    
```php

El ejemplo anterior mostrará:

    columna 0
    Campo: autor
    Tamaño mostrado: 6 caracteres
    Tamaño de almacenamiento: -1 bytes
    Tipo de campo: varchar

    columna 1
    Campo: año
    Tamaño mostrado: 4 caracteres
    Tamaño de almacenamiento: 2 bytes
    Tipo de campo: int2

    columna 2
    Campo: título
    Tamaño mostrado: 24 caracteres
    Tamaño de almacenamiento: -1 bytes
    Tipo de campo: varchar

## Véase también

`pg_field_num`
