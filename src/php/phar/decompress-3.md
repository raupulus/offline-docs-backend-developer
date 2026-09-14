---
title: PharFileInfo::decompress
description: Descomprime la entrada Phar actual dentro del phar
source_url: https://www.php.net/manual/es/pharfileinfo.decompress.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharFileInfo/decompress.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: c8ba91f7e
order: 64740
---

PharFileInfo::decompress

Descomprime la entrada Phar actual dentro del phar

## Descripción

```php
public PharFileInfo::decompress(): true
```php

Este método descomprime el fichero dentro del archivo Phar. Según la forma en que el fichero esté comprimido, las extensiones [bzip2](#ref.bzip2) o [zlib](#ref.zlib) deben estar activadas para aprovechar esta funcionalidad. Al igual que con todas las funcionalidades que modifican el contenido de un phar, la variable INI [phar.readonly](#ini.phar.readonly) debe estar a off para tener éxito si el fichero se encuentra en un archivo `Phar`. Los ficheros dentro de archivos `PharData` no tienen esta restricción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Se genera una excepción `BadMethodCallException` si la variable INI [phar.readonly](#ini.phar.readonly) está a on, o si la extensión [bzip2](#ref.bzip2)/[zlib](#ref.zlib) no está disponible.

## Ejemplos

Ejemplo con `PharFileInfo::decompress`

```
<?php
try {
    $p = new Phar('/ruta/hacia/mon.phar', 0, 'mon.phar');
    $p['monfichier.txt'] = 'hola';
    $file = $p['monfichier.txt'];
    $file->compress(Phar::GZ);
    var_dump($file->isCompressed());
    $p['monfichier.txt']->decompress();
    var_dump($file->isCompressed());
} catch (Exception $e) {
    echo 'No puede crear/modificar mon.phar: ', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    int(4096)
    bool(false)

## Véase también

`PharFileInfo::getCompressedSize`, `PharFileInfo::isCompressed`, `PharFileInfo::compress`, `Phar::canCompress`, `Phar::isCompressed`, `Phar::compressFiles`, `Phar::decompressFiles`, `Phar::compress`, `Phar::decompress`, `Phar::getSupportedCompression`
