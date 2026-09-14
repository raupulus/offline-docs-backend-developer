---
title: Imagick::morphology
description: Aplica un núcleo personalizado a la imagen según el método de morfología
  dado
source_url: https://www.php.net/manual/es/imagick.morphology.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/morphology.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1ef9c7a76
order: 34520
---

Imagick::morphology

Aplica un núcleo personalizado a la imagen según el método de morfología dado

## Descripción

```php
public Imagick::morphology(int $morphologyMethod, int $iterations, ImagickKernel $ImagickKernel, [int $channel]): bool
```php

Aplica un núcleo personalizado a la imagen según el método de morfología dado.

## Parámetros

`morphologyMethod`  
Qué método de morfología utilizar entre las constantes \Imagick::MORPHOLOGY\_\*.

`iterations`  
El número de iteraciones a aplicar a la función de morfología. Un valor de -1 significa iterar hasta que no se encuentren más cambios. Cómo se aplica esto puede depender del método de morfología. Típicamente, se trata de un valor de 1.

`ImagickKernel`  

`channel`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Convolución `Imagick::morphology`

```
      
<?php
        $imagick = $this->getCharacter();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_GAUSSIAN, "5,1");
        $imagick->morphology(\Imagick::MORPHOLOGY_CONVOLVE, 2, $kernel);
        header("Content-Type: image/png");
        echo $imagick->getImageBlob();
?>

      
```php

Correlación `Imagick::morphology`

```
      
<?php
        // El píxel en la esquina superior izquierda debe ser negro
        // El píxel en la esquina inferior derecha debe ser blanco
        // El resto no importa.

        $imagick = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromMatrix(self::$correlateMatrix, [2, 2]);
        $imagick->morphology(\Imagick::MORPHOLOGY_CORRELATE, 1, $kernel);
        header("Content-Type: image/png");
        echo $imagick->getImageBlob();
?>

      
```php

Erosión `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_OCTAGON, "3");
        $canvas->morphology(\Imagick::MORPHOLOGY_ERODE, 2, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Erosión de intensidad `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacter();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_OCTAGON, "1");
        $canvas->morphology(\Imagick::MORPHOLOGY_ERODE_INTENSITY, 2, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Dilatación `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_OCTAGON, "3");
        $canvas->morphology(\Imagick::MORPHOLOGY_DILATE, 4, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Dilatación de intensidad `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacter();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_OCTAGON, "1");
        $canvas->morphology(\Imagick::MORPHOLOGY_DILATE_INTENSITY, 4, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Distancia con núcleo de Chebyshev `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_CHEBYSHEV, "3");
        $canvas->morphology(\Imagick::MORPHOLOGY_DISTANCE, 3, $kernel);
        $canvas->autoLevelImage();
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Distancia con núcleo de Manhattan `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_MANHATTAN, "5");
        $canvas->morphology(\Imagick::MORPHOLOGY_DISTANCE, 3, $kernel);
        $canvas->autoLevelImage();
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Distancia con núcleo octagonal `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_OCTAGONAL, "5");
        $canvas->morphology(\Imagick::MORPHOLOGY_DISTANCE, 3, $kernel);
        $canvas->autoLevelImage();
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Distancia con núcleo euclidiano `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_EUCLIDEAN, "4");
        $canvas->morphology(\Imagick::MORPHOLOGY_DISTANCE, 3, $kernel);
        $canvas->autoLevelImage();
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Borde `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_OCTAGON, "3");
        $canvas->morphology(\Imagick::MORPHOLOGY_EDGE, 1, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Apertura `Imagick::morphology`

```
      
