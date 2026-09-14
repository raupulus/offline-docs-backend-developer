---
title: Imagick::getImageChannelMean
description: Obtiene la media y la desviación estándar
source_url: https://www.php.net/manual/es/imagick.getimagechannelmean.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagechannelmean.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 02639373d
order: 33570
---

Imagick::getImageChannelMean

Obtiene la media y la desviación estándar

## Descripción

```php
public Imagick::getImageChannelMean(int $channel): array
```php

Obtiene la media y la desviación estándar de uno o más canales de imagen.

## Parámetros

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve una matriz con miembros `"mean"` y `"standardDeviation"`.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
