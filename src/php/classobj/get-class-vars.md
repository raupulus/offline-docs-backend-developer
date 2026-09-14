---
title: get_class_vars
description: Devuelve los valores por defecto de las propiedades de una clase
source_url: https://www.php.net/manual/es/function.get-class-vars.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/get-class-vars.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: 1debc7606
order: 6790
---

get_class_vars

Devuelve los valores por defecto de las propiedades de una clase

## Descripción

```php
get_class_vars(string $class): array
```php

Devuelve los valores por defecto de las propiedades de una clase.

## Parámetros

`class`  
El nombre de la clase

## Valores devueltos

Devuelve un array asociativo que contiene los nombres/valores de las propiedades visibles en el ámbito actual, con sus valores por defecto. Los elementos del array resultante están en la forma `varname => value`. En caso de error, la función devolverá `false`.

## Ejemplos

Ejemplo con `get_class_vars`

```
<?php

class MyClass
{
    public $var1; // Esto no tiene un valor por defecto explícito (técnicamente tiene NULL como valor por defecto)...
    public $var2 = "xyz";
    public $var3 = 100;
    private $var4;

    // constructor
    function __construct()
    {
        // cambio de algunas propiedades
        $this->var1 = "foo";
        $this->var2 = "bar";
        return true;
    }

}

$my_class = new MyClass();

$class_vars = get_class_vars(get_class($my_class));

foreach ($class_vars as $name => $value) {
     echo "{$name}: ", var_export($value, true), "\n";
}

?>

    
```php

El ejemplo anterior mostrará:

    var1: NULL
    var2: 'xyz'
    var3: 100

Ejemplo con `get_class_vars` y los contextos

```
<?php

function format($array)
{
    return implode('|', array_keys($array)) . "\r\n";
}

class TestCase
{
    public $a = 1;
    protected $b = 2;
    private $c = 3;

    public static function expose()
    {
        echo format(get_class_vars(__CLASS__));
    }
}

TestCase::expose();
echo format(get_class_vars('TestCase'));

?>

    
```php

El ejemplo anterior mostrará:

    // 5.0.0
    a| * b| TestCase c
    a| * b| TestCase c

    // 5.0.1 - 5.0.2
    a|b|c
    a|b|c

    // 5.0.3 +
    a|b|c
    a

## Véase también

`get_class_methods`, `get_object_vars`
