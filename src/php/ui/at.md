---
title: UI\Point::at
description: Tamaño de coerción
source_url: https://www.php.net/manual/es/ui-point.at.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ui/ui/point/at.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ui
translation_status: ready
translation_reviewed: false
translation_revision: 99aaaf7ec
order: 97850
---

UI\Point::at

Tamaño de coerción

## Descripción

```php
public static UI\Point::at(float $point): UI\Point
```php

```php
public static UI\Point::at(UI\Size $size): UI\Point
```

Devolverá un objeto de punto UI donde x y y son iguales a los suministrados, ya sea en forma flotante o de tamaño UI.

## Parámetros

`point`  
El valor de x y y

`size`  
El tamaño a convertir

## Valores devueltos

El punto resultante
