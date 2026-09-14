---
title: pg_update
description: Modifica las líneas de una tabla
source_url: https://www.php.net/manual/es/function.pg-update.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-update.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63800
---

pg_update

Modifica las líneas de una tabla

## Descripción

```php
pg_update(PgSql\Connection $connection, string $table_name, array $values, array $conditions, [int $flags]): string
```php

`pg_update` modifica las líneas de la tabla `table_name`, que cumplen la condición `conditions` con `values`.

Si `flags` está especificado, `pg_convert` se aplica a `values` con los flags proporcionados.

Por omisión `pg_update` pasa valores sin tratar. Los valores deben ser escapados o el flag `PGSQL_DML_ESCAPE` debe ser especificado en `flags`. `PGSQL_DML_ESCAPE` añade comillas y escapa los argumentos/identificadores. Por lo tanto, los nombres de tabla/columnas se vuelven sensibles a mayúsculas/minúsculas.

Tenga en cuenta que ni el escape ni las consultas preparadas pueden proteger de consultas LIKE, JSON, arrays, Regex, etc. Estos argumentos deben ser tratados según su contexto. Es decir, escapar/validar los valores.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`table_name`  
El nombre de la tabla en la que las líneas serán actualizadas.

`values`  
Un `array` cuyos claves son los nombres de los campos en la tabla `table_name`, y donde los valores son las líneas correspondientes que serán actualizadas.

`conditions`  
Un `array` cuyos claves son los nombres de los campos en la tabla `table_name`, y donde los valores son las condiciones que deben cumplir las líneas para ser actualizadas.

`flags`  
Cualquier combinación de constantes entre `PGSQL_CONV_FORCE_NULL`, `PGSQL_DML_NO_CONV`, `PGSQL_DML_ESCAPE`, `PGSQL_DML_EXEC`, `PGSQL_DML_ASYNC` o `PGSQL_DML_STRING`. Si `PGSQL_DML_STRING` forma parte del argumento `flags`, entonces la consulta será devuelta. Cuando la constante `PGSQL_DML_NO_CONV` o la constante `PGSQL_DML_ESCAPE` está definida, no se realizará ninguna llamada a la función `pg_convert` internamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Devuelve una `string` si `PGSQL_DML_STRING` es pasado a través del argumento `flags`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_update`

```
<?php
  $db = pg_connect ('dbname=foo');
  $data = array('field1'=>'AA', 'field2'=>'BB');

  // Esto es seguro en cierta medida, ya que todos los valores son escapados
  // Sin embargo PostgreSQL soporta JSON/arrays. Estos no
  // son seguros ni por escape ni por consultas preparadas.
  $res = pg_update($db, 'post_log', $_POST, $data);
  if ($res) {
      echo "Los datos han sido modificados: $res\n";
  } else {
      echo "Problema en los datos del usuario\n";
  }
?>

    
```php

## Véase también

`pg_convert`
