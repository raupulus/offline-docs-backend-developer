---
title: Imagick::levelImage
description: Ajusta los niveles de la imagen
source_url: https://www.php.net/manual/es/imagick.levelimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/levelimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34390
---

Imagick::levelImage

Ajusta los niveles de la imagen

## Descripción

```php
public Imagick::levelImage(float $blackPoint, float $gamma, float $whitePoint, [int $channel]): bool
```php

Ajusta los niveles de una imagen escalando la caída de los colores entre los puntos blanco y negro especificados al rango completo de cuantía disponible. Los parámetros proporcionados representan los puntos negro, mitad, y blanco. El punto negro especifica el color más oscuro de la imagen. Los colores más oscuros que el punto negro se establecen a cero. El punto medio especifica una corrección gamma a aplicar a la imagen. Mientras que el punto blanco especifica el color más claro de la imagen. Los colores más claros que el punto blanco se establecen al valor de cuantía máximo.

## Parámetros

`blackPoint`  
El punto negro de la imagen

`gamma`  
El valor gamma

`whitePoint`  
El punto blanco de la imagen

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::levelImage`

```
      
<?php
function levelImage($blackPoint, $gamma, $whitePoint) {
    $imagick = new \Imagick();
    $imagick->newPseudoimage(500, 500, 'gradient:black-white');

    $imagick->setFormat('png');
    $quantum = $imagick->getQuantum();
    $imagick->levelImage($blackPoint / 100 , $gamma, $quantum * $whitePoint / 100);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

      
```php
