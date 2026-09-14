---
title: imagecolortransparent
description: Define la color transparente
source_url: https://www.php.net/manual/es/function.imagecolortransparent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolortransparent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 31680
---

imagecolortransparent

Define la color transparente

## Descripción

```php
imagecolortransparent(GdImage $image, [int $color]): int
```php

Obtiene o define la color transparente para la `image` proporcionada.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`color`  
Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Se devuelve el identificador de la nueva color transparente (o la actual, si no se especifica ninguna). Si el argumento `color` es `null` y la imagen no tiene color transparente, el identificador devuelto será `-1`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |
| 8.0.0 | `color` ahora es nullable. |

## Ejemplos

Ejemplo con `imagecolortransparent`

```
<?php
// Creación de una imagen de 55x30
$im = imagecreatetruecolor(55, 30);
$red = imagecolorallocate($im, 255, 0, 0);
$black = imagecolorallocate($im, 0, 0, 0);

// Se hace el fondo transparente
imagecolortransparent($im, $black);

// Se dibuja un rectángulo rojo
imagefilledrectangle($im, 4, 4, 50, 25, $red);

// Se guarda la imagen
imagepng($im, './imagecolortransparent.png');
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagecolortransparent()](en/reference/image/figures/imagecolortransparent.png)

## Notas

> [!NOTE]
> La transparencia se copia únicamente con la función `imagecopymerge` y las imágenes en color verdadero, no con la función `imagecopy` ni las imágenes de paleta.

> [!NOTE]
> La color de transparencia es una propiedad de la imagen, no es una propiedad de la color. Una vez que se ha definido la color de transparencia, cada región de la imagen de esa color que se haya dibujado previamente será transparente.
