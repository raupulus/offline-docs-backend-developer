---
title: runkit7_function_add
description: Añade una nueva función, similar a create_function
source_url: https://www.php.net/manual/es/function.runkit7-function-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-function-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 72870
---

runkit7_function_add

Añade una nueva función, similar a

create_function

## Descripción

```php
runkit7_function_add(string $function_name, string $argument_list, string $code, [bool $return_by_reference], [string $doc_comment], [string $return_type], [bool $is_strict]): bool
```php

```php
runkit7_function_add(string $function_name, Closure $closure, [string $doc_comment], [string $return_type], [bool $is_strict]): bool
```

## Parámetros

`function_name`  
El nombre de la función a crear

`argument_list`  
La lista de argumentos separados por comas

`code`  
El código que compone la función

`closure`  
Una `closure` que define la función

`return_by_reference`  
Si la función debe devolver por referencia

`doc_comment`  
El comentario de documentación de la función

`return_type`  
El tipo de retorno de la función

`is_strict`  
Si la función debe comportarse como si fuera declarada en un archivo con `strict_types=1`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Un ejemplo de `runkit7_function_add`

```php
<?php
runkit7_function_add('testme','$a,$b','echo "The value of a is $a\n"; echo "The value of b is $b\n";');
testme(1,2);
?>

   
```

El ejemplo anterior mostrará:

    The value of a is 1
    The value of b is 2

## Véase también

create_function

runkit7_function_redefine

runkit7_function_copy

runkit7_function_rename

runkit7_function_remove

runkit7_method_add
