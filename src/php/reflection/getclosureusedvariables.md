---
title: ReflectionFunctionAbstract::getClosureUsedVariables
description: Devuelve un array de las variables utilizadas en la Closure
source_url: https://www.php.net/manual/es/reflectionfunctionabstract.getclosureusedvariables.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunctionabstract/getclosureusedvariables.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70520
---

ReflectionFunctionAbstract::getClosureUsedVariables

Devuelve un array de las variables utilizadas en la Closure

## Descripción

```php
public ReflectionFunctionAbstract::getClosureUsedVariables(): array
```php

Devuelve un `array` de las variables utilizadas en la `Closure`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `array` de las variables utilizadas en la `Closure`.

## Ejemplos

Ejemplo de ReflectionFunctionAbstract::getClosureUsedVariables

```
<?php

$one = 1;
$two = 2;

$function = function() use ($one, $two) {
    static $three = 3;
};

$reflector = new ReflectionFunction($function);

var_dump($reflector->getClosureUsedVariables());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
      ["one"]=>
      int(1)
      ["two"]=>
      int(2)
    }

## Véase también

`ReflectionFunctionAbstract::getClosureScopeClass`, `ReflectionFunctionAbstract::getClosureThis`
