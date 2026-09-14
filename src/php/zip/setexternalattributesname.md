---
title: ZipArchive::setExternalAttributesName
description: Establece los atributos externos de una entrada definida por su nombre
source_url: https://www.php.net/manual/es/ziparchive.setexternalattributesname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/setexternalattributesname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108560
---

ZipArchive::setExternalAttributesName

Establece los atributos externos de una entrada definida por su nombre

## Descripción

```php
public ZipArchive::setExternalAttributesName(string $name, int $opsys, int $attr, [int $flags]): bool
```php

Establece los atributos externos de una entrada definida por su nombre.

## Parámetros

`name`  
El nombre de la entrada.

`opsys`  
El código del sistema operativo definido por una de las constantes ZipArchive::OPSYS\_.

`attr`  
Los atributos externos. El valor depende del sistema operativo.

`flags`  
Banderas opcionales. Actualmente no se utiliza.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Este ejemplo abre un archivo comprimido ZIP `test.zip` y añade el fichero `test.txt` con sus permisos Unix como atributos externos.

Archivar un fichero, con sus permisos Unix

```
<?php
$zip = new ZipArchive();
$stat = stat($filename='test.txt');
if (is_array($stat) && $zip->open('test.zip', ZipArchive::CREATE) === TRUE) {
    $zip->addFile($filename);
    $zip->setExternalAttributesName($filename, ZipArchive::OPSYS_UNIX, $stat['mode'] << 16);
    $zip->close();
    echo "Ok\n";
} else {
    echo "KO\n";
}
?>

   
```php
