---
title: ReflectionClass::isAbstract
description: Verifica si una clase es abstracta
source_url: https://www.php.net/manual/es/reflectionclass.isabstract.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/isabstract.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_revision: 84f256090
order: 69430
---

ReflectionClass::isAbstract

Verifica si una clase es abstracta

## Descripción

```php
public ReflectionClass::isAbstract(): bool
```php

Verifica si una clase es abstracta.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna `true` si la clase es abstracta o `false` en caso contrario.

## Ejemplos

Ejemplo con ReflectionClass::isAbstract

```
<?php
class          TestClass { }
abstract class TestAbstractClass { }

$testClass     = new ReflectionClass('TestClass');
$abstractClass = new ReflectionClass('TestAbstractClass');

var_dump($testClass->isAbstract());
var_dump($abstractClass->isAbstract());
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

ReflectionClass::isInterface, [La abstracción de clase](#language.oop5.abstract)
