---
title: ps_circle
description: Dibujar un círculo
source_url: https://www.php.net/manual/es/function.ps-circle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-circle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65650
---

ps_circle

Dibujar un círculo

## Descripción

```php
ps_circle(resource $psdoc, float $x, float $y, float $radius): bool
```php

Dibuja un círculo con su punto medio en (`x`, `y`). El círculo comienza y termina en la posición (`x`+`radius`, `y`). Si esta función es llamada fuera de un trazado se iniciará un nuevo trazado. Si es llamada dentro de un trazado añadirá el círculo como un subtrazado. Si la última operación de dibujo no finaliza en el punto (`x`+`radius`, `y`) habrá un hueco en el trazado.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`x`  
La coordenada x del punto medio del círculo.

`y`  
La coordenada y del punto medio del círculo.

`radius`  
El radio del círculo

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_arc`, `ps_arcn`
