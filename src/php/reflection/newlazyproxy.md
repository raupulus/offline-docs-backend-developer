---
title: ReflectionClass::newLazyProxy
description: Crear una nueva instancia proxy perezosa
source_url: https://www.php.net/manual/es/reflectionclass.newlazyproxy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/newlazyproxy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 2d8559c6c
order: 69640
---

ReflectionClass::newLazyProxy

Crear una nueva instancia proxy perezosa

## Descripción

```php
public ReflectionClass::newLazyProxy(callable $factory, [int $options]): object
```php

Crear una nueva instancia proxy perezosa de la clase, adjuntando la `factory` a la misma. El constructor no es llamado, y las propiedades no son definidas a su valor por defecto. Cuando se intenta observar o modificar el estado del proxy por primera vez, la función fábrica es llamada para proporcionar una instancia real, que es luego adjuntada al proxy. Después de esto, todas las interacciones posteriores con el proxy son transmitidas a la instancia real. Ver [disparadores de inicialización](#language.oop5.lazy-objects.initialization-triggers) y [ secuencia de inicialización](#language.oop5.lazy-objects.initialization-sequence).

## Parámetros

`factory`  
La fábrica es una función de devolución de llamada con la siguiente firma:

```php
factory(object $object): object
```

`object`  
El `object` en curso de inicialización. En este punto, el objeto ya no está marcado como perezoso, y acceder a él no dispara la inicialización.

La función fábrica debe devolver un objeto, llamado *instancia real*, que es luego adjuntado al proxy. Esta instancia real no debe ser perezosa ni debe ser el proxy mismo. Si la instancia real no tiene la misma clase que el proxy, la clase del proxy debe ser una subclase de la clase de la instancia real, sin propiedades adicionales, y no debe sobrescribir los métodos \_\_destruct o \_\_clone.

  

## Valores devueltos

Devuelve una instancia proxy perezosa. Si el objeto no tiene propiedades, o si todas sus propiedades son estáticas o virtuales, se devuelve una instancia normal (no perezosa). Ver también [Ciclo de vida de los objetos perezosos](#language.oop5.lazy-objects.lifecycle).

## Ejemplos

Uso básico

```php
<?php
class Example {
    public function __construct(public int $prop) {
        echo __METHOD__, "\n";
    }
}

$reflector = new ReflectionClass(Example::class);
$object = $reflector->newLazyProxy(function (Example $object) {
     $realInstance = new Example(1);
     return $realInstance;
});

var_dump($object);
var_dump($object instanceof Example);

// Dispara la inicialización, y transmite la recuperación de la propiedad a la instancia real
var_dump($object->prop);

var_dump($object);
?>

   
```

El ejemplo anterior mostrará:

    lazy proxy object(Example)#3 (0) {
      ["prop"]=>
      uninitialized(int)
    }
    bool(true)
    Example::__construct
    int(1)
    lazy proxy object(Example)#3 (1) {
      ["instance"]=>
      object(Example)#4 (1) {
        ["prop"]=>
        int(1)
      }
    }

## Véase también

Objetos perezosos

ReflectionClass::newLazyGhost

ReflectionClass::newInstanceWithoutConstructor

ReflectionClass::resetAsLazyProxy

ReflectionClass::markLazyObjectAsInitialized

ReflectionClass::initializeLazyObject

ReflectionClass::isUninitializedLazyObject

ReflectionProperty::setRawValueWithoutLazyInitialization

ReflectionProperty::skipLazyInitialization

ReflectionProperty::isLazy
