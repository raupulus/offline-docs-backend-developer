---
title: imagecreatefromgd2part
description: Crea una nueva imagen a partir de una parte de un archivo GD2 o de una
  URL
source_url: https://www.php.net/manual/es/function.imagecreatefromgd2part.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecreatefromgd2part.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31800
---

imagecreatefromgd2part

Crea una nueva imagen a partir de una parte de un archivo GD2 o de una URL

## Descripción

```php
imagecreatefromgd2part(string $filename, int $x, int $y, int $width, int $height): GdImage
```php

Crea una nueva imagen a partir de una parte de un archivo GD2 o de una URL.

> [!TIP]
> Puede utilizar una URL como nombre de archivo con esta función, si el [gestor fopen](#ini.allow-url-fopen) ha sido activado. Véase `fopen` para más detalles sobre cómo especificar el nombre del archivo. Consulte [???](#wrappers) para más información sobre las capacidades de los diferentes gestores, las notas sobre su uso, así como la información sobre las variables predefinidas que proporcionan.

## Parámetros

`filename`  
Ruta hacia la imagen GD2.

`x`  
Coordenada en X del punto de origen.

`y`  
Coordenada en Y del punto de origen.

`width`  
Ancho de la fuente.

`height`  
Altura de la fuente.

## Valores devueltos

Devuelve un objeto de imagen en caso de éxito, `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Ejemplo con `imagecreatefromgd2part`

```
<?php
// Para este ejemplo, primero se necesitan las dimensiones de la imagen
$image = getimagesize('./test.gd2');

// Creación de la instancia de imagen ahora que se tienen las dimensiones
$im = imagecreatefromgd2part('./test.gd2', 4, 4, ($image[0] / 2) - 6, ($image[1] / 2) - 6);

// Operación sobre la imagen: aquí se imprime la imagen
if(function_exists('imagefilter'))
{
    imagefilter($im, IMG_FILTER_EMBOSS);
}

// Guardado de la imagen optimizada
imagegd2($im, './test_emboss.gd2');
?>

    
```php

## Notas

> [!WARNING]
> Los formatos de imagen GD y GD2 son formatos propietarios de libgd. Deben considerarse *obsoletos*, y solo deben utilizarse con fines de desarrollo y pruebas.
