---
title: Imagick::setPointSize
description: Define la medida del punto
source_url: https://www.php.net/manual/es/imagick.setpointsize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setpointsize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 35650
---

Imagick::setPointSize

Define la medida del punto

## Descripción

```php
public Imagick::setPointSize(float $point_size): bool
```php

Define la propiedad de la medida del punto del objeto. Este método puede ser utilizado para, por ejemplo, definir la medida de la fuente para la leyenda: pseudo-formato. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.7 o superior.

## Parámetros

`point_size`  
La medida del punto.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `Imagick::setPointSize`

Ejemplo de uso del método Imagick::setPointSize

```
<?php
/* Crea un nuevo objeto imagick */
$im = new Imagick();

/* Define la fuente para el objeto */
$im->setFont("example.ttf");

/* Define la medida del punto */
$im->setPointSize(12);

/* Crea una nueva leyenda */
$im->newPseudoImage(100, 100, "caption:Hello");

/* Realiza algunas operaciones con la nueva imagen */
?>

    
```php

## Véase también

`Imagick::getPointSize`
