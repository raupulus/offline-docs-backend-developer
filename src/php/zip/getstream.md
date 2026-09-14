---
title: ZipArchive::getStream
description: Obtener un manejador de fichero para la entrada definido por su nombre
  (sólo lectura)
source_url: https://www.php.net/manual/es/ziparchive.getstream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/getstream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108350
---

ZipArchive::getStream

Obtener un manejador de fichero para la entrada definido por su nombre (sólo lectura)

## Descripción

```php
public ZipArchive::getStream(string $name): resource
```php

Obtener un manejador de fichero para la entrada definido por su nombre. Por ahora, éste solamente soporta operaciones de lectura.

## Parámetros

`name`  
El nombre de la entrada a utilizar.

## Valores devueltos

Devuelve un puntero de fichero (un recurso) en caso de tener éxito, o `false` si ocurre un error.

## Ejemplos

Obtiene los contenidos de entrada con `fread` y lo almacena

```
<?php
$contents = '';
$z = new ZipArchive();
if ($z->open('test.zip')) {
    $fp = $z->getStream('test');
    if(!$fp) exit("failed\n");

    while (!feof($fp)) {
        $contents .= fread($fp, 2);
    }

    fclose($fp);
    file_put_contents('t',$contents);
    echo "done.\n";
}
?>

   
```php

Lo mismo como el ejemplo anterior pero con `fopen` y el envoltorio de flujo de zip

```
<?php
$contents = '';
$fp = fopen('zip://' . dirname(__FILE__) . '/test.zip#test', 'r');
if (!$fp) {
    exit("cannot open\n");
}
while (!feof($fp)) {
    $contents .= fread($fp, 2);
}
echo "$contents\n";
fclose($fp);
echo "done.\n";
?>

   
```php

El flujo de envoltorio y la imagen, también pueden ser utilizados con la función xml

```
<?php
$im = imagecreatefromgif('zip://' . dirname(__FILE__) . '/test_im.zip#pear_item.gif');
imagepng($im, 'a.png');
?>

   
```php

## Véase también

ZipArchive::getStreamIndex, ZipArchive::getStreamName, [Flujos de compresión](#wrappers.compression)
