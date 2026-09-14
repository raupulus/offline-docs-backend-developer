---
title: pg_field_type_oid
description: Devuelve el ID de tipo (OID) para el número de campo correspondiente
source_url: https://www.php.net/manual/es/function.pg-field-type-oid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-field-type-oid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63200
---

pg_field_type_oid

Devuelve el ID de tipo (OID) para el número de campo correspondiente

## Descripción

```php
pg_field_type_oid(PgSql\Result $result, int $field): string
```php

`pg_field_type_oid` devuelve un entero que contiene el OID del tipo base del campo `field` dado en la instancia `result`.

Puede obtenerse más información acerca del tipo de campo consultando la tabla del sistema de PostgreSQL `pg_type` con el OID obtenido por esta función.

> [!NOTE]
> Si el campo utiliza un dominio PostgreSQL (en lugar de un tipo básico), es el OID del dominio subyacente el que se devuelve, en lugar del OID del dominio como tal.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`field`  
Número del campo, comenzando en 0.

## Valores devueltos

El OID del tipo base del campo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Recuperación de información de los campos

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  // Se asume que 'título' es un tipo varchar
  $res = pg_query($dbconn, "select título from autores where autor = 'Orwell'");

  echo "Tipo del campo título OID: ", pg_field_type_oid($res, 0);
?>

    
```php

El ejemplo anterior mostrará:

    Tipo del campo título OID: 1043

## Véase también

`pg_field_type`, `pg_field_prtlen`, `pg_field_name`
