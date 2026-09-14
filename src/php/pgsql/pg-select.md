---
title: pg_select
description: Realiza una selección PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-select.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-select.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 18aa2012f
order: 63640
---

pg_select

Realiza una selección PostgreSQL

## Descripción

```php
pg_select(PgSql\Connection $connection, string $table_name, [array $conditions], [int $flags], [int $mode]): array
```php

`pg_select` selecciona los registros por `conditions` que está en formato `campo=>valor`. Cuando la consulta tiene éxito, devuelve un array que contiene todos los registros y campos que cumplen la condición especificada por `conditions`.

Si `flags` está especificado, `pg_convert` se aplica a `values` con los flags proporcionados.

Si el parámetro `mode` está definido, el valor de retorno será en forma de un array indexado con `PGSQL_NUM`, un array asociativo con `PGSQL_ASSOC` (por defecto), o ambos con `PGSQL_BOTH`.

Por defecto `pg_delete` pasa valores sin tratar. Los valores deben ser escapados o la opción PGSQL_DML_ESCAPE debe ser proporcionada. PGSQL_DML_ESCAPE pone comillas y escapa los parámetros/identificadores. Por lo tanto, los nombres de tabla/columnas deben ser sensibles a mayúsculas y minúsculas.

Tenga en cuenta que ni el escape ni las consultas preparadas pueden proteger de consultas LIKE, JSON, Arrays, Regex, etc. Estos parámetros deberían ser tratados según su contexto. Es decir, escapar/validar los valores.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`table_name`  
Nombre de la tabla desde la cual seleccionar las filas.

`conditions`  
Un `array` cuyas claves son los nombres de los campos en la tabla `table_name`, y cuyos valores son las condiciones que una fila debe cumplir para ser recuperada. A partir de PHP 8.4.0, cuando se proporciona un array vacío, no se aplicará ninguna condición. Anteriormente, la función fallaba con un argumento `conditions` vacío.

`flags`  
Cualquier número de `PGSQL_CONV_FORCE_NULL`, `PGSQL_DML_NO_CONV`, `PGSQL_DML_ESCAPE`, `PGSQL_DML_EXEC`, `PGSQL_DML_ASYNC` o `PGSQL_DML_STRING` combinados. Si `PGSQL_DML_STRING` forma parte de los `flags`, entonces se devuelve la cadena de consulta. Cuando `PGSQL_DML_NO_CONV` o `PGSQL_DML_ESCAPE` está activado, `pg_convert` no es llamado internamente.

`mode`  
Cualquier número de `PGSQL_ASSOC`, `PGSQL_NUM` o `PGSQL_BOTH`. Si `PGSQL_ASSOC` está definido, el valor de retorno será un `array` asociativo, con `PGSQL_NUM`, el valor de retorno será un `array` indexado numéricamente, y con `PGSQL_BOTH`, el valor de retorno será tanto un `array` asociativo como numéricamente indexado.

## Valores devueltos

Devuelve un `string` si `PGSQL_DML_STRING` es proporcionado a través de `flags`, de lo contrario esto devuelve un `array` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `conditions` ahora es opcional. |
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
| 7.1.0 | El parámetro `mode` ha sido añadido. |

## Ejemplos

Ejemplo con `pg_select`

```
<?php
  $db = pg_connect ('dbname=foo');
  // Esto es seguro en cierta medida, ya que todos los valores están escapados
  // Sin embargo PostgreSQL soporta JSON/Arrays. Estos no son
  // seguros ni por escape ni por consultas preparadas.
  $rec = pg_select($db, 'post_log', $_POST, PG_DML_ESCAPE);
  if ($rec) {
    echo "Filas leídas\n";
    var_dump($rec);
  } else {
    echo "Problema en los datos de usuario\n";
  }
?>

    
```php

## Véase también

`pg_convert`
