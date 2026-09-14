---
title: ps_symbol_width
description: Obtener el ancho de un glifo
source_url: https://www.php.net/manual/es/function.ps-symbol-width.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-symbol-width.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66290
---

ps_symbol_width

Obtener el ancho de un glifo

## Descripción

```php
ps_symbol_width(resource $psdoc, int $ord, [int $fontid], [float $size]): float
```php

Calcula el ancho de un glifo en puntos si fue impreso con la fuente y el tamaño de fuente dados. Esta función necesita un fichero de métrica de fuentes de Adobe para calcular el ancho preciso.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`ord`  
La posición del glifo en el vector de codificación de fuente.

`fontid`  
El identificador de la fuente a usar. Si no se especifica ninguna fuente se usará la fuente actual.

`size`  
El tamaño de la fuente. Si no se especifica ningún tamaño se usará el tamaño actual.

## Valores devueltos

El ancho de un glifo en puntos.

## Véase también

`ps_symbol`, `ps_symbol_name`
