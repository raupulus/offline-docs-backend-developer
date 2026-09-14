---
title: Gmagick::shearimage
description: Crea un paralelogramo
source_url: https://www.php.net/manual/es/gmagick.shearimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/shearimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27770
---

Gmagick::shearimage

Crea un paralelogramo

## Descripción

```php
public Gmagick::shearimage(mixed $color, float $xShear, float $yShear): Gmagick
```php

Mueve una esquina de la imagen a lo largo de los ejes X o Y para crear un paralelogramo. Una dirección en X mueve a lo largo del eje X, mientras que una dirección en Y mueve a lo largo del eje Y. La cantidad de corte se controla mediante un ángulo de corte. Para los cortes en dirección X, x_shear se mide relativamente al eje Y, e inversamente, para los cortes en dirección Y, y_shear se mide relativamente al eje X. Los triángulos vacíos así creados durante el corte de la imagen serán rellenados con el color de fondo.

## Parámetros

`color`  
El píxel de fondo.

`xShear`  
El grado de corte de la imagen.

`yShear`  
El grado de corte de la imagen.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
