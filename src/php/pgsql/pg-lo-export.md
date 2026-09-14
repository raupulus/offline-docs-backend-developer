---
title: pg_lo_export
description: Exporta un objeto grande a un fichero
source_url: https://www.php.net/manual/es/function.pg-lo-export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-lo-export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c43a3cd9b
order: 63350
---

pg_lo_export

Exporta un objeto grande a un fichero

## Descripción

```php
pg_lo_export([PgSql\Connection $connection], int $oid, string $filename): bool
```php

`pg_lo_export` toma un objeto grande de la base de datos PostgreSQL y guarda su contenido en un fichero local en el sistema.

Para utilizar un objeto grande (`lo`), es necesario hacerlo dentro de una transacción.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_loexport`.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`oid`  
El `OID` del objeto grande en la base de datos.

`filename`  
La ruta de acceso completa y el fichero en el que se escribirá el objeto grande en el sistema del cliente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_lo_export`

```
<?php
   $database = pg_connect("dbname=jacarta");
   pg_query($database, "begin");
   $oid = pg_lo_create($database);
   $handle = pg_lo_open($database, $oid, "w");
   pg_lo_write($handle, "datos objeto grande");
   pg_lo_close($handle);
   pg_lo_export($database, $oid, '/tmp/lob.dat');
   pg_query($database, "commit");
?>

    
```php

## Véase también

`pg_lo_import`
