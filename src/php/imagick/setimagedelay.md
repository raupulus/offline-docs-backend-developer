---
title: Imagick::setImageDelay
description: Establece el retardo de una imagen
source_url: https://www.php.net/manual/es/imagick.setimagedelay.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimagedelay.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35310
---

Imagick::setImageDelay

Establece el retardo de una imagen

## Descripción

```php
public Imagick::setImageDelay(int $delay): bool
```php

Establece el retardo de una imagen. Para una imagen animada, esto es la cantidad de tiempo que debería mostrarse este marco de la imagen, antes de mostrar el siguiente marco.

El retardo se puede establecer individualmente para cada marco de una imagen.

## Parámetros

`delay`  
La cantidad de tiempo expresado en 'ticks' que debería mostrarse la imagen. Para GIFs animados son 100 ticks por segundo, por lo que un valor de 20 sería 20/100 de un segundo, es decir 1/5 de un segundo.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Modificar un GIF animado con `Imagick::setImageDelay`

```
<?php

// Modificar un GIF animado, y así sus marcos se reproduzcan a una velocidad variable,
// variando entre que se muestre para 50ms hasta 0ms, que causará que el marco
// sea saltado en la mayoría de los navegadores.
$imagick = new Imagick(realpath("Test.gif"));
$imagick = $imagick->coalesceImages();

$numMarcos = 0;

foreach ($imagick as $marco) {
    $imagick->setImageDelay((($numMarcos % 11) * 5));
    $numMarcos++;
}

$imagick = $imagick->deconstructImages();

$imagick->writeImages("/ruta/donde/guardar/output.gif", true);

?>

    
```php
