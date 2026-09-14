---
title: ZipArchive::deleteName
description: Elimina una entrada en el archivo por su nombre
source_url: https://www.php.net/manual/es/ziparchive.deletename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/deletename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108230
---

ZipArchive::deleteName

Elimina una entrada en el archivo por su nombre

## Descripción

```php
public ZipArchive::deleteName(string $name): bool
```php

Elimina una entrada en el archivo por su nombre

## Parámetros

`name`  
Nombre de la entrada a eliminar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Eliminado un fichero y un directorio desde un archivo, usando nombres

```
<?php
$zip = new ZipArchive;
if ($zip->open('test1.zip') === TRUE) {
    $zip->deleteName('testfromfile.php');
    $zip->deleteName('testDir/');
    $zip->close();
    echo 'ok';
} else {
    echo 'Falló';
}
?>

   
```php
