---
title: Imagick::profileImage
description: Añade o elimina un perfil de una imagen
source_url: https://www.php.net/manual/es/imagick.profileimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/profileimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: aec0a64f5
order: 34740
---

Imagick::profileImage

Añade o elimina un perfil de una imagen

## Descripción

```php
public Imagick::profileImage(string $name, [string $profile]): bool
```php

Añade o elimina un perfil ICC, IPTC, o genérico de una imagen. Si el `profile` es `null`, se elimina de la imagen en lugar de añadirse.

Para eliminar todos los perfiles de la imagen, use `'*'` como `name` y `null` para el `profile`.

## Parámetros

`name`  
El nombre del perfil.

`profile`  
Datos del perfil. Si es `null`, el perfil especificado será eliminado.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
