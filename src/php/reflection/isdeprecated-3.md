---
title: ReflectionFunctionAbstract::isDeprecated
description: Verifica si la función es obsoleta
source_url: https://www.php.net/manual/es/reflectionfunctionabstract.isdeprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunctionabstract/isdeprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: e890e4a7f
order: 70720
---

ReflectionFunctionAbstract::isDeprecated

Verifica si la función es obsoleta

## Descripción

```php
public ReflectionFunctionAbstract::isDeprecated(): bool
```php

Verifica si la función es obsoleta.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si la función es obsoleta, `false` en caso contrario.

## Ejemplos

Ejemplo con ReflectionFunctionAbstract::isDeprecated

```
<?php
$rf = new ReflectionFunction('ereg');
var_dump($rf->isDeprecated());
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

`Deprecated`, ReflectionFunctionAbstract::getDocComment
