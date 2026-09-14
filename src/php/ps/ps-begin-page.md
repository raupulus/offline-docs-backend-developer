---
title: ps_begin_page
description: Empezar una nueva página
source_url: https://www.php.net/manual/es/function.ps-begin-page.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-begin-page.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65620
---

ps_begin_page

Empezar una nueva página

## Descripción

```php
ps_begin_page(resource $psdoc, float $width, float $height): bool
```php

Empiza una nueva página. Aunque los parámetros `width` y `height` implican un tamaño de página diferente para cada página, esto no es posible en PostScript. La primera llamada a la función `ps_begin_page` establecerá el tamaño de página para el documento entero. Las llamadas consecutivas no tendrán efecto, excepto para crear una nueva página. La situación es diferente si se intenta convertir el documento PostScript a PDF. Esta función coloca marcas pdf dentro del documento, con lo que se puede establecer el tamaño de cada página individualmente. El documento PDF resultante tendrá diferentes tamaños de página.

Aunque PostScript no conoce diferentes tamaños de página, pslib coloca una caja circundante para cada página dentro del documento. Este tamaño es evaluado por algunos visualizadores de PostScript y tendrá precedencia sobre el campo BoundingBox de la cabecera (Header) del documento. Esto puede llevar a resultados inesperados cuando se establece BoundingBox con su esquina inferior izquierda diferente de (0, 0), ya que la caja circundante de la página siempre tendrá una esquina inferior izquierda (0, 0) y sobrescribirá la configuración global.

Cada página está encapsulada en la forma guardar/restaurar. Esto significa que la mayoría de los ajustes hechos en una página no se conservarán para la siguiente página.

Si hasta la primera llamada a la función `ps_begin_page` no existen llamadas a la función `ps_findfont`, la cabecera del documento PostScript se imprimirá y la caja circundante será establecida al tamaño de la primera página. La esquina inferior izquierda de la caja circundante se establecerá a (0, 0). Si si llamó antes a la función `ps_findfont`, la cabecera ya ha sido impresa, y el documento no tendrá una caja circundante válida. Para prevenir esto, se debería llamar a la función `ps_set_info` para establecer el campo de información `BoundingBox` y posiblemente `Orientation` antes de cualquier llamada a las funciones `ps_findfont` o `ps_begin_page`.

> [!NOTE]
> Hasta la versión 0.2.6 de pslib, esta función siempre sobrescribía los campos BoundingBox y Orientation si antes habían sido establecidos con la función `ps_set_info` y no se había llamado antes a la función `ps_findfont`.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`width`  
El ancho de la página en píxeles, p.ej. 596 para el formato A4

`height`  
El alto de la página en píxeles, p.ej. 842 para el formato A4

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_end_page`, `ps_findfont`, `ps_set_info`
