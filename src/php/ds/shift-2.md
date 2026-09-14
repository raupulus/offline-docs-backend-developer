---
title: Ds\Sequence::shift
description: Elimina y devuelve el primer valor
source_url: https://www.php.net/manual/es/ds-sequence.shift.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/shift.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15700
---

Ds\Sequence::shift

Elimina y devuelve el primer valor

## Descripción

```php
abstract public Ds\Sequence::shift(): mixed
```php

Elimina y devuelve el primer valor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El primer valor, que ha sido eliminado.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\Sequence::shift`

```
<?php
$sequence = new \Ds\Vector(["a", "b", "c"]);

var_dump($sequence->shift());
var_dump($sequence->shift());
var_dump($sequence->shift());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "a"
    string(1) "b"
    string(1) "c"
