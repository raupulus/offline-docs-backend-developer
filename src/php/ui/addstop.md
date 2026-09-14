---
title: UI\Draw\Brush\Gradient::addStop
description: Dejar de manipular
source_url: https://www.php.net/manual/es/ui-draw-brush-gradient.addstop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ui/ui/draw/brush.gradient/addstop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ui
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 97140
---

UI\Draw\Brush\Gradient::addStop

Dejar de manipular

## Descripción

```php
public UI\Draw\Brush\Gradient::addStop(float $position, UI\Draw\Color $color): int
```php

```php
public UI\Draw\Brush\Gradient::addStop(float $position, int $color): int
```

Añade un tope en la posición dada con el color dado

## Parámetros

`position`  
La posición para la nueva parada

`color`  
El color para la nueva parada puede ser un objeto UI\Draw\Color o un entero RRGGBBAA.

## Valores devueltos

Número total de paradas
