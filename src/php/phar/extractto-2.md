---
title: PharData::extractTo
description: Extrae el contenido de un archivo tar/zip hacia un directorio
source_url: https://www.php.net/manual/es/phardata.extractto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/extractTo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64600
---

PharData::extractTo

Extrae el contenido de un archivo tar/zip hacia un directorio

## Descripción

```php
public PharData::extractTo(string $directory, [array $files], [bool $overwrite]): bool
```php

Extrae todos los ficheros de un archivo tar/zip hacia el disco. Los ficheros y directorios extraídos conservan los permisos tal como en el archivo. Los parámetros opcionales permiten un eventual control sobre qué ficheros serán extraídos y si los ficheros ya existentes en el disco pueden ser sobrescritos. El segundo parámetro `files` puede ser el nombre de un fichero o directorio a extraer, o un array de nombres de ficheros y directorios a extraer. Por omisión, este método no sobrescribirá ningún fichero ya existente, a menos que el tercer parámetro sea `true`. Este método es idéntico a `ZipArchive::extractTo`.

## Parámetros

`directory`  
Ruta donde los ficheros serán extraídos.

`files`  
El nombre de un fichero o directorio a extraer, o un array de ficheros/directorios a extraer

`overwrite`  
Pasarlo a `true` para activar la sobrescritura de ficheros ya existentes

## Valores devueltos

Devuelve `true` en caso de éxito, pero es preferible verificar las excepciones lanzadas y considerar el éxito si ninguna se produce.

## Errores/Excepciones

Lanza una excepción `PharException` si se encuentran errores al escribir los cambios en el disco.

## Ejemplos

Ejemplo con `PharData::extractTo`

```
<?php
try {
    $phar = new PharData('monphar.tar');
    $phar->extractTo('/ruta/completa'); // extrae todos los ficheros
    $phar->extractTo('/otra/ruta', 'fichero.txt'); // extrae solo fichero.txt
    $phar->extractTo('/esta/ruta',
        array('fichero1.txt', 'fichero2.txt')); // extrae solo 2 ficheros
    $phar->extractTo('/tercera/ruta', null, true); // extrae todos los ficheros, sobrescribiendo
} catch (Exception $e) {
    // se manejan los errores
}
?>

    
```php

## Notas

> [!NOTE]
> Los sistemas de archivos NTFS de Windows no soportan ciertos caracteres en los nombres de fichero, como `<|>*?":`. Los nombres de fichero con un punto final no son soportados. A diferencia de algunas herramientas de extracción, este método no reemplaza estos caracteres con un guión bajo, sino que falla al extraer tales ficheros.

## Véase también

`Phar::extractTo`
