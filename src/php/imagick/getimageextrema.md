---
title: Imagick::getImageExtrema
description: Lee los extremos de una imagen
source_url: https://www.php.net/manual/es/imagick.getimageextrema.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimageextrema.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 33710
---

Imagick::getImageExtrema

Lee los extremos de una imagen

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::getImageExtrema(): array
```php

Lee los extremos de una imagen. Devuelve un array asociativo, con las claves "min" y "max".

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array asociativo, con las claves "min" y "max".

## Errores/Excepciones

Lanza una ImagickException en caso de error.
