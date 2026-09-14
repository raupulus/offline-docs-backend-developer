---
title: Phar::compressFiles
description: Comprime todos los ficheros del archivo Phar actual
source_url: https://www.php.net/manual/es/phar.compressfiles.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/compressFiles.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 63960
---

Phar::compressFiles

Comprime todos los ficheros del archivo Phar actual

## Descripción

```php
public Phar::compressFiles(int $compression): void
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Para los archivos phar basados en tar, este método lanza una excepción `BadMethodCallException` ya que la compresión de ficheros individuales dentro de un archivo tar no es soportada por el formato de archivo. Utilice `Phar::compress` para comprimir un archivo phar basado en tar en su totalidad.

Para las extensiones phar basadas en Zip, este método comprime todos los ficheros del archivo Phar utilizando la compresión especificada. Las extensiones [zlib](#ref.zlib) o [bzip2](#ref.bzip2) deben estar activadas para aprovechar esta funcionalidad. Asimismo, si uno o varios ficheros ya han sido comprimidos utilizando la compresión bzip2/zlib, la extensión adecuada debe estar activada para descomprimir los ficheros antes de recomprimirlos. Como con todas las funcionalidades que modifican el contenido de un phar, la variable INI [phar.readonly](#ini.phar.readonly) debe estar a off para funcionar.

## Parámetros

`compression`  
La compresión debe ser `Phar::GZ`, `Phar::BZ2` para beneficiarse de la compresión, o bien `Phar::NONE` para eliminar la compresión.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción `BadMethodCallException` si la variable INI [phar.readonly](#ini.phar.readonly) está a on, si la extensión [zlib](#ref.zlib) no está disponible, o si uno o varios ficheros han sido comprimidos con el algoritmo bzip2 y la extensión [bzip2](#ref.bzip2) no está activada.

## Ejemplos

Un ejemplo con `Phar::compressFiles`

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

    string(10) "monfichero.txt"
    bool(false)
    bool(false)
    bool(false)
    string(11) "monfichero2.txt"
    bool(false)
    bool(false)
    bool(false)
    string(10) "monfichero.txt"
    int(4096)
    bool(false)
    bool(true)
    string(11) "monfichero2.txt"
    int(4096)
    bool(false)
    bool(true)

## Véase también

`PharFileInfo::getCompressedSize`, `PharFileInfo::isCompressed`, `PharFileInfo::compress`, `PharFileInfo::decompress`, `Phar::canCompress`, `Phar::isCompressed`, `Phar::decompressFiles`, `Phar::getSupportedCompression`, `Phar::compress`, `Phar::decompress`
