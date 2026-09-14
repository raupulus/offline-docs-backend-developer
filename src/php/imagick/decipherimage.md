---
title: Imagick::decipherImage
description: Descifra una imagen
source_url: https://www.php.net/manual/es/imagick.decipherimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/decipherimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33050
---

Imagick::decipherImage

Descifra una imagen

## Descripción

```php
public Imagick::decipherImage(string $passphrase): bool
```php

Descifra una imagen que ha sido cifrada anteriormente. La iamgen debe ser cifrada usando `Imagick::encipherImage`. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.9 o superior.

## Parámetros

`passphrase`  
La frase de contraseña

## Valores devueltos

Devuelve `true` en caso de éxito.

## Véase también

`Imagick::encipherImage`
