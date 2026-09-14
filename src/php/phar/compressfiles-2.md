---
title: PharData::compressFiles
description: Comprime todos los ficheros del archivo tar/zip actual
source_url: https://www.php.net/manual/es/phardata.compressfiles.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/compressFiles.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64500
---

PharData::compressFiles

Comprime todos los ficheros del archivo tar/zip actual

## Descripción

```php
public PharData::compressFiles(int $compression): void
```php

Para los archivos basados en tar, este método genera una excepción `BadMethodCallException` ya que la compresión individual de los ficheros de un archivo tar no es soportada por este formato de archivo. Utilice `PharData::compress` para comprimir un archivo basado en tar completo.

Para los archivos basados en Zip, este método comprime todos los ficheros del archivo utilizando la compresión especificada. Las extensiones [zlib](#ref.zlib) o [bzip2](#ref.bzip2) deben estar activadas para aprovechar esta funcionalidad. Además, si al menos un fichero ya está comprimido utilizando la compresión bzip2/zlib, la extensión adecuada debe estar activada para descomprimir los ficheros antes de volver a comprimirlos.

## Parámetros

`compression`  
La compresión debe ser `Phar::GZ` o `Phar::BZ2` para aplicar una compresión, o `Phar::NONE` para eliminarla.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Genera una excepción `BadMethodCallException` si la variable INI [phar.readonly](#ini.phar.readonly) está a on, si la extensión [zlib](#ref.zlib) no está disponible o si al menos un fichero está comprimido vía bzip2 y la extensión [bzip2](#ref.bzip2) no está activada.

## Ejemplos

Un ejemplo con `PharData::compressFiles`

```
<?php
$p = new Phar('/ruta/al/mon.phar', 0, 'mon.phar');
$p['monfichero.txt'] = 'hola';
$p['monfichero2.txt'] = 'hola';
foreach ($p as $file) {
    var_dump($file->getFileName());
    var_dump($file->isCompressed());
    var_dump($file->isCompressed(Phar::BZ2));
    var_dump($file->isCompressed(Phar::GZ));
}
$p->compressFiles(Phar::GZ);
foreach ($p as $file) {
    var_dump($file->getFileName());
    var_dump($file->isCompressed());
    var_dump($file->isCompressed(Phar::BZ2));
    var_dump($file->isCompressed(Phar::GZ));
}
?>

    
```php

El ejemplo anterior mostrará:

    string(14) "monfichero.txt"
    bool(false)
    bool(false)
    bool(false)
    string(15) "monfichero2.txt"
    bool(false)
    bool(false)
    bool(false)
    string(14) "monfichero.txt"
    int(4096)
    bool(false)
    bool(true)
    string(15) "monfichero2.txt"
    int(4096)
    bool(false)
    bool(true)

## Véase también

`PharFileInfo::getCompressedSize`, `PharFileInfo::isCompressed`, `PharFileInfo::compress`, `PharFileInfo::decompress`, `Phar::canCompress`, `Phar::isCompressed`, `PharData::decompressFiles`, `Phar::getSupportedCompression`, `PharData::compress`, `PharData::decompress`
