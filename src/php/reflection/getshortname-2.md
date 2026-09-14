---
title: ReflectionConstant::getShortName
description: Devuelve el nombre corto
source_url: https://www.php.net/manual/es/reflectionconstant.getshortname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionconstant/getshortname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c477749c8
order: 69950
---

ReflectionConstant::getShortName

Devuelve el nombre corto

## Descripción

```php
public ReflectionConstant::getShortName(): string
```php

Devuelve el nombre corto de la constante, la parte sin el espacio de nombres.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nombre corto de la constante.

## Ejemplos

Ejemplo de ReflectionConstant::getShortName

```
<?php
namespace Foo;

const BAR = 'bar';

echo (new \ReflectionConstant('Foo\BAR'))->getName();
?>

   
```php

El ejemplo anterior mostrará:

    BAR

## Véase también

ReflectionConstant::getName
