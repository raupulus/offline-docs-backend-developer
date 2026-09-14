---
title: Imagick::getImageChannelExtrema
description: Obtiene los extremos de uno o más canales de imagen
source_url: https://www.php.net/manual/es/imagick.getimagechannelextrema.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagechannelextrema.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33550
---

Imagick::getImageChannelExtrema

Obtiene los extremos de uno o más canales de imagen

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::getImageChannelExtrema(int $channel): array
```php

Obtiene los extremos (mínimo y máximo) de uno o más canales de imagen. El valor devuelto es una matriz asociativa con las claves "minima" (mínimo) y "maxima" (máximo).

## Parámetros

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
