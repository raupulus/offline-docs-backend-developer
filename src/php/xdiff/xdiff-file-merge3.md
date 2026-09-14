---
title: xdiff_file_merge3
description: Une 3 archivos en uno
source_url: https://www.php.net/manual/es/function.xdiff-file-merge3.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-file-merge3.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: 14af302c9
order: 102140
---

xdiff_file_merge3

Une 3 archivos en uno

## Descripción

```php
xdiff_file_merge3(string $old_file, string $new_file1, string $new_file2, string $dest): mixed
```php

Une tres archivos en uno y almacena el resultado en un archivo `dest`. El `old_file` es una versión original mientras `new_file1` y `new_file2` son versiones modificadas de un original.

## Parámetros

`old_file`  
Ruta a el primer archivo. Este archivo actúa como "viejo" archivo.

`new_file1`  
Ruta a el segundo archivo. Este actúa como una versión modificada de `old_file`.

`new_file2`  
Ruta a el tercer archivo. Este actúa como una versión modificada de `old_file`.

`dest`  
La ruta del archivo resultante, contiene la unión modificada de `new_file1` y `new_file2`.

## Valores devueltos

Devuelve `true` si la unión fue satisfactoria, una cadena con fragmento erróneo si esta no lo fue o `false` si ocurrió un error interno.

## Ejemplos

Ejemplo de `xdiff_file_merge3`

El código siguiente combina tres archivos en uno.

```
<?php
$old_version = 'original_script.php';
$fix1 = 'script_with_fix1.php';
$fix2 = 'script_with_fix2.php';

$errors = xdiff_file_merge3($old_version, $fix1, $fix2, 'fixed_script.php');
if (is_string($errors)) {
    echo "Rejects:\n";
    echo $errors;
}
?>

    
```php

## Véase también

`xdiff_string_merge3`
