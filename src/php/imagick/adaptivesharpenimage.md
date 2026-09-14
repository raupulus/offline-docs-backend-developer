---
title: Imagick::adaptiveSharpenImage
description: Afila la imagen adaptativamente
source_url: https://www.php.net/manual/es/imagick.adaptivesharpenimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/adaptivesharpenimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32620
---

Imagick::adaptiveSharpenImage

Afila la imagen adaptativamente

## Descripción

```php
public Imagick::adaptiveSharpenImage(float $radius, float $sigma, [int $channel]): bool
```php

Afila la imagen adaptativamente afilando con más intensidad cerca de los bordes de la imagen y con menos intensidad lejos de los bordes. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`radius`  
El radio gaussiano, en píxeles, sin contar el píxel central. Use 0 para autoseleccionar.

`sigma`  
La desviación estándar gaussiana, en píxeles.

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para aplicarlo a más de un canal, combínense las [constantes de canales](#imagick.constants.channel) utilizando un operador a nivel de bits. Por defecto, vale `Imagick::CHANNEL_DEFAULT`. Consúltese la lista de [constantes de canales](#imagick.constants.channel)

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Un ejemplo de `Imagick::adaptiveSharpenImage`

Afilar la imagen adaptativamente con radio 2 y sigma 1.

```
<?php
try {
    $imagen = new Imagick('image.png');
    $imagen->adaptiveSharpenImage(2,1);
} catch(ImagickException $e) {
    echo 'Error: ' , $e->getMessage();
    die();
}
header('Content-type: image/png');
echo $imagen;
?>

    
```php

## Véase también

`Imagick::sharpenImage`
