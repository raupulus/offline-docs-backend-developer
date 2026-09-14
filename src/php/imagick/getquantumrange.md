---
title: Imagick::getQuantumRange
description: Devuelve el intervalo cuántico de Imagick
source_url: https://www.php.net/manual/es/imagick.getquantumrange.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getquantumrange.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 34210
---

Imagick::getQuantumRange

Devuelve el intervalo cuántico de Imagick

## Descripción

```php
public static Imagick::getQuantumRange(): array
```php

Devuelve el intervalo cuántico de la instancia Imagick.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array asociativo que contiene el intervalo cuántico en forma de `int` (`"quantumRangeLong"`) y en forma de `string` (`"quantumRangeString"`).

## Errores/Excepciones

Lanza una ImagickException en caso de error.
