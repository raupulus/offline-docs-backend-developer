---
title: ReflectionClass::isInstance
description: Verifica si una clase es una instancia de otra clase
source_url: https://www.php.net/manual/es/reflectionclass.isinstance.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/isinstance.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_revision: eb557099e
order: 69480
---

ReflectionClass::isInstance

Verifica si una clase es una instancia de otra clase

## Descripción

```php
public ReflectionClass::isInstance(object $object): bool
```php

Verifica si una clase es una instancia de otra clase.

## Parámetros

`object`  
El objeto utilizado para la comparación.

## Valores devueltos

Retorna `true` si el objeto es una instancia de la clase, o `false` en caso contrario.

## Ejemplos

Ejemplo con ReflectionClass::isInstance

```
<?php

class Foo {}

$object = new Foo();

$reflection = new ReflectionClass('Foo');

if ($reflection->isInstance($object)) {
    echo "Sí\n";
}

// Equivalente a
if ($object instanceof Foo) {
    echo "Sí\n";
}

// Equivalente a
if (is_a($object, 'Foo')) {
    echo "Sí";
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Sí
    Sí
    Sí

## Véase también

ReflectionClass::isInterface, [Operadores de tipos (instanceof)](#language.operators.type), [Las interfaces](#language.oop5.interfaces), `is_a`
