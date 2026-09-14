---
title: Phar::getSupportedCompression
description: Devuelve un array de los algoritmos de compresión soportados
source_url: https://www.php.net/manual/es/phar.getsupportedcompression.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/getSupportedCompression.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64150
---

Phar::getSupportedCompression

Devuelve un array de los algoritmos de compresión soportados

## Descripción

```php
final public static Phar::getSupportedCompression(): array
```php

## Parámetros

No se admiten argumentos.

## Valores devueltos

Devuelve un array que contiene uno de los algoritmos `Phar::GZ` o `Phar::BZ2`, según la disponibilidad de la extensión [zlib](#book.zlib) o de la extensión [bz2](#book.bzip2).

## Véase también

`PharFileInfo::getCompressedSize`, `PharFileInfo::isCompressed`, `PharFileInfo::compress`, `PharFileInfo::decompress`, `Phar::compress`, `Phar::decompress`, `Phar::canCompress`, `Phar::isCompressed`, `Phar::compressFiles`, `Phar::decompressFiles`
