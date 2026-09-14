---
title: ps_string_geometry
description: Establecer la geometría de una cadena de caracteres
source_url: https://www.php.net/manual/es/function.ps-string-geometry.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-string-geometry.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66250
---

ps_string_geometry

Establecer la geometría de una cadena de caracteres

## Descripción

```php
ps_string_geometry(resource $psdoc, string $text, [int $fontid], [float $size]): array
```php

Esta función es similar a la función `ps_stringwidth`, excepto que devuelve un array de dimensiones que contiene el ancho, el ascendente y el descendente del texto.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`text`  
El texto por el cual se calcula la geometría.

`fontid`  
El identificador de la fuente a usar. Si no se especifica una fuente se usará la fuente actual.

`size`  
El tamaño de la fuente. Si no se especifica un tamaño se usará el tamaño actual.

## Valores devueltos

Un array con las dimensiones de una cadena. El elemento 'width' contiene el ancho de la cadena devuelto por la función `ps_stringwidth`. El elemento 'descender' contiene el descendente máximo y 'ascender' el ascendente máximo de la cadena.

## Véase también

`ps_continue_text`, `ps_stringwidth`
