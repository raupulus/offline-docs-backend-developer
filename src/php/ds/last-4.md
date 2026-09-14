---
title: Ds\Set::last
description: Devuelve el último valor de la secuencia
source_url: https://www.php.net/manual/es/ds-set.last.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/last.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 11e991f71
order: 15920
---

Ds\Set::last

Devuelve el último valor de la secuencia

## Descripción

```php
public Ds\Set::last(): mixed
```php

Devuelve el último valor de la secuencia.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El último valor de la secuencia.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\Set::last`

```
<?php
$set = new \Ds\Set([1, 2, 3]);
var_dump($set->last());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(3)
