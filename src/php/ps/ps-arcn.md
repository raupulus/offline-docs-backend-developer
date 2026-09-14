---
title: ps_arcn
description: Dibujar un arco en el sentido de las agujas del reloj
source_url: https://www.php.net/manual/es/function.ps-arcn.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-arcn.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65610
---

ps_arcn

Dibujar un arco en el sentido de las agujas del reloj

## Descripción

```php
ps_arcn(resource $psdoc, float $x, float $y, float $radius, float $alpha, float $beta): bool
```php

Dibuja una porción de un círculo con su punto medio en (`x`, `y`). El arco comienza en un ángulo dado por `alpha` y termina en un ángulo dado por `beta`. Se dibuja en el sentido de las agujas del reloj (use la función `ps_arc` para dibujarlo en sentido contrario al de las agujas del reloj). El trazado añadido al trazado actual comienza en el arco con el ángulo `beta` y termina en el arco con el ángulo `alpha`.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`x`  
La coordenada x del punto medio del círculo.

`y`  
La coordenada y del punto medio del círculo.

`radius`  
El radio del círculo

`alpha`  
El ángulo de inicio dado en grados.

`beta`  
El ángulo final dado en grados.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_arc`
