---
title: ZipArchive::getFromName
description: Devuelve el contenido de la entrada utilizando su nombre
source_url: https://www.php.net/manual/es/ziparchive.getfromname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/getfromname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108320
---

ZipArchive::getFromName

Devuelve el contenido de la entrada utilizando su nombre

## Descripción

```php
public ZipArchive::getFromName(string $name, [int $len], [int $flags]): string
```php

Devuelve el contenido de la entrada utilizando su nombre

## Parámetros

`name`  
Nombre de la entrada

`len`  
La longitud a ser leída desde la entrada. Si es `0`, entonces toda la entrada es leída.

`flags`  
Los indicadores a utilizar para abrir el archivo. Los siguientes valores podrían ser escritos juntos con un OR lógico en él.

- `ZipArchive::FL_UNCHANGED`

- `ZipArchive::FL_COMPRESSED`

- `ZipArchive::FL_NOCASE`

## Valores devueltos

Devuelve el contenido de la entrada en caso de tener éxito, o `false` si ocurre un error.

## Ejemplos

Obtener el contenido de los ficheros

```
<?php
$zip = new ZipArchive;
if ($zip->open('test1.zip') === TRUE) {
    echo $zip->getFromName('testfromfile.php');
    $zip->close();
} else {
    echo 'falló';
}
?>

     
```php

Convierte una imagen desde una entrada de fichero zip

```
<?php
$z = new ZipArchive();
if ($z->open(dirname(__FILE__) . '/test_im.zip')) {
    $im_string = $z->getFromName("pear_item.gif");
    $im = imagecreatefromstring($im_string);
    imagepng($im, 'b.png');
}
?>

     
```php

## Véase también

ZipArchive::getFromIndex
