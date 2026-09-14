---
title: Imagick::setOption
description: Configura una opción de un objeto Imagick
source_url: https://www.php.net/manual/es/imagick.setoption.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setoption.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e50e79746
order: 35630
---

Imagick::setOption

Configura una opción de un objeto Imagick

## Descripción

```php
public Imagick::setOption(string $key, string $value): bool
```php

Configura una o varias opciones del objeto Imagick.

## Parámetros

`key`  

`value`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Intento de alcanzar el tamaño '\$extent' con `Imagick::setOption`

```
<?php
    function renderJPG($extent) {
        $imagePath = $this->control->getImagePath();
        $imagick = new \Imagick(realpath($imagePath));
        $imagick->setImageFormat('jpg');
        $imagick->setOption('jpeg:extent', $extent);
        header("Content-Type: image/jpg");
        echo $imagick->getImageBlob();
    }

?>

     
```php

Ejemplo con `Imagick::setOption`

```
<?php
    function renderPNG($imagePath, $format) {

        $imagick = new \Imagick(realpath($imagePath));
        $imagick->setImageFormat('png');
        $imagick->setOption('png:format', $format);
        header("Content-Type: image/png");
        echo $imagick->getImageBlob();
    }

    //Guardar como PNG de 64 bits.
    renderPNG($imagePath, 'png64');

?>

     
```php

Ejemplo con `Imagick::setOption`

```
<?php
    function renderCustomBitDepthPNG() {
        $imagePath = $this->control->getImagePath();
        $imagick = new \Imagick(realpath($imagePath));
        $imagick->setImageFormat('png');

        $imagick->setOption('png:bit-depth', '16');
        $imagick->setOption('png:color-type', 6);
        header("Content-Type: image/png");
        $crash = true;
        if ($crash) {
            echo $imagick->getImageBlob();
        }
        else {
            $tempFilename = tempnam('./', 'imagick');
            $imagick->writeimage(realpath($tempFilename));
            echo file_get_contents($tempFilename);
        }
    }

?>

     
```php
