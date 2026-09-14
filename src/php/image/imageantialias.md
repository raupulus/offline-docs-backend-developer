---
title: imageantialias
description: Activar o desactivar las funciones de antialias
source_url: https://www.php.net/manual/es/function.imageantialias.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageantialias.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 31470
---

imageantialias

Activar o desactivar las funciones de antialias

## Descripción

```php
imageantialias(GdImage $image, bool $enable): true
```php

Activa los métodos de dibujo rápido antialias para líneas y polígonos. Los componentes alpha no son soportados. Funciona utilizando una operación directa de mezcla, únicamente con imágenes truecolor.

El grosor y los estilos no son soportados.

El uso de primitivas antialias con fondos transparentes puede llevar a resultados inesperados. El método de mezcla utiliza el color de fondo como cualquier otra color. La falta de soporte del componente alpha impide el uso de antialias basado en alpha.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`enable`  
Si se debe activar el antialias o no.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |
| 7.2.0 | `imageantialias` ahora está generalmente disponible. Anteriormente, solo estaba disponible si PHP fue compilado con la versión agrupada de la biblioteca GD. |

## Ejemplos

Comparación de 2 líneas, una con antialias y otra sin

```
<?php
// Define una imagen antialias y una normal
$aa = imagecreatetruecolor(400, 100);
$normal = imagecreatetruecolor(200, 100);

// Activa el antialiasing para una imagen
imageantialias($aa, true);

// Asigna los colores
$red = imagecolorallocate($normal, 255, 0, 0);
$red_aa = imagecolorallocate($aa, 255, 0, 0);

// Dibuja 2 líneas, una con antialiasing
imageline($normal, 0, 0, 200, 100, $red);
imageline($aa, 0, 0, 200, 100, $red_aa);

// Fusiona las 2 imágenes, lado a lado para la visualización
// (AA: izquierda, Normal: derecha)
imagecopymerge($aa, $normal, 200, 0, 0, 0, 200, 100, 100);

// Muestra la imagen
header('Content-type: image/png');

imagepng($aa);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: Comparación de 2 líneas, una con antialias](en/reference/image/figures/imageantialias.png)

## Véase también

imagecreatetruecolor
