---
title: Imagick::setImageProfile
description: Añade un perfil nominado al objeto Imagick
source_url: https://www.php.net/manual/es/imagick.setimageprofile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimageprofile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35490
---

Imagick::setImageProfile

Añade un perfil nominado al objeto Imagick

## Descripción

```php
public Imagick::setImageProfile(string $name, string $profile): bool
```php

Añade un perfil nominado al objeto Imagick. Si un perfil con el mismo nobre ya existe, se reemplaza. Este método difiere del método Imagick::ProfileImage() en que no aplica ningún perfil de color CMS.

## Parámetros

`name`  

`profile`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
