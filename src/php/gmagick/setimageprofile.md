---
title: Gmagick::setimageprofile
description: Añade un perfil nombrado al objeto Gmagick
source_url: https://www.php.net/manual/es/gmagick.setimageprofile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/setimageprofile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 27670
---

Gmagick::setimageprofile

Añade un perfil nombrado al objeto Gmagick

## Descripción

```php
public Gmagick::setimageprofile(string $name, string $profile): Gmagick
```php

Añade un perfil nombrado al objeto Gmagick. Si un perfil con el mismo nobre ya existe, se reemplaza. Este método difiere del método Gmagick::ProfileImage() en que no aplica ningún perfil de color CMS.

## Parámetros

`name`  
El nombre del perfil a añadir o eliminar: ICC, IPTC, o perfil genérico.

`profile`  
El perfil.

## Valores devueltos

El objeto Gmagick si se tuvo éxito.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
