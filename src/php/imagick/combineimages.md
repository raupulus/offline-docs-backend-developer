---
title: Imagick::combineImages
description: Combina una o más imágenes en una sóla imagen
source_url: https://www.php.net/manual/es/imagick.combineimages.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/combineimages.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32900
---

Imagick::combineImages

Combina una o más imágenes en una sóla imagen

## Descripción

```php
public Imagick::combineImages(int $channelType): Imagick
```php

Combina una o más imágenes en una sóla imagen. El valor de la escala de grises de los píxeles de cada imagen en la secuencia se asigna para especificar los canales de la imagen combinada. El orden típico sería imagen 1 =\> Red, 2 =\> Green, 3 =\> Blue, etc.

## Parámetros

`channelType`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
