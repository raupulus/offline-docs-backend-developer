---
title: Gmagick::cyclecolormapimage
description: Desplaza un mapa de color de una imagen
source_url: https://www.php.net/manual/es/gmagick.cyclecolormapimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/cyclecolormapimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26590
---

Gmagick::cyclecolormapimage

Desplaza un mapa de color de una imagen

## Descripción

```php
public Gmagick::cyclecolormapimage(int $displace): Gmagick
```php

Desplaza un mapa de color de una imagen por el número de posiciones dado. Si se realiza un ciclo del mapa de colores varias veces se puede obtener un efecto psicodélico.

## Parámetros

`displace`  
La cantidad a desplazar el mapa de color.

## Valores devueltos

Se devuelve a sí mismo si se tuvo éxito.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
