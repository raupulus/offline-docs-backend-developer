---
title: pg_lo_tell
description: Devuelve la posición actual en un objeto grande de PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-lo-tell.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-lo-tell.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63410
---

pg_lo_tell

Devuelve la posición actual en un objeto grande de PostgreSQL

## Descripción

```php
pg_lo_tell(PgSql\Lob $lob): int
```php

`pg_lo_tell` devuelve la posición actual (desde el inicio) del puntero de lectura en el objeto grande `large_object`.

Para utilizar una interfaz con un objeto grande, es necesario incluirlo en un bloque de transacción.

## Parámetros

`lob`  
Una instancia `PgSql\Lob`, devuelta por `pg_lo_open`.

## Valores devueltos

La posición actual del puntero (en número de bytes) desde el inicio del objeto grande. Si hay un error, el valor devuelto será negativo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `lob` ahora espera una instancia de `PgSql\Lob` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_lo_tell`

```
<?php
   $doc_oid = 189762345;
   $database = pg_connect("dbname=jacarta");
   pg_query($database, "begin");
   $handle = pg_lo_open($database, $doc_oid, "r");
   // Salta los primeros 50000 bytes
   pg_lo_seek($handle, 50000, PGSQL_SEEK_SET);
   // Se verifica cuántos bytes se han saltado
   $offset = pg_lo_tell($handle);
   echo "La posición del puntero es: $offset";
   pg_query($database, "commit");
?>

    
```php

El ejemplo anterior mostrará:

    La posición del puntero es: 50000

## Véase también

`pg_lo_seek`
