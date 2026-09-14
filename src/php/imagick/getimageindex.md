---
title: Imagick::getImageIndex
description: Obtiene el índice de la imagen actual
source_url: https://www.php.net/manual/es/imagick.getimageindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimageindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 33800
---

Imagick::getImageIndex

Obtiene el índice de la imagen actual

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::getImageIndex(): int
```php

Devuelve el índice de la imagen actual en la secuencia Imagick. Este método está obsoleto. Consúltese la función `Imagick::getIteratorIndex`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un integer en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
