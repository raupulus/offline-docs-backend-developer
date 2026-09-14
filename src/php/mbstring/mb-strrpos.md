---
title: mb_strrpos
description: Localiza la última ocurrencia de un carácter en una cadena
source_url: https://www.php.net/manual/es/function.mb-strrpos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-strrpos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: 95d055464
order: 45510
---

mb_strrpos

Localiza la última ocurrencia de un carácter en una cadena

## Descripción

```php
mb_strrpos(string $haystack, string $needle, [int $offset], [string $encoding]): int
```php

`mb_strrpos` realiza una búsqueda de tipo `strpos`, teniendo en cuenta los caracteres multioctetos. La posición de `needle` se cuenta a partir del inicio de la cadena `haystack`: las posiciones comienzan en 0.

## Parámetros

`haystack`  
El `string` donde se comprobará, para la última aparición de `needle`.

`needle`  
El `string` a buscar en `haystack`.

`offset`  
Se puede especificar para comenzar la búsqueda en un número arbitrario de caracteres dentro de `haystack`. Los valores negativos detendrán la búsqueda en un punto arbitrario antes del final de `haystack`.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Devuelve la posición numérica de la última ocurrencia del carácter `needle` en la cadena `haystack`. Si `needle` no es encontrado, `mb_strrpos` devuelve `false`.

## Errores/Excepciones

- Si `offset` es mayor que la longitud de `haystack`, se lanzará un `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `needle` ahora acepta una cadena vacía. |
| 8.0.0 | Pasar `encoding` como tercer argumento en lugar de `offset` ha sido eliminado. |
| 8.0.0 | `encoding` ahora acepta `null`. |

## Véase también

`mb_strpos`, `mb_internal_encoding`, `strrpos`
