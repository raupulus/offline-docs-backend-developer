---
title: Imagick::contrastStretchImage
description: Mejora el contraste de una imagen en color
source_url: https://www.php.net/manual/es/imagick.contraststretchimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/contraststretchimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32980
---

Imagick::contrastStretchImage

Mejora el contraste de una imagen en color

## Descripción

```php
public Imagick::contrastStretchImage(float $black_point, float $white_point, [int $channel]): bool
```php

Mejora el contraste de una imagen en color ajustando los colores de los píxeles de color para abarcar el rango completo de los colores disponibles. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`black_point`  
El punto blanco.

`white_point`  
El punto negro.

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. `Imagick::CHANNEL_ALL`. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.
