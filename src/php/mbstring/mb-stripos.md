---
title: mb_stripos
description: Encuentra la primera ocurrencia de una cadena en otra, sin tener en cuenta
  la casilla
source_url: https://www.php.net/manual/es/function.mb-stripos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-stripos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: 95d055464
order: 45440
---

mb_stripos

Encuentra la primera ocurrencia de una cadena en otra, sin tener en cuenta la casilla

## Descripción

```php
mb_stripos(string $haystack, string $needle, [int $offset], [string $encoding]): int
```php

`mb_stripos` devuelve la posición numérica de la primera ocurrencia de `needle` en la cadena `haystack`. A diferencia de `mb_strpos`, `mb_stripos` no distingue entre mayúsculas y minúsculas. Si `needle` no es encontrado, la función devolverá `false`.

## Parámetros

`haystack`  
La cadena desde la cual se obtiene la posición de la primera ocurrencia de `needle`

`needle`  
La cadena a buscar en `haystack`

`offset`  
La posición en `haystack` donde se debe comenzar a buscar. Una posición negativa cuenta desde el final de la `string`.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Devuelve la posición numérica de la primera ocurrencia de `needle` en la cadena `haystack` o `false` si `needle` no es encontrado.

## Errores/Excepciones

- Si `offset` es mayor que la longitud de `haystack`, se lanzará un `ValueError`.

## Historial de cambios

| Versión | Descripción                                 |
|---------|---------------------------------------------|
| 8.0.0   | `needle` ahora acepta una cadena vacía.     |
| 8.0.0   | `encoding` ahora acepta `null`.             |
| 7.1.0   | Se añadió soporte para `offset`s negativos. |

## Véase también

`stripos`, `strpos`, `mb_strpos`
