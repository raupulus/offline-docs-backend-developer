---
title: ReflectionClass::isFinal
description: Verifica si una clase es final
source_url: https://www.php.net/manual/es/reflectionclass.isfinal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/isfinal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_revision: 84f256090
order: 69470
---

ReflectionClass::isFinal

Verifica si una clase es final

## Descripción

```php
public ReflectionClass::isFinal(): bool
```php

Verifica si una clase es final.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna `true` si la clase es final o `false` en caso contrario.

## Ejemplos

Ejemplo con ReflectionClass::isFinal

```
<?php
class       TestClass { }
final class TestFinalClass { }

$normalClass = new ReflectionClass('TestClass');
$finalClass  = new ReflectionClass('TestFinalClass');

var_dump($normalClass->isFinal());
var_dump($finalClass->isFinal());

?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

ReflectionClass::isAbstract, [Palabra clave Final](#language.oop5.final)
