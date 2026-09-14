---
title: mb_strpos
description: Localiza la primera ocurrencia de un carácter en una cadena
source_url: https://www.php.net/manual/es/function.mb-strpos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-strpos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: 95d055464
order: 45470
---

mb_strpos

Localiza la primera ocurrencia de un carácter en una cadena

## Descripción

```php
mb_strpos(string $haystack, string $needle, [int $offset], [string $encoding]): int
```php

Localiza la posición de la primera ocurrencia de `needle` en el string `haystack`.

Realiza una búsqueda de tipo `strpos`, teniendo en cuenta los caracteres multioctetos. La posición de `needle` se cuenta desde el inicio de la cadena `haystack`: las posiciones comienzan en 0.

## Parámetros

`haystack`  
El string a partir del cual se obtiene la posición de la primera aparición de `needle`.

`needle`  
La `string` a encontrar en el parámetro `haystack`. A diferencia de la función `strpos`, los valores numéricos no se aplican como valor ordinal de un carácter.

`offset`  
La posición de inicio de la búsqueda. Si se omite, se utilizará cero. Una posición negativa se cuenta desde el final de la `string`.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Devuelve la posición numérica de la primera ocurrencia del carácter `needle` en la cadena `haystack`. Si `needle` no se encuentra, `mb_strpos` devuelve `false`.

## Errores/Excepciones

- Si `offset` es mayor que la longitud de `haystack`, se lanzará un `ValueError`.

## Historial de cambios

| Versión | Descripción                                 |
|---------|---------------------------------------------|
| 8.0.0   | `needle` ahora acepta una cadena vacía.     |
| 8.0.0   | `encoding` ahora acepta `null`.             |
| 7.1.0   | Se añadió soporte para `offset`s negativos. |

## Véase también

`mb_internal_encoding`, `strpos`
