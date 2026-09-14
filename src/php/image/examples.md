---
title: Ejemplos
source_url: https://www.php.net/manual/es/image.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31360
---

## Ejemplos

## Creación de una imagen PNG con PHP

Creación de una imagen PNG con PHP

```php
<?php

header("Content-type: image/png");
$string = $_GET['text'];
$im     = imagecreatefrompng("images/button1.png");
$orange = imagecolorallocate($im, 220, 210, 60);
$px     = (imagesx($im) - 7.5 * strlen($string)) / 2;
imagestring($im, 3, $px, 9, $string, $orange);
imagepng($im);

?>

    
```

Este ejemplo debe ser llamado desde una página HTML con una etiqueta de imagen como: `<img src="button.php?text">`. El script anterior, `button.php`, toma el string `"texto"` y lo escribe sobre el fondo de imagen llamado `"images/button1.png"`, luego lo muestra. Este es un método muy práctico para evitar redibujar un nuevo botón cada vez que se cambia su texto. De esta manera, se generan dinámicamente.

## Añadir un sello digital a imágenes utilizando un canal Alpha

Añadir un sello digital a imágenes utilizando un canal Alpha

```php
<?php
// Carga el sello y la foto para aplicar el sello digital
$stamp = imagecreatefrompng('stamp.png');
$im = imagecreatefromjpeg('photo.jpeg');

// Define los márgenes para el sello y obtiene la altura y anchura de este
$marge_right = 10;
$marge_bottom = 10;
$sx = imagesx($stamp);
$sy = imagesy($stamp);

// Copia el sello sobre la foto utilizando los márgenes y la anchura de la
// foto original para calcular la posición del sello
imagecopy($im, $stamp, imagesx($im) - $sx - $marge_right, imagesy($im) - $sy - $marge_bottom, 0, 0, imagesx($stamp), imagesy($stamp));

// Mostrar
header('Content-type: image/png');
imagepng($im);
?>

    
```

![Añadir un sello digital a la imagen utilizando un canal alpha](en/reference/image/figures/watermarks.png)

Este ejemplo muestra un método simple para aplicar un sello digital y un sello a sus fotos e imágenes con licencia. Observe la presencia de un canal Alpha en el sello así como texto anti-aliaseado. Estos dos elementos serán preservados durante la copia.

## Ejemplo con `imagecopymerge` para crear un sello digital translúcido

Ejemplo con `imagecopymerge` para crear un sello digital translúcido

```php
<?php
// Carga el sello y la foto para aplicar el sello digital
$im = imagecreatefromjpeg('photo.jpeg');

// Primero, creamos un sello manualmente usando GD
$stamp = imagecreatetruecolor(100, 70);
imagefilledrectangle($stamp, 0, 0, 99, 69, 0x0000FF);
imagefilledrectangle($stamp, 9, 9, 90, 60, 0xFFFFFF);
imagestring($stamp, 5, 20, 20, 'libGD', 0x0000FF);
imagestring($stamp, 3, 20, 40, '(c) 2007-9', 0x0000FF);

// Define los márgenes del sello y obtiene la anchura y altura del sello
$marge_right = 10;
$marge_bottom = 10;
$sx = imagesx($stamp);
$sy = imagesy($stamp);

// Fusiona el sello en nuestra foto con una opacidad del 50%
imagecopymerge($im, $stamp, imagesx($im) - $sx - $marge_right, imagesy($im) - $sy - $marge_bottom, 0, 0, imagesx($stamp), imagesy($stamp), 50);

// Guarda la imagen en un archivo
imagepng($im, 'photo_stamp.png');

?>

    
```

![Uso de imagecopymerge() para crear un sello translúcido](en/reference/image/figures/watermark-merged.png)

Este ejemplo utiliza la función `imagecopymerge` para fusionar el sello con nuestra imagen original. Usando esta función, podemos definir la opacidad de nuestro sello - en nuestro ejemplo, lo hemos establecido en 50%. En la práctica, es más conveniente hacer nuestra protección semi-transparente, lo que la hace más difícil de eliminar pero también permite a los visores de imágenes leerla sin problemas.
