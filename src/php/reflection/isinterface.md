---
title: ReflectionClass::isInterface
description: Verifica si una clase es una interfaz
source_url: https://www.php.net/manual/es/reflectionclass.isinterface.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/isinterface.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: 84f256090
order: 69500
---

ReflectionClass::isInterface

Verifica si una clase es una interfaz

## Descripción

```php
public ReflectionClass::isInterface(): bool
```php

Verifica si una clase es una interfaz.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna `true` si la clase es una \*\*interfaz\*\* o `false` en caso contrario.

## Ejemplos

Ejemplo con ReflectionClass::isInterface

```
<?php
interface SomeInterface {
    public function interfaceMethod();
}

$class = new ReflectionClass('SomeInterface');
var_dump($class->isInterface());
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

ReflectionClass::isInstance
