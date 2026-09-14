---
title: mb_ereg_search_init
description: Configura las cadenas y las expresiones regulares para el soporte de
  caracteres multioctetos
source_url: https://www.php.net/manual/es/function.mb-ereg-search-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-ereg-search-init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 92f1b8b17
order: 45140
---

mb_ereg_search_init

Configura las cadenas y las expresiones regulares para el soporte de caracteres multioctetos

## Descripción

```php
mb_ereg_search_init(string $string, [string $pattern], [string $options]): bool
```php

`mb_ereg_search_init` configura `string` y `pattern` para soportar expresiones regulares multioctetos. Estos valores son utilizados por `mb_ereg_search`, `mb_ereg_search_pos` y `mb_ereg_search_regs`.

## Parámetros

`string`  
La cadena a buscar.

`pattern`  
La máscara de búsqueda.

`options`  
La opción de búsqueda. Para más explicaciones, consulte `mb_regex_set_options`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                            |
|---------|----------------------------------------|
| 8.0.0   | `pattern` y `options` ahora son nulos. |

## Notas

> [!NOTE]
> La codificación interna o la codificación de caracteres especificada por `mb_regex_encoding` se utilizará como codificación de caracteres para esta función.

## Véase también

`mb_regex_encoding`, `mb_ereg_search_regs`
