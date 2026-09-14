---
title: Imagick::setFont
description: Configura la fuente
source_url: https://www.php.net/manual/es/imagick.setfont.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setfont.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 35120
---

Imagick::setFont

Configura la fuente

## Descripción

```php
public Imagick::setFont(string $font): bool
```php

Configura la fuente de la imagen. Este método se utiliza para configurar la fuente utilizada por el pseudoformato : `caption`. La fuente debe estar configurada en la configuración de ImageMagick o bien, un fichero con el nombre de la fuente `font` debe existir. Este método no debe confundirse con el método `ImagickDraw::setFont` que define la fuente para un objeto ImagickDraw específico. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.7 o superior.

## Parámetros

`font`  
El nombre de la fuente o el nombre del fichero

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `Imagick::setFont`

Ejemplo de utilización de `Imagick::setFont`.

```
<?php
/* Crea un nuevo objeto Imagick */
$im = new Imagick();

/* Configura la fuente del objeto */
$im->setFont("example.ttf");

/* Crea un nuevo mensaje */
$im->newPseudoImage(100, 100, "caption:Hello");

/* Continuación del procesamiento de la imagen */
?>

    
```php

## Véase también

`Imagick::getFont`, `ImagickDraw::setFont`, `ImagickDraw::getFont`
