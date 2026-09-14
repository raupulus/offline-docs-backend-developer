---
title: Imagick::sampleImage
description: Escala una imagen con un muestreo de píxeles
source_url: https://www.php.net/manual/es/imagick.sampleimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/sampleimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35000
---

Imagick::sampleImage

Escala una imagen con un muestreo de píxeles

## Descripción

```php
public Imagick::sampleImage(int $columns, int $rows): bool
```php

Escala una imagen a las dimensiones deseadas con un muestreo de píxeles. A diferencia de otros métodos de escala, este método no introduce colores adicionales en la imagen escalada.

## Parámetros

`columns`  

`rows`  

## Valores devueltos

Devuelve `true` en caso de éxito.
