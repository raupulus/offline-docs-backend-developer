---
title: Imagick::remapImage
description: Re-mapea los colores de una imagen
source_url: https://www.php.net/manual/es/imagick.remapimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/remapimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 29b20493d
order: 34890
---

Imagick::remapImage

Re-mapea los colores de una imagen

## Descripción

```php
public Imagick::remapImage(Imagick $replacement, int $DITHER): bool
```php

Reemplaza los colores de una imagen con los definidos por el parámetro `replacement`. Los colores son reemplazados con el color más cercano posible. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.5 o superior.

## Parámetros

`replacement`  
Un objeto Imagick que contiene los colores sustitutos

`DITHER`  
Consulte esta lista de [constantes de métodos de entramado](#imagick.constants.dithermethod)

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
