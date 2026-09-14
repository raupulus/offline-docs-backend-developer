---
title: Ds\Vector::shift
description: Elimina y devuelve el primer valor
source_url: https://www.php.net/manual/es/ds-vector.shift.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/shift.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16450
---

Ds\Vector::shift

Elimina y devuelve el primer valor

## Descripción

```php
public Ds\Vector::shift(): mixed
```php

Elimina y devuelve el primer valor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El primer valor, que ha sido eliminado.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\Vector::shift`

```
<?php
$vector = new \Ds\Vector(["a", "b", "c"]);

var_dump($vector->shift());
var_dump($vector->shift());
var_dump($vector->shift());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "a"
    string(1) "b"
    string(1) "c"