<?php
        // Como consecuencia, se verá que 'Apertura' ha suavizado el contorno, redondeando los puntos salientes y eliminando las partes más pequeñas que la forma utilizada. También desconectará o 'abrirá' los puentes delgados.
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_DISK, "6");
        $canvas->morphology(\Imagick::MORPHOLOGY_OPEN, 1, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Apertura de intensidad `Imagick::morphology`

```
      
<?php
        // Como consecuencia, se verá que 'Apertura' ha suavizado el contorno, redondeando los puntos salientes y eliminando las partes más pequeñas que la forma utilizada. También desconectará o 'abrirá' los puentes delgados.
        $canvas = $this->getCharacter();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_DISK, "6");
        $canvas->morphology(\Imagick::MORPHOLOGY_OPEN_INTENSITY, 1, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Cierre `Imagick::morphology`

```
      
<?php
        //El uso básico del método 'Cierre' es reducir o eliminar los 'huecos' o 'lagunas' aproximadamente del tamaño del elemento de estructura del núcleo. Es decir, 'cerrar' las partes del fondo que son aproximadamente de ese tamaño.
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_DISK, "6");
        $canvas->morphology(\Imagick::MORPHOLOGY_CLOSE, 1, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Cierre de intensidad `Imagick::morphology`

```
      
<?php
        //El uso básico del método 'Cierre' es reducir o eliminar los 'huecos' o 'lagunas' aproximadamente del tamaño del elemento de estructura del núcleo. Es decir, 'cerrar' las partes del fondo que son aproximadamente de ese tamaño.
        $canvas = $this->getCharacter();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_DISK, "6");
        $canvas->morphology(\Imagick::MORPHOLOGY_CLOSE_INTENSITY, 1, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Suavizado `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_OCTAGON, "3");
        $canvas->morphology(\Imagick::MORPHOLOGY_SMOOTH, 1, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Borde interior `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_OCTAGON, "3");
        $canvas->morphology(\Imagick::MORPHOLOGY_EDGE_IN, 1, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Borde exterior `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_OCTAGON, "3");
        $canvas->morphology(\Imagick::MORPHOLOGY_EDGE_OUT, 1, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

El método 'TopHat', o más específicamente 'White Top Hat', devuelve los píxeles que han sido eliminados por una Apertura de la forma, es decir, los píxeles que han sido eliminados para redondear los puntos y los puentes de conexión entre las formas. `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_DISK, "5");
        $canvas->morphology(\Imagick::MORPHOLOGY_TOP_HAT, 1, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

El método 'BottomHat', también conocido como 'Black TopHat', son los píxeles que un Cierre de la forma añade a la imagen. Es decir, los píxeles que han sido utilizados para rellenar los 'huecos', las 'lagunas' y los 'puentes'. `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_DISK, "5");
        $canvas->morphology(\Imagick::MORPHOLOGY_BOTTOM_HAT, 1, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Golpe y fallo `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        //Esto encuentra todos los píxeles con 3 píxeles del borde derecho
        $matrix = [[1, false, false, 0]];
        $kernel = \ImagickKernel::fromMatrix(
            $matrix,
            [0, 0]
        );
        $canvas->morphology(\Imagick::MORPHOLOGY_HIT_AND_MISS, 1, $kernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Afinamiento `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $leftEdgeKernel = \ImagickKernel::fromMatrix([[0, 1]], [1, 0]);
        $rightEdgeKernel = \ImagickKernel::fromMatrix([[1, 0]], [0, 0]);
        $leftEdgeKernel->addKernel($rightEdgeKernel);

        $canvas->morphology(\Imagick::MORPHOLOGY_THINNING, 3, $leftEdgeKernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Engrosamiento `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $leftEdgeKernel = \ImagickKernel::fromMatrix([[0, 1]], [1, 0]);
        $rightEdgeKernel = \ImagickKernel::fromMatrix([[1, 0]], [0, 0]);
        $leftEdgeKernel->addKernel($rightEdgeKernel);

        $canvas->morphology(\Imagick::MORPHOLOGY_THICKEN, 3, $leftEdgeKernel);
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Afinamiento para generar una cáscara convexa `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $diamondKernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_DIAMOND, "1");
        $convexKernel =  \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_CONVEX_HULL, "");

        // La morfología de afinamiento no maneja los pequeños espacios. Los cerramos
        // con la morfología de cierre.
        $canvas->morphology(\Imagick::MORPHOLOGY_CLOSE, 1, $diamondKernel);
        $canvas->morphology(\Imagick::MORPHOLOGY_THICKEN, -1, $convexKernel);
        $canvas->morphology(\Imagick::MORPHOLOGY_CLOSE, 1, $diamondKernel);

        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Morfología iterativa `Imagick::morphology`

```
      
<?php
        $canvas = $this->getCharacterOutline();
        $kernel = \ImagickKernel::fromBuiltIn(\Imagick::KERNEL_DISK, "2");
        $canvas->morphology(\Imagick::MORPHOLOGY_ITERATIVE, 3, $kernel);
        $canvas->autoLevelImage();
        header("Content-Type: image/png");
        echo $canvas->getImageBlob();
?>

      
```php

Función de ayuda para obtener un contorno de imagen `Imagick::morphology`

```
<?php
function getCharacterOutline() {
    $imagick = new \Imagick(realpath("./images/character.png"));
    $character = new \Imagick();
    $character->newPseudoImage(
        $imagick->getImageWidth(),
        $imagick->getImageHeight(),
        "canvas:white"
    );
    $canvas = new \Imagick();
    $canvas->newPseudoImage(
        $imagick->getImageWidth(),
        $imagick->getImageHeight(),
        "canvas:black"
    );

    $character->compositeimage(
        $imagick,
        \Imagick::COMPOSITE_COPYOPACITY,
        0, 0
    );
    $canvas->compositeimage(
        $character,
        \Imagick::COMPOSITE_ATOP,
        0, 0
    );
    $canvas->setFormat('png');

    return $canvas;
}
?>

      
```php
