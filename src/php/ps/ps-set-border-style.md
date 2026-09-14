---
title: ps_set_border_style
description: Establecer el estilo del borde de las anotaciones
source_url: https://www.php.net/manual/es/function.ps-set-border-style.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-set-border-style.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66010
---

ps_set_border_style

Establecer el estilo del borde de las anotaciones

## Descripción

```php
ps_set_border_style(resource $psdoc, string $style, float $width): bool
```php

Los vínculos añadidos con una de las funciones `ps_add_weblink`, `ps_add_pdflink`, etc. se mostrarán con un rectángulo circundante cuando el documento postscript es convertido a pdf y visualizado en un visualizador de pdf. Este rectángulo no es visible en el documento postscript. Esta función establece la apariencia y el ancho de la línea del borde.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`style`  
`style` puede ser `solid` o `dashed`.

`width`  
El ancho del borde.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_set_border_color`, `ps_set_border_dash`
