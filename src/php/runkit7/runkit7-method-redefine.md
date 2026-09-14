---
title: runkit7_method_redefine
description: Cambiar dinámicamente el código del método dado
source_url: https://www.php.net/manual/es/function.runkit7-method-redefine.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-method-redefine.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 72950
---

runkit7_method_redefine

Cambiar dinámicamente el código del método dado

## Descripción

```php
runkit7_method_redefine(string $class_name, string $method_name, string $argument_list, string $code, [int $flags], [string $doc_comment], [string $return_type], [bool $is_strict]): bool
```php

```php
runkit7_method_redefine(string $class_name, string $method_name, Closure $closure, [int $flags], [string $doc_comment], [string $return_type], [bool $is_strict]): bool
```

## Parámetros

`class_name`  
La clase en la que redefinir el método

`method_name`  
El nombre del método a redefinir

`argument_list`  
La lista de argumentos separados por comas para el método redefinido

`code`  
El nuevo código a evaluar cuando `method_name` es llamado

`closure`  
Una `closure` que define el método.

`flags`  
El método redefinido puede ser `RUNKIT7_ACC_PUBLIC`, `RUNKIT7_ACC_PROTECTED` o `RUNKIT7_ACC_PRIVATE` opcionalmente combinado mediante una operación bit a bit OU con `RUNKIT7_ACC_STATIC`

`doc_comment`  
El comentario de documentación del método.

`return_type`  
El tipo de retorno del método.

`is_strict`  
Si el método se comporta como si fuera declarado en un archivo con `strict_types=1`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `runkit7_method_redefine`

```php
<?php
class Example {
    function foo() {
        return "foo!\n";
    }
}

// crear un objeto Example
$e = new Example();

// muestra Example::foo() (antes de la redefinición)
echo "Before: " . $e->foo();

// Redefine el método 'foo'
runkit7_method_redefine(
    'Example',
    'foo',
    '',
    'return "bar!\n";',
    RUNKIT7_ACC_PUBLIC
);

// muestra Example::foo() (después de la redefinición)
echo "After: " . $e->foo();
?>

   
```

El ejemplo anterior mostrará:

    Before: foo!
    After: bar!

## Véase también

runkit7_method_add

runkit7_method_copy

runkit7_method_remove

runkit7_method_rename

runkit7_function_redefine
