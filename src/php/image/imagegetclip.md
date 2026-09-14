---
title: imagegetclip
description: Obtiene el rectángulo de recorte
source_url: https://www.php.net/manual/es/function.imagegetclip.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagegetclip.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 593ea510e
order: 32110
---

imagegetclip

Obtiene el rectángulo de recorte

## Descripción

```php
imagegetclip(GdImage $image): array
```php

`imagegetclip` obtiene el rectángulo de recorte actual, es decir, el área más allá de la cual ningún píxel será dibujado.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

## Valores devueltos

La función devuelve un array indexado con las coordenadas del rectángulo de recorte con las siguientes entradas:

- la coordenada x de la esquina superior izquierda

- la coordenada y de la esquina superior izquierda

- la coordenada x de la esquina inferior derecha

- la coordenada y de la esquina inferior derecha

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagegetclip`

Definir y obtener el rectángulo de recorte.

```
<?php
$im = imagecreate(100, 100);
imagesetclip($im, 10,10, 89,89);
print_r(imagegetclip($im));

   
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => 10
        [1] => 10
        [2] => 89
        [3] => 89
    )

## Véase también

imagesetclip
