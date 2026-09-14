---
title: Ds\Vector::join
description: Reúne todos los valores en un string
source_url: https://www.php.net/manual/es/ds-vector.join.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/join.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: df78bd1d2
order: 16320
---

Ds\Vector::join

Reúne todos los valores en un string

## Descripción

```php
public Ds\Vector::join([string $glue]): string
```php

Reúne todos los valores en un string utilizando un separador opcional entre cada valor.

## Parámetros

`glue`  
Un string opcional para separar cada valor.

## Valores devueltos

Todos los valores de la secuencia reunidos en un string.

## Ejemplos

Ejemplo de `Ds\Vector::join` con un string separador

```
<?php
$vector = new \Ds\Vector(["a", "b", "c", 1, 2, 3]);

var_dump($vector->join("|"));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(11) "a|b|c|1|2|3"

Ejemplo de `Ds\Vector::join` sin string separador

```
<?php
$vector = new \Ds\Vector(["a", "b", "c", 1, 2, 3]);

var_dump($vector->join());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(6) "abc123"
