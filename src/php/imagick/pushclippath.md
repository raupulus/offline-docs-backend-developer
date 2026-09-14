---
title: ImagickDraw::pushClipPath
description: Inicia la definición de un trazado de recorte
source_url: https://www.php.net/manual/es/imagickdraw.pushclippath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/pushclippath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 668b6fc28
order: 36890
---

ImagickDraw::pushClipPath

Inicia la definición de un trazado de recorte

## Descripción

```php
public ImagickDraw::pushClipPath(string $clip_mask_id): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Inicia la definición de un trazado de recorte el cuál está compuesto por cualquier número de comandos de dibujo y finalizado por un comando ImagickDraw::popClipPath.

## Parámetros

`clip_mask_id`  
Id de la máscara de recorte

## Valores devueltos

No se retorna ningún valor.
