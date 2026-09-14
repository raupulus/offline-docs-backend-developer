---
title: sapi_windows_cp_conv
description: Convierte un string de una página de código a otra
source_url: https://www.php.net/manual/es/function.sapi-windows-cp-conv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/sapi-windows-cp-conv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 426d9a8f1
order: 47160
---

sapi_windows_cp_conv

Convierte un string de una página de código a otra

## Descripción

```php
sapi_windows_cp_conv(int $in_codepage, int $out_codepage, string $subject): string
```php

Convierte un string de una página de código a otra.

## Parámetros

`in_codepage`  
La página de código del string `subject`. Puede ser el nombre o el identificador de la página de código.

`out_codepage`  
La página de código a la que se convertirá el string `subject`. Puede ser el nombre o el identificador de la página de código.

`subject`  
El string a convertir.

## Valores devueltos

El string `subject` convertido a `out_codepage`, o `null` en caso de fallo.

## Errores/Excepciones

Esta función emite errores de nivel E_WARNING si se proporcionan páginas de código no válidas, o si el sujeto no es válido para `in_codepage`.

## Véase también

sapi_windows_cp_get

iconv
