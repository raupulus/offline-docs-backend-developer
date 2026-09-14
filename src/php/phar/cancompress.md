---
title: Phar::canCompress
description: Determina si la extensión phar soporta la compresión utilizando zip o
  bzip2
source_url: https://www.php.net/manual/es/phar.cancompress.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/canCompress.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 63930
---

Phar::canCompress

Determina si la extensión phar soporta la compresión utilizando zip o bzip2

## Descripción

```php
final public static Phar::canCompress([int $compression]): bool
```php

Este método debe ser utilizado para determinar si la compresión es posible antes de cargar un archivo phar que contiene ficheros comprimidos.

## Parámetros

`compression`  
`Phar::GZ` y `Phar::BZ2` pueden ser utilizadas para determinar si la compresión es posible con zlib o bzip2, respectivamente.

## Valores devueltos

`true` si la compresión/descompresión está disponible, `false` en caso contrario.

## Ejemplos

Un ejemplo con `Phar::canCompress`

```
<?php
if (Phar::canCompress()) {
    echo file_get_contents('phar://pharcompresse.phar/interne/fichero.txt');
} else {
    echo 'compresión no disponible';
}
?>

    
```php

## Véase también

`PharFileInfo::getCompressedSize`, `PharFileInfo::isCompressed`, `PharFileInfo::compress`, `PharFileInfo::decompress`, `Phar::isCompressed`, `Phar::compressFiles`, `Phar::decompressFiles`, `Phar::getSupportedCompression`, `Phar::convertToExecutable`, `Phar::convertToData`
