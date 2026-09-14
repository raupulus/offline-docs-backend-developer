---
title: pg_escape_bytea
description: Protege una cadena para insertarla en un campo bytea
source_url: https://www.php.net/manual/es/function.pg-escape-bytea.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-escape-bytea.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_revision: c43a3cd9b
order: 63020
---

pg_escape_bytea

Protege una cadena para insertarla en un campo bytea

## Descripción

```php
pg_escape_bytea([PgSql\Connection $connection], string $string): string
```php

`pg_escape_bytea` protege los caracteres de la cadena `string` con el modo bytea. La cadena protegida es devuelta.

> [!NOTE]
> Cuando se utiliza una orden `SELECT` con datos de tipo bytea, PostgreSQL devuelve valores octales, prefijados con backslashs '\\ (por ejemplo \032). Los usuarios deben realizar la conversión al formato binario manualmente.
>
> `pg_escape_bytea` requiere PostgreSQL 7.2 o más reciente. Con PostgreSQL 7.2.0 y 7.2.1, los datos bytea deben ser transtipados cuando se activa el soporte de strings multioctetos. Es decir, `INSERT INTO test_table (image) VALUES ('$image_escaped'::bytea);`. PostgreSQL 7.2.2 o más reciente no requiere esta manipulación. Sin embargo, si el cliente y el servidor no utilizan el mismo juego de caracteres, pueden ocurrir errores. Entonces, se debe forzar el transtipado manualmente.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`string`  
Una `string` que contiene texto o datos binarios que serán insertados en la columna bytea.

## Valores devueltos

Una `string` que contiene los datos escapados.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_escape_bytea`

```
<?php
// Conexión a la base de datos
$dbconn = pg_connect('dbname=foo');

// Lectura de un fichero binario
$data = file_get_contents('image1.jpg');

// Escapado de los datos binarios
$escaped = pg_escape_bytea($data);

// Inserción en la base de datos
pg_query("INSERT INTO gallery (name, data) VALUES ('Pine trees', '{$escaped}')");
?>

    
```php

## Véase también

`pg_unescape_bytea`, `pg_escape_string`
