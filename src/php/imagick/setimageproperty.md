---
title: Imagick::setImageProperty
description: Configura una propiedad de imagen
source_url: https://www.php.net/manual/es/imagick.setimageproperty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimageproperty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 35500
---

Imagick::setImageProperty

Configura una propiedad de imagen

## Descripción

```php
public Imagick::setImageProperty(string $name, string $value): bool
```php

Configura la propiedad de imagen `name` al valor `value`. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.2 o superior.

## Parámetros

`name`  

`value`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `Imagick::setImageProperty`

Define y recupera las propiedades de una imagen.

```
<?php
$image = new Imagick();
$image->newImage(300, 200, "black");

$image->setImageProperty('Exif:Make', 'Imagick');
echo $image->getImageProperty('Exif:Make');
?>

    
```php

## Véase también

`Imagick::getImageProperty`
