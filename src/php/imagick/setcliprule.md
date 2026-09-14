---
title: ImagickDraw::setClipRule
description: Configura la regla de relleno del polígono a utilizar con los caminos
source_url: https://www.php.net/manual/es/imagickdraw.setcliprule.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setcliprule.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 36990
---

ImagickDraw::setClipRule

Configura la regla de relleno del polígono a utilizar con los caminos

## Descripción

```php
public ImagickDraw::setClipRule(int $fillrule): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Configura la regla de relleno del polígono a utilizar con los caminos.

## Parámetros

`fillrule`  
Una de las constantes [FILLRULE](#imagick.constants.fillrule) (`imagick::FILLRULE_*`).

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setClipRule`

```
<?php
function setClipRule($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeOpacity(1);
    $draw->setStrokeWidth(2);
    //\Imagick::FILLRULE_EVENODD
    //\Imagick::FILLRULE_NONZERO

    $clipPathName = 'testClipPath';
    $draw->pushClipPath($clipPathName);
    $draw->setClipRule(\Imagick::FILLRULE_EVENODD);
    $draw->rectangle(0, 0, 300, 500);
    $draw->rectangle(200, 0, 500, 500);
    $draw->popClipPath();
    $draw->setClipPath($clipPathName);
    $draw->rectangle(200, 200, 300, 300);

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");

    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
