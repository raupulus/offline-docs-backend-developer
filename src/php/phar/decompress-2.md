---
title: PharData::decompress
description: Descomprime el archivo Phar completo
source_url: https://www.php.net/manual/es/phardata.decompress.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/decompress.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64550
---

PharData::decompress

Descomprime el archivo Phar completo

## Descripción

```php
public PharData::decompress([string $extension]): PharData
```php

Descomprime el archivo completo, si es un archivo tar.

Para los archivos Zip, este método falla y lanza una excepción. La extensión [zlib](#ref.zlib) debe estar activada para descomprimir un archivo comprimido con gzip y la extensión [bzip2](#ref.bzip2) debe estar disponible para descomprimir un archivo comprimido con bzip2.

Además, este método renombra automáticamente la extensión de archivo del archivo, `.tar` por defecto. De lo contrario, una extensión de archivo puede especificarse con el argumento `extension`.

## Parámetros

`extension`  
Para descomprimir, la extensión por defecto es `.tar`. Utilice este argumento para especificar otra extensión de archivo. Tenga en cuenta que solo los archivos ejecutables pueden contener `.phar` en su nombre de archivo.

## Valores devueltos

Un objeto `PharData` es devuelto en caso de éxito, o `null` en caso de fallo.

## Errores/Excepciones

Levanta una excepción `BadMethodCallException` si la extensión [zlib](#ref.zlib) no está disponible o si la extensión [bzip2](#ref.bzip2) no está activada.

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.0   | `extension` ahora es nullable. |

## Ejemplos

Ejemplo con `PharData::decompress`

```
<?php
$p = new PharData('/path/to/my.tar.gz');
$p->decompress(); // crea /path/to/my.tar
?>

    
```php

## Véase también

`PharFileInfo::getCompressedSize`, `PharFileInfo::isCompressed`, `PharFileInfo::compress`, `PharFileInfo::decompress`, `PharData::compress`, `Phar::canCompress`, `Phar::isCompressed`, `PharData::compress`, `Phar::getSupportedCompression`, `PharData::compressFiles`, `PharData::decompressFiles`
