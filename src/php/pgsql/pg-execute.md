---
title: pg_execute
description: Ejecuta una consulta preparada de PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c43a3cd9b
order: 63060
---

pg_execute

Ejecuta una consulta preparada de PostgreSQL

## Descripción

```php
pg_execute([PgSql\Connection $connection], string $statement_name, array $params): PgSql\Result
```php

Envía una consulta para ejecutar una consulta preparada con los argumentos dados y espera el resultado.

`pg_execute` es similar a `pg_query_params`, pero la consulta que será ejecutada se especifica nombrando una consulta previamente preparada, en lugar de proporcionar una cadena como consulta. Esta característica permite que las consultas que serán utilizadas repetidamente sean analizadas y planificadas una sola vez, en lugar de ser ejecutadas cada vez. La consulta debe haber sido previamente preparada en la sesión actual.

Los argumentos son idénticos a la función `pg_query_params` excepto por el nombre de la consulta preparada que se proporciona en lugar de la consulta en forma de cadena.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`statement_name`  
El nombre de la consulta preparada a ejecutar. Si se especifica una cadena vacía (""), entonces se ejecuta la consulta sin nombre. El nombre debe haber sido previamente preparado utilizando `pg_prepare`, `pg_send_prepare` o una orden SQL `PREPARE`.

`params`  
Un array de valores de argumentos para sustituir las variables \$1, \$2, etc. en la consulta preparada original. El número de elementos presentes en el array debe coincidir con el número de variables a reemplazar.

> [!WARNING]
> Los elementos son convertidos en strings al llamar a esta función.

## Valores devueltos

Una instancia de `PgSql\Result` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `PgSql\Result` ; anteriormente, se devolvía un `resource`. |
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_execute`

```
<?php
// Conexión a una base de datos llamada "marie"
$dbconn = pg_connect("dbname=marie");

// Prepara una consulta para su ejecución
$result = pg_prepare($dbconn, "my_query", 'SELECT * FROM magasins WHERE nom = $1');

// Ejecuta la consulta preparada. Observe que no es necesario escapar
// la cadena "Joe's Widgets"
$result = pg_execute($dbconn, "my_query", array("Joe's Widgets"));

// Ejecuta la misma consulta preparada, esta vez con un argumento diferente
$result = pg_execute($dbconn, "my_query", array("Vêtements Vêtements Vêtements"));

?>

    
```php

## Véase también

`pg_prepare`, `pg_send_prepare`, `pg_query_params`
