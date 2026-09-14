---
title: Ds\Vector::last
description: Devuelve el último valor
source_url: https://www.php.net/manual/es/ds-vector.last.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/last.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16340
---

Ds\Vector::last

Devuelve el último valor

## Descripción

```php
public Ds\Vector::last(): mixed
```php

Devuelve el último valor en el vector.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El último valor en el vector.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\Vector::last`

```
<?php
$vector = new \Ds\Vector([1, 2, 3]);
var_dump($vector->last());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(3)
