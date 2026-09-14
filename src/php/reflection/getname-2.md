---
title: ReflectionClass::getName
description: Obtiene el nombre de la clase
source_url: https://www.php.net/manual/es/reflectionclass.getname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69230
---

ReflectionClass::getName

Obtiene el nombre de la clase

## Descripción

```php
public ReflectionClass::getName(): string
```php

Obtiene el nombre de la clase.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nombre de la clase.

## Ejemplos

Ejemplo con ReflectionClass::getName

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

ReflectionClass::getNamespaceName
