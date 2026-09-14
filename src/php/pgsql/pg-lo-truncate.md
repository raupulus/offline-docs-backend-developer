---
title: pg_lo_truncate
description: Trunca un objeto grande
source_url: https://www.php.net/manual/es/function.pg-lo-truncate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-lo-truncate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63420
---

pg_lo_truncate

Trunca un objeto grande

## Descripción

```php
pg_lo_truncate(PgSql\Lob $lob, int $size): bool
```php

`pg_lo_truncate` trunca una instancia `PgSql\Lob`.

Para utilizar la interfaz de objetos grandes, es necesario encerrarla en un bloqueo de transacción.

## Parámetros

`lob`  
Una instancia `PgSql\Lob`, devuelta por `pg_lo_open`.

`size`  
El número de bytes a truncar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `lob` ahora espera una instancia de `PgSql\Lob` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_lo_truncate`

```
<?php
   $doc_oid = 189762345;
   $database = pg_connect("dbname=jacarta");
   pg_query($database, "begin");
   $handle = pg_lo_open($database, $doc_oid, "r");
   // Trunca a 0
   pg_lo_truncate($handle, 0);
   pg_query($database, "commit");
   echo $data;
?>

    
```php

## Véase también

`pg_lo_tell`
