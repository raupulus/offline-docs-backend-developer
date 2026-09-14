---
title: mb_eregi
description: Expresión regular insensible a mayúsculas/minúsculas con soporte para
  caracteres multioctetos
source_url: https://www.php.net/manual/es/function.mb-eregi.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-eregi.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 9240fafbb
order: 45210
---

mb_eregi

Expresión regular insensible a mayúsculas/minúsculas con soporte para caracteres multioctetos

## Descripción

```php
mb_eregi(string $pattern, string $string, [array $matches]): bool
```php

Ejecuta la expresión regular insensible a mayúsculas/minúsculas con soporte para caracteres multioctetos.

## Parámetros

`pattern`  
La expresión regular.

`string`  
La cadena a buscar.

`matches`  
Si al menos una secuencia es encontrada (eventualmente en los paréntesis capturantes de `pattern`), y la función es llamada con un tercer argumento `matches`, los resultados serán almacenados en `matches`.

`$matches[1]` contendrá el primer paréntesis capturante (aquel que comienza primero), `$matches[2]` contendrá el segundo paréntesis capturante (aquel que comienza después del primero), y así sucesivamente. `$matches[0]` contiene una copia de la cadena.

## Valores devueltos

Devuelve si una correspondencia de `pattern` ha sido encontrada en `string`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función devuelve ahora `true` en caso de éxito. Anteriormente, devolvía la longitud de octeto de la cadena encontrada, si una correspondencia para `pattern` era encontrada en `string` y que `matches` era proporcionado. Si el parámetro opcional `matches` no era proporcionado o que la longitud de la cadena correspondiente era `0`, esta función devolvía `1`. |
| 7.1.0 | `mb_eregi` definirá ahora `matches` como un `array` vacío, si no hay ninguna correspondencia. Anteriormente, `matches` no era modificado en este caso. |

## Notas

> [!NOTE]
> La codificación interna o la codificación de caracteres especificada por `mb_regex_encoding` se utilizará como codificación de caracteres para esta función.

## Véase también

`mb_regex_encoding`, `mb_ereg`
