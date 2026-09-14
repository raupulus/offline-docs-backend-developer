---
title: ps_setcolor
description: Establece el color actual
source_url: https://www.php.net/manual/es/function.ps-setcolor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-setcolor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 9486a954a
order: 66060
---

ps_setcolor

Establece el color actual

## Descripción

```php
ps_setcolor(resource $psdoc, string $type, string $colorspace, float $c1, float $c2, float $c3, float $c4): bool
```php

Establece el color para el dibujo, relleno o ambos.

## Parámetros

`psdoc`  
Identificador de un fichero postscript devuelto por `ps_new`.

`type`  
El argumento `type` puede ser `both`, `fill` o `fillstroke`.

`colorspace`  
El espacio de color puede ser `gray`, `rgb`, `cmyk`, `spot`, `pattern`. Dependiendo del espacio de color, pueden usarse el primer, los tres primeros o todos los argumentos.

`c1`  
Dependiendo del espacio de color, este valor puede ser el componente rojo (rgb), el componente cian (cmyk), el valor de gris (gris), el identificador de la mancha de color o el identificador del patrón.

`c2`  
Dependiendo del espacio de color, este valor puede ser el componente verde (rgb) o el componente magenta (cmyk).

`c3`  
Dependiendo del espacio de color, este valor puede ser el componente azul (rgb) o el componente amarillo (cymk).

`c4`  
Este argumento debe fijarse solo en el espacio de color cymk y especifica el componente negro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Notas

> [!CAUTION]
> El segundo argumento no siempre es evaluado actualmente. La color puede ser establecida para rellenar y dibujar como si `fillstroke` hubiera sido pasado.
