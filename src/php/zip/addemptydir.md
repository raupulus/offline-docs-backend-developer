---
title: ZipArchive::addEmptyDir
description: Añadir un nuevo directorio
source_url: https://www.php.net/manual/es/ziparchive.addemptydir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/addemptydir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108140
---

ZipArchive::addEmptyDir

Añadir un nuevo directorio

## Descripción

```php
public ZipArchive::addEmptyDir(string $dirname, [int $flags]): bool
```php

Añade un directoro vacío en el archivo.

## Parámetros

`dirname`  
El directorio a añadir.

`flags`  
Máscara de bits compuesta por `ZipArchive::FL_ENC_GUESS`, `ZipArchive::FL_ENC_UTF_8`, `ZipArchive::FL_ENC_CP437`. El comportamiento de estas constantes se describe en la página de [constantes ZIP](#zip.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión                | Descripción        |
|------------------------|--------------------|
| 8.0.0, PECL zip 1.18.0 | Se añadio `flags`. |

## Ejemplos

Crea un nuevo directorio en un archivo

```
<?php
$zip = new ZipArchive;
if ($zip->open('test.zip') === TRUE) {
    if($zip->addEmptyDir('newDirectory')) {
        echo 'Creado nuevo directorio root';
    } else {
        echo 'No se puede crear el directorio';
    }
    $zip->close();
} else {
    echo 'falló';
}
?>

   
```php
