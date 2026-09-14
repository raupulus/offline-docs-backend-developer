---
title: Imagick::getImageChannelKurtosis
description: Obtiene la curtosis y la asimetría estadística de un canal específico
source_url: https://www.php.net/manual/es/imagick.getimagechannelkurtosis.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagechannelkurtosis.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 4314ee19f
order: 33560
---

Imagick::getImageChannelKurtosis

Obtiene la curtosis y la asimetría estadística de un canal específico

## Descripción

```php
public Imagick::getImageChannelKurtosis([int $channel]): array
```php

Obtiene la curtosis y la asimetría estadística de un canal específico. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.9 o superior.

## Parámetros

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para aplicarlo a más de un canal, combínense las [constantes de canales](#imagick.constants.channel) utilizando un operador a nivel de bits. Por defecto, vale `Imagick::CHANNEL_DEFAULT`. Consúltese la lista de [constantes de canales](#imagick.constants.channel)

## Valores devueltos

Devuelve una matriz con los miembros `kurtosis` (curtosis) y `skewness` (asimetría estadística).

## Errores/Excepciones

Lanza una ImagickException en caso de error.
