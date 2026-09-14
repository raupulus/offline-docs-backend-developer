---
title: Imagick::gammaImage
description: Corrección gamma de una imagen
source_url: https://www.php.net/manual/es/imagick.gammaimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/gammaimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33330
---

Imagick::gammaImage

Corrección gamma de una imagen

## Descripción

```php
public Imagick::gammaImage(float $gamma, [int $channel]): bool
```php

Corrección gamma de una imagen. La misma imagen vista en diferentes dispositivos tendrá diferencias perceptuales en la manera en que la intensidad de la imagen esté representada en la pantalla. Especifique niveles gamma indivuduales para los canales rojo, verde y azul, o ajústelos todos con el parámetro gamma. El rango de valores es típicamente desde 0.8 a 2.3.

## Parámetros

`gamma`  
La cantidad de corrección gamma.

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::gammaImage`

```
      
<?php
function gammaImage($imagePath, $gamma, $channel) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->gammaImage($gamma, $channel);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
