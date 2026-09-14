---
title: pg_lo_write
description: Escribe un objeto de gran tamaño de PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-lo-write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-lo-write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63440
---

pg_lo_write

Escribe un objeto de gran tamaño de PostgreSQL

## Descripción

```php
pg_lo_write(PgSql\Lob $lob, string $data, [int $length]): int
```php

`pg_lo_write` escribe datos dentro de un objeto de gran tamaño en la posición actual.

Para manipular un objeto de gran tamaño (`lo`), es necesario colocar las operaciones dentro de un bloque de transacción.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_lowrite`.

## Parámetros

`lob`  
Una instancia `PgSql\Lob`, devuelta por `pg_lo_open`.

`data`  
Los datos a ser escritos en el objeto de gran tamaño. Si `length` es un `int` y es inferior al tamaño de `data`, solo los primeros `length` bytes serán escritos.

`length`  
Un número máximo de bytes a escribir. Debe ser superior a cero y menor al tamaño de `data`. Este argumento es opcional; si se omite, tomará por defecto el tamaño de `data`.

## Valores devueltos

El número de bytes escritos en el objeto de gran tamaño o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `lob` ahora espera una instancia de `PgSql\Lob` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `connection` es ahora nullable. |

## Ejemplos

Ejemplo con `pg_lo_write`

```
<?php
   $doc_oid = 189762345;
   $data = "Esto sobrescribirá el inicio del objeto de gran tamaño.";
   $database = pg_connect("dbname=jacarta");
   pg_query($database, "begin");
   $handle = pg_lo_open($database, $doc_oid, "w");
   $data = pg_lo_write($handle, $data);
   pg_query($database, "commit");
?>

    
```php

## Véase también

`pg_lo_create`, `pg_lo_open`
