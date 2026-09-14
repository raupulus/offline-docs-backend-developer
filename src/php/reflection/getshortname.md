---
title: ReflectionClass::getShortName
description: Obtiene el nombre corto de una clase
source_url: https://www.php.net/manual/es/reflectionclass.getshortname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getshortname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 69300
---

ReflectionClass::getShortName

Obtiene el nombre corto de una clase

## Descripción

```php
public ReflectionClass::getShortName(): string
```php

Obtiene el nombre corto de una clase, es decir, la parte sin el espacio de nombres.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nombre corto de la clase.

## Ejemplos

Ejemplo con ReflectionClass::getShortName

```
<?php
namespace A\B;

class Foo { }

$function = new \ReflectionClass('stdClass');

var_dump($function->inNamespace());
var_dump($function->getName());
var_dump($function->getNamespaceName());
var_dump($function->getShortName());

$function = new \ReflectionClass('A\\B\\Foo');

var_dump($function->inNamespace());
var_dump($function->getName());
var_dump($function->getNamespaceName());
var_dump($function->getShortName());
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

ReflectionClass::getName
