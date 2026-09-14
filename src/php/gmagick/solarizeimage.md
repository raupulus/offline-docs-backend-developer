---
title: Gmagick::solarizeimage
description: Aplica un efecto de solarización a la imagen
source_url: https://www.php.net/manual/es/gmagick.solarizeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/solarizeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27780
---

Gmagick::solarizeimage

Aplica un efecto de solarización a la imagen

## Descripción

```php
public Gmagick::solarizeimage(int $threshold): Gmagick
```php

Aplica un efecto de solarización a la imagen, similar al efecto creado en una foto en cámara oscura, exponiendo las zonas de una foto sobre papel sensible a la luz. El umbral varía de 0 a QuantumRange y es una medida de la extensión de la solarización.

## Parámetros

`threshold`  
Define la extensión de la solarización.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
