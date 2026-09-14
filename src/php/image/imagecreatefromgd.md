---
title: imagecreatefromgd
description: Crea una nueva imagen a partir de un fichero GD o de una URL
source_url: https://www.php.net/manual/es/function.imagecreatefromgd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecreatefromgd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 9960a09a5
order: 31780
---

imagecreatefromgd

Crea una nueva imagen a partir de un fichero GD o de una URL

## Descripción

```php
imagecreatefromgd(string $filename): GdImage
```php

Crea una nueva imagen a partir de un fichero GD o de una URL.

> [!TIP]
> Puede utilizar una URL como nombre de archivo con esta función, si el [gestor fopen](#ini.allow-url-fopen) ha sido activado. Véase `fopen` para más detalles sobre cómo especificar el nombre del archivo. Consulte [???](#wrappers) para más información sobre las capacidades de los diferentes gestores, las notas sobre su uso, así como la información sobre las variables predefinidas que proporcionan.

## Parámetros

`filename`  
Ruta de acceso a un fichero GD.

## Valores devueltos

Devuelve un objeto de imagen en caso de éxito, `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Ejemplo con `imagecreatefromgd`

```
<?php
// Carga una imagen GD
$im = @imagecreatefromgd('./test.gd');

// Verifica si la imagen se ha cargado correctamente
if(!$im)
{
     die('No ha sido posible cargar la imagen GD');
}

// Operaciones sobre la imagen aquí

// Guardado de la imagen
imagegd($im, './test_updated.gd');
?>

    
```php

## Notas

> [!WARNING]
> Los formatos de imagen GD y GD2 son formatos propietarios de libgd. Deben considerarse *obsoletos*, y solo deben utilizarse con fines de desarrollo y pruebas.
