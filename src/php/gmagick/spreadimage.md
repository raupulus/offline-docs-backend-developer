---
title: Gmagick::spreadimage
description: Desplaza aleatoriamente cada píxel de un bloque
source_url: https://www.php.net/manual/es/gmagick.spreadimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/spreadimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27790
---

Gmagick::spreadimage

Desplaza aleatoriamente cada píxel de un bloque

## Descripción

```php
public Gmagick::spreadimage(float $radius): Gmagick
```php

Efecto especial que desplaza aleatoriamente cada píxel de un bloque definido por el argumento `radius`.

## Parámetros

`radius`  
Selecciona píxeles aleatoriamente en el vecindario de este alcance.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
