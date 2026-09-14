---
title: Imagick::encipherImage
description: Cifra una imagen
source_url: https://www.php.net/manual/es/imagick.encipherimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/encipherimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33180
---

Imagick::encipherImage

Cifra una imagen

## Descripción

```php
public Imagick::encipherImage(string $passphrase): bool
```php

Covierte los píxeles planos en píxeles cifrados. La imagen no es legible hasta que haya sido descifrada usando `Imagick::decipherImage` Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.9 o superior.

## Parámetros

`passphrase`  
La frase de contraseña

## Valores devueltos

Devuelve `true` en caso de éxito.

## Véase también

`Imagick::decipherImage`
