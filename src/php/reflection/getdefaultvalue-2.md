---
title: ReflectionProperty::getDefaultValue
description: Devuelve el valor por defecto definido para una propiedad
source_url: https://www.php.net/manual/es/reflectionproperty.getdefaultvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/getdefaultvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 525aa5f19
order: 71480
---

ReflectionProperty::getDefaultValue

Devuelve el valor por defecto definido para una propiedad

## Descripción

```php
public ReflectionProperty::getDefaultValue(): mixed
```php

Devuelve el valor por defecto implícito o explícitamente definido para una propiedad.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor por defecto si la propiedad tiene un valor por defecto (incluyendo `null`). Si no hay valor por defecto, entonces se devuelve `null`. No es posible diferenciar un `null` por defecto de una propiedad tipada no inicializada. Utilizar ReflectionProperty::hasDefaultValue para detectar la diferencia.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | La llamada a ReflectionProperty::getDefaultValue para propiedades sin valor por defecto ha quedado obsoleta. |

## Ejemplos

Ejemplo de ReflectionProperty::getDefaultValue

```
<?php
class Foo {
    public $bar = 1;
    public ?int $baz;
    public int $boing = 0;
    public function __construct(public string $bak = "default") { }
}

$ro = new ReflectionClass(Foo::class);
var_dump($ro->getProperty('bar')->getDefaultValue());
var_dump($ro->getProperty('baz')->getDefaultValue());
var_dump($ro->getProperty('boing')->getDefaultValue());
var_dump($ro->getProperty('bak')->getDefaultValue());
?>

 
```php

El ejemplo anterior mostrará:

    int(1)
    NULL
    int(0)
    NULL

## Véase también

ReflectionProperty::hasDefaultValue
