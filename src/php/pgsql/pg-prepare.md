---
title: pg_prepare
description: Envía una solicitud al servidor para crear una sentencia preparada con
  los parámetros dados y espera la ejecución
source_url: https://www.php.net/manual/es/function.pg-prepare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-prepare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c43a3cd9b
order: 63530
---

pg_prepare

Envía una solicitud al servidor para crear una sentencia preparada con los parámetros dados y espera la ejecución

## Descripción

```php
pg_prepare([PgSql\Connection $connection], string $statement_name, string $query): PgSql\Result
```php

`pg_prepare` crea una consulta preparada para una ejecución posterior con `pg_execute` o `pg_send_execute`. Esta característica permite que las órdenes que serán utilizadas repetidamente sean analizadas y planificadas una sola vez, en lugar de ser ejecutadas cada vez.

La función crea una consulta preparada llamada `statement_name` a partir de la cadena `query`, la cual debe contener una sola orden SQL. `statement_name` puede ser `""` para crear una consulta sin nombre. En este caso, las consultas que existían y que no tenían nombres son automáticamente sobrescritas; de lo contrario, habrá un error si el nombre de la consulta ya está definido en la sesión actual. Si se utilizan parámetros, estos son referenciados como `$1`, `$2`, etc. en `query`.

Las consultas preparadas para ser utilizadas con `pg_prepare` también pueden ser creadas ejecutando la orden SQL `PREPARE`. (Sin embargo, `pg_prepare` es más flexible ya que no requiere que los tipos de los parámetros sean preespecificados.) Además, aunque no existe una función PHP para eliminar una consulta preparada, la orden SQL `DEALLOCATE` puede ser utilizada para este propósito.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`statement_name`  
El nombre a dar a la consulta preparada. Debe ser único para cada sesión. Si se especifica una cadena vacía `""` entonces se crea una consulta sin nombre, sobrescribiendo las consultas sin nombres previamente definidas.

`query`  
La consulta SQL con sus parámetros. Debe contener solo una sola consulta. Varios comandos separados por punto y coma no son permitidos. Si se utilizan parámetros, estos son referenciados como `$1`, `$2`, etc.

## Valores devueltos

Una instancia `PgSql\Result` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `PgSql\Result` ; anteriormente, se devolvía un `resource`. |
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_prepare`

```
<?php
// Conexión a una base de datos llamada "marie"
$dbconn = pg_connect("dbname=marie");

// Prepara una consulta para la ejecución
$result = pg_prepare($dbconn, "my_query", 'SELECT * FROM magasins WHERE nom = $1');

// Ejecuta la consulta preparada. Note que no es necesario escapar
// la cadena "Joe's Widgets"
$result = pg_execute($dbconn, "my_query", array("Joe's Widgets"));

// Ejecuta la misma consulta preparada, esta vez con un parámetro diferente
$result = pg_execute($dbconn, "my_query", array("Vêtements Vêtements Vêtements"));

?>

    
```php

## Véase también

`pg_execute`, `pg_send_execute`
