---
title: forward_static_call
description: Llamar a un método estático
source_url: https://www.php.net/manual/es/function.forward-static-call.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/funchand/functions/forward-static-call.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: funchand
translation_status: ready
translation_revision: 0c9c2dd66
order: 24760
---

forward_static_call

Llamar a un método estático

## Descripción

```php
forward_static_call(callable $callback, mixed ...$args): mixed
```php

Llama a una función o método definido por el usuario, dado por el parámetro `function`, con los siguientes argumentos. Esta función debe ser llamada dentro del contexto de un método, no se puede usar fuera de una clase. Usa el [Enlace estático en tiempo de ejecución](#language.oop5.late-static-bindings).

## Parámetros

`callback`  
La función o método a ser llamado. Este parámetro puede ser una matriz, con el nombre de la clase y del método, o una cadena, con el nombre una función.

`args`  
Cero o más parámetros a ser pasados a la función.

## Valores devueltos

Devuelve el resultado de la función, o `false` en caso de error.

## Ejemplos

Ejemplo de `forward_static_call`

```
<?php

class A
{
    const NOMBRE = 'A';
    public static function prueba() {
        $args = func_get_args();
        echo static::NOMBRE, " ".join(',', $args)." \n";
    }
}

class B extends A
{
    const NOMBRE = 'B';

    public static function prueba() {
        echo self::NOMBRE, "\n";
        forward_static_call(array('A', 'prueba'), 'más', 'args');
        forward_static_call( 'prueba', 'otro', 'args');
    }
}

B::prueba('foo');

function prueba() {
        $args = func_get_args();
        echo "C ".join(',', $args)." \n";
    }

?>

    
```php

El ejemplo anterior mostrará:

    B
    B más,args
    C otro,args

## Véase también

`forward_static_call_array`, `call_user_func_array`, `call_user_func`, `is_callable`
