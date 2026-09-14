---
title: runkit7_function_copy
description: Copia una función hacia un nuevo nombre de función
source_url: https://www.php.net/manual/es/function.runkit7-function-copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-function-copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 72880
---

runkit7_function_copy

Copia una función hacia un nuevo nombre de función

## Descripción

```php
runkit7_function_copy(string $source_name, string $target_name): bool
```php

## Parámetros

`source_name`  
El nombre de la función existente

`target_name`  
El nombre de la nueva función hacia la cual copiar la definición

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Un ejemplo de `runkit7_function_copy`

```
<?php
function original() {
  echo "In a function\n";
}
runkit7_function_copy('original','duplicate');
original();
duplicate();
?>

   
```php

El ejemplo anterior mostrará:

    In a function
    In a function

## Véase también

runkit7_function_add

runkit7_function_redefine

runkit7_function_rename

runkit7_function_remove
