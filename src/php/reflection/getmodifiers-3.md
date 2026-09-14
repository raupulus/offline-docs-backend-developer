---
title: ReflectionMethod::getModifiers
description: Obtiene los modificadores del método
source_url: https://www.php.net/manual/es/reflectionmethod.getmodifiers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionmethod/getmodifiers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 70970
---

ReflectionMethod::getModifiers

Obtiene los modificadores del método

## Descripción

```php
public ReflectionMethod::getModifiers(): int
```php

Devuelve un campo de bits de modificadores de acceso para este método.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una representación numérica de los modificadores. El significado actual de estos modificadores se describe en las [constantes predefinidas](#reflectionmethod.constants.modifiers).

## Ejemplos

Ejemplo con ReflectionMethod::getModifiers

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
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Modificadores para el método foo():
    49
    final public static
    Modificadores para el método bar():
    1
    public

## Véase también

Reflection::getModifierNames
