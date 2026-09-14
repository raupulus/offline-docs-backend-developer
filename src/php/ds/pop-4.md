---
title: Ds\Sequence::pop
description: Elimina y devuelve el último valor
source_url: https://www.php.net/manual/es/ds-sequence.pop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/pop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15620
---

Ds\Sequence::pop

Elimina y devuelve el último valor

## Descripción

```php
abstract public Ds\Sequence::pop(): mixed
```php

Elimina y devuelve el último valor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El último valor eliminado.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\Sequence::pop`

```
<?php
$sequence = new \Ds\Vector([1, 2, 3]);

var_dump($sequence->pop());
var_dump($sequence->pop());
var_dump($sequence->pop());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(3)
    int(2)
    int(1)
