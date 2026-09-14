---
title: pg_lo_import
description: Importa un objeto grande desde un fichero
source_url: https://www.php.net/manual/es/function.pg-lo-import.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-lo-import.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c43a3cd9b
order: 63360
---

pg_lo_import

Importa un objeto grande desde un fichero

## Descripción

```php
pg_lo_import([PgSql\Connection $connection], string $filename, [int $oid]): int
```php

`pg_lo_import` crea un nuevo objeto grande en la base de datos usando un fichero en el sistema de ficheros como fuente de datos.

Para usar la interfaz de objetos grandes, es necesario encerrarla dentro de un bloque de transacción.

> [!NOTE]
> Esta función antes se llamaba `pg_loimport`.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`filename`  
La ruta completa y nombre del fichero en el sistema de ficheros del cliente desde el cual leer los datos del objeto grande.

`oid`  
Si se proporciona un `oid`, la función intentará crear un objeto grande con este ID, de lo contrario, el servidor asignará un ID de objeto libre. Este parámetro depende de funcionalidad que apareció por primera vez en PostgreSQL 8.1.

## Valores devueltos

El `OID` del objeto grande recién creado, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo de `pg_lo_import`

```
<?php
   $database = pg_connect("dbname=jacarta");
   pg_query($database, "begin");
   $oid = pg_lo_import($database, '/tmp/lob.dat');
   pg_query($database, "commit");
?>

    
```php

## Véase también

`pg_lo_export`, `pg_lo_open`
