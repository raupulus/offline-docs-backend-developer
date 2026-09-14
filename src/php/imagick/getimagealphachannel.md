---
title: Imagick::getImageAlphaChannel
description: Verifica si la imagen tiene un canal alfa
source_url: https://www.php.net/manual/es/imagick.getimagealphachannel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagealphachannel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 0545e305c
order: 33450
---

Imagick::getImageAlphaChannel

Verifica si la imagen tiene un canal alfa

## Descripción

```php
public Imagick::getImageAlphaChannel(): bool
```php

Devuelve si la imagen tiene un canal alfa.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la imagen tiene un valor de canal alfa y `false` en caso contrario, es decir, que la imagen es RGB en lugar de RGBA o CMYK en lugar de CMYKA.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 3.6.0 | Ahora devuelve un `bool` ; anteriormente se devolvía un `int`. |
