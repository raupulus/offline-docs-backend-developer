---
title: Imagick::adaptiveResizeImage
description: Redimensiona una imagen adaptativamente con información dependiente de
  la triangulación
source_url: https://www.php.net/manual/es/imagick.adaptiveresizeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/adaptiveresizeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32610
---

Imagick::adaptiveResizeImage

Redimensiona una imagen adaptativamente con información dependiente de la triangulación

## Descripción

```php
public Imagick::adaptiveResizeImage(int $columns, int $rows, [bool $bestfit], [bool $legacy]): bool
```php

Redimensiona una imagen adaptativamente con información dependiente de la triangulación. Evita la borrosidad a través de cambios de color bruscos. Muy útil cuando se usa para encoger ligeramente imágenes a un "tamaño web" ligeramente más pequeño; puede que no tenga una buena apariencia cuando una imagen a tamaño completo se redimensiona adaptativamente a una miniatura. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

> [!NOTE]
> El comportamiento del parámetro `bestfit` cambió con Imagick 3.0.0. Antes de esta versión, proporcionar las dimensiones 400x400 a una imagen de dimensiones 200x150 hacía que la parte izquierda permaneciera sin cambios. Con Imagick 3.0.0 y posteriores, la imagen se reduce al tamaño 400x300, siendo este el mejor resultado para esas dimensiones. Si el parámetro `bestfit` es utilizado, la anchura y la altura deben ser proporcionadas.

## Parámetros

`columns`  
El número de columnas en la imagen escalada.

`rows`  
El número de filas en la imagen escalada.

`bestfit`  
Si ajustar la imagen dentro de una caja limitada.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Añadido el parámetro opcional de ajuste. |
| PECL imagick 2.1.0 | Este método ahora soporta escalas proporcionales. Pase cero como parámetro para escalar proporcionalmente. |

## Ejemplos

Usar `Imagick::adaptiveResizeImage`

Redimensiona una imagen al tamaño estándar para la web. Este método trabaja mejor cuando se redimensiona a un tamaño sólo ligeramente menor que el tamaño de la imagen previa.

```
<?php
header('Content-type: image/jpeg');

$imagen = new Imagick('image.jpg');
$image->adaptiveResizeImage(1024,768);

echo $imagen;
?>

    
```php

## Véase también

`Imagick::chopImage`, `Imagick::cropImage`, `Imagick::magnifyImage`, `Imagick::minifyImage`, `Imagick::resizeImage`, `Imagick::scaleImage`, `Imagick::shaveImage`, `Imagick::thumbnailImage`, `Imagick::trimImage`
