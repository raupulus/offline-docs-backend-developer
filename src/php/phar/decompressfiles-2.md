---
title: PharData::decompressFiles
description: Descomprime todos los ficheros del archivo zip actual
source_url: https://www.php.net/manual/es/phardata.decompressfiles.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/decompressFiles.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: c8ba91f7e
order: 64560
---

PharData::decompressFiles

Descomprime todos los ficheros del archivo zip actual

## Descripción

```php
public PharData::decompressFiles(): true
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Para los archivos basados en tar, este método levanta una excepción `BadMethodCallException`, ya que la compresión individual de los ficheros dentro de un archivo tar no es soportada por el formato de archivo. Utilice `PharData::compress` para comprimir un archivo completo basado en tar.

Para los archivos basados en Zip, este método descomprime todos los ficheros del archivo. Las extensiones [zlib](#ref.zlib) o [bzip2](#ref.bzip2) deben estar activadas para aprovechar esta funcionalidad si al menos uno de los ficheros está comprimido con bzip2/zlib.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Levanta una excepción `BadMethodCallException` si la extensión [zlib](#ref.zlib) no está disponible o si al menos uno de los ficheros está comprimido con bzip2 y la extensión [bzip2](#ref.bzip2) no está activada.

## Ejemplos

Un ejemplo con `PharData::decompressFiles`

```
<?php
$p = new PharData('/ruta/hacia/mion.zip');
$p['mifichero.txt'] = 'hola';
$p['mifichero2.txt'] = 'hola';
$p->compressFiles(Phar::GZ);
foreach ($p as $file) {
    var_dump($file->getFileName());
    var_dump($file->isCompressed());
    var_dump($file->isCompressed(Phar::BZ2));
    var_dump($file->isCompressed(Phar::GZ));
}
$p->decompressFiles();
foreach ($p as $file) {
    var_dump($file->getFileName());
    var_dump($file->isCompressed());
    var_dump($file->isCompressed(Phar::BZ2));
    var_dump($file->isCompressed(Phar::GZ));
}
?>

    
```php

El ejemplo anterior mostrará:

    string(14) "mifichero.txt"
    int(4096)
    bool(false)
    bool(true)
    string(15) "mifichero2.txt"
    int(4096)
    bool(false)
    bool(true)
    string(14) "mifichero.txt"
    bool(false)
    bool(false)
    bool(false)
    string(15) "mifichero2.txt"
    bool(false)
    bool(false)
    bool(false)

## Véase también

`PharFileInfo::getCompressedSize`, `PharFileInfo::isCompressed`, `PharFileInfo::compress`, `PharFileInfo::decompress`, `Phar::canCompress`, `Phar::isCompressed`, `PharData::compressFiles`, `Phar::getSupportedCompression`, `PharData::compress`, `PharData::decompress`
