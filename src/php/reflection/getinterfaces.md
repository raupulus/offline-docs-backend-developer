---
title: ReflectionClass::getInterfaces
description: Obtiene las interfaces
source_url: https://www.php.net/manual/es/reflectionclass.getinterfaces.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getinterfaces.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69180
---

ReflectionClass::getInterfaces

Obtiene las interfaces

## Descripción

```php
public ReflectionClass::getInterfaces(): array
```php

Obtiene las interfaces.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` asociativo que contiene las interfaces, donde las claves son los nombres de las interfaces y los valores los objetos `ReflectionClass`.

## Ejemplos

\>Ejemplo con ReflectionClass::getInterfaces

```
<?php
interface Foo { }

interface Bar { }

class Baz implements Foo, Bar { }

$rc1 = new ReflectionClass("Baz");

print_r($rc1->getInterfaces());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [Foo] => ReflectionClass Object
            (
                [name] => Foo
            )

        [Bar] => ReflectionClass Object
            (
                [name] => Bar
            )

    )

## Véase también

ReflectionClass::getInterfaceNames
