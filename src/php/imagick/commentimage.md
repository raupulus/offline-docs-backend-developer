---
title: Imagick::commentImage
description: Añade un comentario a la imagen
source_url: https://www.php.net/manual/es/imagick.commentimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/commentimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32910
---

Imagick::commentImage

Añade un comentario a la imagen

## Descripción

```php
public Imagick::commentImage(string $comment): bool
```php

Añade un comentario a la imagen.

## Parámetros

`comment`  
El comentario a añadir

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Usar `Imagick::commentImage`:

Comentar una imagen y recuperar el comentario:

```
<?php

/* Crear un nuevo objeto Imagick */
$im = new imagick();

/* Crear una imagen vacía */
$im->newImage(100, 100, new ImagickPixel("red"));

/* Añadir el comentario a la imagen */
$im->commentImage("¡Hola Mundo!");

/* Mostrar el comentario */
echo $im->getImageProperty("comment");

?>

    
```php
