---
title: ImagickDraw::pushPattern
description: Indica que los comandos subsiguientes hasta un comando ImagickDraw::opPattern()
  comprenden la definición de un patrón nominado
source_url: https://www.php.net/manual/es/imagickdraw.pushpattern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/pushpattern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 668b6fc28
order: 36910
---

ImagickDraw::pushPattern

Indica que los comandos subsiguientes hasta un comando ImagickDraw::opPattern() comprenden la definición de un patrón nominado

## Descripción

```php
public ImagickDraw::pushPattern(string $pattern_id, float $x, float $y, float $width, float $height): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Indica que los comandos subsiguientes hasta un comando DrawPopPattern() comprenden la definición de un patrón nominado. Al espacio del patrón se le asigna las coordenadas de la esquina superior izquierda, un ancho y alto, y se convierte en su propio espacio de dibujo. Cualquier cosa que se pueda dibujar se puede usar en una definición de patrón. Los patrones nominados se pueden usar como definiciones de contorno o pincel.

## Parámetros

`pattern_id`  
el id del patrón

`x`  
coordenada x de la esquina superior izquierda

`y`  
coordenada y de la esquina superior izquierda

`width`  
ancho del patrón

`height`  
alto del patrón

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `ImagickDraw::pushPattern`

```
      
<?php
function pushPattern($strokeColor, $fillColor, $backgroundColor) {
    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeWidth(1);
    $draw->setStrokeOpacity(1);
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(1);

    $draw->pushPattern("MyFirstPattern", 0, 0, 50, 50);
    for ($x = 0; $x < 50; $x += 10) {
        for ($y = 0; $y < 50; $y += 5) {
            $positionX = $x + (($y / 5) % 5);
            $draw->rectangle($positionX, $y, $positionX + 5, $y + 5);
        }
    }
    $draw->popPattern();

    $draw->setFillOpacity(0);
    $draw->rectangle(100, 100, 400, 400);
    $draw->setFillOpacity(1);

    $draw->setFillOpacity(1);

    $draw->push();
    $draw->setFillPatternURL('#MyFirstPattern');
    $draw->setFillColor('yellow');
    $draw->rectangle(100, 100, 400, 400);
    $draw->pop();

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");

    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

      
```php
