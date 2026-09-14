---
title: xdiff_file_patch_binary
description: Alias de xdiff_file_bpatch
source_url: https://www.php.net/manual/es/function.xdiff-file-patch-binary.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-file-patch-binary.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: bc0556b65
order: 102150
---

xdiff_file_patch_binary

Alias de

xdiff_file_bpatch

## Descripción

```php
xdiff_file_patch_binary(string $file, string $patch, string $dest): bool
```php

Parchea un `file` con un `patch` binario y almacena el resultado en un archivo `dest`. Esta función acepta parches creados tanto a través de funciones `xdiff_file_bdiff` o `xdiff_file_rabdiff` como de sus equivalentes de cadena.

Desde la versión 1.5.0 esta función es un alias de `xdiff_file_bpatch`.

## Parámetros

`file`  
El archivo original.

`patch`  
El archivo parche binario.

`dest`  
La ruta de el archivo resultante.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `xdiff_file_patch_binary`

El siguiente código aplica una diferencia binaria a un archivo.

```
<?php
$old_version = 'archive-1.0.tgz';
$patch = 'archive.bpatch';

$result = xdiff_file_patch_binary($old_version, $patch, 'archive-1.1.tgz');
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

`xdiff_string_patch_binary`
