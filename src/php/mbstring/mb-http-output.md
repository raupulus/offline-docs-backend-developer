---
title: mb_http_output
description: Lee/modifica la codificación de visualización
source_url: https://www.php.net/manual/es/function.mb-http-output.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-http-output.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: d553fa369
order: 45240
---

mb_http_output

Lee/modifica la codificación de visualización

## Descripción

```php
mb_http_output([string $encoding]): string
```php

Lee/modifica la codificación de visualización. La visualización después de la llamada a esta función será convertida desde la codificación interna hacia la codificación proporcionada por el argumento `encoding`.

## Parámetros

`encoding`  
Si `encoding` es proporcionado, `mb_http_output` utilizará la codificación `encoding` para las visualizaciones HTTP: los caracteres que serán enviados a los clientes web serán convertidos al juego de caracteres `encoding`.

Si `encoding` es omitido, `mb_http_output` devuelve la codificación de visualización actual.

## Valores devueltos

Si el argumento `encoding` es omitido, `mb_http_output` devuelve la codificación HTTP actual. De lo contrario, Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Levanta una excepción ValueError si `encoding` contiene octetos nulos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `mb_http_output` levanta ahora una excepción ValueError si `encoding` contiene octetos nulos. |
| 8.0.0 | `encoding` ahora acepta `null`. |

## Véase también

`mb_internal_encoding`, `mb_http_input`, `mb_detect_order`
