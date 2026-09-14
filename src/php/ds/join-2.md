---
title: Ds\Sequence::join
description: Reúne todos los valores en un string
source_url: https://www.php.net/manual/es/ds-sequence.join.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/join.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15580
---

Ds\Sequence::join

Reúne todos los valores en un string

## Descripción

```php
abstract public Ds\Sequence::join([string $glue]): string
```php

Reúne todos los valores en un string utilizando un separador opcional entre cada valor.

## Parámetros

`glue`  
Un string opcional para separar cada valor.

## Valores devueltos

Todos los valores de la secuencia reunidos en un string.

## Ejemplos

Ejemplo de `Ds\Sequence::join` con un string separador

```
<?php
$sequence = new \Ds\Vector(["a", "b", "c", 1, 2, 3]);

var_dump($sequence->join("|"));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(11) "a|b|c|1|2|3"

Ejemplo de `Ds\Sequence::join` sin string separador

```
<?php
$sequence = new \Ds\Vector(["a", "b", "c", 1, 2, 3]);

var_dump($sequence->join());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(11) "abc123"
