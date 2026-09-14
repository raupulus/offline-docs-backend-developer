---
title: ReflectionConstant::getNamespaceName
description: Devuelve el nombre del espacio de nombres
source_url: https://www.php.net/manual/es/reflectionconstant.getnamespacename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionconstant/getnamespacename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c477749c8
order: 69940
---

ReflectionConstant::getNamespaceName

Devuelve el nombre del espacio de nombres

## Descripción

```php
public ReflectionConstant::getNamespaceName(): string
```php

Devuelve el nombre del espacio de nombres de la constante.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nombre del espacio de nombres, o una cadena vacía para el espacio de nombres global.

## Ejemplos

Ejemplo de ReflectionConstant::getNamespaceName

```
<?php
namespace Foo {
   const BAR = 'bar';
   var_dump((new \ReflectionConstant('Foo\BAR'))->getNamespaceName());
}

namespace {
   const BAR = 'bar';
   var_dump((new \ReflectionConstant('BAR'))->getNamespaceName());
}
?>

   
```php

El ejemplo anterior mostrará:

    string(3) "Foo"
    string(0) ""
