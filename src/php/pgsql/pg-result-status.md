---
title: pg_result_status
description: Lee el estado del resultado
source_url: https://www.php.net/manual/es/function.pg-result-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-result-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 3c6c95fcf
order: 63630
---

pg_result_status

Lee el estado del resultado

## Descripción

```php
pg_result_status(PgSql\Result $result, [int $mode]): string
```php

`pg_result_status` devuelve el estado de la instancia de `PgSql\Result`, o la etiqueta de comando PostgreSQL asociada al resultado.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`mode`  
Puede ser `PGSQL_STATUS_LONG` para devolver un estado numérico de `result` o `PGSQL_STATUS_STRING` para devolver la etiqueta del comando de `result`. Si el argumento no se especifica, `PGSQL_STATUS_LONG` es el valor por omisión.

## Valores devueltos

Los valores de retorno posibles son `PGSQL_EMPTY_QUERY`, `PGSQL_COMMAND_OK`, `PGSQL_TUPLES_OK`, `PGSQL_TUPLES_CHUNK`, `PGSQL_COPY_OUT`, `PGSQL_COPY_IN`, `PGSQL_BAD_RESPONSE`, `PGSQL_NONFATAL_ERROR` y `PGSQL_FATAL_ERROR` si `PGSQL_STATUS_LONG` se especifica. De lo contrario, se devuelve un `string` que contiene la etiqueta del comando PostgreSQL.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_result_status`

```
<?php

// Conexión a la base de datos
$conn = pg_pconnect("dbname=publisher");

// Ejecución de COPY
$result = pg_query($conn, "COPY autores FROM STDIN;");

// Obtención del estado
$status = pg_result_status($result);

// Determinación del estado
if ($status == PGSQL_COPY_IN)
   echo "La copia se ha realizado.";
else
   echo "La copia ha fallado.";

?>

    
```php

El ejemplo anterior mostrará:

    La copia se ha realizado.

## Véase también

`pg_connection_status`
