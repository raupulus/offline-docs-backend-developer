---
title: Imagick::setImageTicksPerSecond
description: Establece los ticks por segundo de la imagen
source_url: https://www.php.net/manual/es/imagick.setimagetickspersecond.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimagetickspersecond.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35550
---

Imagick::setImageTicksPerSecond

Establece los ticks por segundo de la imagen

## Descripción

```php
public Imagick::setImageTicksPerSecond(int $ticks_per_second): bool
```php

Ajusta la cantidad de tiempo que se muestra un marco de una imagen animada.

> [!NOTE]
> Para GIFs animados, esta función no cambia el número de 'ticks de imagen' por segundo, el cual está siempre definido como 100. En su lugar, ajusta la cantidad de tiempo que se muestra un marco para simular el cambio de 'ticks por segundo'.
>
> Por ejemplo, para un GIF animado donde cada marco se muestra para 20 ticks (1/5 de un segundo), al llamar a este método en cada marco de esa imagen con un argumento de `50`, los marcos se ajustan para que se muestren por 40 ticks (2/5 de un segundo) y así, la animación se reproducirá a la mitad de la velocidad original.

## Parámetros

`ticks_per_second`  
La duración por la que imagen debería mostrarse expresada en ticks por segundo.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Modificar un GIF animado con `Imagick::setImageTicksPerSecond`

```
<?php

// Modificar un GIF animado para que la primera mitad del GIF se reproduzca a
// la mitad de su velocidad, y la segunda mitad se reproduzca al doble de su
// velocidad actual

$imagick = new Imagick(realpath("Test.gif"));
$imagick = $imagick->coalesceImages();

$totalFrames = $imagick->getNumberImages();

$frameCount = 0;

foreach ($imagick as $frame) {
    $imagick->setImageTicksPerSecond(50);

    if ($frameCount < ($totalFrames / 2)) {
        // Modificar el marco para que se muestre al doble de lo actual
        $imagick->setImageTicksPerSecond(50);
    } else {
        // Modificar el marco para que se muestre a la mitad de lo actual
        $imagick->setImageTicksPerSecond(200);
    }

    $frameCount++;
}

$imagick = $imagick->deconstructImages();

$imagick->writeImages("/ruta/donde/guardar/salida.gif", true);

?>

    
```php
