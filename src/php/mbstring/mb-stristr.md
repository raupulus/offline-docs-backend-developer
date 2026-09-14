---
title: mb_stristr
description: Encuentra la primera ocurrencia de una cadena en otra, sin tener en cuenta
  la casilla
source_url: https://www.php.net/manual/es/function.mb-stristr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-stristr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: 95d055464
order: 45450
---

mb_stristr

Encuentra la primera ocurrencia de una cadena en otra, sin tener en cuenta la casilla

## Descripción

```php
mb_stristr(string $haystack, string $needle, [bool $before_needle], [string $encoding]): string
```php

`mb_stristr` encuentra la primera ocurrencia de `needle` en `haystack` y devuelve la porción de `haystack`. A diferencia de `mb_strstr`, `mb_stristr` no distingue entre mayúsculas y minúsculas. Si `needle` no se encuentra, la función devolverá `false`.

## Parámetros

`haystack`  
La cadena desde la cual se recupera la primera ocurrencia de `needle`

`needle`  
La cadena a buscar en `haystack`

`before_needle`  
Determina qué porción de `haystack` devuelve esta función. Si se establece en `true`, la función devolverá toda la cadena `haystack` desde el principio hasta la primera ocurrencia de `needle` (`needle` excluido). Si se establece en `false`, la función devolverá toda la cadena `haystack` desde la primera ocurrencia de `needle` hasta el final (`needle` incluido).

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Devuelve la porción de `haystack`, o `false` si `needle` no se encuentra.

## Historial de cambios

| Versión | Descripción                             |
|---------|-----------------------------------------|
| 8.0.0   | `needle` ahora acepta una cadena vacía. |
| 8.0.0   | `encoding` ahora acepta `null`.         |

## Véase también

`stristr`, `strstr`, `mb_strstr`
