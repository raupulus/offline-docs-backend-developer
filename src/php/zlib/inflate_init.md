---
title: inflate_init
description: Inicializa un contexto de descompresión incremental
source_url: https://www.php.net/manual/es/function.inflate-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/inflate_init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: true
translation_revision: aa120f36c
order: 108960
---

inflate_init

Inicializa un contexto de descompresión incremental

## Descripción

```php
inflate_init(int $encoding, [array $options]): InflateContext
```php

Inicializa un contexto de descompresión incremental con el `encoding` especificado.

## Parámetros

`encoding`  
Una de las constantes `ZLIB_ENCODING_*`.

`options`  
Un array asociativo que puede contener los siguientes elementos:

`level`  
El nivel de compresión en el rango -1..9; por defecto -1.

`memory`  
El nivel de memoria de compresión en el rango 1..9; por defecto 8.

`window`  
El tamaño de la ventana de compresión (logarítmica) en el rango 8..15; por defecto 15.

`strategy`  
Una de las `ZLIB_FILTERED`, `ZLIB_HUFFMAN_ONLY`, `ZLIB_RLE`, `ZLIB_FIXED` o `ZLIB_DEFAULT_STRATEGY` (por defecto).

`dictionary`  
Un `string` o un `array` de `strings` del diccionario predefinido (por defecto: ningún diccionario predefinido).

## Valores devueltos

Devuelve un contexto de descompresión (`zlib.inflate`) en caso de éxito, o `false` si ocurre un error.

## Errores/Excepciones

Si se pasa un codificación o una opción inválida a `options`, o si el contexto no pudo ser creado, se genera un error de nivel `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función ahora devuelve una instancia de `InflateContext`; anteriormente, se devolvía un `resource`. |

## Notas

> [!CAUTION]
> A diferencia de `gzinflate`, los contextos de inflado incremental no limitan la longitud de los datos decodificados, por lo que no proporcionan ninguna protección automática contra las bombas Zip.

## Véase también

inflate_add

deflate_init
