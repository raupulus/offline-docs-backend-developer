---
title: Imagick::getImageChannelDistortion
description: Compara los canales de imagen de una imagen con una imagen reconstruida
source_url: https://www.php.net/manual/es/imagick.getimagechanneldistortion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagechanneldistortion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33530
---

Imagick::getImageChannelDistortion

Compara los canales de imagen de una imagen con una imagen reconstruida

## Descripción

```php
public Imagick::getImageChannelDistortion(Imagick $reference, int $channel, int $metric): float
```php

Compara uno o más canales de imagen de una imagen con una imagen reconstruida y devuelve la métrica de distorsión especificada.

## Parámetros

`reference`  
Objeto Imagick que se va a comparar.

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

`metric`  
Una de las [constantes de tipo de métrica](#imagick.constants.metric).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
