---
title: mb_ereg_replace
description: Reemplaza segmentos de cadena mediante expresiones regulares
source_url: https://www.php.net/manual/es/function.mb-ereg-replace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-ereg-replace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 1187e24a8
order: 45110
---

mb_ereg_replace

Reemplaza segmentos de cadena mediante expresiones regulares

## Descripción

```php
mb_ereg_replace(string $pattern, string $replacement, string $string, [string $options]): string
```php

Busca en la cadena `string` las ocurrencias que coinciden con el patrón `pattern`, y las reemplaza con el texto de reemplazo `replacement`.

## Parámetros

`pattern`  
La expresión regular.

Los caracteres multi-octeto pueden ser utilizados en `pattern`.

`replacement`  
El texto de reemplazo.

`string`  
La cadena a analizar.

`options`  
La opción de búsqueda. Para más explicaciones, consulte `mb_regex_set_options`.

## Valores devueltos

La cadena resultante en caso de éxito, o `false` si ocurre un error. Si `string` no es válido para la codificación actual, `null` es devuelto.

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

`mb_regex_encoding`, `mb_eregi_replace`
