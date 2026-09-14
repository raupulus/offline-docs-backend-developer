---
title: Imagick::opaquePaintImage
description: Cambia el color de cualquier píxel que coincida con el objetivo
source_url: https://www.php.net/manual/es/imagick.opaquepaintimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/opaquepaintimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34610
---

Imagick::opaquePaintImage

Cambia el color de cualquier píxel que coincida con el objetivo

## Descripción

```php
public Imagick::opaquePaintImage(mixed $target, mixed $fill, float $fuzz, bool $invert, [int $channel]): bool
```php

Cambia cualquier píxel que coincida con el color definido para el relleno. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.8 o superior.

## Parámetros

`target`  
Objeto ImagickPixel o una cadena que contiene el color a cambiar

`fill`  
El color sustituto

`fuzz`  
La cantidad de polvo de papel. Por ejemplo, definir el polvo de papel a 10 y el color rojo a una intensidad de 100 y 102 no será interpretado como el mismo color.

`invert`  
Si es `true` pinta cualquier píxel que no coincida con el color objetivo.

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para aplicarlo a más de un canal, combínense las [constantes de canales](#imagick.constants.channel) utilizando un operador a nivel de bits. Por defecto, vale `Imagick::CHANNEL_DEFAULT`. Consúltese la lista de [constantes de canales](#imagick.constants.channel)

## Valores devueltos

Devuelve `true` en caso de éxito.
