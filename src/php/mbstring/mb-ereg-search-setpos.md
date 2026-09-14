---
title: mb_ereg_search_setpos
description: Selecciona el punto de partida para la búsqueda mediante expresión regular
source_url: https://www.php.net/manual/es/function.mb-ereg-search-setpos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-ereg-search-setpos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 92f1b8b17
order: 45170
---

mb_ereg_search_setpos

Selecciona el punto de partida para la búsqueda mediante expresión regular

## Descripción

```php
mb_ereg_search_setpos(int $offset): bool
```php

`mb_ereg_search_setpos` selecciona el punto de partida para la búsqueda que va a realizar la función `mb_ereg_search`.

## Parámetros

`offset`  
La posición a definir. Si es negativa, se cuenta desde el final de la cadena.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                                         |
|---------|-----------------------------------------------------|
| 7.1.0   | Se ha añadido el soporte para un `offset` negativo. |

## Notas

> [!NOTE]
> La codificación interna o la codificación de caracteres especificada por `mb_regex_encoding` se utilizará como codificación de caracteres para esta función.

## Véase también

`mb_regex_encoding`, `mb_ereg_search_init`
