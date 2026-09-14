---
title: Imagick::distortImage
description: Deforma una imagen utilizando varios métodos de distorsión
source_url: https://www.php.net/manual/es/imagick.distortimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/distortimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 6047c10c1
order: 33140
---

Imagick::distortImage

Deforma una imagen utilizando varios métodos de distorsión

## Descripción

```php
public Imagick::distortImage(int $method, array $arguments, bool $bestfit): bool
```php

Deforma una imagen utilizando varios métodos de distorsión, mapeando la paleta de colores de la imagen de origen a una nueva imagen destino normalmente del mismo tamaño que la imagen de origen, a menos que 'bestfit' esté establecido a `true`.

Si 'bestfit' está habilitado, y la distorsión lo permite, la imagen destino se ajusta para asegurarse de que la 'imagen' de origen entera se ajustará dentro de la imagen destino final, la cuál será redimensionada e compensada acordemente. También, en la mayoría de los casos el índice virtual de la imagen de origen será tomado en cuenta en el mapeado.

Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

## Parámetros

`method`  
El método de distorsión de la imagen. Véase [constantes de distorsión](#imagick.constants.distortion)

`arguments`  
Los argumentos para este método de distorsión

`bestfit`  
Intenta redimensionar la imagen destino para ajustarse a la imagen de origen deformada

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Usar `Imagick::distortImage`:

Deformar una imagen y mostrarla en el navegador.

```
<?php
/* Crear un nuevo objeto */
$im = new Imagick();

/* Crear un nuevo patrón de tablero de ajedrez */
$im->newPseudoImage(100, 100, "pattern:checkerboard");

/* Establecer el formato de la imagen a png */
$im->setImageFormat('png');

/* Rellenar las nuevas áreas visibles con transparente */
$im->setImageVirtualPixelMethod(Imagick::VIRTUALPIXELMETHOD_TRANSPARENT);

/* Activar el mate */
$im->setImageMatte(true);

/* Puntos de control para la distorsión */
$puntosControl = array( 10, 10,
                        10, 5,

                        10, $im->getImageHeight() - 20,
                        10, $im->getImageHeight() - 5,

                        $im->getImageWidth() - 10, 10,
                        $im->getImageWidth() - 10, 20,

                        $im->getImageWidth() - 10, $im->getImageHeight() - 10,
                        $im->getImageWidth() - 10, $im->getImageHeight() - 30);

/* Realizar la distorsión */
$im->distortImage(Imagick::DISTORTION_PERSPECTIVE, $puntosControl, true);

/* Imprimir la imagen */
header("Content-Type: image/png");
echo $im;
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Salida del ejemplo : Using Imagick::distortImage()](en/reference/imagick/figures/distortImage.png)

## Véase también

`Imagick::blurImage`, `Imagick::motionBlurImage`, `Imagick::radialBlurImage`
