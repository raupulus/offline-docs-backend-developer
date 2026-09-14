---
title: Gmagick::implodeimage
description: Crea una nueva imagen como una copia
source_url: https://www.php.net/manual/es/gmagick.implodeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/implodeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 27140
---

Gmagick::implodeimage

Crea una nueva imagen como una copia

## Descripción

```php
public Gmagick::implodeimage(float $radius): mixed
```php

Crea una nueva imagen que es una copia de una existente con los píxeles de la imagen "implosionados" por el porcentaje especificado.

## Parámetros

`radius`  
El radio de la implosión.

## Valores devueltos

Devuelve el objeto `Gmagick` implosionado.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
