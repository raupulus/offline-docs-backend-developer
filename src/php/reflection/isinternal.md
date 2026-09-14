---
title: ReflectionClass::isInternal
description: Verifica si una clase está definida como interna por una extensión
source_url: https://www.php.net/manual/es/reflectionclass.isinternal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/isinternal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_revision: 84f256090
order: 69510
---

ReflectionClass::isInternal

Verifica si una clase está definida como interna por una extensión

## Descripción

```php
public ReflectionClass::isInternal(): bool
```php

Verifica si una clase está definida como interna por una extensión, o forma parte del núcleo, en oposición a una clase definida por el usuario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna `true` si la clase está definida internamente por una extensión o el núcleo (core), o `false` en caso contrario.

## Ejemplos

Ejemplo con ReflectionClass::isInternal

```
<?php
$internalclass = new ReflectionClass('ReflectionClass');

class Apple {}
$userclass = new ReflectionClass('Apple');

var_dump($internalclass->isInternal());
var_dump($userclass->isInternal());
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

## Véase también

ReflectionClass::isUserDefined
