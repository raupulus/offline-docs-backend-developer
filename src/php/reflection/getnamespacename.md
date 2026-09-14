---
title: ReflectionClass::getNamespaceName
description: Obtiene el espacio de nombres
source_url: https://www.php.net/manual/es/reflectionclass.getnamespacename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getnamespacename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 69240
---

ReflectionClass::getNamespaceName

Obtiene el espacio de nombres

## Descripción

```php
public ReflectionClass::getNamespaceName(): string
```php

Obtiene el espacio de nombres.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El espacio de nombres.

## Ejemplos

Ejemplo con ReflectionClass::getNamespaceName

```
<?php
namespace A\B;

class Foo { }

$class = new \ReflectionClass('stdClass');

var_dump($class->inNamespace());
var_dump($class->getName());
var_dump($class->getNamespaceName());
var_dump($class->getShortName());

$class = new \ReflectionClass('A\\B\\Foo');

var_dump($class->inNamespace());
var_dump($class->getName());
var_dump($class->getNamespaceName());
var_dump($class->getShortName());
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    string(8) "stdClass"
    string(0) ""
    string(8) "stdClass"

    bool(true)
    string(7) "A\B\Foo"
    string(3) "A\B"
    string(3) "Foo"

## Véase también

ReflectionClass::getParentClass, [Los espacios de nombres](#language.namespaces)
