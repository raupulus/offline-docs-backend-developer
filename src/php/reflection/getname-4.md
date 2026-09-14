---
title: ReflectionConstant::getName
description: Devuelve el nombre
source_url: https://www.php.net/manual/es/reflectionconstant.getname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionconstant/getname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c477749c8
order: 69930
---

ReflectionConstant::getName

Devuelve el nombre

## Descripción

```php
public ReflectionConstant::getName(): string
```php

Devuelve el nombre de la constante.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nombre de la constante, que está compuesto por su espacio de nombres y su nombre.

## Ejemplos

Ejemplo de ReflectionConstant::getName

```
<?php
namespace Foo;

const BAR = 'bar';

echo (new \ReflectionConstant('Foo\BAR'))->getName();
?>

   
```php

El ejemplo anterior mostrará:

    Foo\BAR

## Véase también

ReflectionConstant::getNamespaceName
