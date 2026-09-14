---
title: Phar::decompress
description: Descomprime el archivo tar completo
source_url: https://www.php.net/manual/es/phar.decompress.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/decompress.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64030
---

Phar::decompress

Descomprime el archivo tar completo

## Descripción

```php
public Phar::decompress([string $extension]): Phar
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Para los archivos phar basados en tar y en phar, este método descomprime el archivo completo.

Para los archivos phar basados en Zip, este método falla y lanza una excepción. La extensión [zlib](#ref.zlib) debe estar activa para descomprimir un archivo comprimido con gzip, y la extensión [bzip2](#ref.bzip2) debe estar activa para descomprimir un archivo comprimido con bzip2. Al igual que con todas las funcionalidades que modifican el contenido de un phar, la variable INI [phar.readonly](#ini.phar.readonly) debe estar a off para que funcione.

Además, este método cambia automáticamente la extensión del archivo, `.phar` Por omisión para los archivos phar, o `.phar.tar` para los archivos phar basados en tar. De lo contrario, se puede especificar una extensión de archivo utilizando el segundo argumento.

## Parámetros

`extension`  
Para descomprimir, las extensiones de archivo por omisión son `.phar` y `.phar.tar`. Utilice este argumento para especificar otra extensión de archivo. Cabe señalar que todos los archivos phar ejecutables deben contener `.phar` en su nombre de archivo.

## Valores devueltos

Se devuelve un objeto `Phar` en caso de éxito, o `null` en caso de fallo.

## Errores/Excepciones

Se lanza una excepción `BadMethodCallException` si la variable INI [phar.readonly](#ini.phar.readonly) está a on, si la extensión [zlib](#ref.zlib) no está disponible, o si la extensión [bzip2](#ref.bzip2) no está activada.

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.0   | `extension` ahora es nullable. |

## Ejemplos

Un ejemplo con `Phar::decompress`

```
<?php
$p = new Phar('/ruta/al/mon.phar', 0, 'mon.phar.gz');
$p['monfichero.txt'] = 'hola';
$p['monfichero.txt'] = 'hola';
$p3 = $p2->decompress(); // crea /ruta/al/mon.phar
?>

    
```php

## Véase también

`PharFileInfo::getCompressedSize`, `PharFileInfo::isCompressed`, `PharFileInfo::compress`, `PharFileInfo::decompress`, `PharData::compress`, `Phar::canCompress`, `Phar::isCompressed`, `Phar::compress`, `Phar::getSupportedCompression`, `Phar::compressFiles`, `Phar::decompressFiles`
