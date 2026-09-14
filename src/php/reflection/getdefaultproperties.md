---
title: ReflectionClass::getDefaultProperties
description: Obtiene las propiedades por defecto
source_url: https://www.php.net/manual/es/reflectionclass.getdefaultproperties.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getdefaultproperties.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69110
---

ReflectionClass::getDefaultProperties

Obtiene las propiedades por defecto

## Descripción

```php
public ReflectionClass::getDefaultProperties(): array
```php

Obtiene las propiedades por defecto de una clase (incluyendo las propiedades heredadas).

> [!NOTE]
> Este método funciona únicamente para las propiedades estáticas cuando se utiliza en clases internas. El valor por defecto de una propiedad de clase estática no puede ser monitoreado al utilizar este método en clases definidas por el usuario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` de propiedades por defecto donde la clave es el nombre de la propiedad y el valor es el valor por defecto de la propiedad o `null` si la propiedad no tiene valor por defecto. La función no distingue entre propiedades estáticas y no estáticas y no considera la visibilidad.

## Ejemplos

Ejemplo con ReflectionClass::getDefaultProperties

```
<?php
class Bar {
    protected $inheritedProperty = 'inheritedDefault';
}

class Foo extends Bar {
    public $property = 'propertyDefault';
    private $privateProperty = 'privatePropertyDefault';
    public static $staticProperty = 'staticProperty';
    public $defaultlessProperty;
}

$reflectionClass = new ReflectionClass('Foo');
var_dump($reflectionClass->getDefaultProperties());
?>

    
```php

El ejemplo anterior mostrará:

    array(5) {
       ["staticProperty"]=>
       string(14) "staticProperty"
       ["property"]=>
       string(15) "propertyDefault"
       ["privateProperty"]=>
       string(22) "privatePropertyDefault"
       ["defaultlessProperty"]=>
       NULL
       ["inheritedProperty"]=>
       string(16) "inheritedDefault"
    }

## Véase también

ReflectionClass::getProperties, ReflectionClass::getStaticProperties, ReflectionClass::getProperty
