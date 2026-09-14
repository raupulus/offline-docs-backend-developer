---
title: pg_last_error
description: Lee el último mensaje de error en la conexión
source_url: https://www.php.net/manual/es/function.pg-last-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-last-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63300
---

pg_last_error

Lee el último mensaje de error en la conexión

## Descripción

```php
pg_last_error([PgSql\Connection $connection]): string
```php

`pg_last_error` devuelve el último mensaje de error para una conexión `connection`.

Los mensajes de error pueden ser sobrescritos por llamadas internas a la extensión PostgreSQL (libpq): es posible que el mensaje devuelto no sea apropiado, especialmente si han ocurrido múltiples errores en el módulo.

Utilícese `pg_result_error`, `pg_result_error_field`, `pg_result_status` y `pg_connection_status` para mejorar la gestión de errores.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_errormessage`.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`. Cuando `connection` es `null`, se usa la conexión predeterminada. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

## Valores devueltos

Una `string` que contiene el último mensaje de error en la conexión `connection`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `connection` ahora es nullable. |

## Ejemplos

Ejemplo con `pg_last_error`

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  // Consulta que falla
  $res = pg_query($dbconn, "select * from doesnotexist");

  echo pg_last_error($dbconn);
?>

    
```php

## Véase también

`pg_result_error`, `pg_result_error_field`
