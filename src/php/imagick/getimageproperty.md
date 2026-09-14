---
title: Imagick::getImageProperty
description: Devuelve una propiedad de una imagen
source_url: https://www.php.net/manual/es/imagick.getimageproperty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimageproperty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 33940
---

Imagick::getImageProperty

Devuelve una propiedad de una imagen

## Descripción

```php
public Imagick::getImageProperty(string $name): string
```php

Devuelve una propiedad de una imagen. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.2 o superior.

## Parámetros

`name`  
El nombre de la propiedad (por ejemplo, `Exif:DateTime`)

## Valores devueltos

Devuelve una propiedad de una imagen, o `false` si el nombre solicitado no existe.

## Ejemplos

Ejemplo con `Imagick::getImageProperty`

Definición y recuperación de las propiedades de la imagen.

```
<?php
$image = new Imagick();
$image->newImage(300, 200, "black");

$image->setImageProperty('Exif:Make', 'Imagick');
echo $image->getImageProperty('Exif:Make');
?>

    
```php

## Véase también

`Imagick::setImageProperty`
