---
title: ps_shfill
description: Rellenar un área con un sombreado
source_url: https://www.php.net/manual/es/function.ps-shfill.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-shfill.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66190
---

ps_shfill

Rellenar un área con un sombreado

## Descripción

```php
ps_shfill(resource $psdoc, int $shadingid): bool
```php

Rellena un área con un sombreado, que ha de ser creado antes con la función `ps_shading`. Esta es una manera alternativa de crear un patrón desde un sombreado con la función `ps_shading_pattern` y usar el patrón como color de relleno.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`shadingid`  
El identificador de un sombreado previamente creado con la función `ps_shading`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_shading`, `ps_shading_pattern`
