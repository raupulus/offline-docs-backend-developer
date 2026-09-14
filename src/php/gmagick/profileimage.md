---
title: Gmagick::profileimage
description: Añade o elimina un perfil de una imagen
source_url: https://www.php.net/manual/es/gmagick.profileimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/profileimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27280
---

Gmagick::profileimage

Añade o elimina un perfil de una imagen

## Descripción

```php
public Gmagick::profileimage(string $name, string $profile): Gmagick
```php

Añade o elimina un perfil ICC, IPTC o genérico de una imagen. Si el perfil es `null`, será eliminado de la imagen, de lo contrario, será añadido. Utilice `*` como nombre y un perfil `null` para eliminar todos los perfiles de la imagen.

## Parámetros

`name`  
Nombre del perfil a añadir o eliminar: perfil ICC, IPTC o genérico.

`profile`  
El perfil.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
