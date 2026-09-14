---
title: Imagick::setImageMatteColor
description: Establece el color mate de la imagen
source_url: https://www.php.net/manual/es/imagick.setimagemattecolor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimagemattecolor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35450
---

Imagick::setImageMatteColor

Establece el color mate de la imagen

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::setImageMatteColor(mixed $matte): bool
```php

Establece el color mate de la imagen.

## Parámetros

`matte`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que un string represente el color como parámetro. Versiones anteriores sólo permitían un objeto ImagickPixel. |
