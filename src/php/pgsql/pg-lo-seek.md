---
title: pg_lo_seek
description: Modifica la posición en un objeto de gran tamaño
source_url: https://www.php.net/manual/es/function.pg-lo-seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-lo-seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63400
---

pg_lo_seek

Modifica la posición en un objeto de gran tamaño

## Descripción

```php
pg_lo_seek(PgSql\Lob $lob, int $offset, [int $whence]): bool
```php

`pg_lo_seek` modifica la posición del puntero en la instancia `PgSql\Lob`.

Para utilizar un objeto de gran tamaño (`lo`), es necesario hacerlo dentro de una transacción.

## Parámetros

`lob`  
Una instancia `PgSql\Lob`, devuelta por `pg_lo_open`.

`offset`  
El número de bytes de desplazamiento.

`whence`  
Una de estas constantes `PGSQL_SEEK_SET` (posiciona a partir del inicio del objeto), `PGSQL_SEEK_CUR` (posiciona a partir de la posición actual) o `PGSQL_SEEK_END` (posiciona a partir del final del objeto).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `lob` ahora espera una instancia de `PgSql\Lob` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_lo_seek`

```
<?php
   $doc_oid = 189762345;
   $database = pg_connect("dbname=jacarta");
   pg_query($database, "begin");
   $handle = pg_lo_open($database, $doc_oid, "r");
   // Salta los primeros 50000 bytes
   pg_lo_seek($handle, 50000, PGSQL_SEEK_SET);
   // Lee los siguientes 10000 bytes
   $data = pg_lo_read($handle, 10000);
   pg_query($database, "commit");
   echo $data;
?>

    
```php

## Véase también

`pg_lo_tell`
