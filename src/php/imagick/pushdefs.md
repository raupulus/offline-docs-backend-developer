---
title: ImagickDraw::pushDefs
description: Indica que los siguientes comandos crean elementos con nombre para un
  procesamiento previo
source_url: https://www.php.net/manual/es/imagickdraw.pushdefs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/pushdefs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 668b6fc28
order: 36900
---

ImagickDraw::pushDefs

Indica que los siguientes comandos crean elementos con nombre para un procesamiento previo

## Descripción

```php
public ImagickDraw::pushDefs(): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Indica que los comandos hasta un comando ImagickDraw::popDefs finalizador crean elementos nominados (p.ej. trazados de recorte, texturas, etc.) los cuales pueden ser procesados previamente de forma segura para la eficiencia.

## Valores devueltos

No se retorna ningún valor.
