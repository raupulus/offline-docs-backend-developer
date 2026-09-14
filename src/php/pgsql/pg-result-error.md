---
title: pg_result_error
description: Lee el mensaje de error asociado a un resultado
source_url: https://www.php.net/manual/es/function.pg-result-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-result-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63600
---

pg_result_error

Lee el mensaje de error asociado a un resultado

## Descripción

```php
pg_result_error(PgSql\Result $result): string
```php

`pg_result_error` devuelve el mensaje de error asociado al resultado `result`. Por consiguiente, es probable que se obtenga un mensaje de error más apropiado que mediante `pg_last_error`.

La función `pg_result_error_field` puede proporcionar muchos más detalles sobre los errores que `pg_result_error`.

Dado que `pg_query` devuelve `false` si la consulta falla, se debe utilizar `pg_send_query` y `pg_get_result` para recuperar el recurso de resultado.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

## Valores devueltos

Devuelve un `string`. Devuelve una cadena vacía si no hay ningún error. Si hay un error asociado con el parámetro `result`, se devolverá `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_result_error`

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  if (!pg_connection_busy($dbconn)) {
      pg_send_query($dbconn, "select * from nexistepas;");
  }

  $res1 = pg_get_result($dbconn);
  echo pg_result_error($res1);
?>

    
```php

## Véase también

`pg_result_error_field`, `pg_query`, `pg_send_query`, `pg_get_result`, `pg_last_error`, `pg_last_notice`
