---
title: ps_symbol_name
description: Obtener el nombre de un glifo
source_url: https://www.php.net/manual/es/function.ps-symbol-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-symbol-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66280
---

ps_symbol_name

Obtener el nombre de un glifo

## Descripción

```php
ps_symbol_name(resource $psdoc, int $ord, [int $fontid]): string
```php

Esta función necesita un fichero de métrica de fuentes de Adobe para conocer los glifos que están disponibles.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`ord`  
El parámetro `ord` es la posición del glifo en el vector de codificación de fuente.

`fontid`  
El identificador de la fuente a usar. Si no se especifica ninguna fuente se usará la fuente actual.

## Valores devueltos

El nombre de un glifo de la fuente dada.

## Véase también

`ps_symbol`, `ps_symbol_width`
