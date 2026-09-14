---
title: call_user_func_array
description: Llama a una función de retorno con los argumentos agrupados en un array
source_url: https://www.php.net/manual/es/function.call-user-func-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/funchand/functions/call-user-func-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: funchand
translation_status: ready
translation_reviewed: true
translation_revision: 5832a97c6
order: 24720
---

call_user_func_array

Llama a una función de retorno con los argumentos agrupados en un array

## Descripción

```php
call_user_func_array(callable $callback, array $args): mixed
```php

Llama a la función de retorno `callback` proporcionada con los argumentos `args`, agrupados en un array.

## Parámetros

`callback`  
La función de retorno a llamar.

`args`  
Los argumentos a pasar a la función de retorno, en forma de array.

Si las claves de `args` son todas numéricas, las claves son ignoradas y cada elemento será transmitido a `callback` como argumento posicional, en el orden.

Si algunas claves de `args` son strings, estos elementos serán transmitidos a `callback` como argumentos nombrados, con el nombre dado por la clave.

No es permitido tener una clave numérica en `args` que aparezca después de una clave de string, o tener una clave de string que no corresponda al nombre de algún parámetro de `callback`

## Valores devueltos

Retorna el valor retornado por la función de retorno, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Las claves `args` serán interpretadas como nombres de parámetros, en lugar de ser ignoradas silenciosamente. |

## Ejemplos

Ejemplo con `call_user_func_array`

```
<?php
function foobar($arg, $arg2) {
    echo __FUNCTION__, " recibió $arg y $arg2\n";
}
class foo {
    function bar($arg, $arg2) {
        echo __METHOD__, " recibió $arg y $arg2\n";
    }
}

// Llamar a la función foobar() con 2 argumentos
call_user_func_array("foobar", array("one", "two"));

// Llamar al método $foo->bar() con 2 argumentos
$foo = new foo;
call_user_func_array(array($foo, "bar"), array("three", "four"));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    foobar recibió one y two
    foo::bar recibió three y four

Ejemplo con `call_user_func_array` utilizando un espacio de nombres

```
<?php

namespace Foobar;

class Foo {
    static public function test($name) {
        print "¡Hola {$name}!\n";
    }
}

call_user_func_array(__NAMESPACE__ .'\Foo::test', array('Hannes'));

call_user_func_array(array(__NAMESPACE__ .'\Foo', 'test'), array('Philip'));

?>

    
```php

El ejemplo anterior mostrará:

    ¡Hola Hannes!
    ¡Hola Philip!

Uso de una función lambda

```
<?php

$func = function($arg1, $arg2) {
    return $arg1 * $arg2;
};

var_dump(call_user_func_array($func, array(2, 4)));

?>

    
```php

El ejemplo anterior mostrará:

    int(8)

Pasando un valor por referencia

```
<?php

function mega(&$a){
    $a = 55;
    echo "function mega \$a=$a\n";
}
$bar = 77;
call_user_func_array('mega',array(&$bar));
echo "global \$bar=$bar\n";

?>

    
```php

El ejemplo anterior mostrará:

    function mega $a=55
    global $bar=55

`call_user_func_array` utilizando argumentos nombrados

```
<?php
function foobar($first, $second) {
    echo __FUNCTION__, " recibió $first y $second\n";
}

// Llamar a la función foobar() con argumentos nombrados en orden no posicional
call_user_func_array("foobar", array("second" => "two", "first" => "one"));

// Llamar a la función foobar() con un argumento nombrado
call_user_func_array("foobar", array("foo", "second" => "bar"));

// Error fatal: No se puede usar un argumento posicional después de un argumento nombrado
call_user_func_array("foobar", array("first" => "one", "bar"));

?>

    
```php

Resultado del ejemplo anterior es similar a:

    foobar recibió one y two
    foobar recibió foo y bar

    Fatal error: Uncaught Error: Cannot use positional argument after named argument

## Notas

> [!NOTE]
> Las devoluciónes de llamada registradas con funciones como `call_user_func` y `call_user_func_array` no serán llamadas si una excepción no es interceptada cuando ha sido lanzada en una función de devolución de llamada anterior.

## Véase también

`call_user_func`, ReflectionFunction::invokeArgs, ReflectionMethod::invokeArgs
