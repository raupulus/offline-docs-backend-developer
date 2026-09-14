---
title: Imagick::orderedPosterizeImage
description: Realiza un entramado ordenado
source_url: https://www.php.net/manual/es/imagick.orderedposterizeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/orderedposterizeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34630
---

Imagick::orderedPosterizeImage

Realiza un entramado ordenado

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::orderedPosterizeImage(string $threshold_map, [int $channel]): bool
```php

Realiza un entramado ordenado basado en varios mapas de umbral de entramado predefinidos, pero sobre múltiples niveles de intensidad, lo que puede ser diferente para distintos canales, según los argumentos de entrada. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.1 o superior.

## Parámetros

`threshold_map`  
Un string que contiene el nombre del mapa de umbral de entramado que se va a usar

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::orderedPosterizeImage`

```
      
<?php
function orderedPosterizeImage($imagePath, $orderedPosterizeType) {
    $imagick = new \Imagick(realpath($imagePath));

    $imagick->orderedPosterizeImage($orderedPosterizeType);
    $imagick->setImageFormat('png');

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

//orderedPosterizeImage($imagePath, 'o4x4,3,3');
//orderedPosterizeImage($imagePath, 'o8x8,6,6');
orderedPosterizeImage($imagePath, 'h8x8a');

?>

      
```php
