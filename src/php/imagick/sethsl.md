---
title: ImagickPixel::setHSL
description: Define el color HSL normalizado
source_url: https://www.php.net/manual/es/imagickpixel.sethsl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/sethsl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 37680
---

ImagickPixel::setHSL

Define el color HSL normalizado

## Descripción

```php
public ImagickPixel::setHSL(float $hue, float $saturation, float $luminosity): bool
```php

Define el color descrito por el objeto ImagickPixel utilizando los valores normalizados para la densidad, la saturación y la luminosidad.

## Parámetros

`hue`  
El valor normalizado para la densidad, descrito por un arco fraccionario (entre 0 y 1) del círculo de densidad, cuyo valor cero corresponde a rojo.

`saturation`  
El valor normalizado para la saturación, donde 1 corresponde a una saturación completa.

`luminosity`  
El valor normalizado para la luminosidad, comprendido entre 0 (negro) y 1 (blanco), con el valor HS completo a 0.5 de luminosidad.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `ImagickPixel::setHSL` para modificar un color

```
<?php

// Crea un rojo puro
$color = new ImagickPixel('rgb(90%, 10%, 10%)');

// Obtiene sus valores HSL
$colorInfo = $color->getHSL();

// Realiza una rotación del tono de 180 grados
$newHue = $colorInfo['hue'] + 0.5;
if ($newHue > 1) {
    $newHue = $newHue - 1;
}

// Define el objeto ImagickPixel al nuevo color
$colorInfo = $color->setHSL($newHue, $colorInfo['saturation'], $colorInfo['luminosity']);

// Verifica que el nuevo color sea azul/verde
$colorInfo = $color->getcolor();
print_r($colorInfo);

?>
        
    
```php

El ejemplo anterior mostrará:

    Array
    (
        [r] => 26
        [g] => 230
        [b] => 230
        [a] => 255
    )

## Notas

> [!NOTE]
> Disponible a partir de la versión 6.2.9 de la biblioteca ImageMagick.
