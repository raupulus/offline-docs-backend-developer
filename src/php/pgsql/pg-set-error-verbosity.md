---
title: pg_set_error_verbosity
description: Determina el nivel de detalle de los mensajes devueltos por pg_last_error
  y pg_result_error
source_url: https://www.php.net/manual/es/function.pg-set-error-verbosity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-set-error-verbosity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c43a3cd9b
order: 63720
---

pg_set_error_verbosity

Determina el nivel de detalle de los mensajes devueltos por

pg_last_error

y

pg_result_error

## Descripción

```php
pg_set_error_verbosity([PgSql\Connection $connection], int $verbosity): int
```php

Determina el nivel de detalle de los mensajes devueltos por `pg_last_error` y `pg_result_error`.

`pg_set_error_verbosity` establece el nivel de detalle de los errores y devuelve el parámetro anterior de la conexión. Con el modo `PGSQL_ERRORS_TERSE`, los mensajes devueltos incluyen la severidad, el texto principal y la posición solamente; normalmente, esto cabrá en una sola línea. El modo por defecto (`PGSQL_ERRORS_DEFAULT`) produce mensajes que incluyen los mensajes anteriores y detalles, sugerencias o campos contextuales (estos mensajes pueden extenderse en varias líneas). El modo `PGSQL_ERRORS_VERBOSE` incluye todos los campos disponibles. El cambio del nivel de detalle de los mensajes no afecta a los mensajes disponibles que provienen de resultados ya existentes, sino solo a los mensajes de los resultados creados posteriormente.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`verbosity`  
El nivel de detalle del mensaje de error: `PGSQL_ERRORS_TERSE`, `PGSQL_ERRORS_DEFAULT` o `PGSQL_ERRORS_VERBOSE`.

## Valores devueltos

El nivel de detalle del mensaje de error anterior: `PGSQL_ERRORS_TERSE`, `PGSQL_ERRORS_DEFAULT` o `PGSQL_ERRORS_VERBOSE`, o `false` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_set_error_verbosity`

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  if (!pg_connection_busy($dbconn)) {
      pg_send_query($dbconn, "select * from nexistepas;");
  }

  pg_set_error_verbosity($dbconn, PGSQL_ERRORS_VERBOSE);
  $res1 = pg_get_result($dbconn);
  echo pg_result_error($res1);
?>

    
```php

## Véase también

`pg_last_error`, `pg_result_error`
