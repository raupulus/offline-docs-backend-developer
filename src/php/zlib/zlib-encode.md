---
title: zlib_encode
description: Comprime datos con la codificación especificada
source_url: https://www.php.net/manual/es/function.zlib-encode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/zlib-encode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_revision: 02ba67b51
order: 109000
---

zlib_encode

Comprime datos con la codificación especificada

## Descripción

```php
zlib_encode(string $data, int $encoding, [int $level]): string
```php

Comprime datos con la codificación especificada.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`data`  
Los datos a comprimir.

`encoding`  
El algoritmo de compresión. O bien `ZLIB_ENCODING_RAW`, `ZLIB_ENCODING_DEFLATE` o `ZLIB_ENCODING_GZIP`.

`level`  

## Valores devueltos

## Ejemplos

Ejemplo de `zlib_encode`

```
<?php
$str = 'hello world';
$enc = zlib_encode($str, ZLIB_ENCODING_DEFLATE);
echo bin2hex($enc);
?>

   
```php

El ejemplo anterior mostrará:

    789ccb48cdc9c95728cf2fca4901001a0b045d

## Véase también

zlib_decode
