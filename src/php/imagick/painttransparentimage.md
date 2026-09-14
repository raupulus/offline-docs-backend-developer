---
title: Imagick::paintTransparentImage
description: Cambia cualquier píxel que coincida con el color definido para el relleno
source_url: https://www.php.net/manual/es/imagick.painttransparentimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/painttransparentimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34660
---

Imagick::paintTransparentImage

Cambia cualquier píxel que coincida con el color definido para el relleno

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::paintTransparentImage(mixed $target, float $alpha, float $fuzz): bool
```php

Cambia cualquier píxel que coincida con el color definido para el relleno.

## Parámetros

`target`  
Cambia este color objetivo por el valor de opacidad especificado dentro de la imagen.

`alpha`  
El nivel de transparencia: 1.0 es completamente opaco y 0.0 es completamente transparente.

`fuzz`  
El miembro enfoque de la imagen define cuánta tolerancia es aceptable para considerar que dos colores son el mismo.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que una cadena represente el color como primer parámetro. Versiones anteriores sólo permitían un objeto ImagickPixel. |
