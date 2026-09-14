---
title: Imagick::inverseFourierTransformImage
description: Implementa la transformada inversa de Fourier discreta (Discrete Fourier
  Transform - DFT)
source_url: https://www.php.net/manual/es/imagick.inversefouriertransformimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/inversefouriertransformimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1ef9c7a76
order: 34370
---

Imagick::inverseFourierTransformImage

Implementa la transformada inversa de Fourier discreta (Discrete Fourier Transform - DFT)

## Descripción

```php
public Imagick::inverseFourierTransformImage(Imagick $complement, bool $magnitude): bool
```php

Implementa la transformada inversa de Fourier discreta (DFT) de la imagen, ya sea como un par de imágenes magnitud/fase o como un par de imágenes reales/imaginarias.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`complement`  
La segunda imagen a combinar con esta para formar ya sea el par de imágenes magnitud/fase o el par de imágenes reales/imaginarias.

`magnitude`  
Si es verdadero, combina como un par magnitud/fase, de lo contrario, un par de imágenes reales/imaginarias.

## Valores devueltos

Devuelve `true` en caso de éxito.
