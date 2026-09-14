---
title: mb_ereg_search
description: Búsqueda por expresión regular multioctets
source_url: https://www.php.net/manual/es/function.mb-ereg-search.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-ereg-search.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 92f1b8b17
order: 45180
---

mb_ereg_search

Búsqueda por expresión regular multioctets

## Descripción

```php
mb_ereg_search([string $pattern], [string $options]): bool
```php

Búsqueda por expresión regular multioctets.

## Parámetros

`pattern`  
El patrón de búsqueda.

`options`  
La opción de búsqueda. Para más explicaciones, consúltese `mb_regex_set_options`.

## Valores devueltos

`mb_ereg_search` devuelve `true` si la cadena multioctets coincide con el patrón de expresión regular, o bien `false` en caso contrario. La cadena a estudiar ha sido configurada con la función `mb_ereg_search_init`. Si el patrón `pattern` no está especificado, se utilizará el anterior.

## Historial de cambios

| Versión | Descripción                            |
|---------|----------------------------------------|
| 8.0.0   | `pattern` y `options` ahora son nulos. |

## Notas

> [!NOTE]
> La codificación interna o la codificación de caracteres especificada por `mb_regex_encoding` se utilizará como codificación de caracteres para esta función.

## Véase también

`mb_regex_encoding`, `mb_ereg_search_init`
