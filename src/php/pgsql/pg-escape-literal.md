---
title: pg_escape_literal
description: Protege una consulta SQL literal para insertar en un campo de texto
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-escape-literal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c43a3cd9b
order: 63040
---

pg_escape_literal

Protege una consulta SQL literal para insertar en un campo de texto

## Descripción

```php
pg_escape_literal([PgSql\Connection $connection], string $string): string
```php

`pg_escape_literal` protege una consulta SQL literal para su ejecución en la base de datos PostgreSQL. El resultado devuelto es un string protegido en formato PostgreSQL. `pg_escape_literal` añade comillas simples antes y después de los datos. Los usuarios no deben, por tanto, añadir comillas simples. Se recomienda el uso de esta función en lugar de `pg_escape_string`. Si la columna es de tipo bytea, se debe utilizar en su lugar la función `pg_escape_bytea`. Para proteger los identificadores (por ejemplo, nombres de tabla, nombres de campos), se debe utilizar la función `pg_escape_identifier`.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`string`  
Un `string` que contiene texto a proteger.

## Valores devueltos

Una `string` que contiene los datos protegidos, o `false` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_escape_literal`

```
<?php
  // Conexión a la base de datos
  $dbconn = pg_connect('dbname=foo');

  // Lectura de un fichero (que contiene apóstrofes y barras invertidas)
  $data = file_get_contents('letter.txt');

  // Protección de los datos
  $escaped = pg_escape_literal($data);

  // Inserción en la base de datos. Observe que no hay comillas simples alrededor de {$escaped}
  pg_query("INSERT INTO correspondence (name, data) VALUES ('My letter', {$escaped})");
?>

    
```php

## Véase también

`pg_escape_identifier`, `pg_escape_bytea`, `pg_escape_string`
