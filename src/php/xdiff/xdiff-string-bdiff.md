---
title: xdiff_string_bdiff
description: Hacer una diferencia binaria de dos cadenas
source_url: https://www.php.net/manual/es/function.xdiff-string-bdiff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-string-bdiff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: '475439775'
order: 102190
---

xdiff_string_bdiff

Hacer una diferencia binaria de dos cadenas

## Descripción

```php
xdiff_string_bdiff(string $old_data, string $new_data): string
```php

Hace una diferencia binaria de dos cadenas y devuelve el resultado. Esta función trabaja con texto y datos binarios. El parche resultante puede ser posteriormente aplicado utilizando `xdiff_string_bpatch`/`xdiff_file_bpatch`.

## Parámetros

`old_data`  
Primera cadena con información binaria. Esta actúa como "vieja" información.

`new_data`  
Segunda cadena con información binaria. Esta actúa como "nueva" información.

## Valores devueltos

Devuelve la cadena con la diferencia binaria conteniendo las diferencias entre "vieja" y "nueva" información o `false` si se producido un error interno.

## Véase también

`xdiff_string_bpatch`
