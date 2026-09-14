---
title: ps_shading_pattern
description: Crea un patrón basado en el tono
source_url: https://www.php.net/manual/es/function.ps-shading-pattern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-shading-pattern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: b95d28e6e
order: 66170
---

ps_shading_pattern

Crea un patrón basado en el tono

## Descripción

```php
ps_shading_pattern(resource $psdoc, int $shadingid, string $optlist): int
```php

Crea un patrón basado en el tono, que debe haber sido creado previamente con `ps_shading`. Los patrones de tono pueden ser utilizados como patrones regulares.

## Parámetros

`psdoc`  
Identificador de un fichero postscript devuelto por `ps_new`.

`shadingid`  
El identificador de tono creado previamente con `ps_shading`.

`optlist`  
Este argumento no se utiliza actualmente.

## Valores devueltos

El identificador del patrón o `false` si ocurre un error.

## Véase también

`ps_shading`, `ps_shfill`
