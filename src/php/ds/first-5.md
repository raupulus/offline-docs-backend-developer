---
title: Ds\Vector::first
description: Devuelve el primer valor en el vector
source_url: https://www.php.net/manual/es/ds-vector.first.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/first.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16280
---

Ds\Vector::first

Devuelve el primer valor en el vector

## Descripción

```php
public Ds\Vector::first(): mixed
```php

Devuelve el primer valor en el vector.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El primer valor en el vector.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\Vector::first`

```
<?php
$vector = new \Ds\Vector([1, 2, 3]);
var_dump($vector->first());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(1)
