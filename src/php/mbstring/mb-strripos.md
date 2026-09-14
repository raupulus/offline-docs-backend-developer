---
title: mb_strripos
description: Encuentra la posición de la última ocurrencia de una cadena en otra,
  sin tener en cuenta la casilla
source_url: https://www.php.net/manual/es/function.mb-strripos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-strripos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: 95d055464
order: 45500
---

mb_strripos

Encuentra la posición de la última ocurrencia de una cadena en otra, sin tener en cuenta la casilla

## Descripción

```php
mb_strripos(string $haystack, string $needle, [int $offset], [string $encoding]): int
```php

`mb_strripos` realiza una operación `strripos` basada en el número de caracteres. La posición `needle` se cuenta desde el inicio de `haystack`. La posición del primer carácter es 0. El segundo tiene como posición 1, etc. A diferencia de `mb_strrpos`, `mb_strripos` no es sensible a la casilla.

## Parámetros

`haystack`  
La cadena desde la cual se recupera la posición de la última ocurrencia de `needle`.

`needle`  
La cadena a buscar en `haystack`.

`offset`  
Se puede especificar para comenzar la búsqueda en un número arbitrario de caracteres dentro de `haystack`. Los valores negativos detendrán la búsqueda en un punto arbitrario antes del final de `haystack`.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Devuelve la posición numérica de la última ocurrencia de `needle` en la cadena `haystack`, o `false` si `needle` no es encontrado.

## Errores/Excepciones

- Si `offset` es mayor que la longitud de `haystack`, se lanzará un `ValueError`.

## Historial de cambios

| Versión | Descripción                             |
|---------|-----------------------------------------|
| 8.0.0   | `needle` ahora acepta una cadena vacía. |
| 8.0.0   | `encoding` ahora acepta `null`.         |

## Véase también

`strripos`, `strrpos`, `mb_strrpos`
