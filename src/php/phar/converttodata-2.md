---
title: PharData::convertToData
description: Convierte un archivo phar en un archivo tar o zip no ejecutable
source_url: https://www.php.net/manual/es/phardata.converttodata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/convertToData.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64520
---

PharData::convertToData

Convierte un archivo phar en un archivo tar o zip no ejecutable

## Descripción

```php
public PharData::convertToData([int $format], [int $compression], [string $extension]): PharData
```php

Este método se utiliza para convertir un archivo tar o zip no ejecutable en otro formato no ejecutable.

Si no se solicita ningún cambio, este método, este método lanza una excepción `BadMethodCallException`. Este método debe utilizarse para convertir un archivo tar al formato zip y viceversa. Aunque es posible cambiar la compresión de un archivo tar con este método, es preferible utilizar el método `PharData::compress` para mantener la coherencia a nivel de lógica.

En caso de éxito, este método crea un nuevo archivo en el disco y devuelve un objeto `PharData`. El archivo antiguo no se borra del disco, lo cual debe hacerse manualmente una vez finalizado el procesamiento.

## Parámetros

`format`  
El formato debe ser `Phar::TAR` o `Phar::ZIP`. Si es `null`, se conservará el formato de archivo actual.

`compression`  
La compresión debe ser `Phar::NONE` para evitar la compresión del archivo completo, `Phar::GZ` para la compresión basada en zlib, y `Phar::BZ2` para la compresión basada en bzip.

`extension`  
Este parámetro se utiliza para sobrescribir la extensión de archivo por defecto del archivo convertido. Tenga en cuenta que `.phar` no puede utilizarse en ninguna parte del nombre de archivo de un archivo tar o zip no ejecutable.

En caso de conversión a un archivo phar basado en tar, las extensiones por defecto son `.tar`, `.tar.gz` y `.tar.bz2` según la compresión especificada. Para los archivos basados en zip, la extensión por defecto es `.zip`.

## Valores devueltos

Este método devuelve un objeto `PharData` en caso de éxito, o `null` en caso de fallo.

## Errores/Excepciones

Este método lanza una excepción `BadMethodCallException` cuando no es capaz de comprimir, cuando se ha especificado un método de compresión desconocido, cuando el archivo solicitado está en búfer con `Phar::startBuffering` y no se ha finalizado con `Phar::stopBuffering`, y lanza una excepción `PharException` si se produce algún problema durante la creación del phar.

## Historial de cambios

| Versión | Descripción                                                |
|---------|------------------------------------------------------------|
| 8.0.0   | `format`, `compression`, y `extension` ahora son nullable. |

## Ejemplos

Un ejemplo con `PharData::convertToData`

Utilicemos PharData::convertToData():

```
<?php
try {
    $tarphar = new PharData('monphar.tar');
    // note que monphar.tar no se *borra*
    // al convertirlo al formato tar no ejecutable
    // se crea monphar.zip
    $zip = $tarphar->convertToData(Phar::ZIP);
    // se crea monphar.tbz
    $tgz = $zip->convertToData(Phar::TAR, Phar::BZ2, '.tbz');
    // se crea monphar.phar.tgz
    $phar = $tarphar->convertToData(Phar::PHAR); // lanza una excepción
} catch (Exception $e) {
    // los errores se manejan aquí
}
?>

    
```php

## Véase también

`Phar::convertToExecutable`, `Phar::convertToData`, `PharData::convertToExecutable`
