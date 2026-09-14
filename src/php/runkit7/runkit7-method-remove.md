---
title: runkit7_method_remove
description: Elimina dinámicamente el método especificado
source_url: https://www.php.net/manual/es/function.runkit7-method-remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-method-remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 72960
---

runkit7_method_remove

Elimina dinámicamente el método especificado

## Descripción

```php
runkit7_method_remove(string $class_name, string $method_name): bool
```php

> [!NOTE]
> Esta función no puede ser utilizada para manipular el método en curso de utilización (o encadenado).

## Parámetros

`class_name`  
La clase de la cual eliminar el método

`method_name`  
El nombre del método a eliminar

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `runkit7_method_remove`

```
<?php
class Example {
    function foo() {
        return "foo!\n";
    }

    function bar() {
        return "bar!\n";
    }
}

// Elimina el método 'foo'
runkit7_method_remove(
    'Example',
    'foo'
);

echo implode(' ', get_class_methods('Example'));

?>

   
```php

El ejemplo anterior mostrará:

    bar

## Véase también

runkit7_method_add

runkit7_method_copy

runkit7_method_redefine

runkit7_method_rename

runkit7_function_remove
