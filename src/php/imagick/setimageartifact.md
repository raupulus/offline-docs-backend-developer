---
title: Imagick::setImageArtifact
description: Define el artefacto de la imagen
source_url: https://www.php.net/manual/es/imagick.setimageartifact.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimageartifact.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 35170
---

Imagick::setImageArtifact

Define el artefacto de la imagen

## Descripción

```php
public Imagick::setImageArtifact(string $artifact, string $value): bool
```php

Asocia un artefacto con la imagen. La diferencia entre las propiedades de la imagen y el artefacto de la imagen es que las propiedades son públicas mientras que los artefactos son privados. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.5.7 o superior.

## Parámetros

`artifact`  
El nombre del artefacto.

`value`  
El valor del artefacto.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::setImageArtifact`

```
<?php
function setImageArtifact() {

    $src1 = new \Imagick(realpath("./images/artifact/source1.png"));
    $src2 = new \Imagick(realpath("./images/artifact/source2.png"));

    $src2->setImageVirtualPixelMethod(\Imagick::VIRTUALPIXELMETHOD_TRANSPARENT);
    $src2->setImageArtifact('compose:args', "1,0,-0.5,0.5");
    $src1->compositeImage($src2, Imagick::COMPOSITE_MATHEMATICS, 0, 0);

    $src1->setImageFormat('png');
    header("Content-Type: image/png");
    echo $src1->getImagesBlob();
}

?>

     
```php

## Véase también

`Imagick::getImageArtifact`, `Imagick::deleteImageArtifact`
