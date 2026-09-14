---
title: gzdeflate
description: Comprime una cadena
source_url: https://www.php.net/manual/es/function.gzdeflate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzdeflate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 108760
---

gzdeflate

Comprime una cadena

## Descripción

```php
gzdeflate(string $data, [int $level], [int $encoding]): string
```php

Esta función comprime la cadena dada utilizando el formato de datos `DEFLATE`.

Para más detalles sobre el algoritmo de compresión DEFLATE ver el documento "[Especificación del formato de datos comprimidos DEFLATE versión 1.3](https://datatracker.ietf.org/doc/html/rfc1951)" (RFC 1951).

## Parámetros

`data`  
Los datos a comprimir.

`level`  
El nivel de compresión. Se puede dar desde 0 para ninguna compresión hasta 9 para máxima compresión. Si no se especifica, se utilizará el nivel de compresión por defecto de la librería zlib.

`encoding`  
Una de las constantes `ZLIB_ENCODING_*`.

## Valores devueltos

La cadena comprimida o `false` si ocurre un error.

## Ejemplos

Ejemplo de `gzdeflate`

```
<?php
$compressed = gzdeflate('Compress me', 9);
echo $compressed;
?>

    
```php

## Véase también

`gzinflate`, `gzcompress`, `gzuncompress`, `gzencode`
