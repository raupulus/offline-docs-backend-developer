---
title: Phar::convertToExecutable
description: Convierte un archivo phar a otro formato de archivo de archivo phar ejecutable
source_url: https://www.php.net/manual/es/phar.converttoexecutable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/convertToExecutable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: befe29ff6
order: 63990
---

Phar::convertToExecutable

Convierte un archivo phar a otro formato de archivo de archivo phar ejecutable

## Descripción

```php
public Phar::convertToExecutable([int $format], [int $compression], [string $extension]): Phar
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Este método se utiliza para convertir un archivo phar a otro formato de archivo. Por ejemplo, puede ser utilizado para crear un archivo phar basado en tar a partir de un archivo phar basado en zip o a partir de un archivo phar ejecutable basado en el formato de archivo phar. Asimismo, puede ser utilizado para aplicar una compresión global a un archivo basado en tar o en phar.

Si no se especifica ningún cambio, este método lanza una excepción `BadMethodCallException`.

En caso de éxito, el método crea un nuevo archivo en el disco y devuelve un objeto `Phar`. El archivo antiguo no es eliminado del disco, lo cual debe hacerse manualmente al final del procedimiento.

## Parámetros

`format`  
Debe ser uno de los formatos `Phar::PHAR`, `Phar::TAR`, o `Phar::ZIP`. Si este argumento es `null`, el formato de archivo actual será conservado.

`compression`  
Debe ser `Phar::NONE` para ninguna compresión global, `Phar::GZ` para una compresión basada en zlib y `Phar::BZ2` para una compresión basada en bzip2.

`extension`  
Este argumento se utiliza para sobrescribir la extensión por defecto de un archivo convertido. Cabe señalar que todos los archivos phar basados en zip o en tar deben contener `.phar` en su extensión para ser tratados como un archivo phar.

Si se convierte a un archivo basado en phar, las extensiones por defecto son `.phar`, `.phar.gz`, o `.phar.bz2` según la compresión especificada. Para los archivos phar basados en tar, las extensiones por defecto son `.phar.tar`, `.phar.tar.gz`, y `.phar.tar.bz2`. Para los archivos phar basados en zip, la extensión por defecto es `.phar.zip`.

## Valores devueltos

El método devuelve un objeto `Phar` en caso de éxito, o `null` en caso de fallo.

## Errores/Excepciones

Este método lanza una excepción `BadMethodCallException` si no es capaz de comprimir, si se ha especificado un método de compresión desconocido o si el archivo solicitado ha sido almacenado en búfer con `Phar::startBuffering` sin ser concluido con `Phar::stopBuffering`, lanza una excepción `UnexpectedValueException` si el soporte de escritura ha sido desactivado y lanza una excepción `PharException` si se ha encontrado algún problema durante la fase de creación del archivo.

## Historial de cambios

| Versión | Descripción                                                |
|---------|------------------------------------------------------------|
| 8.0.0   | `format`, `compression`, y `extension` ahora son nullable. |

## Ejemplos

Un ejemplo con `Phar::convertToExecutable`

Utilicemos Phar::convertToExecutable() :

```
<?php
try {
    $tarphar = new Phar('monphar.phar.tar');
    // se convierte al formato de archivo phar
    // note que monphar.phar.tar *no* es borrado
    $phar = $tarphar->convertToExecutable(Phar::PHAR); // crea monphar.phar
    $phar->setStub($phar->createDefaultStub('cli.php', 'web/index.php'));
    // crea monphar.phar.tgz
    $compressed = $phar->convertToExecutable(Phar::TAR, Phar::GZ, '.phar.tgz');
} catch (Exception $e) {
    // se manejan los errores aquí
}
?>

    
```php

## Véase también

`Phar::convertToData`, `PharData::convertToExecutable`, `PharData::convertToData`
