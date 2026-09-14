---
title: ps_open_image
description: Leer una imagen para su colocación posterior
source_url: https://www.php.net/manual/es/function.ps-open-image.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-open-image.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: c6fb604f3
order: 65910
---

ps_open_image

Leer una imagen para su colocación posterior

## Descripción

```php
ps_open_image(resource $psdoc, string $type, string $source, string $data, int $length, int $width, int $height, int $components, int $bpc, string $params): int
```php

Lee una imagen que ya está disponible en memoria. El parámetro `source` actualmente no se evalua y se asume que es `memory`. La información de la imagen es una secuencia de píxeles que comienza en la esquina superior izquierda y termina en la esquina inferior derecha. Cada píxel consiste en componentes de color dados por `components`, y cada componente tiene `bpc` bits.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`type`  
El tipo de la imagen. Los posibles valores son `png`, `jpeg`, o `eps`.

`source`  
No se utiliza.

`data`  
La información de la imagen.

`length`  
La longitud de la información de la imagen.

`width`  
El ancho de la imagen.

`height`  
El alto de la imagen.

`components`  
El número de componentes de cada píxel. Puede ser 1 (imágenes en escala de grises), 3 (imágenes rgb), o 4 (imágenes cmyk, rgba).

`bpc`  
Número de bits por componente (normalmente 8).

`params`  

## Valores devueltos

Devuelve el identificador de la imagen, o cero en caso de error. El identificador es un número positivo mayor que 0.

## Véase también

`ps_open_image_file`, `ps_place_image`, `ps_close_image`
