---
title: odbc_result
description: Lee un campo de resultado UODBC
source_url: https://www.php.net/manual/es/function.odbc-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 99040
---

odbc_result

Lee un campo de resultado UODBC

## Descripción

```php
odbc_result(Odbc\Result $statement, string $field): string
```php

Lee un campo de resultado UODBC.

## Parámetros

`statement`  
The ODBC result object.

`field`  
El nombre del campo a recuperar. Puede ser tanto un entero, que contiene el número de columna del campo, en el resultado, como una cadena de caracteres, que representa el nombre del campo.

## Valores devueltos

Devuelve el contenido del campo, `false` si ocurre un error, `null` para datos NULL, o `true` para datos binarios.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

La primera llamada a `odbc_result` devuelve el valor del tercer campo de la fila actual del resultado de la consulta. La segunda llamada a `odbc_result` devuelve el valor del tercer campo cuyo nombre es "val" de la fila actual del resultado de la consulta. Se produce un error si el parámetro de columna es inferior a 1, o supera el número de columnas del resultado. De la misma manera, se produce un error si el nombre del campo pasado no corresponde a ningún campo en el resultado.

Ejemplo con `odbc_result`

```
<?php
$item_3   = odbc_result($Query_ID, 3);
$item_val = odbc_result($Query_ID, "val");
?>

    
```php

## Notas

Los índices de campos comienzan en 1. Para más información sobre cómo leer columnas de tipo binario o largo, consulte `odbc_binmode` y `odbc_longreadlen`.
