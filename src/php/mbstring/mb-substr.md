---
title: mb_substr
description: Extrae una subcadena
source_url: https://www.php.net/manual/es/function.mb-substr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-substr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: 911fe79de
order: 45580
---

mb_substr

Extrae una subcadena

## Descripción

```php
mb_substr(string $string, int $start, [int $length], [string $encoding]): string
```php

Realiza una operación similar a `substr` basada en el número de caracteres. La posición se cuenta desde el inicio de la `string` `string`. La posición del primer carácter es `0`, el segundo, uno, etc...

## Parámetros

`string`  
La cadena desde la cual extraer la subcadena.

`start`  
Si `start` es positivo, la cadena devuelta comenzará en el carácter número `start`, dentro de la cadena `string`. El primer carácter está numerado cero. En efecto, en la cadena '`abcdef`', el carácter en la posición `0` es '`a`', el carácter en la posición `2` es '`c`', y así sucesivamente.

Si `start` es negativo, la cadena devuelta comenzará en el carácter número `start` contando desde el final de la cadena `string`.

`length`  
Número máximo de caracteres a utilizar desde `string`. Si este parámetro es omitido, o vale `null`, todos los caracteres hasta el final de la cadena serán extraídos.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

`mb_substr` devuelve la porción de la cadena `string` que comienza en el carácter `start` y tiene una longitud de `length` caracteres.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | En cadenas inválidas (aquellas con errores de codificación), los índices de caracteres ahora se interpretan de la misma manera que la mayoría de las otras funciones de mbstring. Esto significa que los índices de caracteres devueltos por `mb_strpos` pueden pasarse directamente. |
| 8.0.0 | `encoding` ahora acepta `null`. |

## Véase también

`mb_strcut`, `mb_internal_encoding`
