---
title: Imagick::cycleColormapImage
description: Desplaza el mapa de colores de una imagen
source_url: https://www.php.net/manual/es/imagick.cyclecolormapimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/cyclecolormapimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33040
---

Imagick::cycleColormapImage

Desplaza el mapa de colores de una imagen

## Descripción

```php
public Imagick::cycleColormapImage(int $displace): bool
```php

Desplaza el mapa de colores de una imagen por el número de posiciones dados. Si se realiza un ciclo del mapa de colores varias veces se puede obtener un efecto psicodélico.

## Parámetros

`displace`  
La cantidad de desplazamiento del mapa de colores.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
