---
title: Phar::compress
description: Comprime el archivo Phar completo utilizando la compresión Gzip o Bzip2
source_url: https://www.php.net/manual/es/phar.compress.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/compress.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 63950
---

Phar::compress

Comprime el archivo Phar completo utilizando la compresión Gzip o Bzip2

## Descripción

```php
public Phar::compress(int $compression, [string $extension]): Phar
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

En el caso de los archivos phar basados en tar o en phar, este método comprime el archivo completo utilizando la compresión gzip o bzip2. El archivo resultante puede ser procesado con el comando gzip/bzip2, o accedido directamente y de forma transparente con la extensión Phar.

En el caso de los archivos phar basados en Zip, este método falla lanzando una excepción. La extensión [zlib](#ref.zlib) debe estar activada para comprimir con gzip, mientras que la extensión [bzip2](#ref.bzip2) debe estar activada para comprimir con bzip2. Al igual que con todas las funcionalidades que modifican el contenido de un phar, la variable INI [phar.readonly](#ini.phar.readonly) debe estar a off para funcionar.

Además, este método renombra automáticamente el archivo, añadiendo a su nombre `.gz`, `.bz2` o eliminando la extensión si `Phar::NONE` es pasado para eliminar la compresión. De lo contrario, una extensión de archivo puede también ser especificada utilizando el segundo parámetro.

## Parámetros

`compression`  
La compresión debe ser `Phar::GZ`, `Phar::BZ2` para beneficiarse de la compresión, o bien `Phar::NONE` para eliminar la compresión.

`extension`  
Por omisión, la extensión es `.phar.gz` o `.phar.bz2` para comprimir los archivos phar, y `.phar.tar.gz` o `.phar.tar.bz2` para comprimir los archivos tar. Para descomprimir, las extensiones por omisión son `.phar` y `.phar.tar`.

## Valores devueltos

Devuelve un objeto `Phar`, o `null` en caso de error.

## Errores/Excepciones

Levanta una excepción `BadMethodCallException` si la variable INI [phar.readonly](#ini.phar.readonly) está a on, si la extensión [zlib](#ref.zlib) no está disponible, o si la extensión [bzip2](#ref.bzip2) no está activada.

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.0   | `extension` ahora es nullable. |

## Ejemplos

Un ejemplo con `Phar::compress`

```
<?php
$p = new Phar('/ruta/al/mon.phar', 0, 'mon.phar');
$p['monfichier.txt'] = 'hola';
$p['monfichier2.txt'] = 'hola';
$p1 = $p->compress(Phar::GZ); // copia a /ruta/al/mon.phar.gz
$p2 = $p->compress(Phar::BZ2); // copia a /ruta/al/mon.phar.bz2
$p3 = $p2->compress(Phar::NONE); // excepción: /ruta/al/mon.phar ya existe
?>

    
```php

## Véase también

`PharFileInfo::getCompressedSize`, `PharFileInfo::isCompressed`, `PharFileInfo::compress`, `PharFileInfo::decompress`, `PharData::compress`, `Phar::canCompress`, `Phar::isCompressed`, `Phar::decompress`, `Phar::getSupportedCompression`, `Phar::compressFiles`, `Phar::decompressFiles`
