---
title: ps_stringwidth
description: Obtener el ancho de una cadena
source_url: https://www.php.net/manual/es/function.ps-stringwidth.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-stringwidth.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66260
---

ps_stringwidth

Obtener el ancho de una cadena

## Descripción

```php
ps_stringwidth(resource $psdoc, string $text, [int $fontid], [float $size]): float
```php

Calcula el ancho de una cadena en puntos si fue impresa con la fuente y tamaño de fuente dados. Esta función necesita un fichero de métrica de fuente de Adobe para calcular el ancho preciso. Si la partición silábica está activada se tomará en cuenta.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`text`  
El texto por el que calcular el ancho.

`fontid`  
El identificador de la fuente a usar. Si no se especifica ninguna fuente se usará la fuente actual.

`size`  
El tamaño de la fuente. Si no se especifica ningún tamaño se usará el tamaño actual.

## Valores devueltos

El ancho de una cadena en puntos.

## Véase también

`ps_string_geometry`
