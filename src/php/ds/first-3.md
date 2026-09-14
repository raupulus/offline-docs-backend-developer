---
title: Ds\Sequence::first
description: Devuelve el primer valor de la secuencia
source_url: https://www.php.net/manual/es/ds-sequence.first.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/first.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15550
---

Ds\Sequence::first

Devuelve el primer valor de la secuencia

## Descripción

```php
abstract public Ds\Sequence::first(): mixed
```php

Devuelve el primer valor de la secuencia.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el primer valor de la secuencia.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\Sequence::first`

```
<?php
$sequence = new \Ds\Vector([1, 2, 3]);
var_dump($sequence->first());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(1)
