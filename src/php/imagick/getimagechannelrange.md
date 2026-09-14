---
title: Imagick::getImageChannelRange
description: Obtiene el rango del canal
source_url: https://www.php.net/manual/es/imagick.getimagechannelrange.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagechannelrange.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33580
---

Imagick::getImageChannelRange

Obtiene el rango del canal

## Descripción

```php
public Imagick::getImageChannelRange(int $channel): array
```php

Obtiene el rango de uno o más canales de imagen. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.0 o superior.

## Parámetros

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para aplicarlo a más de un canal, combínense las [constantes de canales](#imagick.constants.channel) utilizando un operador a nivel de bits. Por defecto, vale `Imagick::CHANNEL_DEFAULT`. Consúltese la lista de [constantes de canales](#imagick.constants.channel)

## Valores devueltos

Devuelve una matriz que contiene los valores mínimo y máximo de el/los canal/es.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
