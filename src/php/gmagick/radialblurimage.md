---
title: Gmagick::radialblurimage
description: Desenfoca una imagen siguiendo un radio
source_url: https://www.php.net/manual/es/gmagick.radialblurimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/radialblurimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27340
---

Gmagick::radialblurimage

Desenfoca una imagen siguiendo un radio

## Descripción

```php
public Gmagick::radialblurimage(float $angle, [int $channel]): Gmagick
```php

Desenfoca una imagen siguiendo un radio.

## Parámetros

`angle`  
El ángulo de desenfoque, en grados.

`channel`  
Canal afectado.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
