---
title: ReflectionClass::getInterfaceNames
description: Obtiene los nombres de las interfaces
source_url: https://www.php.net/manual/es/reflectionclass.getinterfacenames.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getinterfacenames.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69170
---

ReflectionClass::getInterfaceNames

Obtiene los nombres de las interfaces

## Descripción

```php
public ReflectionClass::getInterfaceNames(): array
```php

Obtiene los nombres de las interfaces.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array numérico cuyos valores son los nombres de las interfaces.

## Ejemplos

Ejemplo con ReflectionClass::getInterfaceNames

```
<?php
interface Foo { }

interface Bar { }

class Baz implements Foo, Bar { }

$rc1 = new ReflectionClass("Baz");

print_r($rc1->getInterfaceNames());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Foo
        [1] => Bar
    )

## Véase también

ReflectionClass::getInterfaces
