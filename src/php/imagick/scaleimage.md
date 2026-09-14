---
title: Imagick::scaleImage
description: Redimensiona la imagen a una escala específica
source_url: https://www.php.net/manual/es/imagick.scaleimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/scaleimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: dc4dddb02
order: 35010
---

Imagick::scaleImage

Redimensiona la imagen a una escala específica

## Descripción

```php
public Imagick::scaleImage(int $columns, int $rows, [bool $bestfit], [bool $legacy]): bool
```php

Redimensiona la imagen a las dimensiones especificadas. En caso de que alguno de los parámetros sea igual a 0, este será calculado automáticamente.

> [!NOTE]
> El comportamiento del parámetro `bestfit` cambió con Imagick 3.0.0. Antes de esta versión, proporcionar las dimensiones 400x400 a una imagen de dimensiones 200x150 hacía que la parte izquierda permaneciera sin cambios. Con Imagick 3.0.0 y posteriores, la imagen se reduce al tamaño 400x300, siendo este el mejor resultado para esas dimensiones. Si el parámetro `bestfit` es utilizado, la anchura y la altura deben ser proporcionadas.

## Parámetros

`columns`  

`rows`  

`bestfit`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Se añadió un parámetro opcional de ajuste. Este método soporta ahora el redimensionamiento proporcional. Pase cero en uno de los parámetros para activar esta opción. |

## Ejemplos

Ejemplo con `Imagick::scaleImage`

```
<?php
function scaleImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->scaleImage(150, 150, true);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

     
```php
