---
title: xdiff_string_bpatch
description: Parchear una cadena con una diferencia binaria
source_url: https://www.php.net/manual/es/function.xdiff-string-bpatch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-string-bpatch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 102200
---

xdiff_string_bpatch

Parchear una cadena con una diferencia binaria

## Descripción

```php
xdiff_string_bpatch(string $str, string $patch): string
```php

Parchea una cadena `str` con un `patch` binario. Esta función acepta parches creados tanto a través de las funciones `xdiff_string_bdiff` y `xdiff_string_rabdiff` o su archivo homólogo equivalente.

## Parámetros

`str`  
La cadena binaria original.

`patch`  
La cadena parche binaria.

## Valores devueltos

Devuelve la cadena parcheada, o `false` en caso de error.

## Véase también

`xdiff_string_bdiff`, `xdiff_string_rabdiff`
