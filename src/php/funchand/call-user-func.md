---
title: call_user_func
description: Llama a una función de retorno proporcionada por el primer argumento
source_url: https://www.php.net/manual/es/function.call-user-func.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/funchand/functions/call-user-func.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: funchand
translation_status: ready
translation_reviewed: true
translation_revision: 2eb43ad4f
order: 24730
---

call_user_func

Llama a una función de retorno proporcionada por el primer argumento

## Descripción

```php
call_user_func(callable $callback, mixed ...$args): mixed
```php

Llama a una función de retorno `callback` proporcionada por el parámetro `callback` donde los otros argumentos serán pasados como argumentos.

## Parámetros

`callback`  
La función de retorno a llamar.

`args`  
`0` o más argumentos a pasar a la función de retorno.

> [!NOTE]
> Tenga en cuenta que los argumentos para `call_user_func` no son pasados por referencia.
>
> <div class="example">
>
> <div class="title">
>
> Ejemplo con `call_user_func` por referencia
>
> </div>
>
> ```
> <?php
> function increment(&$var)
> {
>     $var++;
> }
>
> $a = 0;
> call_user_func('increment', $a);
> echo $a."\n";
>
> // es posible utilizar esto en su lugar
> call_user_func_array('increment', array(&$a));
> echo $a."\n";
>
> // también es posible utilizar funciones variables
> $increment = 'increment';
> $increment($a);
> echo $a."\n";
> ?>
>
>          
> ```
>
> El ejemplo anterior mostrará:
>
>     Warning: Parameter 1 to increment() expected to be a reference, value given in …
>     0
>     1
>     2
>
>              
>
> </div>

## Valores devueltos

Retorna el valor retornado por la función de retorno.

## Ejemplos

Ejemplo con `call_user_func`

```
<?php
function barber($type)
{
    echo "Usted quiere un corte $type, ningún problema";
}
call_user_func('barber', "al tazón");
call_user_func('barber', "con navaja");
?>

    
```php

El ejemplo anterior mostrará:

    Usted quiere un corte al tazón, ningún problema
    Usted quiere un corte con navaja, ningún problema

Ejemplo con `call_user_func` utilizando un espacio de nombres

```
<?php

namespace Foobar;

class Foo {
    static public function test() {
        print "¡Hola mundo!\n";
    }
}

call_user_func(__NAMESPACE__ .'\Foo::test');
call_user_func(array(__NAMESPACE__ .'\Foo', 'test'));
?>

    
```php

El ejemplo anterior mostrará:

    ¡Hola mundo!
    ¡Hola mundo!

Uso de un método de clase con `call_user_func`

```
<?php

class maclasse {
    static function dit_bonjour()
    {
        echo "¡Hola!\n";
    }
}

$classname = "maclasse";

call_user_func(array($classname, 'dit_bonjour'));
call_user_func($classname .'::dit_bonjour');

$monobjet = new maclasse();

call_user_func(array($monobjet, 'dit_bonjour'));

?>

    
```php

El ejemplo anterior mostrará:

    ¡Hola!
    ¡Hola!
    ¡Hola!

Uso de una función lambda con `call_user_func`

```
<?php
call_user_func(function($arg) { print "[$arg]\n"; }, 'test');
?>

    
```php

El ejemplo anterior mostrará:

    [test]

## Notas

> [!NOTE]
> Las devoluciónes de llamada registradas con funciones como `call_user_func` y `call_user_func_array` no serán llamadas si una excepción no es interceptada cuando ha sido lanzada en una función de devolución de llamada anterior.

## Véase también

`call_user_func_array`, `is_callable`, [Funciones variables](#functions.variable-functions), ReflectionFunction::invoke, ReflectionMethod::invoke
