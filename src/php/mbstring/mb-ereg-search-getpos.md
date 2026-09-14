---
title: mb_ereg_search_getpos
description: Devuelve la posición de inicio para la siguiente comparación de una expresión
  regular
source_url: https://www.php.net/manual/es/function.mb-ereg-search-getpos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-ereg-search-getpos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: af4410a7e
order: 45120
---

mb_ereg_search_getpos

Devuelve la posición de inicio para la siguiente comparación de una expresión regular

## Descripción

```php
mb_ereg_search_getpos(): int
```php

Devuelve la posición de inicio para la siguiente coincidencia de una expresión regular.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`mb_ereg_search_getpos` devuelve el punto de inicio de la comparación de una expresión regular para `mb_ereg_search`, `mb_ereg_search_pos`, `mb_ereg_search_regs`. La posición está representada mediante bytes desde la cabeza del string.

## Notas

> [!NOTE]
> La codificación interna o la codificación de caracteres especificada por `mb_regex_encoding` se utilizará como codificación de caracteres para esta función.

## Véase también

`mb_regex_encoding`, `mb_ereg_search_setpos`
