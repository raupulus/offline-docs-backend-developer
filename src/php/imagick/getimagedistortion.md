---
title: Imagick::getImageDistortion
description: Compara una imagen con una imagen reconstruida
source_url: https://www.php.net/manual/es/imagick.getimagedistortion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagedistortion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33700
---

Imagick::getImageDistortion

Compara una imagen con una imagen reconstruida

## Descripción

```php
public Imagick::getImageDistortion(MagickWand $reference, int $metric): float
```php

Compara una imagen con una imagen reconstruida y devuelve la métrica de distorisión especificada.

## Parámetros

`reference`  
Objeto Imagick que se va a comparar.

`metric`  
Una de las [constantes de tipo de métrica](#imagick.constants.metric).

## Valores devueltos

Devuelve la métrica de distorsión usada en la imagen (o la mejor deducción de la misma).

## Errores/Excepciones

Lanza una ImagickException en caso de error.
