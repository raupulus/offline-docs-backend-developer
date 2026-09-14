---
title: ReflectionClass::getProperties
description: Obtiene las propiedades
source_url: https://www.php.net/manual/es/reflectionclass.getproperties.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getproperties.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 69260
---

ReflectionClass::getProperties

Obtiene las propiedades

## Descripción

```php
public ReflectionClass::getProperties([int $filter]): array
```php

Obtiene las propiedades reflejadas.

## Parámetros

`filter`  
El filtro, opcional, para filtrar los tipos de propiedades deseadas. Este filtro se configura utilizando las [constantes ReflectionProperty](#reflectionproperty.constants.modifiers), y por omisión, todos los tipos de propiedades son devueltos.

## Valores devueltos

Un array de objetos `ReflectionProperty`.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 7.2.0   | `filter` ahora es nullable. |

## Ejemplos

Ejemplo con `ReflectionClass::getProperties`

Este ejemplo muestra el uso del parámetro opcional `filter`, que permite filtrar las propiedades privadas.

```
<?php
class Foo {
    public    $foo  = 1;
    protected $bar  = 2;
    private   $baz  = 3;
}

$foo = new Foo();

$reflect = new ReflectionClass($foo);
$props   = $reflect->getProperties(ReflectionProperty::IS_PUBLIC | ReflectionProperty::IS_PROTECTED);

foreach ($props as $prop) {
    print $prop->getName() . "\n";
}

var_dump($props);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    foo
    bar
    array(2) {
      [0]=>
      object(ReflectionProperty)#3 (2) {
        ["name"]=>
        string(3) "foo"
        ["class"]=>
        string(3) "Foo"
      }
      [1]=>
      object(ReflectionProperty)#4 (2) {
        ["name"]=>
        string(3) "bar"
        ["class"]=>
        string(3) "Foo"
      }
    }

## Véase también

ReflectionClass::getProperty, `ReflectionProperty`, Las [constantes de modificadores de ReflectionProperty](#reflectionproperty.constants.modifiers)
