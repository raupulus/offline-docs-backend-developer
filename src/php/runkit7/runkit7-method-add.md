---
title: runkit7_method_add
description: Añade dinámicamente un nuevo método a una clase dada
source_url: https://www.php.net/manual/es/function.runkit7-method-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-method-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 72930
---

runkit7_method_add

Añade dinámicamente un nuevo método a una clase dada

## Descripción

```php
runkit7_method_add(string $class_name, string $method_name, string $argument_list, string $code, [int $flags], [string $doc_comment], [string $return_type], [bool $is_strict]): bool
```php

```php
runkit7_method_add(string $class_name, string $method_name, Closure $closure, [int $flags], [string $doc_comment], [string $return_type], [bool $is_strict]): bool
```

## Parámetros

`class_name`  
La clase a la cual se añadirá este método

`method_name`  
El nombre del método a añadir

`argument_list`  
La lista de argumentos separados por comas para el nuevo método

`code`  
El código a evaluar cuando `method_name` es llamado

`closure`  
Una `closure` que define el método.

`flags`  
El tipo de método a crear, puede ser `RUNKIT7_ACC_PUBLIC`, `RUNKIT7_ACC_PROTECTED` o `RUNKIT7_ACC_PRIVATE` opcionalmente combinado mediante una operación bit a bit OU con `RUNKIT7_ACC_STATIC`

`doc_comment`  
El comentario de documentación del método.

`return_type`  
El tipo de retorno del método.

`is_strict`  
Si el método se comporta como si fuera declarado en un fichero con `strict_types=1`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `runkit7_method_add`

```php
<?php
class Example {
    function foo() {
        echo "foo!\n";
    }
}

// Crear un objeto Example
$e = new Example();

// Añadir un nuevo método público
runkit7_method_add(
    'Example',
    'add',
    '$num1, $num2',
    'return $num1 + $num2;',
    RUNKIT7_ACC_PUBLIC
);

// Sumar 12 + 4
echo $e->add(12, 4);
?>

   
```

El ejemplo anterior mostrará:

    16

## Véase también

runkit7_method_copy

runkit7_method_redefine

runkit7_method_remove

runkit7_method_rename

runkit7_function_add
