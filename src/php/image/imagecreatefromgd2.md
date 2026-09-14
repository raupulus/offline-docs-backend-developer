---
title: imagecreatefromgd2
description: Crea una nueva imagen a partir de un fichero GD2 o de una URL
source_url: https://www.php.net/manual/es/function.imagecreatefromgd2.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecreatefromgd2.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31790
---

imagecreatefromgd2

Crea una nueva imagen a partir de un fichero GD2 o de una URL

## Descripción

```php
imagecreatefromgd2(string $filename): GdImage
```php

Crea una nueva imagen desde un fichero GD2 o una URL.

> [!TIP]
> Puede utilizar una URL como nombre de archivo con esta función, si el [gestor fopen](#ini.allow-url-fopen) ha sido activado. Véase `fopen` para más detalles sobre cómo especificar el nombre del archivo. Consulte [???](#wrappers) para más información sobre las capacidades de los diferentes gestores, las notas sobre su uso, así como la información sobre las variables predefinidas que proporcionan.

## Parámetros

`filename`  
Ruta de acceso a la imagen GD2.

## Valores devueltos

Devuelve un objeto de imagen en caso de éxito, `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Ejemplo con `imagecreatefromgd2`

```
<?php
// Carga la imagen gd2
$im = imagecreatefromgd2('./test.gd2');

// Aplica un efecto a la imagen: se aplica aquí un filtro negativo si existe
if(function_exists('imagefilter'))
{
    imagefilter($im, IMG_FILTER_NEGATE);
}

// Guarda la imagen
imagegd2($im, './test_updated.gd2');
?>

    
```php

## Notas

> [!WARNING]
> Los formatos de imagen GD y GD2 son formatos propietarios de libgd. Deben considerarse *obsoletos*, y solo deben utilizarse con fines de desarrollo y pruebas.
