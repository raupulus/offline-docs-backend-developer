---
title: mb_strrichr
description: Encuentra la última ocurrencia de un carácter de una cadena en otra,
  sin distinción de mayúsculas y minúsculas
source_url: https://www.php.net/manual/es/function.mb-strrichr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-strrichr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: 8c262f2df
order: 45490
---

mb_strrichr

Encuentra la última ocurrencia de un carácter de una cadena en otra, sin distinción de mayúsculas y minúsculas

## Descripción

```php
mb_strrichr(string $haystack, string $needle, [bool $before_needle], [string $encoding]): string
```php

`mb_strrichr` encuentra la última ocurrencia de `needle` en `haystack` y devuelve la porción de `haystack`. A diferencia de `mb_strrchr`, `mb_strrichr` no distingue entre mayúsculas y minúsculas. Si `needle` no se encuentra, la función devolverá `false`.

## Parámetros

`haystack`  
La cadena desde la cual se debe buscar la última ocurrencia de `needle`.

`needle`  
La cadena a buscar en `haystack`.

`before_needle`  
Determina qué porción de `haystack` devuelve esta función. Si se establece en `true`, la función devuelve toda la cadena `haystack` desde el principio hasta la última ocurrencia de `needle`. Si se establece en `false`, la función devuelve toda la cadena `haystack` desde la última ocurrencia de `needle` hasta el final.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Devuelve la porción de `haystack`. o `false` si `needle` no se encuentra.

## Historial de cambios

| Versión | Descripción                             |
|---------|-----------------------------------------|
| 8.0.0   | `needle` ahora acepta una cadena vacía. |
| 8.0.0   | `encoding` ahora acepta `null`.         |

## Véase también

`mb_stristr`, `mb_strrchr`
