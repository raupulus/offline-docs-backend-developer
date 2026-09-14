---
title: mb_substr_count
description: Cuenta el número de ocurrencias de una subcadena
source_url: https://www.php.net/manual/es/function.mb-substr-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-substr-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 92f1b8b17
order: 45570
---

mb_substr_count

Cuenta el número de ocurrencias de una subcadena

## Descripción

```php
mb_substr_count(string $haystack, string $needle, [string $encoding]): int
```php

Cuenta el número de ocurrencias de la cadena `needle` en la cadena `haystack`.

## Parámetros

`haystack`  
La cadena a analizar.

`needle`  
La cadena a buscar.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Devuelve el número de veces que la cadena `needle` aparece en la cadena `haystack`.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | `encoding` ahora acepta `null`. |

## Ejemplos

Ejemplo con `mb_substr_count`

```
<?php
echo mb_substr_count("Ceci est un test", "es"); // muestra 2
?>

    
```php

## Véase también

`mb_strpos`, `mb_substr`, `substr_count`
