---
title: odbc_fetch_row
description: Lee una línea de resultado
source_url: https://www.php.net/manual/es/function.odbc-fetch-row.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-fetch-row.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: 6459ee888
order: 98840
---

odbc_fetch_row

Lee una línea de resultado

## Descripción

```php
odbc_fetch_row(Odbc\Result $statement, [int $row]): bool
```php

Lee una línea de los datos devueltos por `odbc_do` o `odbc_exec`. Tras `odbc_fetch_row`, los campos serán accesibles con la función `odbc_result`.

## Parámetros

`statement`  
The ODBC result object.

`row`  
Si `row` es omitido, `row` intentará leer la siguiente línea en el resultado. Llamadas repetidas a `odbc_fetch_row` con y sin parámetro `row` pueden ser combinadas libremente.

Para revisar todas las líneas de un resultado varias veces, se puede llamar a `odbc_fetch_row` con row_number = 1, luego continuar llamando a `odbc_fetch_row` sin el parámetro `row` para revisar todo el resultado. Si un controlador no soporta la lectura de líneas por número, el parámetro será ignorado.

## Valores devueltos

Devuelve `true` si la línea existe, `false` en caso contrario.

## Errores/Excepciones

Se emite un `E_WARNING` cuando `row` es igual o inferior a cero.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | Ahora se emite un `E_WARNING` cuando `row` es igual o inferior a cero. |
| 8.0.0 | `row` ahora es nullable. |
