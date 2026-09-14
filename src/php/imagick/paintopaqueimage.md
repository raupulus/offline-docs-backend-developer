---
title: Imagick::paintOpaqueImage
description: Cambia cualquier píxel que coincida con el color
source_url: https://www.php.net/manual/es/imagick.paintopaqueimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/paintopaqueimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34650
---

Imagick::paintOpaqueImage

Cambia cualquier píxel que coincida con el color

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::paintOpaqueImage(mixed $target, mixed $fill, float $fuzz, [int $channel]): bool
```php

Cambia cualquier píxel que coincida con el color definido por el relleno.

## Parámetros

`target`  
Cambia este color objetivo por el color de relleno de la imagen. Un objeto ImagickPixel o una cadena que representa el color objetivo.

`fill`  
Un objeto ImagickPixel o un string que representa el color de relleno.

`fuzz`  
El miembro enfoque de la imagen define cúanta tolerancia es aceptable para considerar que dos colores son el mismo.

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que una cadena represente el color como primer y segundo parámetros. Versiones anteriores sólo permitían un objeto ImagickPixel. |
