---
title: mb_ereg_search_regs
description: Retorna el segmento de cadena encontrado por una expresión regular multioctets
source_url: https://www.php.net/manual/es/function.mb-ereg-search-regs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-ereg-search-regs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 92f1b8b17
order: 45160
---

mb_ereg_search_regs

Retorna el segmento de cadena encontrado por una expresión regular multioctets

## Descripción

```php
mb_ereg_search_regs([string $pattern], [string $options]): array
```php

Retorna el segmento de cadena encontrado por una expresión regular multioctets.

## Parámetros

`pattern`  
La máscara de búsqueda.

`options`  
La opción de búsqueda. Para más explicaciones, consulte `mb_regex_set_options`.

## Valores devueltos

`mb_ereg_search_regs` ejecuta la expresión regular `pattern`, y, si un segmento de cadena coincide, lo retorna en un array, cuyo primer elemento es el segmento de cadena encontrado, el segundo el contenido de la primera paréntesis capturante, el tercero el contenido de la segunda paréntesis capturante, etc. La función retorna `false` en caso de error.

## Historial de cambios

| Versión | Descripción                            |
|---------|----------------------------------------|
| 8.0.0   | `pattern` y `options` ahora son nulos. |

## Notas

> [!NOTE]
> La codificación interna o la codificación de caracteres especificada por `mb_regex_encoding` se utilizará como codificación de caracteres para esta función.

## Véase también

`mb_regex_encoding`, `mb_ereg_search_init`
