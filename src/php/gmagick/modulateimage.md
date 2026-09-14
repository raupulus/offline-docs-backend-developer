---
title: Gmagick::modulateimage
description: Controla la luminosidad, la saturación y el tono
source_url: https://www.php.net/manual/es/gmagick.modulateimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/modulateimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27210
---

Gmagick::modulateimage

Controla la luminosidad, la saturación y el tono

## Descripción

```php
public Gmagick::modulateimage(float $brightness, float $saturation, float $hue): Gmagick
```php

Permite controlar la luminosidad, la saturación y el tono de una imagen. El tono es un porcentaje de una rotación absoluta desde la posición actual. Por ejemplo, 50 corresponde a una rotación de 90 grados en el sentido contrario a las agujas de un reloj, 150, una rotación de 90 grados en el sentido de las agujas de un reloj, o bien, 0 o 200 corresponde a una rotación de 180 grados.

## Parámetros

`brightness`  
El número de porcentaje a modificar para la luminosidad (-100 a +100).

`saturation`  
El número de porcentaje a modificar para la saturación (-100 a +100).

`hue`  
El número de porcentaje a modificar para el tono (-100 a +100).

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
