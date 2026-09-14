---
title: pg_port
description: Devuelve el número de puerto
source_url: https://www.php.net/manual/es/function.pg-port.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-port.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63520
---

pg_port

Devuelve el número de puerto

## Descripción

```php
pg_port([PgSql\Connection $connection]): string
```php

`pg_port` devuelve el número de puerto de la conexión dada por `connection`.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`. Cuando `connection` es `null`, se usa la conexión predeterminada. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

## Valores devueltos

Una `string` que contiene el número de puerto del servidor de base de datos identificado por `connection` o una cadena vacía en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `connection` ahora es nullable. |

## Ejemplos

Ejemplo con `pg_port`

```
<?php
$pgsql_conn = pg_connect("dbname=mark host=localhost");

if ($pgsql_conn) {
   print "Conectado correctamente al puerto : " . pg_port($pgsql_conn) . "<br/>\n";
} else {
   print pg_last_error($pgsql_conn);
   exit;
}
?>

    
```php
