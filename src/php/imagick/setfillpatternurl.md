---
title: ImagickDraw::setFillPatternURL
description: Configura la URL del patrón de relleno de superficies
source_url: https://www.php.net/manual/es/imagickdraw.setfillpatternurl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setfillpatternurl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 37040
---

ImagickDraw::setFillPatternURL

Configura la URL del patrón de relleno de superficies

## Descripción

```php
public ImagickDraw::setFillPatternURL(string $fill_url): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Configura la URL del patrón de relleno de superficies. Actualmente, solo se soportan las URL locales (`"#identifier"`). Estas URL se crean normalmente al definir un nombre de patrón de relleno con DrawPushPattern/DrawPopPattern.

## Parámetros

`fill_url`  
La URL a utilizar para acceder al patrón.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
