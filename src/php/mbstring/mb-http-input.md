---
title: mb_http_input
description: Detecta el tipo de codificación de caracteres HTTP
source_url: https://www.php.net/manual/es/function.mb-http-input.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-http-input.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: d553fa369
order: 45230
---

mb_http_input

Detecta el tipo de codificación de caracteres HTTP

## Descripción

```php
mb_http_input([string $type]): array
```php

Detecta el tipo de codificación de caracteres HTTP.

## Parámetros

`type`  
El argumento `type` especifica el tipo de entrada HTTP. Puede tomar uno de los siguientes valores: `"G"` para GET, `"P"` para POST, `"C"` para COOKIE, `"S"` para string, `"L"` para la lista, `"I"` para la lista completa (retornará `array`). Si `type` es omitido, tomará el valor del último tipo utilizado.

## Valores devueltos

El nombre de la codificación de caracteres según `type`, o un array de nombres de juegos de caracteres, si `type` es `"I"`. Si `mb_http_input` no procesa la entrada HTTP especificada, retornará `false`.

## Errores/Excepciones

Levanta una excepción ValueError si `type` es inválido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `mb_http_input` ahora levanta una excepción ValueError si `type` es inválido. |
| 8.0.0 | `type` ahora es nullable. |

## Véase también

`mb_internal_encoding`, `mb_http_output`, `mb_detect_order`
