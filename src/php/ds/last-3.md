---
title: Ds\Sequence::last
description: Devuelve el último valor
source_url: https://www.php.net/manual/es/ds-sequence.last.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/last.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15590
---

Ds\Sequence::last

Devuelve el último valor

## Descripción

```php
abstract public Ds\Sequence::last(): mixed
```php

Devuelve el último valor de la secuencia.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El último valor de la secuencia.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\Sequence::last`

```
<?php
$sequence = new \Ds\Vector([1, 2, 3]);
var_dump($sequence->last());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(3)
