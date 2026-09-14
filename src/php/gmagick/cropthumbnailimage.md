---
title: Gmagick::cropthumbnailimage
description: Crea una miniatura recortada
source_url: https://www.php.net/manual/es/gmagick.cropthumbnailimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/cropthumbnailimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26570
---

Gmagick::cropthumbnailimage

Crea una miniatura recortada

## Descripción

```php
public Gmagick::cropthumbnailimage(int $width, int $height): Gmagick
```php

Crea una miniatura de tamaño fijo ampliando o reduciendo de escala la imagen y recortando un área específica desde el centro.

## Parámetros

`width`  
El ancho de la miniatura.

`height`  
El alto de la miniatura.

## Valores devueltos

El objeto `Gmagick` recortado.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
