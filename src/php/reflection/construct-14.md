---
title: ReflectionParameter::__construct
description: Constructor
source_url: https://www.php.net/manual/es/reflectionparameter.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionparameter/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 71210
---

ReflectionParameter::\_\_construct

Constructor

## Descripción

```php
public ReflectionParameter::__construct(string $function, int $param)
```php

Construye una instancia `ReflectionParameter`.

## Parámetros

`function`  
La función desde la cual los parámetros son reflejados.

`param`  
Puede ser un `int` que especifica la posición del parámetro (comenzando por cero), o el nombre del parámetro como `string`.

## Ejemplos

Ejemplo con `ReflectionParameter`

```
<?php
function foo($a, $b, $c) { }
function bar(Exception $a, &$b, $c) { }
function baz(ReflectionFunction $a, $b = 1, $c = null) { }
function abc() { }

$reflect = new ReflectionFunction('foo');

echo $reflect;

foreach ($reflect->getParameters() as $i => $param) {
    printf(
        "-- Parameter #%d: %s {\n".
        "   Class: %s\n".
        "   Allows NULL: %s\n".
        "   Passed to by reference: %s\n".
        "   Is optional?: %s\n".
        "}\n",
        $i, // $param->getPosition() can be used
        $param->getName(),
        var_export($param->getClass(), 1),
        var_export($param->allowsNull(), 1),
        var_export($param->isPassedByReference(), 1),
        $param->isOptional() ? 'yes' : 'no'
    );
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Function [ <user> function foo ] {
      @@ /Users/philip/cvs/phpdoc/a 2 - 2

      - Parameters [3] {
        Parameter #0 [ <required> $a ]
        Parameter #1 [ <required> $b ]
        Parameter #2 [ <required> $c ]
      }
    }
    -- Parameter #0: a {
       Class: NULL
       Allows NULL: true
       Passed to by reference: false
       Is optional?: no
    }
    -- Parameter #1: b {
       Class: NULL
       Allows NULL: true
       Passed to by reference: false
       Is optional?: no
    }
    -- Parameter #2: c {
       Class: NULL
       Allows NULL: true
       Passed to by reference: false
       Is optional?: no
    }

## Véase también

ReflectionFunctionAbstract::getParameters, ReflectionFunction::\_\_construct, ReflectionMethod::\_\_construct, [Los constructores](#language.oop5.decon.constructor)
