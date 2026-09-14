---
title: mb_regex_set_options
description: Lee y modifica las opciones de las funciones de expresión regular con
  soporte para caracteres multibyte
source_url: https://www.php.net/manual/es/function.mb-regex-set-options.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-regex-set-options.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: 1a025802f
order: 45350
---

mb_regex_set_options

Lee y modifica las opciones de las funciones de expresión regular con soporte para caracteres multibyte

## Descripción

```php
mb_regex_set_options([string $options]): string
```php

Configura las opciones por omisión con los nuevos valores contenidos en `options`, para las funciones de expresión regular con soporte para caracteres multibyte.

## Parámetros

`options`  
Las opciones a definir, en forma de un string donde cada carácter es una opción. Para definir un modo, se debe colocar el carácter que representa este modo al final, el resto de los caracteres serán las opciones. Solo puede definirse un modo, mientras que pueden definirse múltiples opciones.

| Opción | Significado | Historial de cambios |
|----|----|----|
| i | Activa la ambigüedad |  |
| x | Activa los patrones extendidos |  |
| m | El carácter `'.'` también corresponde a nuevas líneas |  |
| s | `'^'` -\> `'\A'`, `'$'` -\> `'\Z'` |  |
| p | Idéntico a las opciones `m` y `s` |  |
| l | Encuentra la correspondencia más larga |  |
| n | Ignora las correspondencias vacías |  |
| e | Utiliza la función `eval` sobre el resultado | Deprecado a partir de PHP 7.1.0 y eliminado a partir de PHP 8.0.0 |

Opciones para la expresión

> [!NOTE]
> La opción `"e"` no tiene efecto cuando es definida por la `mb_regex_set_options`. Úsese con `mb_ereg_replace` o `mb_eregi_replace`.

| Modo | Significado                |
|------|----------------------------|
| j    | Java (Sun java.util.regex) |
| u    | GNU regex                  |
| g    | grep                       |
| c    | Emacs                      |
| r    | Ruby                       |
| z    | Perl                       |
| b    | POSIX Basic regex          |
| d    | POSIX Extended regex       |

Modos de sintaxis de la expresión regular (solo uno puede ser definido)

## Valores devueltos

Las opciones anteriores. Si el parámetro `options` es omitido o `null`, se retornará un string describiendo las opciones actuales.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Si el parámetro `options` es proporcionado y no `null`, se retornan las opciones *anteriores*. Anteriormente, se retornaban las opciones *actuales*. |
| 8.0.0 | `options` ahora es nullable. |
| 8.0.0 | La opción `"e"` ahora lanza una `ValueError`. |
| 7.1.0 | La opción `"e"` ahora emite una `E_DEPRECATED`. |

## Véase también

`mb_split`, `mb_ereg`, `mb_eregi`
