---
title: pg_query
description: Ejecuta una consulta PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63580
---

pg_query

Ejecuta una consulta PostgreSQL

## Descripción

```php
pg_query([PgSql\Connection $connection], string $query): PgSql\Result
```php

`pg_query` ejecuta la consulta `query` en la base de datos especificada `connection`. `pg_query_params` debe preferirse en la mayoría de los casos.

Si ocurre un error y se devuelve `false`, los detalles del error pueden recuperarse utilizando la función `pg_last_error` si la conexión es válida.

> [!NOTE]
> Aunque `connection` puede omitirse, no se recomienda hacerlo, ya que puede resultar difícil encontrar errores en los scripts.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_exec`. `pg_exec` sigue disponible por razones de compatibilidad, pero se recomienda a los usuarios utilizar el nuevo nombre.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`query`  
La consulta o consultas SQL a ejecutarse. Cuando se pasan varias consultas a la función, se ejecutan automáticamente como una transacción, a menos que se incluyan los comandos BEGIN/COMMIT en la consulta. Sin embargo, no se recomienda el uso de múltiples transacciones en una sola llamada de función.

> [!WARNING]
> La interpolación de strings proporcionados por el usuario es extremadamente peligrosa y debe tenerse en cuenta el conjunto de vulnerabilidades relacionadas con las [inyecciones SQL](#security.database.sql-injection). En la mayoría de los casos, debe preferirse la función `pg_query_params`; es preferible pasar los valores proporcionados por el usuario como argumentos, en lugar de sustituirlos en la consulta.
>
> Todos los datos de usuario sustituidos directamente en el string de la consulta deben ser [propiamente escapados](#function.pg-escape-string).

## Valores devueltos

Una instancia `PgSql\Result` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `PgSql\Result` ; anteriormente, se devolvía un `resource`. |
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_query`

```
<?php

$conn = pg_pconnect("dbname=publisher");
if (!$conn) {
  echo "Ocurrió un error.\n";
  exit;
}

$result = pg_query($conn, "SELECT autor, email FROM autores");
if (!$result) {
  echo "Ocurrió un error.\n";
  exit;
}

while ($row = pg_fetch_row($result)) {
  echo "Autor: $row[0]  E-mail: $row[1]";
  echo "<br />\n";
}

?>

    
```php

Uso de `pg_query` con múltiples consultas

```
<?php

$conn = pg_pconnect("dbname=publisher");

// estas consultas se ejecutarán como una sola transacción

$query = "UPDATE authors SET author=UPPER(author) WHERE id=1;";
$query .= "UPDATE authors SET author=LOWER(author) WHERE id=2;";
$query .= "UPDATE authors SET author=NULL WHERE id=3;";

pg_query($conn, $query);

?>

    
```php

## Véase también

`pg_connect`, `pg_pconnect`, `pg_fetch_array`, `pg_fetch_object`, `pg_num_rows`, `pg_affected_rows`
