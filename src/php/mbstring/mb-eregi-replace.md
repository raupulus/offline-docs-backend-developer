---
title: mb_eregi_replace
description: Expresión regular con soporte para caracteres multibyte, sin distinción
  de mayúsculas y minúsculas
source_url: https://www.php.net/manual/es/function.mb-eregi-replace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-eregi-replace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 92f1b8b17
order: 45200
---

mb_eregi_replace

Expresión regular con soporte para caracteres multibyte, sin distinción de mayúsculas y minúsculas

## Descripción

```php
mb_eregi_replace(string $pattern, string $replacement, string $string, [string $options]): string
```php

Analiza la cadena `string` con el patrón de expresión regular `pattern`, luego reemplaza el texto encontrado por `replacement`.

## Parámetros

`pattern`  
La expresión regular. Pueden utilizarse caracteres multibyte. La distinción de mayúsculas y minúsculas será ignorada.

`replacement`  
El texto de sustitución.

`string`  
La cadena a buscar.

`options`  
Las opciones de búsqueda. Ver `mb_regex_set_options` para más detalles.

## Valores devueltos

La cadena resultante, o `false` si ocurre un error. Si `string` no es válido para la codificación actual, se devuelve `null`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `options` ahora es nullable. |
| 7.1.0 | Esta función verifica si `string` es válido para la codificación actual. |
| 7.1.0 | El modificador `e` ahora está obsoleto. |

## Notas

> [!NOTE]
> La codificación interna o la codificación de caracteres especificada por `mb_regex_encoding` se utilizará como codificación de caracteres para esta función.

> [!WARNING]
> Nunca utilice el modificador `e` con datos de entrada no confiables. No se realizará ningún escape automático (como se conoce de `preg_replace`). No tener esto en cuenta probablemente creará vulnerabilidades de ejecución remota de código en la aplicación.

## Véase también

`mb_regex_encoding`, `mb_ereg_replace`
