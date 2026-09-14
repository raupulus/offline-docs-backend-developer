---
title: Imagick::setImageIterations
description: Establece las iteraciones de una imagen
source_url: https://www.php.net/manual/es/imagick.setimageiterations.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimageiterations.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35430
---

Imagick::setImageIterations

Establece las iteraciones de una imagen

## Descripción

```php
public Imagick::setImageIterations(int $iterations): bool
```php

Establece el número de veces que una imagen animada se repite.

## Parámetros

`iterations`  
El número de veces que la imagen debería mostrarse en bucle. Establecer a '0' para un bucle infinito.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Uso básico de `Imagick::setImageIterations`

```
<?php

$imagick = new Imagick(realpath("Test.gif"));

$imagick = $imagick->coalesceImages();
$imagick->setImageIterations(1);
$imagick = $imagick->deconstructImages();

$imagick->writeImages('/ruta/donde/guardar/UnaVez.gif', true);

?>

    
```php
