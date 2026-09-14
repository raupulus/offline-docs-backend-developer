---
title: ImagickDraw::pop
description: Destruye el objeto ImagickDraw actual de la pila, y lo devuelve al objeto
  ImagickDraw previamente metido
source_url: https://www.php.net/manual/es/imagickdraw.pop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/pop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0f49e97ee
order: 36840
---

ImagickDraw::pop

Destruye el objeto ImagickDraw actual de la pila, y lo devuelve al objeto ImagickDraw previamente metido

## Descripción

```php
public ImagickDraw::pop(): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Destruye el objeto ImagickDraw actual de la pila, y lo devuelve al objeto ImagickDraw previamente metido. Pueden existir mútiples objetos ImagickDraw. Es un error intentar sacar más objetos ImagickDraw de los que se han metido, y es una forma apropiada sacar todos los objetos ImagickDraw que han sido metidos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
