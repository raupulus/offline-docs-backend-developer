---
title: mb_ereg_search_pos
description: Retorna la posición y la longitud del segmento de string que cumple con
  el patrón de expresión regular
source_url: https://www.php.net/manual/es/function.mb-ereg-search-pos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-ereg-search-pos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 92f1b8b17
order: 45150
---

mb_ereg_search_pos

Retorna la posición y la longitud del segmento de string que cumple con el patrón de expresión regular

## Descripción

```php
mb_ereg_search_pos([string $pattern], [string $options]): array
```php

Retorna la posición y la longitud del segmento de string que cumple con el patrón de expresión regular.

El string a utilizar es especificado por `mb_ereg_search_init`. Si no es especificado, se utilizará el anterior.

## Parámetros

`pattern`  
El patrón de búsqueda.

`options`  
La opción de búsqueda. Para más explicaciones, consulte `mb_regex_set_options`.

## Valores devueltos

Un array que contiene dos elementos. El primer elemento es la posición, en bytes, donde comienza la coincidencia relativamente al inicio del string buscado, y el segundo elemento es la longitud, en bytes, de la coincidencia.

Si ocurre un error, `false` será retornado.

## Historial de cambios

| Versión | Descripción                            |
|---------|----------------------------------------|
| 8.0.0   | `pattern` y `options` ahora son nulos. |

## Notas

> [!NOTE]
> La codificación interna o la codificación de caracteres especificada por `mb_regex_encoding` se utilizará como codificación de caracteres para esta función.

## Véase también

`mb_regex_encoding`, `mb_ereg_search_init`
