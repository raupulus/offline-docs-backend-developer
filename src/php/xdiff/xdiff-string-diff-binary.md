---
title: xdiff_string_diff_binary
description: Alias de xdiff_string_bdiff
source_url: https://www.php.net/manual/es/function.xdiff-string-diff-binary.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-string-diff-binary.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: bc0556b65
order: 102210
---

xdiff_string_diff_binary

Alias de

xdiff_string_bdiff

## Descripción

```php
xdiff_string_bdiff(string $old_data, string $new_data): string
```php

Hace una diferencia binaria de dos cadenas y devuelve el resultado. Esta función trabaja con texto y datos binarios. El parche resultante puede ser posteriormente aplicado utilizando `xdiff_string_bpatch`/`xdiff_file_bpatch`.

Desde la versión 1.5.0 esta función es un alias de `xdiff_string_bdiff`.

## Parámetros

`old_data`  
Primera cadena con información binaria. Esta actúa como "vieja" información.

`new_data`  
Segunda cadena con información binaria. Esta actúa como "nueva" información.

## Valores devueltos

Devuelve cadena con resultado o `false` si se produce un error interno.

## Véase también

`xdiff_string_bdiff`, `xdiff_string_bpatch`
