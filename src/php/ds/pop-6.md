---
title: Ds\Vector::pop
description: Elimina y devuelve el último valor
source_url: https://www.php.net/manual/es/ds-vector.pop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/pop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16370
---

Ds\Vector::pop

Elimina y devuelve el último valor

## Descripción

```php
public Ds\Vector::pop(): mixed
```php

Elimina y devuelve el último valor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El último elemento eliminado.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\Vector::pop`

```
<?php
$vector = new \Ds\Vector([1, 2, 3]);

var_dump($vector->pop());
var_dump($vector->pop());
var_dump($vector->pop());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(3)
    int(2)
    int(1)
