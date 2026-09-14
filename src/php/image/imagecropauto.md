---
title: imagecropauto
description: Recorta una imagen automáticamente utilizando uno de los modos disponibles
source_url: https://www.php.net/manual/es/function.imagecropauto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecropauto.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31920
---

imagecropauto

Recorta una imagen automáticamente utilizando uno de los modos disponibles

## Descripción

```php
imagecropauto(GdImage $image, [int $mode], [float $threshold], [int $color]): GdImage
```php

Recorta automáticamente una imagen según el `mode`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`mode`  
Una constante entre:

`IMG_CROP_DEFAULT`  
Idéntico a `IMG_CROP_TRANSPARENT`. Anterior a PHP 7.4.0, la biblioteca libgd integrada utilizaba `IMG_CROP_SIDES` como solución de respaldo, si la imagen no tenía color de transparencia.

`IMG_CROP_TRANSPARENT`  
Recorta el fondo transparente.

`IMG_CROP_BLACK`  
Recorta el fondo negro.

`IMG_CROP_WHITE`  
Recorta el fondo blanco.

`IMG_CROP_SIDES`  
Utiliza las 4 esquinas de la imagen para intentar detectar el fondo a recortar.

`IMG_CROP_THRESHOLD`  
Recorta la imagen utilizando el umbral `threshold` y `color`.

`threshold`  
Especifica la tolerancia en porcentaje a utilizar durante la comparación de la color de la imagen y la color a recortar. El método utilizado para calcular la diferencia de color se basa en la distancia de colores en el cubo RVB(a).

Utilizado únicamente en modo `IMG_CROP_THRESHOLD`.

> [!NOTE]
> Anterior a PHP 7.4.0, la biblioteca libgd integrada utilizaba un algoritmo algo diferente, por lo que el mismo `threshold` producía resultados diferentes para libgd sistema e integrado.

`color`  
Puede ser un valor de color RVB o un índice de paleta.

Utilizado únicamente en modo `IMG_CROP_THRESHOLD`.

## Valores devueltos

Devuelve el objeto de la imagen recortada en caso de éxito o `false` si ocurre un error. `false` también será devuelto si toda la imagen ha sido recortada.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage`; anteriormente, se devolvía un `resource`. |
| 7.4.0 | El comportamiento de imagecropauto de la biblioteca libgd integrada ha sido sincronizado con la de libgd sistema: `IMG_CROP_DEFAULT` ya no utiliza `IMG_CROP_SIDES` como solución de respaldo y la tolerancia de recorte utiliza ahora el mismo algoritmo que libgd sistema. |
| 7.4.0 | El valor por omisión de `mode` ha sido modificado a `IMG_CROP_AUTO`. Anteriormente, el valor por omisión era `-1` que corresponde a `IMG_CROP_DEFAULT`, pero pasar `-1` está ahora obsoleto. |

## Ejemplos

Recorte automático correcto

Como se indica en la sección valor de retorno, `imagecropauto` devuelve `false` si toda la imagen ha sido recortada. En este ejemplo, tenemos un objeto de imagen `$im` que solo debería ser automáticamente recortado si hay algo que recortar; de lo contrario, se desea conservar la imagen original.

```
<?php
$cropped = imagecropauto($im, IMG_CROP_DEFAULT);
if ($cropped !== false) { // Si se ha devuelto un nuevo objeto de imagen
    $im = $cropped;       // y asigna la imagen recortada a $im
}
?>

    
```php

## Véase también

imagecrop
