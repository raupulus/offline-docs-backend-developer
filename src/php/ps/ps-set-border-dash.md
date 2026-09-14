---
title: ps_set_border_dash
description: Establece la longitud de las rayas del borde de las anotaciones
source_url: https://www.php.net/manual/es/function.ps-set-border-dash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-set-border-dash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66000
---

ps_set_border_dash

Establece la longitud de las rayas del borde de las anotaciones

## Descripción

```php
ps_set_border_dash(resource $psdoc, float $black, float $white): bool
```php

Los vínculos añadidos con una de las funciones `ps_add_weblink`, `ps_add_pdflink`, etc. se mostrarán con un rectángulo circundante cuando el documento postscript es convertido a pdf y visualizado en un visualizador de pdf. Este rectángulo no es visible en el documento postscript. Esta función establece la longitud de las porciones negras y blancas de una línea de borde discontinua.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`black`  
La longitud de la raya.

`white`  
La longitud del hueco entre rayas.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_set_border_color`, `ps_set_border_style`
