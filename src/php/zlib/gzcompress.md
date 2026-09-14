---
title: gzcompress
description: Comprime una cadena
source_url: https://www.php.net/manual/es/function.gzcompress.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzcompress.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 108740
---

gzcompress

Comprime una cadena

## Descripción

```php
gzcompress(string $data, [int $level], [int $encoding]): string
```php

Esta función comprime la cadena dada usando el formato de datos `ZLIB`.

Para detalles sobre el algoritmo de compresión ZLIB, ver el documento "[Especificación del formato de datos comprimidos ZLIB versión 3.3](https://datatracker.ietf.org/doc/html/rfc1950)" (RFC 1950).

> [!NOTE]
> Esto *no* es lo mismo que la compresión que gzip, la cuál incluye algunos encabezados de datos. Ver `gzencode` para la compresión gzip.

## Parámetros

`data`  
Los datos a comprimir.

`level`  
El nivel de compresión. Se puede dar como 0 para ninguna compresión, hasta 9 para la máxima compresión.

Si se utiliza -1, se usará la compresión por defecto de la librería zlib la cual es 6.

`encoding`  
Una de las constentes `ZLIB_ENCODING_*`.

## Valores devueltos

La cadena comprimida o `false` si ocurre un error.

## Ejemplos

Ejemplo de `gzcompress`

```
<?php
$compressed = gzcompress('Compress me', 9);
echo $compressed;
?>

    
```php

## Véase también

`gzdeflate`, `gzinflate`, `gzuncompress`, `gzencode`
