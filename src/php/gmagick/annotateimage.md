---
title: Gmagick::annotateimage
description: Anota una imagen con texto
source_url: https://www.php.net/manual/es/gmagick.annotateimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/annotateimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26470
---

Gmagick::annotateimage

Anota una imagen con texto

## Descripción

```php
public Gmagick::annotateimage(GmagickDraw $GmagickDraw, float $x, float $y, float $angle, string $text): Gmagick
```php

Anota una imagen con texto.

## Parámetros

`GmagickDraw`  
El objeto `GmagickDraw` que contiene la configuración para dibujar el texto

`x`  
El índice horizontal en píxeles a la izquierda del texto.

`y`  
El índice vertical en píxeles a la línea base del texto.

`angle`  
El ángulo en el que escribir el texto.

`text`  
La cadena a dibujar.

## Valores devueltos

El objeto `Gmagick` con la anotación hecha.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
