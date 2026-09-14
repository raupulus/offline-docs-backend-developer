---
title: xdiff_file_patch
description: Parchea un archivo con un diff unificado
source_url: https://www.php.net/manual/es/function.xdiff-file-patch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-file-patch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: 14af302c9
order: 102160
---

xdiff_file_patch

Parchea un archivo con un diff unificado

## Descripción

```php
xdiff_file_patch(string $file, string $patch, string $dest, [int $flags]): mixed
```php

Parchea un `file` con un `patch` y almacena el resultado en un archivo. `patch` tiene que ser un diff unificado creado por la función `xdiff_file_diff`/`xdiff_string_diff`. Un parámetro opcional `flags` especifica el modo de operación.

## Parámetros

`file`  
El archivo original.

`patch`  
El archivo de revisión unificado. Este tiene que ser creado con las funciones `xdiff_string_diff`, `xdiff_file_diff` o herramientas compatibles.

`dest`  
Ruta de el archivo resultante.

`flags`  
Puede ser `XDIFF_PATCH_NORMAL` (modo por defecto, parche normal) o `XDIFF_PATCH_REVERSE` (parche invertido).

A partir de la versión 1.5.0, también puede utilizar binario OR para habilitar el indicador `XDIFF_PATCH_IGNORESPACE`.

## Valores devueltos

Devuelve `false` si ocurrió un error interno, una cadena con fragmento erróneo si el parche no pudo ser aplicado o `true` si el parche fue aplicado con éxito.

## Ejemplos

Ejemplo de `xdiff_file_patch`

El siguiente código aplica un diff unificado a un archivo.

```
<?php
$old_version = 'my_script-1.0.php';
$patch = 'my_script.patch';

$errors = xdiff_file_patch($old_version, $patch, 'my_script-1.1.php');
if (is_string($errors)) {
   echo "Rejects:\n";
   echo $errors;
}

?>

    
```php

Ejemplo de parche invertido

El código siguiente invierte un parche.

```
<?php
$new_version = 'my_script-1.1.php';
$patch = 'my_script.patch';

$errors = xdiff_file_patch($new_version, $patch, 'my_script-1.0.php', XDIFF_PATCH_REVERSE);
if (is_string($errors)) {
   echo "Fragmentos erróneos:\n";
   echo $errors;
}

?>

    
```php

## Véase también

`xdiff_file_diff`
