---
title: imageloadfont
description: Carga una nueva fuente
source_url: https://www.php.net/manual/es/function.imageloadfont.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageloadfont.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: a24296728
order: 32210
---

imageloadfont

Carga una nueva fuente

## Descripción

```php
imageloadfont(string $filename): GdFont
```php

`imageloadfont` carga una nueva fuente de usuario y devuelve su identificador.

## Parámetros

`filename`  
El formato de las fuentes depende actualmente del sistema operativo. Esto significa que es necesario generar archivos de fuentes para la máquina que ejecuta PHP.

| Posición | Tipo de datos C | Descripción |
|----|----|----|
| Octetos 0-3 | int | Número de caracteres de la fuente |
| Octetos 4-7 | int | Valor del primer carácter de la fuente (generalmente 32 para espacio) |
| Octetos 8-11 | int | Ancho en píxeles de los caracteres |
| Octetos 12-15 | int | Altura en píxeles de los caracteres |
| Octetos 16- | char | Tabla con los datos de los caracteres, un octeto por píxel para cada carácter, con un total de (número de caracteres \* ancho \* altura) octetos. |

Formato de archivo de fuente

## Valores devueltos

Devuelve una instancia `GdFont`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `GdFont`; anteriormente se devolvía un `int`. |

## Ejemplos

Ejemplo con `imageloadfont`

```
<?php
// Creación de una nueva imagen
$im = imagecreatetruecolor(50, 20);
$black = imagecolorallocate($im, 0, 0, 0);
$white = imagecolorallocate($im, 255, 255, 255);

// Define el fondo en blanco
imagefilledrectangle($im, 0, 0, 49, 19, $white);

// Carga la fuente GD y escribe '¡Hola!'
$font = imageloadfont('./04b.gdf');
imagestring($im, $font, 0, 0, '¡Hola!', $black);

// Muestra en el navegador
header('Content-type: image/png');

imagepng($im);
?>

    
```php

## Véase también

imagefontwidth

imagefontheight

imagestring
