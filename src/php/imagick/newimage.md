---
title: Imagick::newImage
description: Crea una nueva imagen
source_url: https://www.php.net/manual/es/imagick.newimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/newimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34560
---

Imagick::newImage

Crea una nueva imagen

## Descripción

```php
public Imagick::newImage(int $cols, int $rows, mixed $background, [string $format]): bool
```php

Crea una nueva imagen y asocia el valor de ImagickPixel al color de fondo

## Parámetros

`cols`  
Columnas en la nueva imagen

`rows`  
Filas en la nueva imagen

`background`  
El color de fondo usado para esta imagen

`format`  
El formato de la imagen. Este parámetro se añadió en la versión 2.0.1 de Imagick.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que una cadena represente el color como tercer parámetro Versiones anteriores sólo permitían un objeto ImagickPixel. |

## Ejemplos

Usar `Imagick::newImage`:

Crear una nueva imagen y mostrarla.

```
<?php

$imagen = new Imagick();
$imagen->newImage(100, 100, new ImagickPixel('red'));
$imagen->setImageFormat('png');

header('Content-type: image/png');
echo $imagen;

?>

    
```php
