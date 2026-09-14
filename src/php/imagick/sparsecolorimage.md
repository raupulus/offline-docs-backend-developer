---
title: Imagick::sparseColorImage
description: Interpola colores
source_url: https://www.php.net/manual/es/imagick.sparsecolorimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/sparsecolorimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 66d9935ec
order: 35830
---

Imagick::sparseColorImage

Interpola colores

## Descripción

```php
public Imagick::sparseColorImage(int $SPARSE_METHOD, array $arguments, [int $channel]): bool
```php

Dada la matriz de argumentos que contiene valores númericos, este método interpola los colores encontrados en esas coordenadas a través de la imagen completa usando `sparse_method`. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.5 o superior.

## Parámetros

`SPARSE_METHOD`  
Consulte esta lista de [constantes de métodos de escasez](#imagick.constants.sparsecolormethod)

`arguments`  
Una matriz que contiene las coordenadas. El formato de la matriz es `array(1,1, 2,45)`

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para aplicarlo a más de un canal, combínense las [constantes de canales](#imagick.constants.channel) utilizando un operador a nivel de bits. Por defecto, vale `Imagick::CHANNEL_DEFAULT`. Consúltese la lista de [constantes de canales](#imagick.constants.channel)

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

SPARSECOLORMETHOD_BARYCENTRIC `Imagick::sparseColorImage`

```
<?php
    function renderImageBarycentric2() {
        $points = [
            [0.30, 0.10, 'red'],
            [0.10, 0.80, 'blue'],
            [0.70, 0.60, 'lime'],
            [0.80, 0.20, 'yellow'],
        ];
        $imagick = createGradientImage(
            400, 400,
            $points,
            \Imagick::SPARSECOLORMETHOD_BARYCENTRIC
        );
        header("Content-Type: image/png");
        echo $imagick->getImageBlob();
    }

?>

     
```php

SPARSECOLORMETHOD_BILINEAR `Imagick::sparseColorImage`

```
<?php
    function renderImageBilinear() {
        $points = [[0.30, 0.10, 'red'], [0.10, 0.80, 'blue'], [0.70, 0.60, 'lime'], [0.80, 0.20, 'yellow'],];
        $imagick = createGradientImage(500, 500, $points, \Imagick::SPARSECOLORMETHOD_BILINEAR);
        header("Content-Type: image/png");
        echo $imagick->getImageBlob();
    }

?>

     
```php

SPARSECOLORMETHOD_SPEPARDS `Imagick::sparseColorImage`

```
<?php
    function renderImageShepards() {
        $points = [
            [0.30, 0.10, 'red'],
            [0.10, 0.80, 'blue'],
            [0.70, 0.60, 'lime'],
            [0.80, 0.20, 'yellow'],
        ];
        $imagick = createGradientImage(600, 600, $points, \Imagick::SPARSECOLORMETHOD_SPEPARDS);
        header("Content-Type: image/png");
        echo $imagick->getImageBlob();
    }

?>

     
```php

SPARSECOLORMETHOD_VORONOI `Imagick::sparseColorImage`

```
<?php
    function renderImageVoronoi() {
        $points = [
            [0.30, 0.10, 'red'],
            [0.10, 0.80, 'blue'],
            [0.70, 0.60, 'lime'],
            [0.80, 0.20, 'yellow'],
        ];
        $imagick = createGradientImage(500, 500, $points, \Imagick::SPARSECOLORMETHOD_VORONOI);
        header("Content-Type: image/png");
        echo $imagick->getImageBlob();
    }

?>

     
```php

SPARSECOLORMETHOD_BARYCENTRIC `Imagick::sparseColorImage`

```
<?php
    function renderImageBarycentric() {
        $points = [
            [0, 0, 'skyblue'],
            [-1, 1, 'skyblue'],
            [1, 1, 'black'],
        ];
        $imagick = createGradientImage(600, 200, $points, \Imagick::SPARSECOLORMETHOD_BARYCENTRIC);
        header("Content-Type: image/png");
        echo $imagick->getImageBlob();
    }

?>

     
```php

createGradientImage is used by other examples. `Imagick::sparseColorImage`

```
<?php
function createGradientImage($width, $height, $colorPoints, $sparseMethod, $absolute = false) {

    $imagick = new \Imagick();
    $imagick->newImage($width, $height, "white");
    $imagick->setImageFormat("png");

    $barycentricPoints = array();

    foreach ($colorPoints as $colorPoint) {

        if ($absolute == true) {
            $barycentricPoints[] = $colorPoint[0];
            $barycentricPoints[] = $colorPoint[1];
        }
        else {
            $barycentricPoints[] = $colorPoint[0] * $width;
            $barycentricPoints[] = $colorPoint[1] * $height;
        }

        if (is_string($colorPoint[2])) {
            $imagickPixel = new \ImagickPixel($colorPoint[2]);
        }
        else if ($colorPoint[2] instanceof \ImagickPixel) {
            $imagickPixel = $colorPoint[2];
        }
        else{
            $errorMessage = sprintf(
                "Value %s is neither a string nor an ImagickPixel class. Cannot use as a color.",
                $colorPoint[2]
            );

            throw new \InvalidArgumentException(
                $errorMessage
            );
        }

        $red = $imagickPixel->getColorValue(\Imagick::COLOR_RED);
        $green = $imagickPixel->getColorValue(\Imagick::COLOR_GREEN);
        $blue = $imagickPixel->getColorValue(\Imagick::COLOR_BLUE);
        $alpha = $imagickPixel->getColorValue(\Imagick::COLOR_ALPHA);

        $barycentricPoints[] = $red;
        $barycentricPoints[] = $green;
        $barycentricPoints[] = $blue;
        $barycentricPoints[] = $alpha;
    }

    $imagick->sparseColorImage($sparseMethod, $barycentricPoints);

    return $imagick;
}

?>

     
```php
