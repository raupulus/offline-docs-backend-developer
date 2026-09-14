---
title: ps_show_xy
description: Imprimir texto en una posición dada
source_url: https://www.php.net/manual/es/function.ps-show-xy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-show-xy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66210
---

ps_show_xy

Imprimir texto en una posición dada

## Descripción

```php
ps_show_xy(resource $psdoc, string $text, float $x, float $y): bool
```php

Imprime texto en la posición de texto dada.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`text`  
El texto a imprimir.

`x`  
La coordenada x de la esquina inferior izquierda de la caja circundante del texto.

`y`  
La coordenada y de la esquina inferior izquierda de la caja circundante del texto.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_continue_text`, `ps_show`
