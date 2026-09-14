---
title: UI\Draw\Stroke::__construct
description: Construye un nuevo trazo
source_url: https://www.php.net/manual/es/ui-draw-stroke.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ui/ui/draw/stroke/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ui
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 97450
---

UI\Draw\Stroke::\_\_construct

Construye un nuevo trazo

## Descripción

```php
public UI\Draw\Stroke::__construct([int $cap], [int $join], [float $thickness], [float $miterLimit])
```php

Construirá un nuevo trazo

## Parámetros

`cap`  
UI\Draw\Line\Cap::Flat, UI\Draw\Line\Cap::Round, o UI\Draw\Line\Cap::Square

`join`  
UI\Draw\Line\Join::Miter, UI\Draw\Line\Join::Round, o UI\Draw\Line\Join::Bevel

`thickness`  
El grosor del trazo

`miterLimit`  
Límite de inglete (el valor por defecto es válido para todas las plataformas)
