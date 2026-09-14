---
title: Ds\Sequence::get
description: Devuelve el valor en un índice dado
source_url: https://www.php.net/manual/es/ds-sequence.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15560
---

Ds\Sequence::get

Devuelve el valor en un índice dado

## Descripción

```php
abstract public Ds\Sequence::get(int $index): mixed
```php

Devuelve el valor en un índice dado.

## Parámetros

`index`  
El índice al que se desea acceder, comenzando en 0.

## Valores devueltos

El valor en el índice solicitado.

## Errores/Excepciones

`OutOfRangeException` si el índice no es válido.

## Ejemplos

Ejemplo de `Ds\Sequence::get`

```
<?php
$sequence = new \Ds\Vector(["a", "b", "c"]);

var_dump($sequence->get(0));
var_dump($sequence->get(1));
var_dump($sequence->get(2));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "a"
    string(1) "b"
    string(1) "c"

Ejemplo de `Ds\Sequence::get` utilizando la sintaxis de array

```
<?php
$sequence = new \Ds\Vector(["a", "b", "c"]);

var_dump($sequence[0]);
var_dump($sequence[1]);
var_dump($sequence[2]);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "a"
    string(1) "b"
    string(1) "c"
