---
title: mb_ereg_search_getregs
description: Lee el último segmento de cadena multioctets que coincide con el patrón
source_url: https://www.php.net/manual/es/function.mb-ereg-search-getregs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-ereg-search-getregs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 92f1b8b17
order: 45130
---

mb_ereg_search_getregs

Lee el último segmento de cadena multioctets que coincide con el patrón

## Descripción

```php
mb_ereg_search_getregs(): array
```php

Lee el último segmento de cadena multioctets que coincide con el patrón.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array que incluye todas las sub-caenas que han sido encontradas por `mb_ereg_search`, `mb_ereg_search_pos` y `mb_ereg_search_regs`. Si se ha encontrado una solución, el primer elemento será la sub-caena encontrada, el segundo representará la primera paréntesis capturante, el tercero representará la segunda paréntesis capturante, etc. Esta función devuelve `false` en caso de error.

## Notas

> [!NOTE]
> La codificación interna o la codificación de caracteres especificada por `mb_regex_encoding` se utilizará como codificación de caracteres para esta función.

## Véase también

`mb_regex_encoding`, `mb_ereg_search_init`
