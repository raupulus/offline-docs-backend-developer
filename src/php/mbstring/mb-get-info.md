---
title: mb_get_info
description: Lee la configuración interna de la extensión mbstring
source_url: https://www.php.net/manual/es/function.mb-get-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-get-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: db22a7cfc
order: 45220
---

mb_get_info

Lee la configuración interna de la extensión mbstring

## Descripción

```php
mb_get_info([string $type]): array
```php

`mb_get_info` lee la configuración interna de la extensión mbstring.

## Parámetros

`type`  
Si `type` no se solicita explícitamente, o si vale `"all"`, `"all"`, `"internal_encoding"`, `"http_input"`, `"http_output"`, `"http_output_conv_mimetypes"`, `"mail_charset"`, `"mail_header_encoding"`, `"mail_body_encoding"`, `"illegal_chars"`, `"encoding_translation"`, `"language"`, `"detect_order"`, `"substitute_character"` y `"strict_detection"` se devolverá.

Si `type` se especifica como `"internal_encoding"`, `"http_input"`, `"http_output"`, `"http_output_conv_mimetypes"`, `"mail_charset"`, `"mail_header_encoding"`, `"mail_body_encoding"`, `"illegal_chars"`, `"encoding_translation"`, `"language"`, `"detect_order"`, `"substitute_character"` o `"strict_detection"` se devolverá el parámetro especificado.

## Valores devueltos

Un `array` de información si `type` no se especifica, de lo contrario, un `type` específico, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Los `type`s `"func_overload"` y `"func_overload_list"` ya no son soportados. |

## Véase también

`mb_regex_encoding`, `mb_http_output`
