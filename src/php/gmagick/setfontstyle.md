---
title: GmagickDraw::setfontstyle
description: Establece el estilo de fuente a usar cuando se anota texto
source_url: https://www.php.net/manual/es/gmagickdraw.setfontstyle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagickdraw/setfontstyle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 28140
---

GmagickDraw::setfontstyle

Establece el estilo de fuente a usar cuando se anota texto

## Descripción

```php
public GmagickDraw::setfontstyle(int $style): GmagickDraw
```php

Establece el estilo de fuente a usar cuando se anota texto. La enumeración AnyStyle actúa como una opción comodín para "no tener cuidado".

## Parámetros

`style`  
El estilo de la fuente (NormalStyle, ItalicStyle, ObliqueStyle, AnyStyle)

## Valores devueltos

El objeto `GmagickDraw` si se tuvo éxito
