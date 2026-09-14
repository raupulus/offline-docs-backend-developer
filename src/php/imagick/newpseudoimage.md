---
title: Imagick::newPseudoImage
description: Crea una nueva imagen
source_url: https://www.php.net/manual/es/imagick.newpseudoimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/newpseudoimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34570
---

Imagick::newPseudoImage

Crea una nueva imagen

## Descripción

```php
public Imagick::newPseudoImage(int $columns, int $rows, string $pseudoString): bool
```php

Crea una nueva imagen usando pseudo-formatos de ImageMagick.

## Parámetros

`columns`  
columnas en la nueva imagen

`rows`  
filas en la nueva imagen

`pseudoString`  
string que contiene la definición de la pseudo-imagen.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::newPseudoImage`

```
      
<?php
function newPseudoImage($canvasType) {
    $imagick = new \Imagick();
    $imagick->newPseudoImage(300, 300, $canvasType);
    $imagick->setImageFormat("png");
    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

//newPseudoImage('gradient:red-rgba(64, 255, 255, 0.5)');
//newPseudoImage("radial-gradient:red-blue");
newPseudoImage("plasma:fractal");

?>

      
```php
