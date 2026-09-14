---
title: Gmagick::addnoiseimage
description: Añade ruido aleatorio a la imagen
source_url: https://www.php.net/manual/es/gmagick.addnoiseimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/addnoiseimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26460
---

Gmagick::addnoiseimage

Añade ruido aleatorio a la imagen

## Descripción

```php
public Gmagick::addnoiseimage(int $noise_type): Gmagick
```php

Añade ruido aleatorio a la imagen.

## Parámetros

`noise_type`  
El tipo de ruido. Consulte esta lista de [constantes de ruido](#gmagick.constants.noise).

## Valores devueltos

El objeto Gmagick con el ruido añadido.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
