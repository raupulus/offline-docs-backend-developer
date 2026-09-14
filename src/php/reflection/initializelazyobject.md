---
title: ReflectionClass::initializeLazyObject
description: Forzar la inicialización de un objeto perezoso
source_url: https://www.php.net/manual/es/reflectionclass.initializelazyobject.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/initializelazyobject.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c0fa5077c
order: 69410
---

ReflectionClass::initializeLazyObject

Forzar la inicialización de un objeto perezoso

## Descripción

```php
public ReflectionClass::initializeLazyObject(object $object): object
```php

Forzar la inicialización del `object` especificado. Este método no tiene ningún efecto si el objeto no es perezoso o ya ha sido inicializado. De lo contrario, la inicialización se realiza como se describe en la [Secuencia de inicialización](#language.oop5.lazy-objects.initialization-sequence).

> [!NOTE]
> En la mayoría de los casos, llamar a este método es innecesario, ya que los objetos perezosos se inicializan automáticamente cuando son observados o modificados.

## Parámetros

`object`  
El objeto a inicializar.

## Valores devueltos

Si `object` es un proxy perezoso, devuelve su instancia real. De lo contrario, devuelve `object` mismo.

## Ejemplos

Uso básico

```
<?php
class Example
{
    public function __construct(public int $prop) {
    }
}

$reflector = new ReflectionClass(Example::class);

$object = $reflector->newLazyGhost(function ($object) {
    echo "Initializer called\n";
    $object->__construct(1);
});

var_dump($object);

$reflector->initializeLazyObject($object);

var_dump($object);
?>

   
```php

El ejemplo anterior mostrará:

    lazy ghost object(Example)#3 (0) {
      ["prop"]=>
      uninitialized(int)
    }
    Initializer called
    object(Example)#3 (1) {
      ["prop"]=>
      int(1)
    }

## Véase también

Objetos perezosos

ReflectionClass::newLazyGhost

ReflectionClass::markLazyObjectAsInitialized

ReflectionClass::isUninitializedLazyObject
