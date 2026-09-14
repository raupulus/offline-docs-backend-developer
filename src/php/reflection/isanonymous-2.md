---
title: ReflectionFunction::isAnonymous
description: Verifica si la función es anónima
source_url: https://www.php.net/manual/es/reflectionfunction.isanonymous.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunction/isanonymous.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70430
---

ReflectionFunction::isAnonymous

Verifica si la función es anónima

## Descripción

```php
public ReflectionFunction::isAnonymous(): bool
```php

Verifica si la función es [anónima](#functions.anonymous).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la función es anónima, de lo contrario `false`.

## Ejemplos

Ejemplo de ReflectionFunction::isAnonymous

```
<?php

$rf = new ReflectionFunction(function() {});
var_dump($rf->isAnonymous());

$rf = new ReflectionFunction('strlen');
var_dump($rf->isAnonymous());
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

## Véase también

[Funciones anónimas](#functions.anonymous)
