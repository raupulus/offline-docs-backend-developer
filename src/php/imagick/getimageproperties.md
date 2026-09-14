---
title: Imagick::getImageProperties
description: Devuelve las propiedades EXIF de la imagen
source_url: https://www.php.net/manual/es/imagick.getimageproperties.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimageproperties.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 6047c10c1
order: 33930
---

Imagick::getImageProperties

Devuelve las propiedades EXIF de la imagen

## Descripción

```php
public Imagick::getImageProperties([string $pattern], [bool $include_values]): array
```php

Devuelve todas las propiedades de la imagen que cumplen con un patrón. Si se pasa `false` como segundo argumento, solo se devuelven los nombres de las propiedades. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

## Parámetros

`pattern`  
El patrón para los nombres de propiedades.

`include_values`  
Si se deben devolver únicamente los nombres de las propiedades. Si se proporciona `false`, entonces solo se devolverán los nombres de las propiedades.

## Valores devueltos

Devuelve un array que contiene las propiedades de la imagen, o sus nombres.

## Ejemplos

Ejemplo con `Imagick::getImageProperties`

Ejemplo de extracción de información EXIF.

```
<?php

/* Crea un objeto */
$im = new imagick("/path/to/example.jpg");

/* Lee las informaciones EXIF */
$exifArray = $im->getImageProperties("exif:*");

/* Recorre las propiedades EXIF */
foreach ($exifArray as $name => $property)
{
    echo "{$name} => {$property}<br />\n";
}

?>

    
```php
