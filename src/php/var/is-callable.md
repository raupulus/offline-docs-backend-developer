---
title: is_callable
description: Determina si un valor puede ser llamado como una función en el ámbito
  actual
source_url: https://www.php.net/manual/es/function.is-callable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/is-callable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: 32c55286c
order: 100570
---

is_callable

Determina si un valor puede ser llamado como una función en el ámbito actual

## Descripción

```php
is_callable(mixed $value, [bool $syntax_only], [string $callable_name]): bool
```php

Verifica que `value` es un `callable`, o que puede ser llamado utilizando la función `call_user_func`.

## Parámetros

`value`  
El valor a verificar.

`syntax_only`  
Si el argumento `syntax_only` vale `true`, la función solo verificará si `value` puede ser una función o un método. Rechazará todos los valores que no sean objetos [invocables](#object.invoke), `Closure`, `string`s, o `array`s que no tengan una estructura válida para ser utilizados como un callback. Un array invocable válido contiene 2 entradas: la primera debe ser un objeto o un string, y la segunda un string.

`callable_name`  
Recibe el "nombre de la función invocable", por ejemplo `"SomeClass::someMethod"`. Tenga en cuenta, sin embargo, que, a pesar de la implicación de que `SomeClass::someMethod()` es un método estático invocable, no es el caso.

## Valores devueltos

Retorna `true` si `value` puede ser llamado como una función, `false` en caso contrario.

## Ejemplos

Verificación si un string puede ser llamado como una función

```
<?php

function someFunction() {}

$functionVariable = 'someFunction';

var_dump(is_callable($functionVariable, false, $callable_name));

var_dump($callable_name);

?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    string(12) "someFunction"

Verificación si un array puede ser llamado como una función

```
<?php

class someClass
{
    public function someMethod() {}
}

$anObject = new SomeClass();

$methodVariable = [$anObject, 'someMethod'];

var_dump(is_callable($methodVariable, true, $callable_name));

var_dump($callable_name);

?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    string(21) "SomeClass::someMethod"

`is_callable` y los constructores

A pesar de que los constructores son los métodos que se llaman cuando un objeto es creado, no son métodos estáticos y `is_callable` retornará `false` para ellos. No es posible utilizar `is_callable` para verificar si una clase puede ser instanciada desde el ámbito actual.

```
<?php

class Foo
{
    public function __construct() {}

    public function foo() {}
}

var_dump(
    is_callable(['Foo', '__construct']),
    is_callable(['Foo', 'foo'])
);

$foo = new Foo();
var_dump(is_callable([$foo, '__construct']));

?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(false)
    bool(true)

## Notas

Un objeto es siempre invocable si implementa

\_\_invoke()

, y que el método es visible en el ámbito actual.

Un nombre de clase es invocable si implementa

\_\_callStatic()

Si un objeto implementa

\_\_call()

, entonces esta función retornará

true

para cualquier método en ese objeto, incluso si el método no está definido.

Esta función puede desencadenar el autoload si es llamada con el nombre de una clase.

## Véase también

`call_user_func`, `function_exists`, `method_exists`
