---
title: Imagick::getSize
description: Retorna el tamaño asociado con un objeto Imagick
source_url: https://www.php.net/manual/es/imagick.getsize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getsize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 73fae4ee5
order: 34270
---

Imagick::getSize

Retorna el tamaño asociado con un objeto Imagick

## Descripción

```php
public Imagick::getSize(): array
```php

Obtener el tamaño asociado con un objeto Imagick, previamente definido por `Imagick::setSize`.

> [!NOTE]
> Este método retorna simplemente el tamaño que ha sido definido utilizando `Imagick::setSize`. Si se desea obtener la anchura/altura real de la imagen, utilícense `Imagick::getImageWidth` y `Imagick::getImageHeight`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna el tamaño asociado con un objeto `Imagick`, en forma de array, con las claves "`columns`" (columnas) y "`rows`" (filas).

## Ejemplos

Obtención del tamaño de una imagen RGB cruda definida a 200x400, tras escalado a 400x800 (en relación a la anchura/altura)

```
<?php
//Establecer el tamaño primero y luego cargar la imagen cruda
$img = new Imagick();
$img->setSize(200, 400);
$img->readImage("image.rgb");

$img->scaleImage(400, 800);

$size = $img->getSize();
print_r($size);

echo $img->getImageWidth()."x".$img->getImageHeight();
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [columns] => 200
        [rows] => 400
    )
    400x800
