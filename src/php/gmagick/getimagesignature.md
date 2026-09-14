---
title: Gmagick::getimagesignature
description: Genera un resumen de un mensaje SHA-256
source_url: https://www.php.net/manual/es/gmagick.getimagesignature.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/getimagesignature.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 27010
---

Gmagick::getimagesignature

Genera un resumen de un mensaje SHA-256

## Descripción

```php
public Gmagick::getimagesignature(): string
```php

Genera un resumen de un mensaje SHA-256 para el flujo de píxeles de la imagen.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una cadena que contiene el hash SHA-256 del archivo.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
