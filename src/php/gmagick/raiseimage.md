---
title: Gmagick::raiseimage
description: Crea un botón con un efecto 3D
source_url: https://www.php.net/manual/es/gmagick.raiseimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/raiseimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27350
---

Gmagick::raiseimage

Crea un botón con un efecto 3D

## Descripción

```php
public Gmagick::raiseimage(int $width, int $height, int $x, int $y, bool $raise): Gmagick
```php

Crea un botón con un efecto 3D aclarando y oscureciendo los ángulos de la imagen. La altura y el margen de los miembros de raise_info definen el ancho del borde vertical y horizontal del efecto.

## Parámetros

`width`  
Ancho de la zona a tratar.

`height`  
Altura de la zona a tratar.

`x`  
Coordenada en X.

`y`  
Coordenada en Y.

`raise`  
Un valor, distinto de 0, para crear el efecto 3D; de lo contrario, el efecto será atenuado.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
