---
title: pg_result_error_field
description: Devuelve un campo individual de un informe de error
source_url: https://www.php.net/manual/es/function.pg-result-error-field.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-result-error-field.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 5f1a92089
order: 63590
---

pg_result_error_field

Devuelve un campo individual de un informe de error

## Descripción

```php
pg_result_error_field(PgSql\Result $result, int $field_code): string
```php

`pg_result_error_field` devuelve uno de los campos detallados del mensaje de error asociados al recurso `result`. El campo de error se especifica mediante `field_code`.

Dado que `pg_query` y `pg_query_params` devuelven `false` si la consulta falla, se debe utilizar `pg_send_query` y `pg_get_result` para obtener el conjunto de resultados.

Si se necesita obtener más información sobre el error al fallar las consultas con `pg_query`, se debe utilizar `pg_set_error_verbosity` y `pg_last_error` y analizar posteriormente el resultado.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`field_code`  
Los valores posibles de `field_code` son: `PGSQL_DIAG_SEVERITY`, `PGSQL_DIAG_SQLSTATE`, `PGSQL_DIAG_MESSAGE_PRIMARY`, `PGSQL_DIAG_MESSAGE_DETAIL`, `PGSQL_DIAG_MESSAGE_HINT`, `PGSQL_DIAG_STATEMENT_POSITION`, `PGSQL_DIAG_INTERNAL_POSITION`, `PGSQL_DIAG_INTERNAL_QUERY`, `PGSQL_DIAG_CONTEXT`, `PGSQL_DIAG_SOURCE_FILE`, `PGSQL_DIAG_SOURCE_LINE` o `PGSQL_DIAG_SOURCE_FUNCTION`.

## Valores devueltos

Devuelve una `string` que contiene el contenido del campo de error, `null` si el campo no existe o `false` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_result_error_field`

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  if (!pg_connection_busy($dbconn)) {
      pg_send_query($dbconn, "select * from nexistepas;");
  }

  $res1 = pg_get_result($dbconn);
  echo pg_result_error_field($res1, PGSQL_DIAG_SQLSTATE);
?>

    
```php

## Véase también

`pg_result_error`
