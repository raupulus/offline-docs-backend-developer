---
title: ReflectionProperty::getValue
description: Obtiene el valor de la propiedad
source_url: https://www.php.net/manual/es/reflectionproperty.getvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/getvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 71570
---

ReflectionProperty::getValue

Obtiene el valor de la propiedad

## Descripción

```php
public ReflectionProperty::getValue([object $object]): mixed
```php

Obtiene el valor de la propiedad.

## Parámetros

`object`  
El objeto a utilizar en el caso de una propiedad no estática. Si se desea obtener el valor por defecto de la propiedad, debe utilizarse ReflectionClass::getDefaultProperties en su lugar.

## Valores devueltos

El valor actual de la propiedad.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Las propiedades privadas y protegidas son inmediatamente accesibles por ReflectionProperty::setValue. Anteriormente, debían ser hechas accesibles llamando ReflectionProperty::setAccessible, de lo contrario se lanzaba una `ReflectionException`. |
| 8.0.0 | `object` ahora es nullable. |

## Ejemplos

Ejemplo con ReflectionProperty::getValue

```
<?php
class Foo {
    public static $staticProperty = 'foobar';

    public $property = 'barfoo';
    protected $privateProperty = 'foofoo';
}

$reflectionClass = new ReflectionClass('Foo');

var_dump($reflectionClass->getProperty('staticProperty')->getValue());
var_dump($reflectionClass->getProperty('property')->getValue(new Foo));

$reflectionProperty = $reflectionClass->getProperty('privateProperty');
$reflectionProperty->setAccessible(true); // Solo necesario antes de PHP 8.1.0.
var_dump($reflectionProperty->getValue(new Foo));
?>

    
```php

El ejemplo anterior mostrará:

    string(6) "foobar"
    string(6) "barfoo"
    string(6) "foofoo"

## Véase también

ReflectionProperty::setValue, ReflectionProperty::setAccessible, ReflectionClass::getDefaultProperties, ReflectionClass::getStaticPropertyValue
