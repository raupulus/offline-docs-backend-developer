---
title: Ds\Deque::last
description: Devuelve el último valor
source_url: https://www.php.net/manual/es/ds-deque.last.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/last.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14610
---

Ds\Deque::last

Devuelve el último valor

## Descripción

```php
public Ds\Deque::last(): mixed
```php

Devuelve el último valor del deque.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El último valor del deque.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\Deque::last`

```
<?php
$deque = new \Ds\Deque([1, 2, 3]);
var_dump($deque->last());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(3)
