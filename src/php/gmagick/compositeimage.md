---
title: Gmagick::compositeimage
description: Compone una imagen en otra
source_url: https://www.php.net/manual/es/gmagick.compositeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/compositeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26540
---

Gmagick::compositeimage

Compone una imagen en otra

## Descripción

```php
public Gmagick::compositeimage(Gmagick $source, int $COMPOSE, int $x, int $y): Gmagick
```php

Compone una imagen en otra en el índice especificado.

## Parámetros

`source`  
Objeto `Gmagick` que contiene la imagen compuesta

`COMPOSE`  
Operador de composción.

`x`  
El índice de columna de la imagen compuesta.

`y`  
El índice de fila de la imagen compuesta.

## Valores devueltos

El objeto `Gmagick` con composiciones.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
