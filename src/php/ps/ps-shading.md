---
title: ps_shading
description: Crea un tono para uso futuro
source_url: https://www.php.net/manual/es/function.ps-shading.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-shading.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: b95d28e6e
order: 66180
---

ps_shading

Crea un tono para uso futuro

## Descripción

```php
ps_shading(resource $psdoc, string $type, float $x0, float $y0, float $x1, float $y1, float $c1, float $c2, float $c3, float $c4, string $optlist): int
```php

Crea un tono, que puede ser utilizado por `ps_shfill` o `ps_shading_pattern`.

El color del tono puede ser cualquier color de espacio excepto para `pattern`.

## Parámetros

`psdoc`  
Identificador de un fichero postscript devuelto por `ps_new`.

`type`  
El tipo de tono puede ser `radial` o `axial`. Cada tono comienza con el color de relleno actual y termina con el valor de color dado pasado en los argumentos `c1` a `c4` (véase `ps_setcolor` para su significado).

`x0, x1, y0, y1`  
Las coordenadas `x0`, `y0`, `x1`, `y1` son el punto de inicio y fin del tono. Si el tipo de tono es `radial`, los dos puntos son los puntos medios del inicio y fin del círculo.

`c1, c2, c3, c4`  
Véase `ps_setcolor` para su significado.

`optlist`  
Si el tono es de tipo `radial`, el `optlist` debe contener también los argumentos `r0` y `r1` con el radio de inicio y fin del círculo.

## Valores devueltos

Devuelve un identificador del patrón o `false` si ocurre un error.

## Véase también

`ps_shading_pattern`, `ps_shfill`
