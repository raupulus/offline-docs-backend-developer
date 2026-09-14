---
title: gzencode
description: Crea una cadena comprimida con gzip
source_url: https://www.php.net/manual/es/function.gzencode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzencode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: f9c4a68ef
order: 108770
---

gzencode

Crea una cadena comprimida con gzip

## Descripción

```php
gzencode(string $data, [int $level], [int $encoding]): string
```php

Esta función retorna una versión comprimida de la `data` de entrada, compatible con la salida del programa `gzip`.

Para más información sobre el formato de archivo GZIP, ver el documento: [Especificación del formato de archivo GZIP versión 4.3](https://datatracker.ietf.org/doc/html/rfc1952) (RFC 1952).

## Parámetros

`data`  
Los datos a codificar.

`level`  
El nivel de compresión. Se puede dar como 0 para ninguna compresión, hasta 9 para la máxima compresión. Si no se incluye, se utilizará el nivel de compresión por defecto de la librería zlib.

`encoding`  
El modo de codificación. Puede ser `FORCE_GZIP` (por defecto) o `FORCE_DEFLATE`.

`FORCE_DEFLATE` genera una salida que cumple el RFC 1950, consistente en un encabezado zlib, los datos comprimidos y una suma de control Adler.

## Valores devueltos

La cadena codificada o `false` si ocurre un error.

## Ejemplos

Los datos resultantes contienen los encabezados y estructura de datos apropiados para construir un archivo .gz estándar, por ejemplo:

Creando un archivo gzip

```
<?php
$data = file_get_contents("bigfile.txt");
$gzdata = gzencode($data, 9);
file_put_contents("bigfile.txt.gz", $gzdata);
?>

    
```php

## Véase también

`gzdecode`, `gzdeflate`, `gzinflate`, `gzuncompress`, `gzcompress`, [ Especificación del formato ZLIB de compresión de datos (RFC 1950) ](https://datatracker.ietf.org/doc/html/rfc1950)
