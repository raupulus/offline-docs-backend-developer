---
title: UI\Draw\Pen::stroke
description: Traza una ruta
source_url: https://www.php.net/manual/es/ui-draw-pen.stroke.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ui/ui/draw/pen/stroke.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ui
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 97420
---

UI\Draw\Pen::stroke

Traza una ruta

## Descripción

```php
public UI\Draw\Pen::stroke(UI\Draw\Path $path, UI\Draw\Brush $with, UI\Draw\Stroke $stroke)
```php

```php
public UI\Draw\Pen::stroke(UI\Draw\Path $path, UI\Draw\Color $with, UI\Draw\Stroke $stroke)
```

```php
public UI\Draw\Pen::stroke(UI\Draw\Path $path, int $with, UI\Draw\Stroke $stroke)
```php

Trazará la ruta dada

## Parámetros

`path`  
La ruta del trazo

`with`  
El color o el pincel con el que trazar

`stroke`  
La configuración del trazo
