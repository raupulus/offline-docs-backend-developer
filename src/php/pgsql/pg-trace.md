---
title: pg_trace
description: Activa el seguimiento de una conexión PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-trace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-trace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 3f2e2d4a8
order: 63750
---

pg_trace

Activa el seguimiento de una conexión PostgreSQL

## Descripción

```php
pg_trace(string $filename, [string $mode], [PgSql\Connection $connection], [int $trace_mode]): bool
```php

`pg_trace` activa el seguimiento de las comunicaciones entre PHP y el servidor PostgreSQL. Este historial se registrará en un fichero. Para comprender estas líneas, es necesario estar familiarizado con el protocolo de comunicación interno de PostgreSQL.

Para quienes no lo estén, pueden ser útiles para seguir las consultas y los errores: con el comando `grep '^To backend' trace.log`, se podrán ver las consultas realmente enviadas al servidor PostgreSQL. Para más información, consulte la [Documentación PostgreSQL](http://www.postgresql.org/docs/current/interactive/).

## Parámetros

`filename`  
La ruta completa y el nombre del fichero en el que se registrará el seguimiento. Como `fopen`.

`mode`  
El modo de acceso opcional, como `fopen`.

`connection`  
Una instancia `PgSql\Connection`. Cuando `connection` es `null`, se usa la conexión predeterminada. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`trace_mode`  
Un modo de seguimiento opcional con las constantes siguientes: `PGSQL_TRACE_SUPPRESS_TIMESTAMPS` y `PGSQL_TRACE_REGRESS_MODE`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | `trace_mode` ha sido añadido. |
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `connection` ahora es nullable. |

## Ejemplos

Ejemplo con `pg_trace`

```
<?php
$pgsql_conn = pg_connect("dbname=mark host=localhost");

if ($pgsql_conn) {
   pg_trace('/tmp/trace.log', 'w', $pgsql_conn);
   pg_query("SELECT 1");
   pg_untrace($pgsql_conn);
   // Ahora /tmp/trace.log contendrá el seguimiento de las comunicaciones
} else {
   print pg_last_error($pgsql_conn);
   exit;
}
?>

    
```php

## Véase también

`fopen`, `pg_untrace`
