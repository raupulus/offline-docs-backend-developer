---
title: xdiff_string_patch_binary
description: Alias de xdiff_string_bpatch
source_url: https://www.php.net/manual/es/function.xdiff-string-patch-binary.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-string-patch-binary.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: bc0556b65
order: 102240
---

xdiff_string_patch_binary

Alias de

xdiff_string_bpatch

## Descripción

```php
xdiff_string_patch_binary(string $str, string $patch): string
```php

Parchea una cadena `str` con un `patch` binario. Esta función acepta parches creados tanto a través de las funciones `xdiff_string_bdiff` y `xdiff_string_rabdiff` o de su archivo homólogo equivalente.

Desde la versión 1.5.0 esta función es un alias de `xdiff_string_bpatch`.

## Parámetros

`str`  
La cadena binaria original.

`patch`  
La cadena parche binaria.

## Valores devueltos

Devuelve la cadena parcheada, o `false` en caso de error.

## Véase también

`xdiff_string_bpatch`, `xdiff_string_bdiff`, `xdiff_string_rabdiff`
