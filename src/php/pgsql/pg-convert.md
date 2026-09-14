---
title: pg_convert
description: Convierte valores de un array asociativo a una forma adecuada para consultas
  SQL
source_url: https://www.php.net/manual/es/function.pg-convert.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-convert.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 39bb8a868
order: 62960
---

pg_convert

Convierte valores de un array asociativo a una forma adecuada para consultas SQL

## Descripción

```php
pg_convert(PgSql\Connection $connection, string $table_name, array $values, [int $flags]): array
```php

`pg_convert` verifica y convierte el array asociativo `values` en una consulta SQL válida. Para que `pg_convert` funcione, debe existir la tabla `table_name`, y debe contener al menos tantas columnas como elementos tenga el array `values`. Los nombres de los campos de `table_name` deben corresponder a los índices del array en `values`. Devuelve un array con los valores convertidos en caso de éxito, y de lo contrario, `false`.

> [!NOTE]
> Los valores booleanos son admitidos y convertidos a booleanos PostgreSQL. Las representaciones de valores booleanos en forma de strings también son soportadas. `null` es convertido a NULL PostgreSQL.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`table_name`  
Nombre de la tabla para la cual se convertirán los tipos.

`values`  
Datos a ser convertidos.

`flags`  
Un número de `PGSQL_CONV_IGNORE_DEFAULT`, `PGSQL_CONV_FORCE_NULL` o `PGSQL_CONV_IGNORE_NOT_NULL`, combinados.

## Valores devueltos

Un `array` de valores convertidos, o `false` si ocurre un error.

## Errores/Excepciones

Se lanza una `ValueError` o `TypeError` cuando el valor o el tipo del campo no coincide correctamente con un tipo PostgreSQL.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Ahora lanza un error `ValueError` o `TypeError` cuando el valor o el tipo del campo no coincide correctamente con un tipo PostgreSQL; previamente, se emitía un `E_WARNING`. |
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_convert`

```
<?php
  $dbconn = pg_connect('dbname=foo');

  $tmp = array(
      'auteur' => 'Joe Thackery',
      'annee' => 2005,
      'titre' => 'Ma Vie, par Joe Thackery'
  );

  $vals = pg_convert($dbconn, 'auteurs', $tmp);
?>

    
```php

## Véase también

`pg_meta_data`, `pg_insert`, `pg_select`, `pg_update`, `pg_delete`
