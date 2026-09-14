---
title: imagefilter
description: Aplica un filtro a una imagen
source_url: https://www.php.net/manual/es/function.imagefilter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagefilter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 32020
---

imagefilter

Aplica un filtro a una imagen

## Descripción

```php
imagefilter(GdImage $image, int $filter, array ...$args): bool
```php

`imagefilter` aplica el filtro dado `filter` sobre la `image`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`filter`  
`filter` puede ser uno de los siguientes:

- `IMG_FILTER_NEGATE` : Invierte todos los colores de la imagen.

- `IMG_FILTER_GRAYSCALE` : Convierte la imagen a niveles de gris cambiando las componentes roja, verde y azul a su suma ponderada utilizando los mismos coeficientes que el cálculo luma REC.601 (Y'). Las componentes alfa se conservan. Para imágenes de paleta, el resultado puede ser diferente debido a las limitaciones de la paleta.

- `IMG_FILTER_BRIGHTNESS` : Modifica el brillo de la imagen. Utilice `args` para definir el nivel de brillo. El rango de brillo está entre -255 y 255.

- `IMG_FILTER_CONTRAST` : Modifica el contraste de la imagen. Utilice `args` para definir el nivel de contraste.

- `IMG_FILTER_COLORIZE` : similar a `IMG_FILTER_GRAYSCALE`, excepto que es posible especificar el color. Utilice `args`, `arg2` y `arg3` en forma de `red`, `green`, `blue` y `arg4` para el canal `alpha`. El rango de cada color está entre 0 y 255.

- `IMG_FILTER_EDGEDETECT` : Utiliza la detección de bordes para resaltar los bordes de la imagen.

- `IMG_FILTER_EMBOSS` : Permite embosar la imagen.

- `IMG_FILTER_GAUSSIAN_BLUR` : Desenfoca la imagen utilizando el método gaussiano.

- `IMG_FILTER_SELECTIVE_BLUR` : Desenfoca la imagen.

- `IMG_FILTER_MEAN_REMOVAL` : Utiliza la supresión de la media para obtener un efecto "croquis".

- `IMG_FILTER_SMOOTH` : Hace la imagen más suave. Utilice `args` para definir el nivel de suavizado.

- `IMG_FILTER_PIXELATE` : Aplica un efecto de pixeles a la imagen, utilice `args` para definir el tamaño del bloque y `arg2` para definir el modo de efecto de pixeles.

- `IMG_FILTER_SCATTER` : Aplica un efecto de dispersión a la imagen, utilice `args` y `arg2` para definir la intensidad del efecto y `arg3` para aplicar el efecto solo sobre ciertos colores de píxeles.

`args`  
- `IMG_FILTER_BRIGHTNESS` : Nivel de brillo.

- `IMG_FILTER_CONTRAST` : Nivel de contraste.

- `IMG_FILTER_COLORIZE` : Valor del componente rojo.

- `IMG_FILTER_SMOOTH` : Nivel de suavizado.

- `IMG_FILTER_PIXELATE` : Tamaño del bloque en píxeles.

- `IMG_FILTER_SCATTER` : Nivel de sustracción del efecto. No debe ser superior o igual al nivel de adición definido con `arg2`.

`arg2`  
- `IMG_FILTER_COLORIZE` : Valor del componente verde.

- `IMG_FILTER_PIXELATE` : Uso o no del efecto de pixeles avanzado (el valor por omisión es `false`).

- `IMG_FILTER_SCATTER` : Nivel de adición del efecto.

`arg3`  
- `IMG_FILTER_COLORIZE` : Valor del componente azul.

- `IMG_FILTER_SCATTER` : Array opcional de valores de color indexados para aplicar el efecto.

`arg4`  
- `IMG_FILTER_COLORIZE` canal Alpha, un valor entre 0 y 127. 0 indica opacidad total mientras que 127 indica transparencia total.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Genera un `ValueError` si `sub` o `plus` provoca un desbordamiento o un subdesbordamiento con el `IMG_FILTER_SCATTER` `filter`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Genera ahora un `ValueError` si `sub` o `plus` provoca un desbordamiento o un subdesbordamiento con el `IMG_FILTER_SCATTER` `filter`. |
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |
| 7.4.0 | Se añadió el soporte para la dispersión (`IMG_FILTER_SCATTER`). |

## Ejemplos

Ejemplo de niveles de gris con `imagefilter`

```
<?php
$im = imagecreatefrompng('dave.png');

if($im && imagefilter($im, IMG_FILTER_GRAYSCALE))
{
    echo 'Imagen convertida a escala de grises.';

    imagepng($im, 'dave.png');
}
else
{
    echo 'Conversión a escala de grises fallida.';
}
?>

    
```php

Ejemplo de brillo con `imagefilter`

```
<?php
$im = imagecreatefrompng('sean.png');

if($im && imagefilter($im, IMG_FILTER_BRIGHTNESS, 20))
{
    echo 'Brillo de la imagen cambiado.';

    imagepng($im, 'sean.png');
}
else
{
    echo 'Cambio de brillo fallido.';
}
?>

    
```php

Ejemplo de colorización con `imagefilter`

```
<?php
$im = imagecreatefrompng('philip.png');

/* R, G, B, así que 0, 255, 0 es verde */
if($im && imagefilter($im, IMG_FILTER_COLORIZE, 0, 255, 0))
{
    echo 'Imagen teñida de verde con éxito.';

    imagepng($im, 'philip.png');
}
else
{
    echo 'Teñido de verde fallido.';
}
?>

    
```php

Ejemplo de negativo con `imagefilter`

```
<?php
// Define la función negate para que sea portable para
// versiones de php sin imagefilter()
function negate($im)
{
    if(function_exists('imagefilter'))
    {
        return imagefilter($im, IMG_FILTER_NEGATE);
    }

    for($x = 0; $x < imagesx($im); ++$x)
    {
        for($y = 0; $y < imagesy($im); ++$y)
        {
            $index = imagecolorat($im, $x, $y);
            $rgb = imagecolorsforindex($index);
            $color = imagecolorallocate($im, 255 - $rgb['red'], 255 - $rgb['green'], 255 - $rgb['blue']);

            imagesetpixel($im, $x, $y, $color);
        }
    }

    return(true);
}

$im = imagecreatefromjpeg('kalle.jpg');

if($im && negate($im))
{
    echo 'Imagen convertida a colores negativos con éxito.';

    imagejpeg($im, 'kalle.jpg', 100);
}
else
{
    echo 'Conversión a colores negativos fallida.';
}
?>

    
```php

Ejemplo de pixeles con `imagefilter`

```
<?php
// Carga el logo PHP, debemos crear dos instancias
// para ver las diferencias
$logo1 = imagecreatefrompng('./php.png');
$logo2 = imagecreatefrompng('./php.png');

// Creación de la instancia de imagen sobre la cual queremos
// ver las diferencias
$output = imagecreatetruecolor(imagesx($logo1) * 2, imagesy($logo1));

// Aplica el efecto de pixeles a cada instancia con un
// tamaño de bloque de 3
imagefilter($logo1, IMG_FILTER_PIXELATE, 3);
imagefilter($logo2, IMG_FILTER_PIXELATE, 3, true);

// Fusiona las diferencias sobre la imagen de salida
imagecopy($output, $logo1, 0, 0, 0, 0, imagesx($logo1) - 1, imagesy($logo1) - 1);
imagecopy($output, $logo2, imagesx($logo2), 0, 0, 0, imagesx($logo2) - 1, imagesy($logo2) - 1);

// Muestra las diferencias
header('Content-Type: image/png');
imagepng($output);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Salida del ejemplo de pixeles con imagefilter](en/reference/image/figures/imagefilterpixelate.png)

Ejemplo de dispersión con `imagefilter`

```
<?php
// Carga la imagen
$logo = imagecreatefrompng('./php.png');

// Aplica un efecto de dispersión muy suave a la imagen
imagefilter($logo, IMG_FILTER_SCATTER, 3, 5);

// Muestra la imagen con el efecto de dispersión
header('Content-Type: image/png');
imagepng($logo);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Salida del ejemplo de dispersión con imagefilter](en/reference/image/figures/scatter.png)

## Notas

> [!NOTE]
> El resultado de `IMG_FILTER_SCATTER` siempre es aleatorio.

## Véase también

imageconvolution
