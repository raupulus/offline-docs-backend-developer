---
title: ReflectionClass::newLazyGhost
description: Crear una nueva instancia fantasma perezosa
source_url: https://www.php.net/manual/es/reflectionclass.newlazyghost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/newlazyghost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 2d8559c6c
order: 69630
---

ReflectionClass::newLazyGhost

Crear una nueva instancia fantasma perezosa

## Descripción

```php
public ReflectionClass::newLazyGhost(callable $initializer, [int $options]): object
```php

Crear una nueva instancia fantasma perezosa de la clase, adjuntando el `initializer` a esta. El constructor no es llamado, y las propiedades no son definidas a su valor por defecto. Sin embargo, el objeto será automáticamente inicializado invocando el `initializer` la primera vez que su estado es observado o modificado. Ver [disparadores de inicialización](#language.oop5.lazy-objects.initialization-triggers) y [ secuencia de inicialización](#language.oop5.lazy-objects.initialization-sequence).

## Parámetros

`initializer`  
El inicializador es una función de retrollamada con la siguiente firma:

```php
initializer(object $object): void
```

`object`  
El `object` en curso de inicialización. En este punto, el objeto ya no está marcado como perezoso, y acceder a él no desencadena la inicialización.

La función `initializer` debe devolver `null` o no devolver nada.

`options`  
`options` puede ser una combinación de los siguientes flags:

`ReflectionClass::SKIP_INITIALIZATION_ON_SERIALIZE`  
Por omisión, la serialización de un objeto perezoso desencadena su inicialización. Definir este flag evita la inicialización, permitiendo que los objetos perezosos sean serializados sin ser inicializados.

## Valores devueltos

Devolver una instancia fantasma perezosa. Si el objeto no tiene propiedades, o si todas sus propiedades son estáticas o virtuales, se devuelve una instancia normal (no perezosa). Ver también [Ciclo de vida de los objetos perezosos](#language.oop5.lazy-objects.lifecycle).

## Errores/Excepciones

Una `ReflectionException` si la clase es interna o extiende una clase interna, excepto `stdClass`.

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
$object = $reflector->newLazyGhost(function (Example $object) {
     $object->__construct(1);
});

var_dump($object);
var_dump($object instanceof Example);

// Desencadena la inicialización, y obtiene la propiedad después de esto
var_dump($object->prop);

?>

   
```

El ejemplo anterior mostrará:

    lazy ghost object(Example)#3 (0) {
      ["prop"]=>
      uninitialized(int)
    }
    bool(true)
    Example::__construct
    int(1)

## Véase también

Objetos perezosos

ReflectionClass::newLazyProxy

ReflectionClass::newInstanceWithoutConstructor

ReflectionClass::resetAsLazyGhost

ReflectionClass::markLazyObjectAsInitialized

ReflectionClass::initializeLazyObject

ReflectionClass::isUninitializedLazyObject

ReflectionProperty::setRawValueWithoutLazyInitialization

ReflectionProperty::skipLazyInitialization

ReflectionProperty::isLazy
