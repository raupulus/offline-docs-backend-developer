---
title: ps_setdash
description: Establecer la apariencia de una línea discontinua
source_url: https://www.php.net/manual/es/function.ps-setdash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-setdash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66070
---

ps_setdash

Establecer la apariencia de una línea discontinua

## Descripción

```php
ps_setdash(resource $psdoc, float $on, float $off): bool
```php

Establece la longitud de las porciones negras y blancas de una línea discontinua.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`on`  
La longitud de la raya.

`off`  
La longitud del hueco entre rayas.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_setpolydash`
