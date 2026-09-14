---
title: imagecreatefromwebp
description: Crear una nueva imagen a partir de un fichero o una URL
source_url: https://www.php.net/manual/es/function.imagecreatefromwebp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecreatefromwebp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 9960a09a5
order: 31870
---

imagecreatefromwebp

Crear una nueva imagen a partir de un fichero o una URL

## Descripción

```php
imagecreatefromwebp(string $filename): GdImage
```php

`imagecreatefromwebp` devuelve un identificador de imagen que representa la imagen obtenida desde el fichero proporcionado. Tenga en cuenta que los ficheros WebP animados no pueden ser leídos.

> [!TIP]
> Puede utilizar una URL como nombre de archivo con esta función, si el [gestor fopen](#ini.allow-url-fopen) ha sido activado. Véase `fopen` para más detalles sobre cómo especificar el nombre del archivo. Consulte [???](#wrappers) para más información sobre las capacidades de los diferentes gestores, las notas sobre su uso, así como la información sobre las variables predefinidas que proporcionan.

## Parámetros

`filename`  
Ruta hacia la imagen WebP.

## Valores devueltos

Devuelve un objeto de imagen en caso de éxito, `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Convierte una imagen WebP en una imagen jpeg utilizando la función `imagecreatefromwebp`

```
<?php
// Carga el fichero WebP
$im = imagecreatefromwebp('./example.webp');

// Se convierte en un fichero jpeg con una calidad del 100%
imagejpeg($im, './example.jpeg', 100);
?>

    
```php
