---
title: pg_unescape_bytea
description: Elimina la protección de una cadena de tipo bytea
source_url: https://www.php.net/manual/es/function.pg-unescape-bytea.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-unescape-bytea.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 5f1a92089
order: 63780
---

pg_unescape_bytea

Elimina la protección de una cadena de tipo bytea

## Descripción

```php
pg_unescape_bytea(string $string): string
```php

`pg_unescape_bytea` elimina la protección de los caracteres de tipo bytea. Devuelve el `string` protegido, que puede contener datos binarios.

> [!NOTE]
> Al utilizar una sentencia `SELECT` con datos de tipo bytea, PostgreSQL devuelve valores octales, precedidos por barras invertidas \\ (p. ej. \032). Los usuarios deben realizar la conversión al formato binario por sí mismos.

## Parámetros

`string`  
Una `string` que contiene los datos bytea de PostgreSQL a ser convertidos en `string` binario de PHP.

## Valores devueltos

Una `string` que contiene los datos protegidos.

## Ejemplos

Ejemplo con `pg_unescape_bytea`

```
<?php
  // Conexión a la base de datos
  $dbconn = pg_connect('dbname=foo');

  // Recuperación de los datos bytea
  $res = pg_query("SELECT data FROM galeria WHERE nombre='Arboles Pino'");
  $raw = pg_fetch_result($res, 'data');

  // Convierte a binario y envía al navegador
  header('Content-type: image/jpeg');
  echo pg_unescape_bytea($raw);
?>

    
```php

## Véase también

`pg_escape_bytea`, `pg_escape_string`
