---
title: Imagick::setImage
description: Reemplaza una imagen en el objeto
source_url: https://www.php.net/manual/es/imagick.setimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35150
---

Imagick::setImage

Reemplaza una imagen en el objeto

## Descripción

```php
public Imagick::setImage(Imagick $replace): bool
```php

Reemplaza la secuencia de imágenes actual por la imagen del objeto sustituto.

## Parámetros

`replace`  
El objeto Imagick sustituto.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Un ejemplo de `Imagick::setImage`

Un ejemplo usando Imagick::setImage()

```
<?php
/* Crear los objetos */
$imagen = new Imagick('origen.jpg');
$sustituto = new Imagick('sustituto.jpg');

/* origen.jpg es reemplazado por sustituto.jpg */
$imagen->setImage($sustituto);

/* imprimir la imagen */
header('Content-type: image/jpeg');
echo $imagen;

?>

    
```php
