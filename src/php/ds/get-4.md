---
title: Ds\Set::get
description: Devuelve el valor en un índice dado
source_url: https://www.php.net/manual/es/ds-set.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15870
---

Ds\Set::get

Devuelve el valor en un índice dado

## Descripción

```php
public Ds\Set::get(int $index): mixed
```php

Devuelve el valor en un índice dado.

## Parámetros

`index`  
El índice al que se accede, comenzando en 0.

## Valores devueltos

El valor en el índice solicitado.

## Errores/Excepciones

`OutOfRangeException` si el índice es inválido.

## Ejemplos

Ejemplo de `Ds\Set::get`

```
<?php
$set = new \Ds\Set(["a", "b", "c"]);

var_dump($set->get(0));
var_dump($set->get(1));
var_dump($set->get(2));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "a"
    string(1) "b"
    string(1) "c"

Ejemplo de `Ds\Set::get` utilizando la sintaxis de array

```
<?php
$set = new \Ds\Set(["a", "b", "c"]);

var_dump($set[0]);
var_dump($set[1]);
var_dump($set[2]);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "a"
    string(1) "b"
    string(1) "c"
