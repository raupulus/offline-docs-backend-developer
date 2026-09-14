---
title: deflate_init
description: Inicializa un contexto de compresión incremental
source_url: https://www.php.net/manual/es/function.deflate-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/deflate_init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: true
translation_revision: aa120f36c
order: 108720
---

deflate_init

Inicializa un contexto de compresión incremental

## Descripción

```php
deflate_init(int $encoding, [array $options]): DeflateContext
```php

Inicializa un contexto de compresión incremental utilizando el `encoding` especificado.

Es importante señalar que la opción `window` aquí solo define el tamaño de la ventana del algoritmo, diferente de los filtros zlib donde el mismo parámetro también define la codificación a utilizar; la codificación debe ser definida con el parámetro `encoding`.

Limitación: actualmente no hay manera de establecer la información del encabezado en un flujo comprimido GZIP, que se define como sigue: firma GZIP (`\x1f\x8B`); método de compresión (`\x08` == DEFLATE); 6 bytes nulos; el sistema operativo establecido en el sistema actual (`\x00` = Windows, `\x03` = Unix, etc.).

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
El tamaño de la ventana zlib (logarítmico) en el rango `8`..`15`; por defecto `15`. zlib cambia un tamaño de ventana de `8` a `9`, y a partir de zlib 1.2.8 falla con una advertencia, si se solicita un tamaño de ventana de `8` para `ZLIB_ENCODING_RAW` o `ZLIB_ENCODING_GZIP`.

`strategy`  
Una de las `ZLIB_FILTERED`, `ZLIB_HUFFMAN_ONLY`, `ZLIB_RLE`, `ZLIB_FIXED` o `ZLIB_DEFAULT_STRATEGY` (por defecto).

`dictionary`  
Un `string` o un `array` de `strings` del diccionario predefinido (por defecto: ningún diccionario predefinido).

## Valores devueltos

Devuelve un contexto de compresión (`zlib.deflate`) en caso de éxito, o `false` si ocurre un error.

## Errores/Excepciones

Si se pasa una opción inválida a `options` o si el contexto no pudo ser creado, se genera un error de nivel `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función ahora devuelve una instancia de `DeflateContext`; anteriormente, se devolvía un `resource`. |

## Véase también

deflate_add

inflate_init
