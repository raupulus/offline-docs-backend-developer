---
title: pg_lo_read
description: Lee un objeto de gran tamaño
source_url: https://www.php.net/manual/es/function.pg-lo-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-lo-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63390
---

pg_lo_read

Lee un objeto de gran tamaño

## Descripción

```php
pg_lo_read(PgSql\Lob $lob, [int $length]): string
```php

`pg_lo_read` lee como máximo `length` bytes de un objeto de gran tamaño y devuelve los datos como un string.

Para utilizar un objeto de gran tamaño (`lo`), es necesario hacerlo dentro de una transacción.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_loread`.

## Parámetros

`lob`  
Una instancia `PgSql\Lob`, devuelta por `pg_lo_open`.

`length`  
Un número máximo de bytes a devolver. Este argumento es opcional.

## Valores devueltos

Una `string` que contiene `length` bytes del objeto de gran tamaño o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `lob` ahora espera una instancia de `PgSql\Lob` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_lo_read`

```
<?php
   $doc_oid = 189762345;
   $database = pg_connect("dbname=jacarta");
   pg_query($database, "begin");
   $handle = pg_lo_open($database, $doc_oid, "r");
   $data = pg_lo_read($handle, 50000);
   pg_query($database, "commit");
   echo $data;
?>

    
```php

## Véase también

`pg_lo_read_all`
