---
title: pg_version
description: Devuelve un array con las versiones del cliente, del protocolo y del
  servidor (si está disponible)
source_url: https://www.php.net/manual/es/function.pg-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 5f1a92089
order: 63810
---

pg_version

Devuelve un array con las versiones del cliente, del protocolo y del servidor (si está disponible)

## Descripción

```php
pg_version([PgSql\Connection $connection]): array
```php

`pg_version` devuelve un array con las versiones del cliente, del protocolo y del servidor.

Para obtener más información sobre el servidor, utilice `pg_parameter_status`.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`. Cuando `connection` es `null`, se usa la conexión predeterminada. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

## Valores devueltos

Devuelve un array con las claves `client`, `protocol` y `server` y valores (si están disponibles).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `connection` ahora es nullable. |

## Ejemplos

Ejemplo con `pg_version`

```
<?php
$dbconn = pg_connect("host=localhost port=5432 dbname=marie")
   or die("Conexión imposible");

$v = pg_version($dbconn);

echo $v['client'];
?>

    
```php

El ejemplo anterior mostrará:

    7.4

## Véase también

`pg_parameter_status`
