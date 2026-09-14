---
title: ReflectionProperty::setValue
description: Define el valor de la propiedad
source_url: https://www.php.net/manual/es/reflectionproperty.setvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/setvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c4aabaa0b
order: 71800
---

ReflectionProperty::setValue

Define el valor de la propiedad

## Descripción

```php
public ReflectionProperty::setValue(object $object, object $object, mixed $value): void
```php

```php
public ReflectionProperty::setValue(mixed $value): void
```

Define (modifica) el valor de la propiedad.

> [!NOTE]
> Para definir los valores de las propiedades estáticas, utilice `ReflectionProperty::setValue(null, $value)`.

## Parámetros

`object`  
Para las propiedades estáticas, pase `null`. Para las propiedades no estáticas, pase el objeto.

`value`  
El nuevo valor.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | La llamada a este método con un solo argumento está obsoleto, utilice en su lugar `ReflectionProperty::setValue(null, $value)` para las propiedades estáticas. |
| 8.1.0 | Las propiedades privadas y protegidas son inmediatamente accesibles por ReflectionProperty::setValue. Anteriormente, debían ser hechas accesibles llamando a ReflectionProperty::setAccessible, de lo contrario se lanzaba una `ReflectionException`. |

## Ejemplos

Ejemplo con ReflectionProperty::setValue

```php
<?php
class Foo {
    public static $staticProperty;

    public $property;
    protected $privateProperty;
}

$reflectionClass = new ReflectionClass('Foo');

// A partir de PHP 8.3, pasar null como primer argumento es requerido
// para acceder a las propiedades estáticas.
$reflectionProperty = $reflectionClass->getProperty('staticProperty');
$reflectionProperty->setValue(null, 'foo');
var_dump(Foo::$staticProperty);

$foo = new Foo;

$reflectionClass->getProperty('property')->setValue($foo, 'bar');
var_dump($foo->property);

$reflectionProperty = $reflectionClass->getProperty('privateProperty');
$reflectionProperty->setAccessible(true); // Solo necesario antes de PHP 8.1.0.
$reflectionProperty->setValue($foo, 'foobar');
var_dump($reflectionProperty->getValue($foo));
?>

    
```

El ejemplo anterior mostrará:

    string(3) "foo"
    string(3) "bar"
    string(6) "foobar"

## Véase también

ReflectionProperty::getValue, ReflectionProperty::setAccessible, ReflectionClass::setStaticPropertyValue
