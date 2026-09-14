---
title: UI\Draw\Brush\Gradient::setStop
description: Dejar de manipular
source_url: https://www.php.net/manual/es/ui-draw-brush-gradient.setstop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ui/ui/draw/brush.gradient/setstop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ui
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 97160
---

UI\Draw\Brush\Gradient::setStop

Dejar de manipular

## Descripción

```php
public UI\Draw\Brush\Gradient::setStop(int $index, float $position, UI\Draw\Color $color): bool
```php

```php
public UI\Draw\Brush\Gradient::setStop(int $index, float $position, int $color): bool
```

## Parámetros

`index`  
El índice de la parada que debe definirse

`position`  
Posición de parada

`color`  
El color del tope puede ser un objeto UI\Draw\Color o un entero RRGGBBAA.

## Valores devueltos

Indicación de éxito
