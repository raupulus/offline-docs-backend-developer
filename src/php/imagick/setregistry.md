---
title: Imagick::setRegistry
description: Define la entrada del registro ImageMagick nombrada clave para valor
source_url: https://www.php.net/manual/es/imagick.setregistry.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setregistry.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1ef9c7a76
order: 35670
---

Imagick::setRegistry

Define la entrada del registro ImageMagick nombrada clave para valor

## Descripción

```php
public static Imagick::setRegistry(string $key, string $value): bool
```php

Define la entrada del registro ImageMagick nombrada clave para valor. Esto es lo más útil para definir "temporary-path" que controla dónde ImageMagick crea imágenes temporales, por ejemplo durante el procesamiento de PDF.

## Parámetros

`key`  

`value`  

## Valores devueltos

Devuelve `true` en caso de éxito.
