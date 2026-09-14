---
title: Gmagick::removeimageprofile
description: Elimina el perfil nombrado de la imagen y lo devuelve
source_url: https://www.php.net/manual/es/gmagick.removeimageprofile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/removeimageprofile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 27420
---

Gmagick::removeimageprofile

Elimina el perfil nombrado de la imagen y lo devuelve

## Descripción

```php
public Gmagick::removeimageprofile(string $name): string
```php

Elimina el perfil nombrado de la imagen y lo devuelve.

## Parámetros

`name`  
El nombre del perfil a devolver: ICC, IPTC, o perfil genérico.

## Valores devueltos

El perfil nombrado.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
