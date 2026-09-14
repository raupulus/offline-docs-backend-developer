---
title: Callables
source_url: https://www.php.net/manual/es/language.types.callable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/callable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 312c0c7b3
order: 4400
---

## Callables

Un callable es una referencia a una función o método que se pasa a otra función como argumento. Se representa con la declaración de tipo `callable`.

```php
<?php
function foo(callable $callback) {
    $callback();
}
?>

  
```

Algunas funciones aceptan funciones de retrollamada como parámetro, por ejemplo `array_map`, `usort`, o `preg_replace_callback`.

## Creación de callables

Un callable es un tipo que representa algo que se puede invocar. Los callables se pueden pasar como argumentos a funciones o métodos que esperan un parámetro de retrollamada o se pueden invocar directamente. El tipo `callable` no se puede usar como declaración de tipo para propiedades de clase. En su lugar, use una declaración de tipo `Closure`.

Los callables se pueden crear de varias maneras diferentes:

- Un objeto `Closure`

- Un `string` conteniendo el nombre de una función o método

- Un `array` conteniendo un nombre de clase o un `object` en el índice 0 y el nombre del método en el índice 1

- Un `object` implementando el método mágico [\_\_invoke()](#object.invoke)

Un objeto `Closure` puede ser creado usando la sintaxis de [funciones anónimas](#functions.anonymous), sintaxis de [funciones de flecha](#functions.arrow), [sintaxis callable de primera clase](#functions.first_class_callable_syntax), o el método Closure::fromCallable.

> [!NOTE]
> La [sintaxis callable de primera clase](#functions.first_class_callable_syntax) solo está disponible a partir de PHP 8.1.0.

Ejemplo de callback usando una `Closure`

```php
<?php
// Usando sintaxis de función anónima
$double1 = function ($a) {
    return $a * 2;
};

// Usando sintaxis de callable de primera clase
function double_function($a) {
    return $a * 2;
}
$double2 = double_function(...);

// Usando sintaxis de función de flecha
$double3 = fn($a) => $a * 2;

// Usando Closure::fromCallable
$double4 = Closure::fromCallable('double_function');

// Utilizar clousure como función de devolución de retrollamada
// para duplicar el tamaño de cada elemento en nuestro rango
$new_numbers = array_map($double1, range(1, 5));
print implode(' ', $new_numbers) . PHP_EOL;

$new_numbers = array_map($double2, range(1, 5));
print implode(' ', $new_numbers) . PHP_EOL;

$new_numbers = array_map($double3, range(1, 5));
print implode(' ', $new_numbers) . PHP_EOL;

$new_numbers = array_map($double4, range(1, 5));
print implode(' ', $new_numbers);

?>

   
```

Resultado del ejemplo anterior en PHP 8.1:

    2 4 6 8 10
    2 4 6 8 10
    2 4 6 8 10
    2 4 6 8 10

Un callable también puede ser un string que contenga el nombre de una función o método estático. Cualquier función interna o definida por el usuario puede ser usada, excepto las construcciones del lenguaje como: `array`, `echo`, `empty`, `eval`, `isset`, `list`, `print`, o `unset`.

Un método de clase estático puede ser usado sin instanciar un `object` de esa clase, ya sea creando un array con el nombre de la clase en el índice 0 y el nombre del método en el índice 1, o usando la sintaxis especial con el operador de resolución de ámbito `::`, como en `'ClassName::methodName'`.

Un método de un `object` instanciado puede ser un callable cuando se pasa como un array con el `object` en el índice 0 y el nombre del método en el índice 1.

La principal diferencia entre un objeto `Closure` y el tipo `callable` es que un objeto `Closure` es independiente del ámbito y siempre se puede invocar, mientras que un tipo callable puede depender del ámbito y puede que no se pueda invocar directamente. `Closure` es la forma preferida de crear callables.

> [!NOTE]
> Mientras que los objetos `Closure` están vinculados al ámbito donde se crean, los callables que hacen referencia a métodos de clase como strings o arrays se resuelven en el ámbito donde se llaman. Para crear un callable a partir de un método privado o protegido, que luego se pueda invocar desde fuera del ámbito de la clase, use Closure::fromCallable o la [sintaxis callable de primera clase](#functions.first_class_callable_syntax).

PHP permite la creación de callables que pueden ser usados como argumento de retrollamada pero que no pueden ser llamados directamente. Estos son callables dependientes del contexto que hacen referencia a un método de clase en la jerarquía de herencia de una clase, por ejemplo `'parent::method'` o `["static", "method"]`.

> [!NOTE]
> A partir de PHP 8.2.0, los callables dependientes del contexto están obsoletos. Elimine la dependencia del contexto reemplazando `'parent::method'` con `parent::class . '::method'` o use la [sintaxis callable de primera clase](#functions.first_class_callable_syntax).

Invocando varios tipos de callables con `call_user_func`

```php
<?php

// Un ejemplo de función de retrollamada
function my_callback_function() {
    echo '¡hola mundo!', PHP_EOL;
}

// Un ejemplo de método de retrollamada
class MyClass {
    static function myCallbackMethod() {
        echo '¡Hola Mundo!', PHP_EOL;
    }
}

// Tipo 1: Función de retrollamada simple
call_user_func('my_callback_function');

// Tipo 2: Llamada a un método estático de clase
call_user_func(['MyClass', 'myCallbackMethod']);

// Tipo 3: Llamada a un método de objeto
$obj = new MyClass();
call_user_func([$obj, 'myCallbackMethod']);

// Tipo 4: Llamada a un método estático de clase
call_user_func('MyClass::myCallbackMethod');

// Type 5: Llamada a un método estático de clase usando la palabla clave ::class
call_user_func([MyClass::class, 'myCallbackMethod']);

// Tipo 6: Llamada a un método estático de clase relativo
class A {
    public static function who() {
        echo 'A', PHP_EOL;
    }
}

class B extends A {
    public static function who() {
        echo 'B', PHP_EOL;
    }
}

call_user_func(['B', 'parent::who']); // obsoleto a partir de PHP 8.2.0

// Tipo 7: Los objetos que implementan __invoke pueden ser utilizados como callables
class C {
    public function __invoke($name) {
        echo 'Hola ', $name;
    }
}

$c = new C();
call_user_func($c, 'PHP!');
?>

   
```

El ejemplo anterior mostrará:

    ¡hola mundo!
    ¡Hola Mundo!
    ¡Hola Mundo!
    ¡Hola Mundo!
    ¡Hola Mundo!

    Deprecated: Callables of the form ["B", "parent::who"] are deprecated in script on line 41
    A
    Hola PHP!

> [!NOTE]
> Las devoluciónes de llamada registradas con funciones como `call_user_func` y `call_user_func_array` no serán llamadas si una excepción no es interceptada cuando ha sido lanzada en una función de devolución de llamada anterior.
