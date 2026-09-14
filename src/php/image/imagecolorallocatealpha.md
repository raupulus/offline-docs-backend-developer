---
title: imagecolorallocatealpha
description: Asigna un color a una imagen
source_url: https://www.php.net/manual/es/function.imagecolorallocatealpha.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolorallocatealpha.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 9960a09a5
order: 31540
---

imagecolorallocatealpha

Asigna un color a una imagen

## Descripción

```php
imagecolorallocatealpha(GdImage $image, int $red, int $green, int $blue, int $alpha): int
```php

`imagecolorallocatealpha` se comporta como `imagecolorallocate` con el parámetro adicional de transparencia `alpha`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`red`  
Valor del componente rojo.

`green`  
Valor del componente verde.

`blue`  
Valor del componente azul.

`alpha`  
Un valor entre `0` y `127`. `0` indica opacidad completa mientras que `127` indica transparencia completa.

Los parámetros `red`, `green` y `blue` son enteros comprendidos entre 0 y 255, o hexadecimales comprendidos entre 0x00 y 0xFF.

## Valores devueltos

Un identificador de color o `false` si la asignación falla.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo de uso de `imagecolorallocatealpha`

```
<?php
$size = 300;
$image=imagecreatetruecolor($size, $size);

// algo para obtener un fondo blanco con un borde negro
$back = imagecolorallocate($image, 255, 255, 255);
$border = imagecolorallocate($image, 0, 0, 0);
imagefilledrectangle($image, 0, 0, $size - 1, $size - 1, $back);
imagerectangle($image, 0, 0, $size - 1, $size - 1, $border);

$yellow_x = 100;
$yellow_y = 75;
$red_x    = 120;
$red_y    = 165;
$blue_x   = 187;
$blue_y   = 125;
$radius   = 150;

// asigna colores con valores alpha
$yellow = imagecolorallocatealpha($image, 255, 255, 0, 75);
$red    = imagecolorallocatealpha($image, 255, 0, 0, 75);
$blue   = imagecolorallocatealpha($image, 0, 0, 255, 75);

// Dibuja 3 elipses
imagefilledellipse($image, $yellow_x, $yellow_y, $radius, $radius, $yellow);
imagefilledellipse($image, $red_x, $red_y, $radius, $radius, $red);
imagefilledellipse($image, $blue_x, $blue_y, $radius, $radius, $blue);

// No olvidar enviar un header correcto
header('Content-Type: image/png');

// y finalmente, mostrar el resultado
imagepng($image);
?>

   
```php

Resultado del ejemplo anterior es similar a:

![Salida del ejemplo: imagecolorallocatealpha()](en/reference/image/figures/imagecolorallocatealpha.png)

Conversión de valor alpha típico para usarlo con `imagecolorallocatealpha`

Generalmente los valores alpha `0` designan los píxeles completamente transparentes, y el canal alpha tiene 8 bits. Para convertir tales valores alpha para ser compatibles con `imagecolorallocatealpha`, un poco de aritmética simple es suficiente:

```
<?php
$alpha8 = 0; // completamente transparente
var_dump(127 - ($alpha8 >> 1));
$alpha8 = 255; // completamente opaco
var_dump(127 - ($alpha8 >> 1));
?>

   
```php

El ejemplo anterior mostrará:

    int(127)
    int(0)

## Véase también

imagecolorallocate

imagecolordeallocate
