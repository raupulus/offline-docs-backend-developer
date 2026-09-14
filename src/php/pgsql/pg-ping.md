---
title: pg_ping
description: Ping la conexión a la base de datos
source_url: https://www.php.net/manual/es/function.pg-ping.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-ping.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63510
---

pg_ping

Ping la conexión a la base de datos

## Descripción

```php
pg_ping([PgSql\Connection $connection]): bool
```php

`pg_ping` realiza un ping a la conexión a la base de datos y intenta reconectarse si la conexión se ha perdido.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`. Cuando `connection` es `null`, se usa la conexión predeterminada. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `connection` ahora es nullable. |

## Ejemplos

Ejemplo con `pg_ping`

```
<?php
$conn = pg_pconnect ("dbname=publisher");
if (!$conn) {
  echo "Se ha producido un error.\n";
  exit;
}

if (!pg_ping($conn))
  die("La conexión se ha perdido\n");
?>

    
```php

## Véase también

`pg_connection_status`, `pg_connection_reset`
