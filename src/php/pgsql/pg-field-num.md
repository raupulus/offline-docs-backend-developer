---
title: pg_field_num
description: Devuelve el número de una columna
source_url: https://www.php.net/manual/es/function.pg-field-num.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-field-num.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 6fcf14255
order: 63160
---

pg_field_num

Devuelve el número de una columna

## Descripción

```php
pg_field_num(PgSql\Result $result, string $field): int
```php

`pg_field_num` devuelve el número de la columna, cuyo nombre es `field`, en el resultado `result`.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_fieldnum`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`field`  
El nombre del campo. El nombre dado es tratado como un identificador en un comando SQL, es decir, que se convierte a minúsculas a menos que esté citado dos veces.

## Valores devueltos

El número del campo (comenzando en 0) o -1 en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Obtención de información de los campos

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  $res = pg_query($dbconn, "select autor, año, título from autores where autor = 'Orwell'");

  echo "El número de la columna 'título' es: ", pg_field_num($res, 'título');
?>

    
```php

El ejemplo anterior mostrará:

    El número de la columna 'título' es: 2

## Véase también

`pg_field_name`
