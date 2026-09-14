---
title: imagecreatefromstring
description: Crea una imagen a partir de una cadena
source_url: https://www.php.net/manual/es/function.imagecreatefromstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecreatefromstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31840
---

imagecreatefromstring

Crea una imagen a partir de una cadena

## Descripción

```php
imagecreatefromstring(string $data): GdImage
```php

`imagecreatefromstring` devuelve un identificador de imagen que representa la imagen obtenida desde la cadena `data`. El tipo de la imagen será detectado automáticamente si PHP ha sido compilado con soporte para: JPEG, PNG, GIF, BMP, WBMP, GD2, WEBP y AVIF.

## Parámetros

`data`  
Una cadena que contiene los datos de la imagen.

## Valores devueltos

Un objeto de imagen será devuelto en caso de éxito. `false` es devuelto si el tipo de la imagen no es soportado, si los datos no están en un formato reconocido o si la imagen está corrupta y por lo tanto no puede ser cargada.

## Errores/Excepciones

`imagecreatefromstring` emite un error de nivel E_WARNING si los datos no están en un formato reconocido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage`; anteriormente, se devolvía un `resource`. |
| 7.3.0 | WEBP es soportado ahora (si es soportado por la libgd utilizada). |

## Ejemplos

Ejemplo con `imagecreatefromstring`

```
<?php
$data = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAASCAMAAAB/2U7WAAAABl'
       . 'BMVEUAAAD///+l2Z/dAAAASUlEQVR4XqWQUQoAIAxC2/0vXZDr'
       . 'EX4IJTRkb7lobNUStXsB0jIXIAMSsQnWlsV+wULF4Avk9fLq2r'
       . '8a5HSE35Q3eO2XP1A1wQkZSgETvDtKdQAAAABJRU5ErkJggg==';
$data = base64_decode($data);

$im = imagecreatefromstring($data);
if ($im !== false) {
    header('Content-Type: image/png');
    imagepng($im);
}
else {
    echo 'Ha ocurrido un error.';
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagecreatefromstring()](en/reference/image/figures/imagecreatefromstring.png)

## Véase también

imagecreatefromjpeg

imagecreatefrompng

imagecreatefromgif

imagecreatetruecolor
