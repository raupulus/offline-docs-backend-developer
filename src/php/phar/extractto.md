---
title: Phar::extractTo
description: Extrae el contenido de un archivo phar hacia un directorio
source_url: https://www.php.net/manual/es/phar.extractto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/extractTo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64080
---

Phar::extractTo

Extrae el contenido de un archivo phar hacia un directorio

## Descripción

```php
public Phar::extractTo(string $directory, [array $files], [bool $overwrite]): bool
```php

Extrae todos los ficheros de un archivo phar hacia el disco. Los ficheros y los directorios extraídos conservan los permisos de manera idéntica a los del interior del archivo. Los parámetros opcionales permiten controlar qué ficheros se extraen y si los ficheros ya existentes en el disco pueden ser sobrescritos. El segundo parámetro `files` puede ser el nombre de un fichero o directorio, o un array de nombres de ficheros y directorios a extraer. Por omisión, este método no sobrescribe los ficheros existentes, el tercer parámetro puede ser pasado a `true` para activar la sobrescritura de ficheros. Este método es idéntico a `ZipArchive::extractTo`.

## Parámetros

`directory`  
Ruta de acceso hacia la cual extraer los ficheros `files`

`files`  
El nombre de un fichero o directorio o un array de ficheros/directorios a extraer, `null` para ignorar este parámetro

`overwrite`  
Pasarlo a `true` para activar la sobrescritura de ficheros existentes

## Valores devueltos

devuelve `true` en caso de éxito, pero es más seguro verificar si se lanzan excepciones, y considerar que todo ha ido bien si ninguna es lanzada.

## Errores/Excepciones

Lanza una excepción `PharException` si ocurren errores durante la escritura en el disco.

## Ejemplos

Ejemplo con `Phar::extractTo`

```
<?php
try {
    $phar = new Phar('monphar.phar');
    $phar->extractTo('/chemin/complet'); // extrae todos los ficheros
    $phar->extractTo('/autre/chemin', 'fichier.txt'); // extrae solo fichier.txt
    $phar->extractTo('/ce/chemin',
        array('fichier1.txt', 'fichier2.txt')); // extrae solo 2 ficheros
    $phar->extractTo('/troisieme/chemin', null, true); // extrae todos los ficheros, sobrescribiendo
} catch (Exception $e) {
    // maneja los errores
}
?>

    
```php

## Notas

> [!NOTE]
> Los sistemas de archivos NTFS de Windows no soportan ciertos caracteres en los nombres de fichero, como `<|>*?":`. Los nombres de fichero con un punto final no son soportados. A diferencia de algunas herramientas de extracción, este método no reemplaza estos caracteres con un guión bajo, sino que falla al extraer tales ficheros.

## Véase también

`PharData::extractTo`
