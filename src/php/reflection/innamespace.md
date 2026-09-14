---
title: ReflectionClass::inNamespace
description: Verifica si una clase está definida en un espacio de nombres
source_url: https://www.php.net/manual/es/reflectionclass.innamespace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/innamespace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_revision: 84f256090
order: 69420
---

ReflectionClass::inNamespace

Verifica si una clase está definida en un espacio de nombres

## Descripción

```php
public ReflectionClass::inNamespace(): bool
```php

Verifica si una clase está definida en un espacio de nombres.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna `true` si la clase está en el espacio de nombres especificado o `false` en caso contrario.

## Ejemplos

Ejemplo con ReflectionClass::inNamespace

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

ReflectionClass::getNamespaceName, [Los espacios de nombres PHP](#language.namespaces)
