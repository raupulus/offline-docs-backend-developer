---
title: Gmagick::gammaimage
description: Corrección gamma de una imagen
source_url: https://www.php.net/manual/es/gmagick.gammaimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/gammaimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26710
---

Gmagick::gammaimage

Corrección gamma de una imagen

## Descripción

```php
public Gmagick::gammaimage(float $gamma): Gmagick
```php

Corrección gamma de una imagen. La misma imagen vista en diferentes dispositivos tendrá diferencias perceptuales en la manera en que la intensidad de la imagen esté representada en la pantalla. Especifique niveles gamma indivuduales para los canales rojo, verde y azul, o ajústelos todos con el parámetro gamma. El rango de valores es típicamente desde 0.8 a 2.3.

## Parámetros

`gamma`  
La cantidad de corrección gamma.

## Valores devueltos

El objeto `Gmagick` con el valor gamma corregido.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
