---
title: Imagick::colorFloodfillImage
description: Cambia el valor del color de cualquier píxel que coincida con el objetivo
source_url: https://www.php.net/manual/es/imagick.colorfloodfillimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/colorfloodfillimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32870
---

Imagick::colorFloodfillImage

Cambia el valor del color de cualquier píxel que coincida con el objetivo

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::colorFloodfillImage(mixed $fill, float $fuzz, mixed $bordercolor, int $x, int $y): bool
```php

Cambia el valor del color de cualquier píxel que coincida con el objetivo y esté en el área inmediata.

## Parámetros

`fill`  
Objeto ImagickPixel que contiene el color de relleno

`fuzz`  
La cantidad de enfoque. Por ejemplo, establecer el enfoque a 10 y el color a rojo con una intensidad de 100 y 102 respectivamente ahora se interpreta como el mismo color para los propósitos del relleno.

`bordercolor`  
Objeto ImagickPixel que contiene el color de borde

`x`  
Posición X del inicio del relleno

`y`  
Posición Y del inicio del relleno

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que una cadena represente el color como el primer y tercer parámetros. Versiones anteriores sólo permitían un objeto ImagickPixel. |
