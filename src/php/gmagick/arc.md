---
title: GmagickDraw::arc
description: Dibuja un arco
source_url: https://www.php.net/manual/es/gmagickdraw.arc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagickdraw/arc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 27880
---

GmagickDraw::arc

Dibuja un arco

## Descripción

```php
public GmagickDraw::arc(float $sx, float $sy, float $ex, float $ey, float $sd, float $ed): GmagickDraw
```php

Dibuja un arco que cae dentro de un rectángulo circundante en la imagen.

## Parámetros

`sx`  
coordenada x del inicio del rectángulo circundante

`sy`  
coordenada y del inicio del rectángulo circundante

`ex`  
coordenada x del final del rectángulo circundante

`ey`  
coordenada y del final del rectángulo circundante

`sd`  
grados de inicio de rotación

`ed`  
grados finales de rotación

## Valores devueltos

El objeto `GmagickDraw` si se tuvo éxito.
