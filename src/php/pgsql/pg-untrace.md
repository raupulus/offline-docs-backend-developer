---
title: pg_untrace
description: Finaliza el seguimiento de una conexión PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-untrace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-untrace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 2ca090342
order: 63790
---

pg_untrace

Finaliza el seguimiento de una conexión PostgreSQL

## Descripción

```php
pg_untrace([PgSql\Connection $connection]): true
```php

`pg_untrace` finaliza el seguimiento de una conexión PostgreSQL, iniciado con `pg_trace`.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`. Cuando `connection` es `null`, se usa la conexión predeterminada. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | El tipo de retorno es ahora `true`, anteriormente era `bool`. |
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `connection` ahora es nullable. |

## Ejemplos

Ejemplo con `pg_untrace`

```
<?php
$pgsql_conn = pg_connect("dbname=mark host=localhost");

if ($pgsql_conn) {
   pg_trace('/tmp/trace.log', 'w', $pgsql_conn);
   pg_query("SELECT 1");
   pg_untrace($pgsql_conn);
   // Ahora el seguimiento de las comunicaciones está desactivado
} else {
   print pg_last_error($pgsql_conn);
   exit;
}
?>

    
```php

## Véase también

`pg_trace`
