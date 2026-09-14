---
title: Imagick::compareImageChannels
description: Devuelve la diferencia entre una o más imágenes
source_url: https://www.php.net/manual/es/imagick.compareimagechannels.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/compareimagechannels.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32920
---

Imagick::compareImageChannels

Devuelve la diferencia entre una o más imágenes

## Descripción

```php
public Imagick::compareImageChannels(Imagick $image, int $channelType, int $metricType): array
```php

Compara una o más imágenes y devuelve la imagen de diferencia.

## Parámetros

`image`  
Un objeto Imagick que contiene la imagen a comparar.

`channelType`  
Proporcione cualquier constante de canal que sea válida para el modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

`metricType`  
Una de las [constantes de tipos de métrica](#imagick.constants.metric).

## Valores devueltos

Array que consiste en `new_wand` y `distortion`.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
