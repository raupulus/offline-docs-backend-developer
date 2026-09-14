---
title: mb_ereg_match
description: Expresión regular POSIX para strings multibyte
source_url: https://www.php.net/manual/es/function.mb-ereg-match.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-ereg-match.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 7fcb23ea9
order: 45090
---

mb_ereg_match

Expresión regular POSIX para strings multibyte

## Descripción

```php
mb_ereg_match(string $pattern, string $string, [string $options]): bool
```php

Ejecuta la expresión regular POSIX para strings multibyte.

> [!NOTE]
> `pattern` se asocia únicamente al inicio de `string`.

## Parámetros

`pattern`  
La expresión regular.

`string`  
El string a evaluar.

`options`  
La opción de búsqueda. Para más explicaciones, consulte `mb_regex_set_options`.

## Valores devueltos

`string` retorna `true` si `string` verifica la expresión regular `pattern`, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 8.0.0   | `options` ahora es nullable. |

## Notas

> [!NOTE]
> La codificación interna o la codificación de caracteres especificada por `mb_regex_encoding` se utilizará como codificación de caracteres para esta función.

## Véase también

`mb_regex_encoding`, `mb_ereg`
