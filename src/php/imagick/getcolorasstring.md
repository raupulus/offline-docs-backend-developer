---
title: ImagickPixel::getColorAsString
description: Devuelve un color
source_url: https://www.php.net/manual/es/imagickpixel.getcolorasstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/getcolorasstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 37540
---

ImagickPixel::getColorAsString

Devuelve un color

## Descripción

```php
public ImagickPixel::getColorAsString(): string
```php

Devuelve el color del objeto ImagickPixel, en forma de `string`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el color del objeto ImagickPixel, en forma de `string`.

## Ejemplos

Uso básico del método `Imagick::getColorAsString`

```
<?php

//Crea un objeto ImagickPixel con el color predefinido 'marron'
$color = new ImagickPixel('brown');

$color->setColorValue(Imagick::COLOR_ALPHA, 64 / 256.0);

$colorInfo = $color->getColorAsString();

print_r($colorInfo);
?>

    
```php

El ejemplo anterior mostrará:

    rgb(165,42,42)

## Notas

> [!NOTE]
> Este método no devuelve el valor del alpha del color en la cadena.
