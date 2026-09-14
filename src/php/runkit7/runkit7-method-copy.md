---
title: runkit7_method_copy
description: Copia un método de una clase a otra
source_url: https://www.php.net/manual/es/function.runkit7-method-copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-method-copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 72940
---

runkit7_method_copy

Copia un método de una clase a otra

## Descripción

```php
runkit7_method_copy(string $destination_class, string $destination_method_name, string $source_class, [string $source_method_name]): bool
```php

## Parámetros

`destination_class`  
La clase de destino para el método copiado

`destination_method_name`  
El nombre del método de destino

`source_class`  
La clase fuente del método a copiar

`source_method_name`  
El nombre del método a copiar de la clase fuente. Si este argumento es omitido, se asume el valor de `destination_method_name`.

## Valores devueltos

## Ejemplos

Ejemplo de `runkit7_method_copy`

```
<?php
class Foo {
    function example() {
        return "foo!\n";
    }
}

class Bar {
    // sin métodos inicialmente
}

// copia el example() de la clase Foo a la clase Bar, como baz()
runkit7_method_copy('Bar', 'baz', 'Foo', 'example');

// muestra la función copiada
echo Bar::baz();
?>

   
```php

El ejemplo anterior mostrará:

    foo!

## Véase también

runkit7_method_add

runkit7_method_redefine

runkit7_method_remove

runkit7_method_rename

runkit7_function_copy
