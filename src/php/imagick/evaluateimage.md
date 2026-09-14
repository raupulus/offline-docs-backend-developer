---
title: Imagick::evaluateImage
description: Aplica una expresión a una imagen
source_url: https://www.php.net/manual/es/imagick.evaluateimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/evaluateimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 6047c10c1
order: 33210
---

Imagick::evaluateImage

Aplica una expresión a una imagen

## Descripción

```php
public Imagick::evaluateImage(int $op, float $constant, [int $channel]): bool
```php

Aplica una expresión aritmética, relacional o lógica a una imagen. Utilice estos operadores para aclarar u oscurecer una imagen, para aumentar o reducir el contraste, o para producir una imagen invertida.

## Parámetros

`op`  
El operador de evaluación

`constant`  
El valor del operador

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para utilizar más de un canal, combine las constantes de tipo de canal utilizando los operadores a nivel de bits. Consulte la lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::evaluateImage`

Uso de evaluateImage para reducir la opacidad de una imagen.

```
<?php
// Creación de un nuevo objeto con la imagen
$im = new Imagick('example-alpha.png');

// Reducción del alpha en un 50%
$im->evaluateImage(Imagick::EVALUATE_DIVIDE, 2, Imagick::CHANNEL_ALPHA);

// Mostrar la imagen
header("Content-Type: image/png");
echo $im;
?>

   
```php
