---
title: pg_field_type
description: Devuelve el tipo de un campo PostgreSQL dado por índice
source_url: https://www.php.net/manual/es/function.pg-field-type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-field-type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63210
---

pg_field_type

Devuelve el tipo de un campo PostgreSQL dado por índice

## Descripción

```php
pg_field_type(PgSql\Result $result, int $field): string
```php

`pg_field_type` devuelve una cadena que contiene el tipo base del campo dado por su índice `field`.

> [!NOTE]
> Si el campo utiliza un dominio PostgreSQL (en lugar de un tipo básico), es el nombre del dominio subyacente el que se devuelve, en lugar del nombre del dominio en sí.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_fieldtype`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`field`  
Número del campo, comenzando en 0.

## Valores devueltos

Una `string` que contiene el nombre base del tipo de campo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Recuperación de información de los campos

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  // Se asume que 'titre' es un tipo varchar
  $res = pg_query($dbconn, "select titre from autores where autor = 'Orwell'");

  echo "Tipo del campo titre : ", pg_field_type($res, 0);
?>

    
```php

El ejemplo anterior mostrará:

    Tipo del campo titre : varchar

## Véase también

`pg_field_prtlen`, `pg_field_name`, `pg_field_type_oid`
