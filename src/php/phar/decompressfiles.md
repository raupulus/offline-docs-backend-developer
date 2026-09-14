---
title: Phar::decompressFiles
description: Descomprime todos los ficheros del archivo Phar actual
source_url: https://www.php.net/manual/es/phar.decompressfiles.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/decompressFiles.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: c8ba91f7e
order: 64040
---

Phar::decompressFiles

Descomprime todos los ficheros del archivo Phar actual

## Descripción

```php
public Phar::decompressFiles(): true
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Para los archivos phar basados en tar, este método lanza una excepción `BadMethodCallException`, ya que la compresión individual de los ficheros dentro de un archivo tar no es soportada por el formato de archivo. Utilice `Phar::compress` para comprimir en un archivo phar basado en tar en su totalidad.

Para los archivos phar basados en Zip o en phar, este método descomprime todos los ficheros del archivo Phar. Las extensiones [zlib](#ref.zlib) o [bzip2](#ref.bzip2) deben estar activadas para aprovechar esta funcionalidad si alguno de los ficheros está comprimido utilizando la compresión bzip2/zlib. Al igual que con todas las funcionalidades que modifican el contenido de un phar, la variable INI [phar.readonly](#ini.phar.readonly) debe estar a off para que funcione.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Lanza una excepción `BadMethodCallException` si la variable INI [phar.readonly](#ini.phar.readonly) está a on, si la extensión [zlib](#ref.zlib) no está disponible o si alguno de los ficheros está comprimido utilizando la compresión bzip2 y la extensión [bzip2](#ref.bzip2) no está activada.

## Ejemplos

Un ejemplo con `Phar::decompressFiles`

```
<?php
$p = new Phar('/ruta/hacia/mon.phar', 0, 'mon.phar');
$p['monfichier.txt'] = 'hola';
$p['monfichier2.txt'] = 'hola';
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

    string(10) "monfichier.txt"
    int(4096)
    bool(false)
    bool(true)
    string(11) "monfichier2.txt"
    int(4096)
    bool(false)
    bool(true)
    string(10) "monfichier.txt"
    bool(false)
    bool(false)
    bool(false)
    string(11) "monfichier2.txt"
    bool(false)
    bool(false)
    bool(false)

## Véase también

`PharFileInfo::getCompressedSize`, `PharFileInfo::isCompressed`, `PharFileInfo::compress`, `PharFileInfo::decompress`, `Phar::canCompress`, `Phar::isCompressed`, `Phar::compressFiles`, `Phar::getSupportedCompression`, `Phar::compress`, `Phar::decompress`
