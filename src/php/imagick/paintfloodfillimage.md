---
title: Imagick::paintFloodfillImage
description: Cambia el valor del color de cualquier píxel que coincida con el objetivo
source_url: https://www.php.net/manual/es/imagick.paintfloodfillimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/paintfloodfillimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34640
---

Imagick::paintFloodfillImage

Cambia el valor del color de cualquier píxel que coincida con el objetivo

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::paintFloodfillImage(mixed $fill, float $fuzz, mixed $bordercolor, int $x, int $y, [int $channel]): bool
```php

Cambia el valor del color de cualquier píxel que coincida con el objetivo y esté en la zona inmediata. A partir de ImageMagick 6.3.8 este método está obsoleto y se debería usar `Imagick::floodfillPaintImage` en su lugar.

## Parámetros

`fill`  
Objeto ImagickPixel o un string que contiene el color de relleno

`fuzz`  
La cantidad de enfoque. Por ejemplo, establecer el enfoque a 10 y el color a rojo con una intensidad de 100 y 102 respectivamente ahora se interpreta como el mismo color para los propósitos del relleno.

`bordercolor`  
Objeto ImagickPixel que contiene el color de borde

`x`  
Posición X del inicio del relleno

`y`  
Posición Y del inicio del relleno

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para aplicarlo a más de un canal, combínense las [constantes de canales](#imagick.constants.channel) utilizando un operador a nivel de bits. Por defecto, vale `Imagick::CHANNEL_DEFAULT`. Consúltese la lista de [constantes de canales](#imagick.constants.channel)

## Valores devueltos

Devuelve `true` en caso de éxito.
