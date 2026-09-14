---
title: ReflectionConstant::getValue
description: Devuelve el valor
source_url: https://www.php.net/manual/es/reflectionconstant.getvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionconstant/getvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c477749c8
order: 69960
---

ReflectionConstant::getValue

Devuelve el valor

## Descripción

```php
public ReflectionConstant::getValue(): mixed
```php

Devuelve el valor de la constante.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor de la constante.

## Ejemplos

Ejemplo de ReflectionProperty::getValue

```
<?php
const FOO = 'foo';

var_dump((new \ReflectionConstant('FOO'))->getValue());
?>

   
```php

El ejemplo anterior mostrará:

    string(3) "foo"
