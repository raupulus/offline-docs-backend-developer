---
title: ps_symbol
description: Imprimir un glifo
source_url: https://www.php.net/manual/es/function.ps-symbol.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-symbol.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66300
---

ps_symbol

Imprimir un glifo

## Descripción

```php
ps_symbol(resource $psdoc, int $ord): bool
```php

Imprime el glifo de la posición `ord` del vector de codificación de fuentes de la fuente actual. La codificación de fuente para una fuente se puede establecer cargando la fuente con la función `ps_findfont`.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`ord`  
La posición del glifo en el vector de codificación de fuentes.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_symbol_name`, `ps_symbol_width`
