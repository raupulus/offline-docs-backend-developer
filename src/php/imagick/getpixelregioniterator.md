---
title: Imagick::getPixelRegionIterator
description: Obtiene un objeto ImagickPixelIterator de una sección de imagen
source_url: https://www.php.net/manual/es/imagick.getpixelregioniterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getpixelregioniterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34170
---

Imagick::getPixelRegionIterator

Obtiene un objeto ImagickPixelIterator de una sección de imagen

## Descripción

```php
public Imagick::getPixelRegionIterator(int $x, int $y, int $columns, int $rows): ImagickPixelIterator
```php

Obtiene un objeto ImagickPixelIterator de una sección de imagen.

## Parámetros

`x`  
La coordenada x de la región.

`y`  
La coordenada y de la región.

`columns`  
El ancho de la región.

`rows`  
El alto de la región.

## Valores devueltos

Devuelve un objeto ImagickPixelIterator de una sección de imagen.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo de Imagick::getPixelRegionIterator

Recorrer los píxeles de la parte alta izquierda de la imagen, cambiándolos a negro.

```
     
<?php
$im = new Imagick(realpath("./testImage.png"));
$areaIterator = $im->getPixelRegionIterator(0, 0, 10, 10);

foreach ($areaIterator as $rowIterator) {
    foreach ($rowIterator as $píxel) {
        // Pintar cada píxel de negro
        $píxel->setColor("rgba(0, 0, 0, 0)");
    }
    $areaIterator->syncIterator();
}
$im->writeImage("./output.png");
?>

    
```php
