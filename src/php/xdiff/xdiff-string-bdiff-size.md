---
title: xdiff_string_bdiff_size
description: Lee el tamaño de un archivo creado tras aplicar una diferencia binaria
source_url: https://www.php.net/manual/es/function.xdiff-string-bdiff-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-string-bdiff-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: 14af302c9
order: 102180
---

xdiff_string_bdiff_size

Lee el tamaño de un archivo creado tras aplicar una diferencia binaria

## Descripción

```php
xdiff_string_bdiff_size(string $patch): int
```php

Devuelve el tamaño de un archivo resultante que será creado tras aplicar el `patch` binario a el archivo original.

## Parámetros

`patch`  
El parche binario creado por la función `xdiff_string_bdiff` o `xdiff_string_rabdiff`.

## Valores devueltos

Devuelve el tamaño del archivo que fue creado.

## Ejemplos

Ejemplo de `xdiff_string_bdiff_size`

El siguiente código lee el tamaño de un archivo que fue creado tras aplicar una diferencia binaria.

```
<?php
$binary_patch = file_get_contents('file.bdiff');
$length = xdiff_string_bdiff_size($binary_patch);
echo "El archivo resultante tendrá $length bytes de longitud";
?>

    
```php

## Véase también

`xdiff_string_bdiff`, `xdiff_string_rabdiff`, `xdiff_string_bpatch`
