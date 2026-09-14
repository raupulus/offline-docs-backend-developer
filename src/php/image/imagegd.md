---
title: imagegd
description: Genera una imagen en formato GD, hacia el navegador o un fichero
source_url: https://www.php.net/manual/es/function.imagegd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagegd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 55f2d0cda
order: 32090
---

imagegd

Genera una imagen en formato GD, hacia el navegador o un fichero

## Descripción

```php
imagegd(GdImage $image, [string $file]): bool
```php

Genera o guarda el fichero `file` en formato GD.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`file`  
La ruta o un recurso de flujo abierto (que se cierra automáticamente después de que esta función retorne) donde guardar el fichero. Si no se define o es `null`, el flujo de imagen sin procesar se enviará directamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!CAUTION]
> Sin embargo, si libgd no logra producir la imagen, esta función devuelve `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.3 | `file` ahora es nullable. |
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |
| 7.2.0 | `imagegd` ahora permite producir imágenes TrueColor. Anteriormente, eran convertidas implícitamente a paleta. |

## Ejemplos

Mostrar una imagen GD

```
<?php
// Creación de una imagen vacía y adición de texto
$im = imagecreatetruecolor(120, 20);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5,  "Un texto simple", $text_color);

// Mostrar la imagen
imagegd($im);

?>

    
```php

Guardar una imagen GD

```
<?php
// Creación de una imagen vacía y adición de texto
$im = imagecreatetruecolor(120, 20);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5,  "Un texto simple", $text_color);

// Guardar la imagen GD
// El formato de fichero para imágenes GD es .gd, ver http://www.libgd.org/GdFileFormats
imagegd($im, 'simple.gd');

?>

    
```php

## Notas

> [!NOTE]
> El formato GD se utiliza comúnmente para permitir la carga rápida de partes de una imagen. Tenga en cuenta que el formato GD solo es utilizable en aplicaciones compatibles con GD.

> [!WARNING]
> Los formatos de imagen GD y GD2 son formatos propietarios de libgd. Deben considerarse *obsoletos*, y solo deben utilizarse con fines de desarrollo y pruebas.

## Véase también

imagegd2
