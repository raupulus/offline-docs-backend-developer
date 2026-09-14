---
title: ReflectionFunctionAbstract::getClosureCalledClass
description: 'Devuelve la clase correspondiente a static:: dentro de una función anónima'
source_url: https://www.php.net/manual/es/reflectionfunctionabstract.getclosurecalledclass.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunctionabstract/getclosurecalledclass.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 1870b4c6a
order: 70490
---

ReflectionFunctionAbstract::getClosureCalledClass

Devuelve la clase correspondiente a static:: dentro de una función anónima

## Descripción

```php
public ReflectionFunctionAbstract::getClosureCalledClass(): ReflectionClass
```php

Devuelve la clase como `ReflectionClass` que corresponde a la resolución del nombre de clase correspondiente a `static::` dentro de la `Closure`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una `ReflectionClass` correspondiente a la clase representada por `static::` en la `Closure`. Si la función no es una función anónima o si tiene un ámbito global, `null` es devuelto en su lugar.

## Ejemplos

Ejemplo que ilustra la diferencia entre ReflectionFunctionAbstract::getClosureCalledClass, ReflectionFunctionAbstract::getClosureScopeClass, y ReflectionFunctionAbstract::getClosureThis con una función anónima en el contexto del objeto

```
<?php

class A
{
    public function getClosure()
    {
        var_dump(self::class, static::class);
        return function () {};
    }
}

class B extends A {}

$b = new B();
$c = $b->getClosure();
$r = new ReflectionFunction($c);

var_dump($r->getClosureThis()); // $this === $b, ya que una función anónima no estática toma el contexto del objeto
var_dump($r->getClosureScopeClass()); // Corresponde a la resolución de self::class dentro de una función anónima
var_dump($r->getClosureCalledClass()); // Corresponde a la resolución de static::class dentro de una función anónima

?>

   
```php

El ejemplo anterior mostrará:

    string(1) "A"
    string(1) "B"
    object(B)#1 (0) {
    }
    object(ReflectionClass)#4 (1) {
      ["name"]=>
      string(1) "A"
    }
    object(ReflectionClass)#4 (1) {
      ["name"]=>
      string(1) "B"
    }

Ejemplo que ilustra la diferencia entre ReflectionFunctionAbstract::getClosureCalledClass, ReflectionFunctionAbstract::getClosureScopeClass, y ReflectionFunctionAbstract::getClosureThis con una función anónima estática sin contexto de objeto

```
    
<?php

class A
{
    public function getClosure()
    {
        var_dump(self::class, static::class);
        return static function () {};
    }
}

class B extends A {}

$b = new B();
$c = $b->getClosure();
$r = new ReflectionFunction($c);

var_dump($r->getClosureThis()); // NULL, ya que la pseudo-variable $this no está disponible en un contexto estático
var_dump($r->getClosureScopeClass()); // Corresponde a la resolución de self::class dentro de una función anónima
var_dump($r->getClosureCalledClass()); // Corresponde a la resolución de static::class dentro de una función anónima

?>

   
```php

El ejemplo anterior mostrará:

    string(1) "A"
    string(1) "B"
    NULL
    object(ReflectionClass)#4 (1) {
      ["name"]=>
      string(1) "A"
    }
    object(ReflectionClass)#4 (1) {
      ["name"]=>
      string(1) "B"
    }

## Véase también

ReflectionFunctionAbstract::getClosureScopeClass

ReflectionFunctionAbstract::getClosureThis
