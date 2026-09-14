---
title: Imagick::getImageChannelDepth
description: Obtiene la profundidad de un canal de imagen en particular
source_url: https://www.php.net/manual/es/imagick.getimagechanneldepth.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagechanneldepth.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33520
---

Imagick::getImageChannelDepth

Obtiene la profundidad de un canal de imagen en particular

## Descripción

```php
public Imagick::getImageChannelDepth(int $channel): int
```php

Obtiene la profundidad de un canal de imagen en particular.

## Parámetros

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para aplicarlo a más de un canal, combínense las [constantes de canales](#imagick.constants.channel) utilizando un operador a nivel de bits. Por defecto, vale `Imagick::CHANNEL_DEFAULT`. Consúltese la lista de [constantes de canales](#imagick.constants.channel)

## Valores devueltos

Devuelve `true` en caso de éxito.
