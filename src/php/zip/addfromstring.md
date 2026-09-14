---
title: ZipArchive::addFromString
description: Añadir un fichero al archivo ZIP usando su contenido
source_url: https://www.php.net/manual/es/ziparchive.addfromstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/addfromstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108160
---

ZipArchive::addFromString

Añadir un fichero al archivo ZIP usando su contenido

## Descripción

```php
public ZipArchive::addFromString(string $name, string $content, [int $flags]): bool
```php

Añade un fichero al archivo ZIP usando su contenido.

> [!NOTE]
> Para una portabilidad máxima, se recomienda siempre utilizar barras oblicuas (`/`) como separador de directorio en los nombres de archivos zip.

## Parámetros

`name`  
Nombre de la entrada a crear.

`content`  
El contenido a usar para crear la entrada. Es usado en modo binary safe.

`flags`  
Máscara de bits compuesta por `ZipArchive::FL_OVERWRITE`, `ZipArchive::FL_ENC_GUESS`, `ZipArchive::FL_ENC_UTF_8`, `ZipArchive::FL_ENC_CP437`. El comportamiento de estas constantes se describe en la página de [constantes ZIP](#zip.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión                | Descripción        |
|------------------------|--------------------|
| 8.0.0, PECL zip 1.18.0 | Se añadio `flags`. |

## Ejemplos

Añade una entrada al nuevo fichero

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test.zip', ZipArchive::CREATE);
if ($res === TRUE) {
    $zip->addFromString('test.txt', 'el contenido del fichero va aquí');
    $zip->close();
    echo 'ok';
} else {
    echo 'failed';
}
?>

   
```php

Añade un fichero en un directorio dentro de un archivo

```
<?php
$zip = new ZipArchive;
if ($zip->open('test.zip') === TRUE) {
    $zip->addFromString('dir/test.txt', 'el contenido del fichero va aquí');
    $zip->close();
    echo 'ok';
} else {
    echo 'falló';
}
?>

   
```php
