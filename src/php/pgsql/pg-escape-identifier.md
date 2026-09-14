---
title: pg_escape_identifier
description: Protege un identificador para su inserción en un campo de texto.
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-escape-identifier.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c43a3cd9b
order: 63030
---

pg_escape_identifier

Protege un identificador para su inserción en un campo de texto.

## Descripción

```php
pg_escape_identifier([PgSql\Connection $connection], string $string): string
```php

`pg_escape_identifier` protege un identificador (ejemplo: tabla, nombre de campo) para una consulta en la base de datos. El resultado es una cadena de caracteres protegida para PostgreSQL. `pg_escape_identifier` añade comillas antes y después de los datos. Los usuarios no deben, por lo tanto, añadir comillas. Se recomienda el uso de esta función para los identificadores de las consultas. Para los datos SQL sin tratar (es decir, los parámetros, excepto de tipo bytea), `pg_escape_literal` o `pg_escape_string` debe ser utilizado. Para los campos de tipo bytea es necesario utilizar `pg_escape_bytea`.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`string`  
Una `string` que contiene texto a proteger.

## Valores devueltos

Una `string` que contiene los datos protegidos, o `false` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_escape_identifier`

```
<?php
  // Conexión a la base de datos
  $dbconn = pg_connect('dbname=foo');

  // Protección del nombre de la tabla
  $escaped = pg_escape_identifier($table_name);

  // Selección de las filas de la tabla $table_name
  pg_query("SELECT * FROM {$escaped};");
?>

    
```php

## Véase también

`pg_escape_literal`, `pg_escape_bytea`, `pg_escape_string`
