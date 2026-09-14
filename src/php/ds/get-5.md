---
title: Ds\Vector::get
description: Devuelve el valor en un índice dado
source_url: https://www.php.net/manual/es/ds-vector.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16290
---

Ds\Vector::get

Devuelve el valor en un índice dado

## Descripción

```php
public Ds\Vector::get(int $index): mixed
```php

Devuelve el valor en un índice dado.

## Parámetros

`index`  
El índice al que se accede, comenzando en 0.

## Valores devueltos

El valor en el índice solicitado.

## Errores/Excepciones

`OutOfRangeException` si el índice no es válido.

## Ejemplos

Ejemplo de `Ds\Vector::get`

```
<?php
$vector = new \Ds\Vector(["a", "b", "c"]);

var_dump($vector->get(0));
var_dump($vector->get(1));
var_dump($vector->get(2));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "a"
    string(1) "b"
    string(1) "c"

Ejemplo de `Ds\Vector::get` utilizando la sintaxis de array

```
<?php
$vector = new \Ds\Vector(["a", "b", "c"]);

var_dump($vector[0]);
var_dump($vector[1]);
var_dump($vector[2]);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "a"
    string(1) "b"
    string(1) "c"
