---
title: UI\Size::of
description: Punto de coerción
source_url: https://www.php.net/manual/es/ui-size.of.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ui/ui/size/of.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ui
translation_status: ready
translation_reviewed: false
translation_revision: 99aaaf7ec
order: 97940
---

UI\Size::of

Punto de coerción

## Descripción

```php
public static UI\Size::of(float $size): UI\Size
```php

```php
public static UI\Size::of(UI\Point $point): UI\Size
```

Devolverá un objeto de tamaño UI en el que el ancho y la altura son iguales a los suministrados, ya sea en forma flotante o en forma de UI.

## Parámetros

`size`  
El valor de la anchura y la altura

`point`  
El punto a convertir

## Valores devueltos

El tamaño resultante
