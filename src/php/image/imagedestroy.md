---
title: imagedestroy
description: Destruye una imagen
source_url: https://www.php.net/manual/es/function.imagedestroy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagedestroy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_revision: fcd921429
order: 31940
---

imagedestroy

Destruye una imagen

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] imagedestroy(GdImage $image): true
```php

> [!NOTE]
> Esta función no tiene ningún efecto. Anterior a PHP 8.0.0, esta función era utilizada para cerrar un recurso.

Anterior a PHP 8.0.0, `imagedestroy` liberaba toda la memoria asociada a la recurso `image`. A partir de la versión 8.0.0, la extensión GD utiliza objetos en lugar de recursos, y los objetos no pueden ser cerrados explícitamente.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Esta función ha sido declarada obsoleta. |
| 8.0.0 | Esta función es ahora un NOP. |
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Uso de `imagedestroy` anterior a PHP 8.0.0

```
<?php
// Crea una imagen de 100 x 100 píxeles
$im = imagecreatetruecolor(100, 100);

// Modificación y/o guardado de la imagen

// Liberación de la memoria asociada
imagedestroy($im);
?>

    
```php
