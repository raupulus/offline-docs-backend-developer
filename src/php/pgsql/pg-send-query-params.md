---
title: pg_send_query_params
description: Envía un comando y separa los parámetros al servidor sin esperar el/los
  resultado(s)
source_url: https://www.php.net/manual/es/function.pg-send-query-params.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-send-query-params.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 9e6c3416c
order: 63670
---

pg_send_query_params

Envía un comando y separa los parámetros al servidor sin esperar el/los resultado(s)

## Descripción

```php
pg_send_query_params(PgSql\Connection $connection, string $query, array $params): int
```php

Envía un comando y separa los parámetros al servidor sin esperar el/los resultado(s).

Esta función es equivalente a `pg_send_query` con la excepción de que los parámetros de la consulta pueden especificarse por separado de la cadena de consulta `query`. Los parámetros de la función se gestionan de la misma manera que `pg_execute`. Como `pg_execute`, la función no funcionará en versiones anteriores a PostgreSQL 7.4 y solo permite un comando por consulta.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`query`  
La consulta SQL con sus parámetros. Debe contener solo una consulta. No se permiten múltiples consultas separadas por punto y coma. Si se utilizan parámetros, se hace referencia a ellos como \$1, \$2, etc.

`params`  
Un array de valores de parámetros para sustituir las variables \$1, \$2, etc. en la consulta preparada original. El número de elementos en el array debe coincidir con el número de variables a reemplazar.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` o `0` en caso de fallo. Utilice `pg_get_result` para determinar el resultado de la consulta.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_send_query_params`

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  // Con parámetros. Tenga en cuenta que no es necesario escapar la cadena del parámetro.
  pg_send_query_params($dbconn, 'select count(*) from autores where ciudad = $1', array('Perth'));

  // Comparar con el uso básico de pg_send_query
  $str = pg_escape_string('Perth');
  pg_send_query($dbconn, "select count(*) from autores where ciudad = '{$str}'");
?>

    
```php

## Véase también

`pg_send_query`
