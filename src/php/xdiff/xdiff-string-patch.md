---
title: xdiff_string_patch
description: Parchear una cadena con un diff unificado
source_url: https://www.php.net/manual/es/function.xdiff-string-patch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-string-patch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 102250
---

xdiff_string_patch

Parchear una cadena con un diff unificado

## Descripción

```php
xdiff_string_patch(string $str, string $patch, [int $flags], [string $error]): string
```php

Parchea una cadena `str` con un parche unificado en parámetro `patch` y devuelve el resultado. `patch` tiene que ser un diff unificado creado por la función `xdiff_file_diff`/`xdiff_string_diff`. Un parámetro opcional `flags` especifica el modo de operación. Cualquier fragmento erróneo del parche será almacenado en el interior de la variable `error` si si esta es proporcionada.

## Parámetros

`str`  
La cadena original.

`patch`  
La cadena parche unificada. Esta tiene que ser creada utilizando las funciones `xdiff_string_diff`, `xdiff_file_diff` o herramientas compatibles.

`flags`  
`flags` uede ser `XDIFF_PATCH_NORMAL` (modo por defecto, parche normal) o `XDIFF_PATCH_REVERSE` (parche invertido).

A partir de la versión 1.5.0, también se puede utilizar binario OR para habilitar el indicador `XDIFF_PATCH_IGNORESPACE`.

`error`  
Si se proporciona entonces los fragmentos erróneos se almacenan dentro de esta variable.

## Valores devueltos

Devuelve la cadena parcheada, o `false` en caso de error.

## Ejemplos

Ejemplo de `xdiff_string_patch`

El siguiente código aplica cambios en algún artículo.

```
<?php
$old_article = file_get_contents('./old_article.txt');
$diff = $_SERVER['patch']; /* Supongamos que alguien pega un parche para un formulario html */

$errors = '';

$new_article = xdiff_string_patch($old_article, $diff, XDIFF_PATCH_NORMAL, $errors);
if (is_string($new_article)) {
    echo "Nuevo artículo:\n";
    echo $new_article;
}

if (strlen($errors)) {
    echo "Fragmentos erróneos: \n";
    echo $errors;
}

?>

    
```php

## Véase también

`xdiff_string_diff`
