---
title: ReflectionReference::getId
description: Devuelve un ID único de una referencia
source_url: https://www.php.net/manual/es/reflectionreference.getid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionreference/getid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 71860
---

ReflectionReference::getId

Devuelve un ID único de una referencia

## Descripción

```php
public ReflectionReference::getId(): string
```php

Devuelve un ID que es único para la referencia durante la vida útil de esta referencia. Este ID puede ser utilizado para comparar referencias por igualdad, o para mantener un mapa de referencias conocidas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `string` de formato no especificado.

## Ejemplos

Uso básico de ReflectionReference::getId

```
<?php
$val1 = 'foo';
$val2 = 'bar';
$arr = [&$val1, &$val2, &$val1];

$rr1 = ReflectionReference::fromArrayElement($arr, 0);
$rr2 = ReflectionReference::fromArrayElement($arr, 1);
$rr3 = ReflectionReference::fromArrayElement($arr, 2);

var_dump($rr1->getId() === $rr2->getId());
var_dump($rr1->getId() === $rr3->getId());
?>

   
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)
