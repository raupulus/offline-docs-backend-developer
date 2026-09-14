---
title: pg_parameter_status
description: Consulta un parámetro de configuración actual del servidor
source_url: https://www.php.net/manual/es/function.pg-parameter-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-parameter-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c43a3cd9b
order: 63490
---

pg_parameter_status

Consulta un parámetro de configuración actual del servidor

## Descripción

```php
pg_parameter_status([PgSql\Connection $connection], string $name): string
```php

Consulta un parámetro de configuración actual del servidor.

Ciertos valores de parámetros son devueltos por el servidor automáticamente al inicio de la conexión o cuando un valor cambia. `pg_parameter_status` puede ser utilizada para consultar estas configuraciones. La función devuelve el valor actual del parámetro si es conocido o `false` si el parámetro es desconocido.

Los parámetros devueltos por el servidor son `server_version`, `server_encoding`, `client_encoding`, `is_superuser`, `session_authorization`, `DateStyle`, `TimeZone` y `integer_datetimes`. Tenga en cuenta que `server_version`, `server_encoding` y `integer_datetimes` no pueden cambiar después del inicio de PostgreSQL.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`name`  
Los valores posibles de `name` son `server_version`, `server_encoding`, `client_encoding`, `is_superuser`, `session_authorization`, `DateStyle`, `TimeZone` y `integer_datetimes`. Cabe señalar que este valor es sensible a mayúsculas y minúsculas.

## Valores devueltos

Una `string` que contiene el valor del parámetro, `false` en caso de fallo o si el parámetro `name` es inválido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_parameter_status`

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  echo "Codificación del servidor: ", pg_parameter_status($dbconn, "server_encoding");
?>

    
```php

El ejemplo anterior mostrará:

    Codificación del servidor: SQL_ASCII
