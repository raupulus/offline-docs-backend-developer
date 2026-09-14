---
title: ReflectionClass::isAnonymous
description: Verifica si la clase es anónima
source_url: https://www.php.net/manual/es/reflectionclass.isanonymous.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/isanonymous.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_revision: 84f256090
order: 69440
---

ReflectionClass::isAnonymous

Verifica si la clase es anónima

## Descripción

```php
public ReflectionClass::isAnonymous(): bool
```php

Verifica si una clase es una clase anónima.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna `true` si la clase es anónima o `false` en caso contrario.

## Ejemplos

Ejemplo con ReflectionClass::isAnonymous

```
<?php
class TestClass {}
$anonClass = new class {};

$normalClass = new ReflectionClass('TestClass');
$anonClass  = new ReflectionClass($anonClass);

var_dump($normalClass->isAnonymous());
var_dump($anonClass->isAnonymous());

?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

ReflectionClass::isFinal
