---
title: Imagick::blurImage
description: Añade un filtro de borrosidad a la imagen
source_url: https://www.php.net/manual/es/imagick.blurimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/blurimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32740
---

Imagick::blurImage

Añade un filtro de borrosidad a la imagen

## Descripción

```php
public Imagick::blurImage(float $radius, float $sigma, [int $channel]): bool
```php

Añade un filtro de borrosidad a la imagen. El tercer parámetro opcional es para hacer borroso un canal específico.

## Parámetros

`radius`  
Radio de la borrosidad

`sigma`  
Desviación estándar

`channel`  
La constante [Channeltype](#imagick.constants.channel). Cuando no es proporciona, todos los canales se hacen borrosos.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Usar `Imagick::blurImage`:

Hacer borrosa una imagen, después mostrarla en el navegador.

```
<?php

header('Content-type: image/jpeg');

$imagen = new Imagick('prueba.jpg');

$imagen->blurImage(5,3);
echo $imagen;

?>

    
```php

## Véase también

`Imagick::adaptiveBlurImage`, `Imagick::motionBlurImage`, `Imagick::radialBlurImage`
