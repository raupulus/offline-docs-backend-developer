---
title: imagesx
description: Devuelve el ancho de una imagen
source_url: https://www.php.net/manual/es/function.imagesx.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagesx.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 0462f49fb
order: 32410
---

imagesx

Devuelve el ancho de una imagen

## Descripción

```php
imagesx(GdImage $image): int
```php

Devuelve el ancho del objeto imagen `image`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

## Valores devueltos

Devuelve el ancho de la imagen `image`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagesx`

```
<?php

// Creación de una imagen de 300*200
$img = imagecreatetruecolor(300, 200);

echo imagesx($img); // 300

?>

    
```php

## Véase también

imagecreatetruecolor

getimagesize

imagesy
