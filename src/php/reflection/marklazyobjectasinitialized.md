---
title: ReflectionClass::markLazyObjectAsInitialized
description: Marca un objeto perezoso como inicializado sin llamar al inicializador
  o a la fábrica
source_url: https://www.php.net/manual/es/reflectionclass.marklazyobjectasinitialized.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/marklazyobjectasinitialized.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c0fa5077c
order: 69590
---

ReflectionClass::markLazyObjectAsInitialized

Marca un objeto perezoso como inicializado sin llamar al inicializador o a la fábrica

## Descripción

```php
public ReflectionClass::markLazyObjectAsInitialized(object $object): object
```php

Marca un objeto perezoso como inicializado sin llamar al inicializador o a la fábrica. Esto no tiene ningún efecto si `object` no es perezoso o ya está inicializado.

El efecto de la llamada a este método es el mismo que se describe para los objetos fantasma (independientemente de la estrategia perezosa de `object`) en [secuencia de inicialización](#language.oop5.lazy-objects.initialization-sequence), excepto que no se llama al inicializador. Después de esto, el objeto es indistinguible de un objeto que nunca fue perezoso y fue creado con ReflectionClass::newInstanceWithoutConstructor, excepto por el valor de las propiedades que ya han sido inicializadas con ReflectionProperty::setRawValueWithoutLazyInitialization o ReflectionProperty::skipLazyInitialization.

## Parámetros

`object`  
El objeto a marcar como inicializado.

## Valores devueltos

Devuelve `object`.

## Ejemplos

Marcar un objeto perezoso no inicializado como inicializado

```
<?php
class Example
{
    public string $prop1;
    public string $prop2;
    public string $prop3 = 'default value';
}

$reflector = new ReflectionClass(Example::class);

$object = $reflector->newLazyGhost(function ($object) {
    echo "Initializer called\n";
    $object->prop1 = 'initialized';
});

$reflector->getProperty('prop1')
          ->setRawValueWithoutLazyInitialization($object, 'prop1 value');

var_dump($object);

$reflector->markLazyObjectAsInitialized($object);

var_dump($object);
?>

   
```php

El ejemplo anterior mostrará:

    lazy ghost object(Example)#3 (1) {
      ["prop1"]=>
      string(11) "prop1 value"
      ["prop2"]=>
      uninitialized(string)
      ["prop3"]=>
      uninitialized(string)
    }
    object(Example)#3 (2) {
      ["prop1"]=>
      string(11) "prop1 value"
      ["prop2"]=>
      uninitialized(string)
      ["prop3"]=>
      string(13) "default value"
    }

Marcar un objeto perezoso inicializado como inicializado

```
<?php
class Example
{
    public string $prop1;
    public string $prop2;
    public string $prop3 = 'default value';
}

$reflector = new ReflectionClass(Example::class);

$object = $reflector->newLazyGhost(function ($object) {
    echo "Initializer called\n";
    $object->prop1 = 'initialized';
});

$reflector->getProperty('prop1')
          ->setRawValueWithoutLazyInitialization($object, 'prop1 value');

var_dump($object->prop3);
var_dump($object);

$reflector->markLazyObjectAsInitialized($object);

var_dump($object);
?>

    
```php

El ejemplo anterior mostrará:

    Initializer called
    string(13) "default value"
    object(Example)#3 (2) {
      ["prop1"]=>
      string(11) "initialized"
      ["prop2"]=>
      uninitialized(string)
      ["prop3"]=>
      string(13) "default value"
    }
    object(Example)#3 (2) {
      ["prop1"]=>
      string(11) "initialized"
      ["prop2"]=>
      uninitialized(string)
      ["prop3"]=>
      string(13) "default value"
    }

## Véase también

Objetos perezosos

ReflectionClass::newLazyGhost

ReflectionClass::initializeLazyObject

ReflectionClass::isUninitializedLazyObject
