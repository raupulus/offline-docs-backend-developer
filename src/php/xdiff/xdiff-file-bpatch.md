---
title: xdiff_file_bpatch
description: Parchea un archivo con una diferencia binaria
source_url: https://www.php.net/manual/es/function.xdiff-file-bpatch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-file-bpatch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: 14af302c9
order: 102110
---

xdiff_file_bpatch

Parchea un archivo con una diferencia binaria

## Descripción

```php
xdiff_file_bpatch(string $file, string $patch, string $dest): bool
```php

Parchea un `file` con un `patch` binario y almacena el resultado en un archivo `dest`. Esta función acepta parches creados tanto a través de la funciones `xdiff_file_bdiff` y `xdiff_file_rabdiff` como de sus equivalentes de cadena.

## Parámetros

`file`  
El archivo original.

`patch`  
El archivo parche binario.

`dest`  
La ruta del archivo resultante.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `xdiff_file_bpatch`

El siguiente código aplica una diferencia binaria a un archivo.

```
<?php
$old_version = 'archive-1.0.tgz';
$patch = 'archive.bpatch';

$result = xdiff_file_bpatch($old_version, $patch, 'archive-1.1.tgz');
if ($result) {
   echo "Archivo parcheado";
} else {
   echo "El archivo no pudo ser parcheado";
}

?>

    
```php

## Notas

> [!NOTE]
> Ambos archivos (`file` y `patch`) serán cargados en memoria así que asegúrese que el valor de memory_limit es lo suficientemente alto.

## Véase también

`xdiff_file_bdiff`, `xdiff_file_rabdiff`
