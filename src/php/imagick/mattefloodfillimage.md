---
title: Imagick::matteFloodfillImage
description: Cambia el valor de transparencia de un color
source_url: https://www.php.net/manual/es/imagick.mattefloodfillimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/mattefloodfillimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34450
---

Imagick::matteFloodfillImage

Cambia el valor de transparencia de un color

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::matteFloodfillImage(float $alpha, float $fuzz, mixed $bordercolor, int $x, int $y): bool
```php

Cambia el valor de transparencia de un píxel que coincide con el objetivo y esté en la zona inmediata. Si el método `FillToBorderMethod` se especifica, el valor de transparencia se cambia por cualquier píxel inmediato que no coincida con el miembro color del borde de la imagen.

## Parámetros

`alpha`  
El nivel de transparencia: 1.0 es completamente opaco y 0.0 es completamente transparente.

`fuzz`  
El miembro enfoque de la imagen define cuánta tolerancia se acepta para considerar que dos colores son el mismo.

`bordercolor`  
Un objeto `ImagickPixel` o una cadena que representa el color del borde.

`x`  
La coordenada x de inicio de la operación.

`y`  
La coordenada y de inicio de la operación.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que una cadena represente el color como tercer parámetro. Versiones anteriores sólo permitían un objeto `ImagickPixel`. |
