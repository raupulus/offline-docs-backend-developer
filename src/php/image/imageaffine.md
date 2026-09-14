---
title: imageaffine
description: Devuelve una imagen que contiene la imagen fuente transformada, utilizando
  opcionalmente una zona de recorte
source_url: https://www.php.net/manual/es/function.imageaffine.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageaffine.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 593ea510e
order: 31430
---

imageaffine

Devuelve una imagen que contiene la imagen fuente transformada, utilizando opcionalmente una zona de recorte

## Descripción

```php
imageaffine(GdImage $image, array $affine, [array $clip]): GdImage
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`affine`  
Un array con las claves de 0 a 5.

`clip`  
Un array con las claves "x", "y", "width" y "height"; o `null`.

## Valores devueltos

Devuelve el objeto de imagen vinculado en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `clip` ahora es nullable. |
| 8.0.0 | En caso de éxito, esta función ahora devuelve una instancia de `GDImage`; anteriormente se devolvía un `resource`. |
