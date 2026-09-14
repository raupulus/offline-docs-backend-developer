---
title: Imagick::thumbnailImage
description: Modifica el tamaño de una imagen
source_url: https://www.php.net/manual/es/imagick.thumbnailimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/thumbnailimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1c1a7fa9f
order: 35940
---

Imagick::thumbnailImage

Modifica el tamaño de una imagen

## Descripción

```php
public Imagick::thumbnailImage(int $columns, int $rows, [bool $bestfit], [bool $fill], [bool $legacy]): bool
```php

Modifica el tamaño de una imagen a las dimensiones dadas y elimina todos los perfiles asociados. El objetivo es producir una miniatura de bajo costo para su visualización en la web. Si `true` se proporciona como tercer argumento, entonces los argumentos `columns` y `rows` se utilizarán como máximo para cada lado. Cada lado se reducirá hasta que se alcance el tamaño deseado.

> [!NOTE]
> El comportamiento del parámetro `bestfit` cambió con Imagick 3.0.0. Antes de esta versión, proporcionar las dimensiones 400x400 a una imagen de dimensiones 200x150 hacía que la parte izquierda permaneciera sin cambios. Con Imagick 3.0.0 y posteriores, la imagen se reduce al tamaño 400x300, siendo este el mejor resultado para esas dimensiones. Si el parámetro `bestfit` es utilizado, la anchura y la altura deben ser proporcionadas.

## Parámetros

`columns`  
Ancho de la imagen

`rows`  
Alto de la imagen

`bestfit`  
Si se deben forzar los valores máximos

`fill`  
Si la imagen no llena completamente el área, entonces esta se rellena con el color de fondo de la imagen.

`legacy`  
Redondea la dimensión más pequeña al entero inferior más cercano.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::thumbnailImage`

```
      
<?php
function thumbnailImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->setbackgroundcolor('rgb(64, 64, 64)');
    $imagick->thumbnailImage(100, 100, true, true);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
