---
title: Reflection::getModifierNames
description: Obtiene los nombres de los modificadores
source_url: https://www.php.net/manual/es/reflection.getmodifiernames.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflection/getmodifiernames.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 68960
---

Reflection::getModifierNames

Obtiene los nombres de los modificadores

## Descripción

```php
public static Reflection::getModifierNames(int $modifiers): array
```php

Obtiene los nombres de los modificadores.

## Parámetros

`modifiers`  
Campo de bits (bitfield) de los modificadores a obtener.

## Valores devueltos

Un array de los nombres de los modificadores.

## Ejemplos

Ejemplo Reflection::getModifierNames

```
<?php
class Testing
{
    final public static function foo()
    {
        return;
    }

    public function bar()
    {
        return;
    }
}

$foo = new ReflectionMethod('Testing', 'foo');

echo "Modificadores para el método foo():\n";
echo $foo->getModifiers() . "\n";
echo implode(' ', Reflection::getModifierNames($foo->getModifiers())) . "\n";

$bar = new ReflectionMethod('Testing', 'bar');

echo "Modificadores para el método bar():\n";
echo $bar->getModifiers() . "\n";
echo implode(' ', Reflection::getModifierNames($bar->getModifiers()));

    
```php

Resultado del ejemplo anterior es similar a:

    Modificadores para el método foo():
    261
    final public static
    Modificadores para el método bar():
    65792
    public

## Véase también

ReflectionClass::getModifiers, ReflectionClassConstant::getModifiers, ReflectionMethod::getModifiers, ReflectionProperty::getModifiers
