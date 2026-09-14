---
title: PharFileInfo::getCompressedSize
description: Devuelve el tamaño actual (con compresión) del fichero dentro del archivo
  Phar
source_url: https://www.php.net/manual/es/pharfileinfo.getcompressedsize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharFileInfo/getCompressedSize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64780
---

PharFileInfo::getCompressedSize

Devuelve el tamaño actual (con compresión) del fichero dentro del archivo Phar

## Descripción

```php
public PharFileInfo::getCompressedSize(): int
```php

Este método devuelve el tamaño del fichero dentro del archivo Phar. Los ficheros no comprimidos devolverán el mismo valor con getCompressedSize que con `filesize`

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El tamaño en bytes del fichero dentro del archivo Phar en el disco.

## Ejemplos

Un ejemplo con `PharFileInfo::getCompressedSize`

```
<?php
try {
    $p = new Phar('/ruta/hacia/mon.phar', 0, 'mon.phar');
    $p['monfichier.txt'] = 'hola';
    $file = $p['monfichier.txt'];
    echo $file->getCompressedSize();
} catch (Exception $e) {
    echo 'La escritura de mon.phar ha fallado: ', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    2

## Véase también

`PharFileInfo::isCompressed`, `PharFileInfo::decompress`, `PharFileInfo::compress`, `Phar::canCompress`, `Phar::isCompressed`, `Phar::compress`, `Phar::decompress`, `Phar::getSupportedCompression`, `Phar::decompressFiles`, `Phar::compressFiles`
