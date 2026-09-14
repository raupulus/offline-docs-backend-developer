---
title: pg_query_params
description: Envía un comando al servidor y espera el resultado, con la capacidad
  de pasar parámetros por separado del texto SQL de la consulta
source_url: https://www.php.net/manual/es/function.pg-query-params.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-query-params.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 5f1a92089
order: 63570
---

pg_query_params

Envía un comando al servidor y espera el resultado, con la capacidad de pasar parámetros por separado del texto SQL de la consulta

## Descripción

```php
pg_query_params([PgSql\Connection $connection], string $query, array $params): PgSql\Result
```php

Envía un comando al servidor y espera el resultado, con la capacidad de pasar parámetros por separado del texto SQL de la consulta.

`pg_query_params` es como `pg_query`, pero ofrece funcionalidades adicionales: los valores de los parámetros pueden especificarse por separado de la línea de comando propia.

Si se utilizan parámetros, se refieren a \$1, \$2, etc. en `query`. El mismo parámetro puede aparecer más de una vez en la consulta `query`; se utilizará el mismo valor en ese caso. `params` especifica los valores actuales de los parámetros. Un valor `null` en este array significa que el parámetro correspondiente es SQL `null`.

La principal ventaja de `pg_query_params` sobre `pg_query` es que los valores de los parámetros pueden separarse de la consulta `query`, por lo tanto, se evitan los escapes de caracteres tediosos y propensos a errores. A diferencia de `pg_query`, `pg_query_params` permite solo un comando SQL en la cadena dada. (Puede haber puntos y coma en el interior pero no más de un comando.)

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`query`  
La consulta SQL con sus parámetros. Debe contener solo una consulta. Múltiples consultas separadas por puntos y coma no están permitidas. Si se utilizan parámetros, se refieren a \$1, \$2, etc.

Los valores proporcionados por el usuario siempre deben pasarse como parámetros, y no interpolados en la cadena de consulta, donde pueden potencialmente formar [inyecciones SQL](#security.database.sql-injection) e introducir errores cuando estos datos contienen comillas. Si por alguna razón no se pueden utilizar parámetros, asegúrese de que los valores interpolados estén [correctamente escapados](#function.pg-escape-string).

`params`  
Un array de valores de parámetros para sustituir las variables \$1, \$2, etc. en la consulta preparada original. El número de elementos presentes en el array debe coincidir con el número de variables a reemplazar.

Los valores esperados para los campos `bytea` no son soportados como parámetros. Utilice en su lugar la función `pg_escape_bytea` o utilice las funciones sobre los objetos grandes.

## Valores devueltos

Una instancia `PgSql\Result` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `PgSql\Result` ; anteriormente, se devolvía un `resource`. |
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_query_params`

```
<?php
// Conexión a una base de datos llamada "marie"
$dbconn = pg_connect("dbname=marie");

// Busca todas las tiendas llamadas Joe's Widgets. Note que no es
// necesario escapar la cadena "Joe's Widgets"
$result = pg_query_params($dbconn, 'SELECT * FROM tiendas WHERE nombre = $1', array("Joe's Widgets"));

// Comparación usando pg_query
$str = pg_escape_string("Joe's Widgets");
$result = pg_query($dbconn, "SELECT * FROM tiendas WHERE nombre = '{$str}'");

?>

    
```php

## Véase también

`pg_query`
