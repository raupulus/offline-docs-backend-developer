---
title: xdiff_file_bdiff_size
description: Lee el tamaño de un archivo creado tras aplicar una diferencia binaria
source_url: https://www.php.net/manual/es/function.xdiff-file-bdiff-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-file-bdiff-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: 14af302c9
order: 102090
---

xdiff_file_bdiff_size

Lee el tamaño de un archivo creado tras aplicar una diferencia binaria

## Descripción

```php
xdiff_file_bdiff_size(string $file): int
```php

Devuelve el tamaño de un archivo resultado que se creó después de aplicar el parche binario desde el archivo `file` a el archivo original.

## Parámetros

`file`  
La ruta al parche binario creado por la función `xdiff_string_bdiff` o `xdiff_string_rabdiff`.

## Valores devueltos

Devuelve el tamaño del archivo que se creará.

## Ejemplos

Ejemplo de `xdiff_file_bdiff_size`

El siguiente código lee el tamaño de un archivo que se creará tras realizar una diferencia binaria.

```
<?php
$length = xdiff_string_bdiff_size('file.bdiff');
echo "El archivo resultante tendrá $length bytes de longitud";
?>

    
```php

## Véase también

`xdiff_file_bdiff`, `xdiff_file_rabdiff`, `xdiff_file_bpatch`
