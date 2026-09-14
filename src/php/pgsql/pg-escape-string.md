---
title: pg_escape_string
description: Protege un string para una consulta SQL
source_url: https://www.php.net/manual/es/function.pg-escape-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-escape-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c43a3cd9b
order: 63050
---

pg_escape_string

Protege un string para una consulta SQL

## Descripción

```php
pg_escape_string([PgSql\Connection $connection], string $string): string
```php

`pg_escape_string` protege un string para insertarlo en la base de datos. Devuelve el string protegido en formato PostgreSQL. Se recomienda el uso de esta función en lugar de `addslashes`. Si el tipo de la columna es bytea, `pg_escape_bytea` debe ser utilizada en su lugar. La función `pg_escape_identifier` debe ser utilizada para escapar identificadores (es decir, nombres de tablas, nombres de campos).

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`string`  
Un `string` que contiene el texto a escapar.

## Valores devueltos

Un `string` que contiene los datos escapados.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_escape_string`

```
<?php
// Conexión a la base de datos
$dbconn = pg_connect('dbname=foo');

// Lectura de un fichero de texto (que contiene apóstrofes y barras invertidas)
$data = file_get_contents('letter.txt');

// Protección de los datos
$escaped = pg_escape_string($data);

// Inserción en la base de datos
pg_query("INSERT INTO correspondence (name, data) VALUES ('Mi carta', '{$escaped}')");
?>

    
```php

## Véase también

`pg_escape_bytea`
