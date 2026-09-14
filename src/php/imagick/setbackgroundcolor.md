---
title: Imagick::setBackgroundColor
description: Establece el color de fondo por omisión del objeto
source_url: https://www.php.net/manual/es/imagick.setbackgroundcolor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setbackgroundcolor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35060
---

Imagick::setBackgroundColor

Establece el color de fondo por omisión del objeto

## Descripción

```php
public Imagick::setBackgroundColor(mixed $background): bool
```php

Establece el color de fondo por omisión del objeto.

## Parámetros

`background`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que un string represente el color como un parámetro. Las versiones anteriores sólo permiten un objeto ImagickPixel. |
