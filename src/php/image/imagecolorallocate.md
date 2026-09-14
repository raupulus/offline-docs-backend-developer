---
title: imagecolorallocate
description: Asigna una coloración para una imagen
source_url: https://www.php.net/manual/es/function.imagecolorallocate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolorallocate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 593ea510e
order: 31530
---

imagecolorallocate

Asigna una coloración para una imagen

## Descripción

```php
imagecolorallocate(GdImage $image, int $red, int $green, int $blue): int
```php

Devuelve un identificador de color, representando la coloración compuesta con los colores RGB.

`imagecolorallocate` debe ser invocada para crear cada color que será representado por `image`.

> [!NOTE]
> La primera llamada a `imagecolorallocate` llena la coloración de fondo con la paleta de las imágenes - imágenes creadas utilizando `imagecreate`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`red`  
Valor del componente rojo.

`green`  
Valor del componente verde.

`blue`  
Valor del componente azul.

Estos argumentos son enteros comprendidos entre 0 y 255 o hexadecimales comprendidos entre 0x00 y 0xFF.

## Valores devueltos

Un identificador de color o `false` si la asignación falla.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagecolorallocate`

```
<?php

$im = imagecreate(100, 100);

// El fondo de la imagen es rojo
$background = imagecolorallocate($im, 255, 0, 0);

// Se definen colores con enteros ..
$white = imagecolorallocate($im, 255, 255, 255);
$black = imagecolorallocate($im, 0, 0, 0);

// .. o hexadecimales
$white = imagecolorallocate($im, 0xFF, 0xFF, 0xFF);
$black = imagecolorallocate($im, 0x00, 0x00, 0x00);

?>

    
```php

## Véase también

imagecolorallocatealpha

imagecolordeallocate
