---
title: xdiff_file_diff
description: Hacer un diff unificado de dos archivos
source_url: https://www.php.net/manual/es/function.xdiff-file-diff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-file-diff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_revision: b8758b060
order: 102130
---

xdiff_file_diff

Hacer un diff unificado de dos archivos

## Descripción

```php
xdiff_file_diff(string $old_file, string $new_file, string $dest, [int $context], [bool $minimal]): bool
```php

Hace un diff unificado que contiene las diferencias entre `old_file` y `new_file` y almacena este en el archivo `dest`. El archivo resultante es legible. Un parámetro opcional `context` especifica el número de líneas de contexto que hay que añadir alrededor de cada cambio. Establecer el parámetro `minimal` a true dará como resultado de salida el archivo parche más corto posible (puede tomar algo de tiempo).

## Parámetros

`old_file`  
Ruta a el primer archivo. Este archivo actúa como "viejo" archivo.

`new_file`  
Ruta a el segundo archivo. Este archivo actúa como "nuevo" archivo.

`dest`  
Ruta del archivo parche resultante.

`context`  
Indica el número de líneas de contexto que desea incluir en el resultado diff.

`minimal`  
Establezca este parámetro a `true` si desea reducir el tamaño del resultado (puede tomar algo de tiempo).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `xdiff_file_diff`

El siguiente código hace un diff unificado de dos archivos php con una longitud de contexto de 2.

```
<?php
$old_version = 'my_script.php';
$new_version = 'my_new_script.php';

xdiff_file_diff($old_version, $new_version, 'my_script.diff', 2);
?>

    
```php

## Notas

> [!NOTE]
> Esta función no funciona bien con archivos binarios. Para hacer una diferencia binaria de archivos utilice la `xdiff_file_bdiff`/`xdiff_file_rabdiff`.

## Véase también

`xdiff_file_patch`
