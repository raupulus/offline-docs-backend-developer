---
title: mb_strrchr
description: Encuentra la última ocurrencia de un carácter de una cadena en otra
source_url: https://www.php.net/manual/es/function.mb-strrchr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-strrchr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: 8c262f2df
order: 45480
---

mb_strrchr

Encuentra la última ocurrencia de un carácter de una cadena en otra

## Descripción

```php
mb_strrchr(string $haystack, string $needle, [bool $before_needle], [string $encoding]): string
```php

`mb_strrchr` encuentra la última ocurrencia de `needle` en `haystack` y devuelve la porción de `haystack`. Si `needle` no es encontrado, la función devolverá `false`.

## Parámetros

`haystack`  
La cadena desde la cual se debe recuperar la última ocurrencia de `needle`.

`needle`  
La cadena a encontrar en `haystack`.

`before_needle`  
Determina qué porción de `haystack` esta función devuelve. Si se define como `true`, la función devuelve toda la cadena `haystack` desde el inicio hasta la última ocurrencia de `needle`. Si se define como `false`, la función devuelve toda la cadena `haystack` desde la última ocurrencia de `needle` hasta el final.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Devuelve la porción de `haystack`. o `false` si `needle` no es encontrado.

## Historial de cambios

| Versión | Descripción                             |
|---------|-----------------------------------------|
| 8.0.0   | `needle` ahora acepta una cadena vacía. |
| 8.0.0   | `encoding` ahora acepta `null`.         |

## Véase también

`strrchr`, `mb_strstr`, `mb_strrichr`
