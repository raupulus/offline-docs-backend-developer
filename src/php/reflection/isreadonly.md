---
title: ReflectionClass::isReadOnly
description: Verifica si una clase es de solo lectura
source_url: https://www.php.net/manual/es/reflectionclass.isreadonly.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/isreadonly.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 7f6236d76
order: 69540
---

ReflectionClass::isReadOnly

Verifica si una clase es de solo lectura

## Descripción

```php
public ReflectionClass::isReadOnly(): bool
```php

Verifica si una clase es de [solo lectura](#language.oop5.basic.class.readonly).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si la clase es de solo lectura, de lo contrario `false`.

## Ejemplos

Ejemplo con ReflectionClass::isReadOnly

```
<?php
class TestClass { }
readonly class TestReadOnlyClass { }

$normalClass = new ReflectionClass('TestClass');
$readonlyClass = new ReflectionClass('TestReadOnlyClass');

var_dump($normalClass->isReadOnly());
var_dump($readonlyClass->isReadOnly());

?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

ReflectionClass::isAbstract, [Clase de solo lectura](#language.oop5.basic.class.readonly)
