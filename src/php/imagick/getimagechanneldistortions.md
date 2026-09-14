---
title: Imagick::getImageChannelDistortions
description: Obtiene las distorsiones de un canal
source_url: https://www.php.net/manual/es/imagick.getimagechanneldistortions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagechanneldistortions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 19e812213
order: 33540
---

Imagick::getImageChannelDistortions

Obtiene las distorsiones de un canal

## Descripción

```php
public Imagick::getImageChannelDistortions(Imagick $reference, int $metric, [int $channel]): float
```php

Compara uno o varios canales de una imagen con una imagen reconstruida, y devuelve las medidas de la distorsión especificada. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

## Parámetros

`reference`  
Objeto Imagick que contiene la referencia de la imagen.

`metric`  
Consúltese la lista de [constantes de tipo de medidas](#imagick.constants.metric).

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para aplicarlo a más de un canal, combínense las [constantes de canales](#imagick.constants.channel) utilizando un operador a nivel de bits. Por defecto, vale `Imagick::CHANNEL_DEFAULT`. Consúltese la lista de [constantes de canales](#imagick.constants.channel)

## Valores devueltos

Devuelve un `float`, que describe la distorsión del canal.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
