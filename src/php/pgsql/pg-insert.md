---
title: pg_insert
description: Inserta un array en una tabla
source_url: https://www.php.net/manual/es/function.pg-insert.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-insert.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 39bb8a868
order: 63280
---

pg_insert

Inserta un array en una tabla

## Descripción

```php
pg_insert(PgSql\Connection $connection, string $table_name, array $values, [int $flags]): PgSql\Result
```php

`pg_insert` inserta los `values` en la tabla `table_name`.

Si `flags` está especificado, `pg_convert` se aplica a `values` con los flags proporcionados.

Por omisión, `pg_insert` pasa valores sin tratar. Los valores deben ser escapados o el flag `PGSQL_DML_ESCAPE` debe ser especificado en `flags`. `PGSQL_DML_ESCAPE` coloca comillas y escapa los parámetros/identificadores. Por consiguiente, los nombres de tabla/columnas se vuelven sensibles a mayúsculas y minúsculas.

Tenga en cuenta que ni el escape ni las consultas preparadas pueden proteger consultas LIKE, JSON, arrays, Regex, etc. Estos parámetros deben ser tratados de acuerdo con su contexto. Es decir, escapar/validar los valores.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`table_name`  
Nombre de la tabla en la que se insertarán las filas. La tabla `table_name` debe tener al menos tantas columnas como elementos tenga `values`.

`values`  
Un `array` cuyas claves son los nombres de los campos en la tabla `table_name`, y cuyos valores son los valores de esos campos que serán insertados.

`flags`  
Cualquier combinación de constantes entre `PGSQL_CONV_OPTS`, `PGSQL_DML_NO_CONV`, `PGSQL_DML_ESCAPE`, `PGSQL_DML_EXEC`, `PGSQL_DML_ASYNC` o `PGSQL_DML_STRING`. Si `PGSQL_DML_STRING` forma parte del parámetro `flags`, entonces la consulta será retornada. Cuando la constante `PGSQL_DML_NO_CONV` o la constante `PGSQL_DML_ESCAPE` está definida, no se realizará ninguna llamada a la función `pg_convert` internamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.. O retorna un `string` si `PGSQL_DML_STRING` es proporcionado a través de `flags`.

## Errores/Excepciones

Se lanza una `ValueError` cuando la tabla especificada es inválida.

Se lanza una `ValueError` o `TypeError` cuando el valor o el tipo del campo no coincide correctamente con un tipo PostgreSQL.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Ahora lanza un error `ValueError` cuando la tabla especificada es inválida; anteriormente, se emitía un `E_WARNING`. |
| 8.3.0 | Ahora lanza un error `ValueError` o `TypeError` cuando el valor o el tipo del campo no coincide correctamente con un tipo PostgreSQL; anteriormente, se emitía un `E_WARNING`. |
| 8.1.0 | Ahora devuelve una instancia de `PgSql\Result` ; anteriormente, se devolvía un `resource`. |
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_insert`

```
<?php
  $db = pg_connect ('dbname=foo');
  // Esto es seguro en cierta medida, ya que todos los valores son escapados
  // Sin embargo, PostgreSQL soporta JSON/arrays. Estos no son
  // seguros ni por escape ni por consultas preparadas.
  $res = pg_insert($dbconn, 'post_log', $_POST, PGSQL_DML_ESCAPE);
  if ($res) {
      echo "Los datos POSTeados han podido ser registrados con éxito.\n";
  } else {
      echo "Hay un problema con los datos.\n";
  }
?>

    
```php

## Véase también

`pg_convert`
