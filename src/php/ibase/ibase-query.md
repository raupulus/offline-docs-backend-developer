---
title: ibase_query
description: Ejecuta una consulta en una base iBase
source_url: https://www.php.net/manual/es/function.ibase-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30480
---

ibase_query

Ejecuta una consulta en una base iBase

## Descripción

```php
ibase_query([resource $link_identifier], string $query, [int $bind_args]): resource
```php

Ejecuta una consulta en una base iBase.

## Parámetros

`link_identifier`  
Un identificador de conexión a InterBase. Si se omite, se utilizará la última conexión abierta.

`query`  
Una consulta InterBase.

`bind_args`  

## Valores devueltos

Si la consulta emite un error, la función devolverá `false`. Si la consulta se ejecuta con éxito, y hay un conjunto de resultados (incluso vacío), la función devolverá un identificador de resultado. Si la consulta se ejecuta con éxito, y no hay resultado, la función devolverá `true`.

> [!NOTE]
> En las versiones 5.0.0 de PHP y siguientes, `ibase_query` devuelve el número de registros afectados por las consultas `INSERT`, `UPDATE` y `DELETE`. Por razones de compatibilidad ascendente, `ibase_query` devolverá `true` si la consulta tiene éxito pero no devuelve ningún registro.

## Errores/Excepciones

Si se recibe un error del tipo `"arithmetic exception, numeric overflow, or string truncation. Cannot transliterate character between character sets"` (esto ocurre cuando se intenta utilizar caracteres acentuados) con la función `ibase_query`, es necesario elegir un juego de caracteres (i.e. `ISO8859_1` o su juego actual).

## Ejemplos

Ejemplo con `ibase_query`

```
<?php

$host = 'localhost:/path/to/your.gdb';

$dbh = ibase_connect($host, $username, $password);
$stmt = 'SELECT * FROM tblname';

$sth = ibase_query($dbh, $stmt) or die(ibase_errmsg());

?>

   
```php

## Véase también

ibase_errmsg

ibase_fetch_row

ibase_fetch_object

ibase_free_result
