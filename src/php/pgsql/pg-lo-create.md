---
title: pg_lo_create
description: Crea un objeto de gran tamaño de PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-lo-create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-lo-create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 5f1a92089
order: 63340
---

pg_lo_create

Crea un objeto de gran tamaño de PostgreSQL

## Descripción

```php
pg_lo_create([PgSql\Connection $connection], [mixed $object_id]): int
```php

```php
pg_lo_create(mixed $object_id): int
```

`pg_lo_create` crea un objeto de gran tamaño y devuelve su `OID`. Los modos de acceso de PostgreSQL `INV_READ` y `INV_WRITE` no son soportados: el objeto siempre puede ser creado con permisos de lectura y escritura.

Para utilizar un objeto de gran tamaño, es necesario hacerlo dentro de una transacción.

En lugar de utilizar la interfaz de objetos de gran tamaño (que no tiene ningún control de acceso y es engorroso de usar), se recomienda utilizar la columna de tipo `bytea` de PostgreSQL y `pg_escape_bytea`.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_locreate`.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`object_id`  
Si se proporciona el argumento `object_id`, la función intentará crear un objeto grande con este identificador; de lo contrario, se asignará un identificador de objeto disponible por el servidor.

## Valores devueltos

Un objeto grande `OID`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_lo_create`

```php
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

    
```
