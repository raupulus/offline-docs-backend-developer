---
title: Imagick::getImageProfiles
description: Devuelve los perfiles de la imagen
source_url: https://www.php.net/manual/es/imagick.getimageprofiles.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimageprofiles.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 0ffb9c9fc
order: 33920
---

Imagick::getImageProfiles

Devuelve los perfiles de la imagen

## Descripción

```php
public Imagick::getImageProfiles([string $pattern], [bool $include_values]): array
```php

Devuelve los perfiles de la imagen que coinciden con un patrón. Si `false` se pasa como segundo argumento, solo se devuelven los nombres de los perfiles. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

## Parámetros

`pattern`  
El patrón de perfil a leer.

`include_values`  
Si se deben devolver solo los nombres de los perfiles. Si `false` se proporciona, solo se devolverán los nombres de las propiedades.

## Valores devueltos

Devuelve un array con los perfiles de la imagen, o bien solo los nombres de los perfiles.
