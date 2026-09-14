---
title: PharData::buildFromIterator
description: Construye un archivo tar o zip a partir de un iterador
source_url: https://www.php.net/manual/es/phardata.buildfromiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/buildFromIterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64480
---

PharData::buildFromIterator

Construye un archivo tar o zip a partir de un iterador

## Descripción

```php
public PharData::buildFromIterator(Traversable $iterator, [string $baseDirectory]): array
```php

Rellena un archivo tar o zip a partir de un iterador. Dos estilos de iteradores son soportados, los iteradores que hacen corresponder la ruta de archivo dentro del archivo con la ruta en el disco y los iteradores como DirectoryIterator que devuelven objetos SplFileInfo. Para los iteradores que devuelven objetos SplFileInfo, el segundo argumento es requerido.

## Parámetros

`iterator`  
Cualquier iterador que haga corresponder de forma asociativa un archivo tar/zip o que devuelva objetos SplFileInfo

`baseDirectory`  
Para los iteradores que devuelven objetos SplFileInfo, la parte del camino completo hacia el archivo a eliminar al añadir al archivo tar/zip

## Valores devueltos

`PharData::buildFromIterator` devuelve un array asociativo que hace corresponder una ruta de archivo interna con una ruta completa hacia el archivo en el sistema de archivos.

## Errores/Excepciones

Este método devuelve una excepción `UnexpectedValueException` cuando el iterador devuelve valores incorrectos, como una clave entera en lugar de una cadena, una excepción `BadMethodCallException` cuando se pasa un iterador basado en SplFileInfo sin el argumento `baseDirectory`, o una excepción `PharException` si se han encontrado errores al guardar el archivo phar.

## Historial de cambios

| Versión | Descripción                                               |
|---------|-----------------------------------------------------------|
| 8.1.0   | PharData::buildFromIterator ya no devuelve `false` ahora. |
| 8.0.0   | `baseDirectory` ahora es nullable.                        |

## Ejemplos

Ejemplo con `PharData::buildFromIterator` y SplFileInfo

Para la mayoría de los archivos tar/zip, el archivo reflejará la estructura de directorio actual y el segundo estilo es el más útil. Por ejemplo, para crear un archivo tar/zip que contenga los archivos con la estructura de directorio a continuación:

    /chemin/vers/projet/
                     config/
                            dist.xml
                            debug.xml
                     lib/
                         fichier1.php
                         fichier2.php
                     src/
                         processthing.php
                     www/
                         index.php
                     cli/
                         index.php

        

Este código puede ser utilizado para añadir archivos a el archivo "projet.tar" tar:

```
<?php
$phar = new PharData('projet.tar');
$phar->buildFromIterator(
    new RecursiveIteratorIterator(
     new RecursiveDirectoryIterator('/chemin/vers/projet')),
    '/chemin/vers/projet');
?>

    
```php

El archivo `projet.tar` puede entonces ser borrado inmediatamente. `PharData::buildFromIterator` no establece parámetros como la compresión, las metadatos, lo cual puede ser hecho después de haber creado el archivo tar/zip.

Se debe notar que `Phar::buildFromIterator` también puede ser utilizado para copiar el contenido de un archivo phar, tar o zip existente, ya que el objeto PharData es derivado de `DirectoryIterator`:

```
<?php
$phar = new PharData('projet.tar');
$phar->buildFromIterator(
    new RecursiveIteratorIterator(
     new Phar('/chemin/vers/unautrephar.phar')),
    'phar:///chemin/vers/unautrephar.phar/chemin/vers/projet');
$phar->setStub($phar->createDefaultStub('cli/index.php', 'www/index.php'));
?>

    
```php

Ejemplo con `PharData::buildFromIterator` y otros iteradores

La segunda forma de iterador puede ser utilizada con cualquier iterador que devuelva una asociación clave =\> valor, tal como `ArrayIterator`:

```
<?php
$phar = new PharData('projet.tar');
$phar->buildFromIterator(
    new ArrayIterator(
     array(
        'interne/fichier.php' => dirname(__FILE__) . '/unfichier.php',
        'unautre/fichier.jpg' => fopen('/chemin/vers/grosfichier.jpg', 'rb'),
     )));
?>

    
```php

## Véase también

`Phar::buildFromIterator`
