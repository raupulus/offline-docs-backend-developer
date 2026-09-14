---
title: ps_setflat
description: Establecer la planicidad
source_url: https://www.php.net/manual/es/function.ps-setflat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-setflat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 9c3786643
order: 66080
---

ps_setflat

Establecer la planicidad

## Descripción

```php
ps_setflat(resource $psdoc, float $value): bool
```php

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`value`  
El valor dado a `value` debe estar entre 0.2 y 1.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
