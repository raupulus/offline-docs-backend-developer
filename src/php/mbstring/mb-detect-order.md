---
title: mb_detect_order
description: Lee/modifica el orden de detección de codificaciones
source_url: https://www.php.net/manual/es/function.mb-detect-order.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-detect-order.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 92f1b8b17
order: 45050
---

mb_detect_order

Lee/modifica el orden de detección de codificaciones

## Descripción

```php
mb_detect_order([array $encoding]): array
```php

Reemplaza el orden de detección de codificaciones actual por `encoding`.

## Parámetros

`encoding`  
`encoding` es un array, o una lista de codificaciones separadas por comas. Ver las [codificaciones soportadas](#mbstring.supported-encodings).

Si `encoding` es omitido o `null`, `mb_detect_order` devuelve el orden de detección de codificaciones actual en un array.

Esta configuración afecta a las funciones `mb_detect_encoding` y `mb_send_mail`.

Actualmente, `mbstring` soporta los siguientes filtros de detección. Si una secuencia de bytes es inválida para uno de los siguientes filtros, la detección fallará.

`UTF-8`, `UTF-7`, `ASCII`, `EUC-JP`,`SJIS`, `eucJP-win`, `SJIS-win`, `JIS`, `ISO-2022-JP`

Para `ISO-8859-*`, `mbstring` siempre detecta `ISO-8859-*`.

Para `UTF-16`, `UTF-32`, `UCS2` y `UCS4` la detección siempre fallará.

## Valores devueltos

Al definir el orden de detección de codificación, `true` es devuelto en caso de éxito o `false` en caso de fallo.

Al obtener el orden de detección de codificación, un array ordenado de codificaciones es devuelto.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | `encoding` ahora acepta `null`. |

## Ejemplos

Ejemplo con `mb_detect_order`

```
<?php
/* Reemplaza el orden de detección por una lista enumerada */
mb_detect_order("eucjp-win,sjis-win,UTF-8");

/* Reemplaza el orden de detección por un array */
$ary[] = "ASCII";
$ary[] = "JIS";
$ary[] = "EUC-JP";
mb_detect_order($ary);

/* Muestra el orden de detección actual */
echo implode(", ", mb_detect_order());
?>

    
```php

Ejemplo de orden de detección innecesario

    ; Siempre detectado como ISO-8859-1
    detect_order = ISO-8859-1, UTF-8

    ; Siempre detectado como UTF-8, desde que los valores ASCII/UTF-7
    ; son válidos para UTF-8
    detect_order = UTF-8, ASCII, UTF-7

## Véase también

`mb_internal_encoding`, `mb_http_input`, `mb_http_output`, `mb_send_mail`
