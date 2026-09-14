---
title: Gmagick::trimimage
description: Elimina los bordes de la imagen
source_url: https://www.php.net/manual/es/gmagick.trimimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/trimimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27830
---

Gmagick::trimimage

Elimina los bordes de la imagen

## Descripción

```php
public Gmagick::trimimage(float $fuzz): Gmagick
```php

Elimina los bordes que son del color del fondo de la imagen.

## Parámetros

`fuzz`  
Por omisión, el objetivo debe coincidir exactamente con el color del píxel preciso. Sin embargo, en muchos casos, 2 colores pueden diferir ligeramente. Este parámetro indica la tolerancia admisible para considerar 2 colores como idénticos.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
