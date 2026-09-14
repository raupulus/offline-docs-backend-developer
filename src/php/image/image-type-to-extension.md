---
title: image_type_to_extension
description: Devuelve la extensión del fichero para el tipo de imagen
source_url: https://www.php.net/manual/es/function.image-type-to-extension.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/image-type-to-extension.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31400
---

image_type_to_extension

Devuelve la extensión del fichero para el tipo de imagen

## Descripción

```php
image_type_to_extension(int $image_type, [bool $include_dot]): string
```php

`image_type_to_extension` devuelve la extensión para la constante `IMAGETYPE_*` proporcionada.

## Parámetros

`image_type`  
Una de las constantes `IMAGETYPE_*`.

`include_dot`  
Si se debe añadir un punto a la extensión o no. Por omisión, vale `true`.

## Valores devueltos

Un `string` con la extensión, correspondiente al tipo de la imagen proporcionada, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `image_type_to_extension`

```
<?php
// Creación de una instancia de imagen
$im = imagecreatetruecolor(100, 100);

// Guardado de la imagen
imagepng($im, './test' . image_type_to_extension(IMAGETYPE_PNG));
?>

    
```php

## Notas

> [!NOTE]
> Esta función no requiere la biblioteca GD.
