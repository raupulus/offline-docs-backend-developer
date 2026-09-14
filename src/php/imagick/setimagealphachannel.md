---
title: Imagick::setImageAlphaChannel
description: Define el canal alfa de la imagen
source_url: https://www.php.net/manual/es/imagick.setimagealphachannel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimagealphachannel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 35160
---

Imagick::setImageAlphaChannel

Define el canal alfa de la imagen

## Descripción

```php
public Imagick::setImageAlphaChannel(int $mode): bool
```php

Activa o desactiva el canal alfa de la imagen. El `mode` es una de las constantes `Imagick::ALPHACHANNEL_*`. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.8 o superior.

## Parámetros

`mode`  
Una constante entre las constantes `Imagick::ALPHACHANNEL_*`.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Véase también

`Imagick::setImageMatte`, Las [constantes del canal Alfa Imagick](#imagick.constants.alphachannel)
