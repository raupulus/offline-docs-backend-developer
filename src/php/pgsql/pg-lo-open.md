---
title: pg_lo_open
description: Abre un objeto de gran tamaño de PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-lo-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-lo-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63370
---

pg_lo_open

Abre un objeto de gran tamaño de PostgreSQL

## Descripción

```php
pg_lo_open(PgSql\Connection $connection, int $oid, string $mode): PgSql\Lob
```php

`pg_lo_open` abre un objeto grande en la base de datos y devuelve una instancia de `PgSql\Lob` para que pueda ser manipulado.

> [!WARNING]
> No cerrar la conexión a la base de datos antes de cerrar la instancia `PgSql\Lob`.

Para utilizar un objeto de gran tamaño (`lo`), es necesario hacerlo dentro de una transacción.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_loopen`.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`oid`  
El `OID` del objeto de gran tamaño en la base de datos.

`mode`  
Puede ser "r" para solo lectura, "w" para solo escritura o "rw" para lectura y escritura.

## Valores devueltos

Una instancia `PgSql\Lob`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `PgSql\Lob`; anteriormente, se devolvía un `resource`. |
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_lo_open`

```
<?php
   $database = pg_connect("dbname=jacarta");
   pg_query($database, "begin");
   $oid = pg_lo_create($database);
   echo "$oid\n";
   $handle = pg_lo_open($database, $oid, "w");
   echo "$handle\n";
   pg_lo_write($handle, "datos de objeto de gran tamaño");
   pg_lo_close($handle);
   pg_query($database, "commit");
?>

    
```php

## Véase también

`pg_lo_close`, `pg_lo_create`
