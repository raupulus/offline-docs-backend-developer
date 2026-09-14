---
title: Gmagick::rotateimage
description: Rota una imagen
source_url: https://www.php.net/manual/es/gmagick.rotateimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/rotateimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 27460
---

Gmagick::rotateimage

Rota una imagen

## Descripción

```php
public Gmagick::rotateimage(mixed $color, float $degrees): Gmagick
```php

Rota una imagen el número de grados especificado. Los triángulos vacíos sobrantes por la rotación de la imagen se rellenan con el color de fondo.

## Parámetros

`color`  
El píxel de color de fondo.

`degrees`  
El número de grados que se va a rotar la imagen.

## Valores devueltos

El objeto Gmagick si se tuvo éxito

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
