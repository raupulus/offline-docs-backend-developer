---
title: Phar::convertToData
description: Convierte un archivo phar en un fichero no ejecutable
source_url: https://www.php.net/manual/es/phar.converttodata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/convertToData.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 63980
---

Phar::convertToData

Convierte un archivo phar en un fichero no ejecutable

## Descripción

```php
public Phar::convertToData([int $format], [int $compression], [string $extension]): PharData
```php

Convierte un archivo phar ejecutable en un fichero tar o zip. Para hacer que el tar o el zip no sea ejecutable, el contenedor phar y el alias phar son eliminados del archivo recién creado.

Si no se especifica ningún cambio, este método lanza una excepción `BadMethodCallException` si el archivo está en el formato de archivo phar. Para los archivos basados en tar o zip, este método convierte el archivo en un archivo no ejecutable.

En caso de éxito, el método crea un nuevo archivo en el disco y devuelve un objeto `PharData`. El archivo antiguo no se elimina del disco, lo cual debe hacerse manualmente al final del proceso.

## Parámetros

`format`  
Debe ser uno de los formatos `Phar::TAR` o `Phar::ZIP`. Si este argumento es `null`, se conservará el formato de archivo actual.

`compression`  
Debe ser `Phar::NONE` para ninguna compresión global, `Phar::GZ` para una compresión basada en zlib y `Phar::BZ2` para una compresión basada en bzip2.

`extension`  
Este argumento se utiliza para sobrescribir la extensión por defecto de un archivo convertido. Cabe señalar que `.phar` no puede ser utilizado en el nombre de archivo de un archivo tar o zip no ejecutable.

Si se convierte a un archivo basado en tar, las extensiones por defecto son `.tar`, `.tar.gz`, y `.tar.bz2` según la compresión especificada. Para los archivos phar basados en zip, la extensión por defecto es `.zip`.

## Valores devueltos

El método devuelve un objeto `PharData` en caso de éxito, o `null` en caso de fallo.

## Errores/Excepciones

Este método lanza una excepción `BadMethodCallException` si no es capaz de comprimir, si se ha especificado un método de compresión desconocido o si el archivo solicitado ha sido almacenado en búfer con `Phar::startBuffering` sin ser concluido con `Phar::stopBuffering`, y lanza una excepción `PharException` si se ha encontrado algún problema durante la fase de creación del archivo.

## Historial de cambios

| Versión | Descripción                                                |
|---------|------------------------------------------------------------|
| 8.0.0   | `format`, `compression`, y `extension` ahora son nullable. |

## Ejemplos

Un ejemplo con `Phar::convertToData`

Utilización de Phar::convertToData():

```
<?php
try {
    $tarphar = new Phar('monphar.phar.tar');
    // note que monphar.phar.tar no es *eliminado*
    // se convierte al formato de archivo tar no ejecutable
    // crea monphar.tar
    $tar = $tarphar->convertToData();
    // se convierte al formato de archivo zip no ejecutable y crea monphar.zip
    $zip = $tarphar->convertToData(Phar::ZIP);
    // crea monphar.tbz
    $tgz = $tarphar->convertToData(Phar::TAR, Phar::BZ2, '.tbz');
    // crea monphar.phar.tgz
    $phar = $tarphar->convertToData(Phar::PHAR); // lanza una excepción
} catch (Exception $e) {
    // se manejan los errores aquí
}
?>

    
```php

## Véase también

`Phar::convertToExecutable`, `PharData::convertToExecutable`, `PharData::convertToData`
