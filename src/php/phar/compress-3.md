---
title: PharFileInfo::compress
description: Comprime la entrada Phar actual con una de las compresiones zlib o bzip2
source_url: https://www.php.net/manual/es/pharfileinfo.compress.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharFileInfo/compress.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: c8ba91f7e
order: 64720
---

PharFileInfo::compress

Comprime la entrada Phar actual con una de las compresiones zlib o bzip2

## Descripción

```php
public PharFileInfo::compress(int $compression): true
```php

Este método comprime el fichero dentro del archivo Phar utilizando una de las compresiones bzip2 o zlib. Las extensiones [bzip2](#ref.bzip2) o [zlib](#ref.zlib) deben estar activadas para aprovechar esta funcionalidad. Además, si el fichero ya está comprimido, la extensión adecuada debe estar activada para descomprimirlo. Al igual que con todas las funcionalidades que modifican el contenido de un phar, la variable INI [phar.readonly](#ini.phar.readonly) debe estar a off para tener éxito si el fichero está dentro de un archivo `Phar`. Los ficheros dentro de archivos `PharData` no tienen esta restricción.

## Parámetros

`compression`  
La compresión debe ser `Phar::GZ` o `Phar::BZ2`.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Levanta una excepción `BadMethodCallException` si la variable INI [phar.readonly](#ini.phar.readonly) está a on, o si la extensión [bzip2](#ref.bzip2)/[zlib](#ref.zlib) no está disponible.

## Ejemplos

Un ejemplo con `PharFileInfo::compress`

```
<?php
try {
    $p = new Phar('/ruta/hacia/mifichero.phar', 0, 'mifichero.phar');
    $p['mifichero.txt'] = 'hola';
    $file = $p['mifichero.txt'];
    var_dump($file->isCompressed(Phar::BZ2));
    $p['mifichero.txt']->compress(Phar::BZ2);
    var_dump($file->isCompressed(Phar::BZ2));
} catch (Exception $e) {
    echo 'No puede crear/modificar mifichero.phar : ', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

`PharFileInfo::getCompressedSize`, `PharFileInfo::isCompressed`, `PharFileInfo::decompress`, `Phar::canCompress`, `Phar::isCompressed`, `Phar::compressFiles`, `Phar::decompressFiles`, `Phar::compress`, `Phar::decompress`, `Phar::getSupportedCompression`
