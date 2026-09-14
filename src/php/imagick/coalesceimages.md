---
title: Imagick::coalesceImages
description: Componer un conjunto de imágenes
source_url: https://www.php.net/manual/es/imagick.coalesceimages.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/coalesceimages.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 32860
---

Imagick::coalesceImages

Componer un conjunto de imágenes

## Descripción

```php
public Imagick::coalesceImages(): Imagick
```php

Componer un conjunto de imágenes respetando todas las posiciones y los métodos de disposición. Las secuencias de animaciones GIF, MIFF y MNG, comienzan típicamente con una imagen de fondo, seguida de todas las imágenes siguientes que varían en tamaño y posición. Retorna un nuevo objeto Imagick donde cada imagen de la secuencia tiene el mismo tamaño que la primera, y compuesta con la siguiente en la secuencia.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna un nuevo objeto Imagick en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
