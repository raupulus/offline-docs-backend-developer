---
title: ps_scale
description: Estalecer el factor de escala
source_url: https://www.php.net/manual/es/function.ps-scale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-scale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65980
---

ps_scale

Estalecer el factor de escala

## Descripción

```php
ps_scale(resource $psdoc, float $x, float $y): bool
```php

Establece el factor de escala horizontal y vertical del sistema de coordenadas.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`x`  
El factor de escala en dirección horizontal.

`y`  
El factor de escala en dirección vertical.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_rotate`, `ps_translate`
