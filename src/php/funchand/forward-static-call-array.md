---
title: forward_static_call_array
description: Llamar a un método estático y pasar los argumentos como matriz
source_url: https://www.php.net/manual/es/function.forward-static-call-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/funchand/functions/forward-static-call-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: funchand
translation_status: ready
translation_revision: c6fb604f3
order: 24750
---

forward_static_call_array

Llamar a un método estático y pasar los argumentos como matriz

## Descripción

```php
forward_static_call_array(callable $function, array $parameters): mixed
```php

Llama a una función o método definido por el usuario, dado por el parámetro `function`. Esta función debe ser llamada dentro del contexto de un método, no se puede usar fuera de una clase. Usa el [Enlace estático en tiempo de ejecución](#language.oop5.late-static-bindings). Todos los argumentos del método a llamar se pasan como valores, y como matriz, similar a `call_user_func_array`.

## Parámetros

`function`  
La función o método a ser llamado. Este parámetro puede ser un `array`, con el nombre de la clase y del método, o un `string`, con el nombre de una función.

`args`  
Un parámetro, reuniendo todos los parámetros del método en una matriz.

> [!NOTE]
> Observe que los parámetros para `forward_static_call_array` no son pasados por referencia.

## Valores devueltos

Devuelve el resultado de la función, o `false` en caso de error.

## Ejemplos

Ejemplo de `forward_static_call_array`

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
        forward_static_call_array(array('A', 'prueba'), array('más', 'args'));
        forward_static_call_array( 'prueba', array('otro', 'args'));
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

`forward_static_call`, `call_user_func`, `call_user_func_array`, `is_callable`
