---
title: ReflectionClass::isUninitializedLazyObject
description: Verifica si un objeto es perezoso y no inicializado
source_url: https://www.php.net/manual/es/reflectionclass.isuninitializedlazyobject.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/isuninitializedlazyobject.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c0fa5077c
order: 69570
---

ReflectionClass::isUninitializedLazyObject

Verifica si un objeto es perezoso y no inicializado

## Descripción

```php
public ReflectionClass::isUninitializedLazyObject(object $object): bool
```php

Verifica si un objeto es perezoso y no inicializado.

## Parámetros

`object`  
El objeto a verificar.

## Valores devueltos

Devuelve `true` si `object` es un objeto perezoso y no inicializado y `false` en caso contrario.

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

var_dump($reflector->isUninitializedLazyObject($object));

var_dump($object->prop);

var_dump($reflector->isUninitializedLazyObject($object));
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
    Initializer called
    int(1)
    bool(false)

## Véase también

Objetos perezosos

ReflectionClass::newLazyGhost

ReflectionClass::markLazyObjectAsInitialized

ReflectionClass::initializeLazyObject
