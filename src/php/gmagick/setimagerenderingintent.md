---
title: Gmagick::setimagerenderingintent
description: Define la imagen de renderizado
source_url: https://www.php.net/manual/es/gmagick.setimagerenderingintent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/setimagerenderingintent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27690
---

Gmagick::setimagerenderingintent

Define la imagen de renderizado

## Descripción

```php
public Gmagick::setimagerenderingintent(int $rendering_intent): Gmagick
```php

Define la imagen de renderizado.

## Parámetros

`rendering_intent`  
Una de las constantes de [renderizado de imagen](#gmagick.constants.renderingintent) (`Gmagick::RENDERINGINTENT_*`).

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
