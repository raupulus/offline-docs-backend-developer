---
title: mb_ereg
description: Búsqueda por expresión regular con soporte para caracteres multibyte
source_url: https://www.php.net/manual/es/function.mb-ereg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-ereg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 9240fafbb
order: 45190
---

mb_ereg

Búsqueda por expresión regular con soporte para caracteres multibyte

## Descripción

```php
mb_ereg(string $pattern, string $string, [array $matches]): bool
```php

Búsqueda por expresión regular con soporte para caracteres multibyte.

## Parámetros

`pattern`  
El patrón de búsqueda.

`string`  
La cadena sobre la que se realiza la búsqueda.

`matches`  
Si se encuentran coincidencias para las subcadenas entre paréntesis de `pattern` y si la función es llamada con el tercer argumento `matches`, las coincidencias serán almacenadas en los elementos del array `matches`. Si no se encuentra ninguna coincidencia, `matches` tendrá como valor un array vacío.

`$matches[1]` contendrá la subcadena que comienza en la primera paréntesis izquierdo; `$matches[2]` contendrá la subcadena que comienza en la segunda, y así sucesivamente. `$matches[0]` contendrá una copia de la cadena completa coincidente.

## Valores devueltos

Devuelve si se ha encontrado una coincidencia de `pattern` en `string`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función devuelve ahora `true` en caso de éxito. Anteriormente, devolvía la longitud en bytes de la cadena encontrada, si se encontraba una coincidencia para `pattern` en `string` y si se proporcionaba `matches`. Si el parámetro opcional `matches` no se proporcionaba o si la longitud de la cadena coincidente era `0`, esta función devolvía `1`. |
| 7.1.0 | `mb_ereg` ahora asignará `matches` a un `array` vacío, si no hay coincidencias. Anteriormente, los `matches` no se modificaban en este caso. |

## Notas

> [!NOTE]
> La codificación interna o la codificación de caracteres especificada por `mb_regex_encoding` se utilizará como codificación de caracteres para esta función.

## Véase también

`mb_regex_encoding`, `mb_eregi`
