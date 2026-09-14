---
title: image2wbmp
description: Enviar la imagen al navegador o a un fichero
source_url: https://www.php.net/manual/es/function.image2wbmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/image2wbmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31420
---

image2wbmp

Enviar la imagen al navegador o a un fichero

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.3.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
image2wbmp(resource $image, [string $filename], [int $foreground]): bool
```php

`image2wbmp` muestra o guarda una versión WBMP de la imagen `image` proporcionada.

## Parámetros

`image`  
Un recurso de imagen, devuelto por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`filename`  
Ruta del fichero de guardado. Si no se proporciona, el flujo de la imagen se mostrará directamente.

`foreground`  
El color del primer plano puede ser definido con este argumento proporcionando un identificador obtenido con `imagecolorallocate`. El color del primer plano por omisión es negro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!CAUTION]
> Sin embargo, si libgd no logra producir la imagen, esta función devuelve `true`.

## Ejemplos

Ejemplo con `image2wbmp`

```
<?php

$file = 'php.png';
$image = imagecreatefrompng($file);

header('Content-Type: ' . image_type_to_mime_type(IMAGETYPE_WBMP));
image2wbmp($image); // Mostrar directamente

?>

    
```php

## Véase también

imagewbmp
