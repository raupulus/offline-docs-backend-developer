---
title: Imagick::trimImage
description: Elimina los extremos de la imagen
source_url: https://www.php.net/manual/es/imagick.trimimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/trimimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 6047c10c1
order: 36020
---

Imagick::trimImage

Elimina los extremos de la imagen

## Descripción

```php
public Imagick::trimImage(float $fuzz): bool
```php

Elimina los extremos que son el color de fondo de la imagen. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`fuzz`  
Por defecto, el objetivo debe coincidir exactamente con un color de píxel en particular. Sin embargo, en la mayoría de los casos dos colores pueden diferir por una cantidad pequeña. El miembro enfoque de la imagen define cuánta tolerancia es aceptable para considerar que dos colores son el mismo. Este parámetro represenata la variación del rango de cuantía.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Usar `Imagick::trimImage`:

Recortar una imagen, después mostrarla en el navegador.

```
<?php
/* Crear el objeto y leer la imagen */
$im = new Imagick("imagen.jpg");

/* Recortar la imagen. */
$im->trimImage(0);

/* Imprimir la imagen */
header("Content-Type: image/" . $im->getImageFormat());
echo $im;
?>

    
```php

## Véase también

`Imagick::getQuantumDepth`, `Imagick::getQuantumRange`, `imagecropauto`
