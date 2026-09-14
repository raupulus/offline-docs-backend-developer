---
title: imagettftext
description: Dibuja un texto con una fuente TrueType
source_url: https://www.php.net/manual/es/function.imagettftext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagettftext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 48220b9fc
order: 32450
---

imagettftext

Dibuja un texto con una fuente TrueType

## Descripción

```php
imagettftext(GdImage $image, float $size, float $angle, int $x, int $y, int $color, string $font_filename, string $text, [array $options]): array
```php

`imagettftext` dibuja el texto `text` con la fuente TrueType `fontfile`.

> [!NOTE]
> Antes de PHP 8.0.0, `imagefttext` era una variante extendida de `imagettftext` que además soporta `extrainfo`. A partir de PHP 8.0.0, `imagefttext` es un alias de `imagefttext`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`size`  
El tamaño de la fuente en puntos.

`angle`  
El ángulo, en grados; 0 grados corresponde a la lectura del texto de izquierda a derecha. Los valores positivos representan una rotación en el sentido contrario a las agujas de un reloj. Por ejemplo, un valor de 90 corresponderá a una lectura del texto de abajo hacia arriba.

`x`  
Las coordenadas dadas por `x` y `y` definirán la posición del primer carácter (la esquina inferior izquierda del carácter). Esto es diferente de la función `imagestring`, donde `x` y `y` definen la esquina superior izquierda del primer carácter. Por ejemplo, "superior izquierda" corresponde a 0, 0.

`y`  
La coordenada Y. Esto define la posición de la línea base de la fuente, y no el fondo de los caracteres.

`color`  
El índice del color. Utilizar un índice de color negativo desactivará el antialiasing. Ver la función `imagecolorallocate`.

`fontfile`  
La ruta de acceso al fichero de la fuente TrueType que desea utilizar.

Dependiendo de qué versión de la biblioteca GD esté utilizando PHP, *cuando `fontfile` no comienza con una barra diagonal inicial `/` entonces `.ttf` será añadido* al nombre del fichero y la biblioteca intentará buscar ese nombre de fichero a lo largo de una ruta de acceso de fuentes definida por la biblioteca.

Al utilizar versiones de la biblioteca GD inferiores a 2.0.18, un carácter `espacio`, en lugar de un punto y coma, se utilizaba como 'separador de rutas' para diferentes ficheros de fuentes. El uso no intencional de esta característica resultará en el mensaje de advertencia: `Advertencia: No se pudo encontrar/abrir la fuente`. Para estas versiones afectadas, la única solución es mover la fuente a una ruta que no contenga espacios.

En muchos casos donde una fuente reside en el mismo directorio que el script que la utiliza, el siguiente truco aliviará cualquier problema de inclusión.

```
<?php
// Set the environment variable for GD
putenv('GDFONTPATH=' . realpath('.'));

// Name the font to be used (note the lack of the .ttf extension)
$font = 'SomeFont';
?>

       
```php

> [!NOTE]
> Tenga en cuenta que [open_basedir](#ini.open-basedir) no *aplica* a `fontfile`.

`text`  
La cadena de texto, en UTF-8.

Puede incluir referencias a caracteres numéricos, decimales (en la forma: `&#8364;`) para acceder a los caracteres de una fuente más allá del primer 127. El formato hexadecimal (como `&#xA9;`) es soportado. Las cadenas de caracteres codificadas en UTF-8 pueden ser pasadas directamente.

Las entidades nombradas, como `&copy;`, no son soportadas. Utilice la función `html_entity_decode` para codificar estas entidades nombradas en cadena UTF-8.

Si un carácter es utilizado en una cadena que no es soportada por la fuente, un rectángulo hueco reemplazará el carácter.

`options`  
Un array con una clave `linespacing` que contiene un valor `float`.

## Valores devueltos

Devuelve un array de 8 elementos que representan cuatro puntos que marcan los límites del texto. El orden de los puntos es: inferior izquierdo, inferior derecho, superior derecho, superior izquierdo. Los puntos son relativos al texto con respecto al ángulo, por lo que, "superior izquierdo" significa en la esquina superior izquierda cuando se mira el texto horizontalmente. Devuelve `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                             |
|---------|-----------------------------------------|
| 8.0.0   | El parámetro `options` ha sido añadido. |

## Ejemplos

Ejemplo con `imagettftext`

Este ejemplo producirá una imagen PNG blanca de 400x30 píxeles, con el texto `"Test..."` en negro, con una sombra gris, utilizando la fuente Arial.

```
<?php

// Definición del content-type
header('Content-Type: image/png');

// Creación de la imagen
$im = imagecreatetruecolor(400, 30);

// Creación de algunos colores
$white = imagecolorallocate($im, 255, 255, 255);
$grey = imagecolorallocate($im, 128, 128, 128);
$black = imagecolorallocate($im, 0, 0, 0);
imagefilledrectangle($im, 0, 0, 399, 29, $white);

// El texto a dibujar
$text = 'Test...';

// Reemplazar la ruta por su propia ruta de fuente
$font = 'arial.ttf';

// Añadir sombras al texto
imagettftext($im, 20, 0, 11, 21, $grey, $font, $text);

// Añadir el texto
imagettftext($im, 20, 0, 10, 20, $black, $font, $text);

// Utilizar imagepng() dará un texto más claro,
// comparado con el uso de la función imagejpeg()
imagepng($im);

?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagettftext()](en/reference/image/figures/imagettftext.png)

## Notas

> [!NOTE]
> Esta función solo está disponible si si PHP es compilado con soporte Freetype (`--with-freetype-dir=DIR`)

## Véase también

imagettfbbox

imagefttext

imagestring
