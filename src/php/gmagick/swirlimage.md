---
title: Gmagick::swirlimage
description: Remue los píxeles del centro de la imagen
source_url: https://www.php.net/manual/es/gmagick.swirlimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/swirlimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27810
---

Gmagick::swirlimage

Remue los píxeles del centro de la imagen

## Descripción

```php
public Gmagick::swirlimage(float $degrees): Gmagick
```php

Remue los píxeles del centro de la imagen, donde los grados indican el arco de remolino alrededor del cual los píxeles son desplazados. Se puede obtener un efecto cada vez más pronunciado modificando los grados de 1 a 360.

## Parámetros

`degrees`  
Define la intensidad del efecto de remolino.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
