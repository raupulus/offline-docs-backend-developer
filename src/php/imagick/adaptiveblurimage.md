---
title: Imagick::adaptiveBlurImage
description: Añade un filtro de borrosidad adaptativo a la imagen
source_url: https://www.php.net/manual/es/imagick.adaptiveblurimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/adaptiveblurimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32600
---

Imagick::adaptiveBlurImage

Añade un filtro de borrosidad adaptativo a la imagen

## Descripción

```php
public Imagick::adaptiveBlurImage(float $radius, float $sigma, [int $channel]): bool
```php

Añade un filtro de borrosidad adaptativo a la imagen. La intensidad de una borrosidad adaptativa depende de si se disminuye dramáticamente en el borde de la imagen, mientras que una borrodidad estándar es uniforme en toda la imagen. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`radius`  
El radio gaussiano, en píxeles, sin contar el píxel central. Proporcione un valor de 0 y el radio será elegido auto-mágicaente.

`sigma`  
La desviación estándar gaussiana, en píxeles.

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para aplicarlo a más de un canal, combínense las [constantes de canales](#imagick.constants.channel) utilizando un operador a nivel de bits. Por defecto, vale `Imagick::CHANNEL_DEFAULT`. Consúltese la lista de [constantes de canales](#imagick.constants.channel)

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Usar `Imagick::adaptiveBlurImage`:

Aplicar borrosidad adaptativa a una imagen, después mostrarla en el navegador.

```
<?php

header('Content-type: image/jpeg');

$imagen = new Imagick('test.jpg');

$imagen->adaptiveBlurImage(5,3);
echo $imagen;

?>

    
```php

Resultado del ejemplo anterior es similar a:

![Salida del ejemplo : Usar Imagick::adaptiveBlurImage()](en/reference/imagick/figures/adaptiveBlurImage.gif)

## Véase también

`Imagick::blurImage`, `Imagick::motionBlurImage`, `Imagick::radialBlurImage`
