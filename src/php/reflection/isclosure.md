---
title: ReflectionFunctionAbstract::isClosure
description: Verifica si es una función anónima
source_url: https://www.php.net/manual/es/reflectionfunctionabstract.isclosure.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunctionabstract/isclosure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 70710
---

ReflectionFunctionAbstract::isClosure

Verifica si es una función anónima

## Descripción

```php
public ReflectionFunctionAbstract::isClosure(): bool
```php

Verifica si la función reflejada es una `Closure`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna `true` si la función es una `Closure`, de lo contrario `false`

## Ejemplos

Ejemplo de ReflectionFunctionAbstract::isClosure

```
<?php
// No es una función anónima
$function1 = 'str_replace';
$reflection1 = new ReflectionFunction($function1);
var_dump($reflection1->isClosure());

// Función anónima
$function2 = function () {};
$reflection2 = new ReflectionFunction($function2);
var_dump($reflection2->isClosure());
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

ReflectionFunctionAbstract::isGenerator
