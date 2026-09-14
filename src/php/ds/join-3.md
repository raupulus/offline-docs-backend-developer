---
title: Ds\Set::join
description: Reúne todos los valores en un string
source_url: https://www.php.net/manual/es/ds-set.join.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/join.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15900
---

Ds\Set::join

Reúne todos los valores en un string

## Descripción

```php
public Ds\Set::join([string $glue]): string
```php

Reúne todos los valores en un string utilizando un separador opcional entre cada valor.

## Parámetros

`glue`  
Un string opcional para separar cada valor.

## Valores devueltos

Todos los valores del conjunto reunidos en un string.

## Ejemplos

Ejemplo de `Ds\Set::join` con un string separador

```
<?php
$set = new \Ds\Set(["a", "b", "c", 1, 2, 3]);

var_dump($set->join("|"));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(11) "a|b|c|1|2|3"

Ejemplo de `Ds\Set::join` sin un string separador

```
<?php
$set = new \Ds\Set(["a", "b", "c", 1, 2, 3]);

var_dump($set->join());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(11) "abc123"
