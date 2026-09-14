---
title: ZipArchive::addPattern
description: Añade ficheros de un directorio a partir de un patrón PCRE
source_url: https://www.php.net/manual/es/ziparchive.addpattern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/addpattern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108180
---

ZipArchive::addPattern

Añade ficheros de un directorio a partir de un patrón PCRE

## Descripción

```php
public ZipArchive::addPattern(string $pattern, [string $path], [array $options]): array
```php

Añade ficheros de un directorio que coinciden con la expresión regular `pattern`. La operación no es recursiva. Únicamente se hará la correspondencia del patrón con el nombre del fichero.

## Parámetros

`pattern`  
Un patrón [PCRE](#book.pcre) contra el cual se realizará la correspondencia.

`path`  
El directorio que será escaneado. Por defecto es el directorio de trabajo actual.

`options`  
Un array asociativo de opciones aceptadas por ZipArchive::addGlob.

## Valores devueltos

Un `array` de archivos añadidos en caso de éxito o `false` si ocurre un error

## Ejemplos

Ejemplo con ZipArchive::addPattern

Añadir todos los scripts y ficheros de texto php del directorio actual

```
<?php
$zip = new ZipArchive();
$ret = $zip->open('application.zip', ZipArchive::CREATE | ZipArchive::OVERWRITE);
if ($ret !== TRUE) {
    printf('Erróneo con código %d', $ret);
} else {
    $directory = realpath('.');
    $options = array('add_path' => 'sources/', 'remove_path' => $directory);
    $zip->addPattern('/\.(?:php|txt)$/', $directory, $options);
    $zip->close();
}
?>

   
```php

## Véase también

ZipArchive::addFile, ZipArchive::addGlob
