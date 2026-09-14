---
title: pg_lo_read_all
description: Lee un objeto de gran tamaño en su totalidad
source_url: https://www.php.net/manual/es/function.pg-lo-read-all.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-lo-read-all.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63380
---

pg_lo_read_all

Lee un objeto de gran tamaño en su totalidad

## Descripción

```php
pg_lo_read_all(PgSql\Lob $lob): int
```php

`pg_lo_read_all` lee un objeto de gran tamaño en su totalidad y lo envía directamente al cliente, después de los encabezados adecuados. Esta función está prevista para transmitir sonidos o imágenes.

Para utilizar un objeto de gran tamaño (`lo`), es necesario hacerlo dentro de una transacción.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_loreadall`.

## Parámetros

`lob`  
Una instancia `PgSql\Lob`, devuelta por `pg_lo_open`.

## Valores devueltos

Número de bytes leídos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `lob` ahora espera una instancia de `PgSql\Lob` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_lo_read_all`

```
<?php
   header('Content-type: image/jpeg');
   $image_oid = 189762345;
   $database = pg_connect("dbname=jacarta");
   pg_query($database, "begin");
   $handle = pg_lo_open($database, $image_oid, "r");
   pg_lo_read_all($handle);
   pg_query($database, "commit");
?>

    
```php

## Véase también

`pg_lo_read`
