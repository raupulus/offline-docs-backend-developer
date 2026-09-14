---
title: UI\Area::onDraw
description: Retrollamada de dibujo
source_url: https://www.php.net/manual/es/ui-area.ondraw.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ui/ui/area/ondraw.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ui
translation_status: ready
translation_reviewed: false
translation_revision: 2735ac5fa
order: 96170
---

UI\Area::onDraw

Retrollamada de dibujo

## Descripción

```php
protected UI\Area::onDraw(UI\Draw\Pen $pen, UI\Size $areaSize, UI\Point $clipPoint, UI\Size $clipSize)
```php

Debe ser invocada cuando esta área necesita ser redibujada

## Parámetros

`pen`  
Un lápiz adecuado para dibujar en esta área

`areaSize`  
El tamaño del área

`clipPoint`  
El punto de recorte del área

`clipSize`  
El tamaño de recorte del área
