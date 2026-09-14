---
title: mb_strstr
description: Encuentra la primera ocurrencia de una cadena en otra
source_url: https://www.php.net/manual/es/function.mb-strstr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-strstr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: 95d055464
order: 45520
---

mb_strstr

Encuentra la primera ocurrencia de una cadena en otra

## Descripción

```php
mb_strstr(string $haystack, string $needle, [bool $before_needle], [string $encoding]): string
```php

`mb_strstr` encuentra la primera ocurrencia de `needle` en `haystack` y devuelve la porción de `haystack`. Si `needle` no es encontrado, la función devolverá `false`.

## Parámetros

`haystack`  
La cadena en la cual se debe buscar la primera ocurrencia de `needle`

`needle`  
La cadena a buscar en `haystack`

`before_needle`  
Determina qué porción de `haystack` esta función devuelve. Si se define como `true`, la función devolverá toda la cadena `haystack` desde el inicio hasta la primera ocurrencia de `needle` (`needle` excluido). Si se define como `false`, la función devolverá toda la cadena `haystack` desde la primera ocurrencia de `needle` hasta el final (`needle` incluido).

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Devuelve la porción de `haystack`, o `false` si `needle` no es encontrado.

## Historial de cambios

| Versión | Descripción                             |
|---------|-----------------------------------------|
| 8.0.0   | `needle` ahora acepta una cadena vacía. |
| 8.0.0   | `encoding` ahora acepta `null`.         |

## Véase también

`stristr`, `strstr`, `mb_stristr`
