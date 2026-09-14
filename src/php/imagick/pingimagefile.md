---
title: Imagick::pingImageFile
description: Obtener los atrbutos básicos de la imagen de una manera liviana
source_url: https://www.php.net/manual/es/imagick.pingimagefile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/pingimagefile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34690
---

Imagick::pingImageFile

Obtener los atrbutos básicos de la imagen de una manera liviana

## Descripción

```php
public Imagick::pingImageFile(resource $filehandle, [string $fileName]): bool
```php

Este método se puede usar para preguntar por el ancho, alto, tamaño y formato de la imagen sin leer toda la imagen de la memoria. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`filehandle`  
Un gestor de archivo abierto a la imagen.

`fileName`  
Nombre de archivo opcional para esta imagen.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Usar `Imagick::pingImageFile`

Abrir una ubicación remota

```
<?php
/* usar fopen para abrir una ubicación remota */
$fp = fopen("http://example.com/test.jpg");

/* crear un nuevo objeto imagick */
$im = new Imagick();

/* pasar el gestor a imagick */
$im->pingImageFile($fp);
?>

    
```php

## Véase también

`Imagick::pingImage`, `Imagick::pingImageBlob`, `Imagick::readImage`, `Imagick::readImageBlob`, `Imagick::readImageFile`
