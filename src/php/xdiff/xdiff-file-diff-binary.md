---
title: xdiff_file_diff_binary
description: Alias de xdiff_file_bdiff
source_url: https://www.php.net/manual/es/function.xdiff-file-diff-binary.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-file-diff-binary.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: bc0556b65
order: 102120
---

xdiff_file_diff_binary

Alias de

xdiff_file_bdiff

## Descripción

```php
xdiff_file_diff_binary(string $old_file, string $new_file, string $dest): bool
```php

Hace una diferencia binaria de dos archivos y almacena el resultado en un archivo de revisión. Esta función trabaja con archivos de texto y binarios. El archivo parche resultante puede ser posteriormente aplicado con `xdiff_file_bpatch`.

Desde la versión 1.5.0 de esta función es un alias de `xdiff_file_bdiff`.

## Parámetros

`old_file`  
Ruta a el primer archivo. Este archivo actúa como "viejo" archivo.

`new_file`  
Ruta a el segundo archivo. Este archivo actúa como "nuevo" archivo.

`dest`  
Ruta de el archivo parche resultante. El archivo resultante contiene diferencias entre los archivos "viejo" y "nuevo". Este será en formato binario y no legible por humanos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `xdiff_file_diff_binary`

El siguiente código hace una diferencia binaria de dos archivos.

```
<?php
$old_version = 'my_script_1.0.tgz';
$new_version = 'my_script_1.1.tgz';

xdiff_file_diff_binary($old_version, $new_version, 'my_script.bdiff');
?>

    
```php

## Notas

> [!NOTE]
> Ambos archivos serán cargados en memoria así que asegúrese que el valor de memory_limit es lo suficientemente alto.

## Véase también

`xdiff_file_bdiff`, `xdiff_file_bpatch`
