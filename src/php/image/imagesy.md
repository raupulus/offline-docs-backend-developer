---
title: imagesy
description: Devuelve la altura de la imagen
source_url: https://www.php.net/manual/es/function.imagesy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagesy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 37f858a55
order: 32420
---

imagesy

Devuelve la altura de la imagen

## Descripción

```php
imagesy(GdImage $image): int
```php

Devuelve la altura de la imagen `image`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

## Valores devueltos

Devuelve la altura de la imagen `image`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagesy`

```
<?php

// Creación de una imagen 300*200
$img = imagecreatetruecolor(300, 200);

echo imagesy($img); // 200

?>

    
```php

## Véase también

imagecreatetruecolor

getimagesize

imagesx
