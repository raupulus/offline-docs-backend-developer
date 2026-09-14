---
title: Gmagick::addimage
description: Añade una nueva imagen a la lista de imágenes del objeto Gmagick
source_url: https://www.php.net/manual/es/gmagick.addimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/addimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26450
---

Gmagick::addimage

Añade una nueva imagen a la lista de imágenes del objeto Gmagick

## Descripción

```php
public Gmagick::addimage(Gmagick $source): Gmagick
```php

Añade una nueva imagen al objeto Gmagick desde la posición actual del objeto de origen. Después de la operación la posición del iterador se mueve al final de la lista.

## Parámetros

`source`  
El objeto Gmagick de origen

## Valores devueltos

El objeto Gmagick con la imagen añadida

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
