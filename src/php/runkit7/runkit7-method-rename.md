---
title: runkit7_method_rename
description: Cambiar dinámicamente el nombre del método dado
source_url: https://www.php.net/manual/es/function.runkit7-method-rename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-method-rename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 72970
---

runkit7_method_rename

Cambiar dinámicamente el nombre del método dado

## Descripción

```php
runkit7_method_rename(string $class_name, string $source_method_name, string $target_method_name): bool
```php

> [!NOTE]
> Esta función no puede ser utilizada para manipular el método en curso de utilización (o encadenado).

## Parámetros

`class_name`  
La clase en la que renombrar el método

`source_method_name`  
El nombre del método a renombrar

`target_method_name`  
El nuevo nombre a dar al método renombrado

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `runkit7_method_rename`

```
<?php
class Example {
    function foo() {
        return "foo!\n";
    }
}

// Renombrar el método 'foo' a 'bar'
runkit7_method_rename(
    'Example',
    'foo',
    'bar'
);

// Mostrar la función renombrada
echo (new Example)->bar();
?>

   
```php

El ejemplo anterior mostrará:

    foo!

## Véase también

runkit7_method_add

runkit7_method_copy

runkit7_method_redefine

runkit7_method_remove

runkit7_function_rename
