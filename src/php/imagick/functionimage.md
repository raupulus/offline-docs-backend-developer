---
title: Imagick::functionImage
description: Aplica una función sobre la imagen
source_url: https://www.php.net/manual/es/imagick.functionimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/functionimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: e50e79746
order: 33310
---

Imagick::functionImage

Aplica una función sobre la imagen

## Descripción

```php
public Imagick::functionImage(int $function, array $arguments, [int $channel]): bool
```php

Aplica una expresión aritmética, relacional o lógica a una pseudo-imagen.

Consulte también los [ejemplos de ImageMagick v6 - Transformaciones de imágenes — Función, evaluación de varios argumentos](https://usage.imagemagick.org/transform/#function).

Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.9 o superior.

## Parámetros

`function`  
Consulte la lista de [constantes de función](#imagick.constants.function).

`arguments`  
Array de argumentos a pasar a la función.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Crea un gradiente sinusoidal

```
<?php
$imagick = new Imagick();
$imagick->newPseudoImage(200, 200, 'gradient:black-white');
$arguments = array(3, -90);
$imagick->functionImage(Imagick::FUNCTION_SINUSOID, $arguments);

header("Content-Type: image/png");
$imagick->setImageFormat("png");
echo $imagick->getImageBlob();
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Resultado de la creación de un gradiente sinusoidal](en/reference/imagick/figures/functionImage_sinusoidal.png)

Crea un gradiente desde el polinomio (4x^2 - 4x + 1)

```
<?php
$imagick = new Imagick();
$imagick->newPseudoImage(200, 200, 'gradient:black-white');
$arguments = array(4, -4, 1);
$imagick->functionImage(Imagick::FUNCTION_POLYNOMIAL, $arguments);

header("Content-Type: image/png");
$imagick->setimageformat("png");
echo $imagick->getImageBlob();
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Resultado de la creación de un gradiente a partir de un polinomio](en/reference/imagick/figures/functionImage_polynomial.png)

Crea un gradiente complejo desde el polinomio (4x^2 - 4x^2 + 1) modulado por un gradiente sinusoidal

```
<?php
$imagick1 = new Imagick();
$imagick1->newPseudoImage(200, 200, 'gradient:black-white');
$arguments = array(9, -90);
$imagick1->functionImage(Imagick::FUNCTION_SINUSOID, $arguments);

$imagick2 = new Imagick();
$imagick2->newPseudoImage(200, 200, 'gradient:black-white');
$arguments = array(0.5, 0);
$imagick2->functionImage(Imagick::FUNCTION_SINUSOID, $arguments);
$imagick1->compositeimage($imagick2, Imagick::COMPOSITE_MULTIPLY, 0, 0);

header("Content-Type: image/png");
$imagick1->setImageFormat("png");
echo $imagick1->getImageBlob();
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Resultado de la creación de un gradiente complejo](en/reference/imagick/figures/functionImage_multiplied.png)
