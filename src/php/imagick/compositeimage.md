---
title: Imagick::compositeImage
description: Compone una imagen en otra
source_url: https://www.php.net/manual/es/imagick.compositeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/compositeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32950
---

Imagick::compositeImage

Compone una imagen en otra

## Descripción

```php
public Imagick::compositeImage(Imagick $composite_object, int $composite, int $x, int $y, [int $channel]): bool
```php

Compone una imagen en otra en el índice especificado. Debería proporcionarse cualquier argumento necesario para el algoritmo de composición a setImageArtifact con 'compose:args' como el primer parámetro y los datos como el segundo.

## Parámetros

`composite_object`  
Objeto Imagick que guarda la imagen compuesta

`compose`  
Operador de composición. Véase [Constantes de Operadores de Composición](#imagick.constants.compositeop)

`x`  
El índice de la columna de la imagen compuesta

`y`  
El índice de la fila de la imagen compuesta

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Empleo de `Imagick::compositeImage`:

Componer dos imágenes con el método de composición 'mathematics'

```
<?php

// Equivalente a ejecutar el comando
// convert src1.png src2.png -compose mathematics -define compose:args="1,0,-0.5,0.5" -composite output.png

$src1 = new \Imagick("./src1.png");
$src2 = new \Imagick("./src2.png");

$src1->setImageVirtualPixelMethod(Imagick::VIRTUALPIXELMETHOD_TRANSPARENT);
$src1->setImageArtifact('compose:args', "1,0,-0.5,0.5");
$src1->compositeImage($src2, Imagick::COMPOSITE_MATHEMATICS, 0, 0);
$src1->writeImage("./output.png");

?>

    
```php

## Véase también

`Imagick::setImageArtifact`
