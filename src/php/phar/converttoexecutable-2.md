---
title: PharData::convertToExecutable
description: Convierte un archivo tar/zip no ejecutable en un archivo phar ejecutable
source_url: https://www.php.net/manual/es/phardata.converttoexecutable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/convertToExecutable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64530
---

PharData::convertToExecutable

Convierte un archivo tar/zip no ejecutable en un archivo phar ejecutable

## Descripción

```php
public PharData::convertToExecutable([int $format], [int $compression], [string $extension]): Phar
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Este método se utiliza para convertir un archivo tar o zip no ejecutable en un archivo phar ejecutable. Cualquiera de los tres formatos de archivo (phar, tar o zip) puede ser utilizado y la compresión del archivo completo también es posible.

Si no se solicita ningún cambio, este método lanza una excepción `BadMethodCallException`.

En caso de éxito, este método crea un nuevo archivo en el disco y devuelve un objeto `Phar`. El archivo antiguo no se borra del disco, lo cual debe hacerse manualmente una vez finalizado el procesamiento.

## Parámetros

`format`  
El formato debe ser `Phar::PHAR`, `Phar::TAR` o `Phar::ZIP`. Si es `null`, se conservará el formato de archivo actual.

`compression`  
La compresión debe ser `Phar::NONE` para evitar la compresión del archivo completo, `Phar::GZ` para la compresión basada en zlib, y `Phar::BZ2` para la compresión basada en bzip.

`extension`  
Este parámetro se utiliza para sobrescribir la extensión de archivo por defecto del archivo convertido. Tenga en cuenta que todos los archivos basados en tar y zip deben contener `.phar` en su extensión de archivo para poder ser tratados como archivos phar.

En caso de conversión a un archivo basado en phar, las extensiones por defecto son `.phar`, `.phar.gz` o `.phar.bz2` según la compresión especificada. Para los archivos phar basados en tar, las extensiones por defecto son `.phar.tar`, `.phar.tar.gz` y `.phar.tar.bz2`. Para los archivos phar basados en zip, la extensión por defecto es `.phar.zip`.

## Valores devueltos

Este método devuelve un objeto `Phar` en caso de éxito, o `null` en caso de fallo

## Errores/Excepciones

Este método lanza una excepción `BadMethodCallException` cuando no puede comprimir, cuando se ha especificado un método de compresión desconocido, cuando el archivo solicitado está en búfer con `Phar::startBuffering` y no se ha concluido con `Phar::stopBuffering`, lanza una excepción `UnexpectedValueException` si el soporte de escritura está desactivado, y lanza una excepción `PharException` si se han encontrado problemas durante la creación del phar.

## Historial de cambios

| Versión | Descripción                                                |
|---------|------------------------------------------------------------|
| 8.0.0   | `format`, `compression`, y `localName` ahora son nullable. |

## Ejemplos

Un ejemplo con `PharData::convertToExecutable`

Utilizando PharData::convertToExecutable() :

```
<?php
try {
    $tarphar = new PharData('monphar.tar');
    // lo convierte al formato de archivo phar
    // note que monphar.tar *no* se borra
    $phar = $tarphar->convertToExecutable(Phar::PHAR); // crea monphar.phar
    $phar->setStub($phar->createDefaultStub('cli.php', 'web/index.php'));
    // crea monphar.phar.tgz
    $compressed = $tarphar->convertToExecutable(Phar::TAR, Phar::GZ, '.phar.tgz');
} catch (Exception $e) {
    // los errores se manejan aquí
}
?>

    
```php

## Véase también

`Phar::convertToExecutable`, `Phar::convertToData`, `PharData::convertToData`
