---
title: Ds\Deque::first
description: Devuelve el primer valor de la deque
source_url: https://www.php.net/manual/es/ds-deque.first.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/first.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14550
---

Ds\Deque::first

Devuelve el primer valor de la deque

## Descripción

```php
public Ds\Deque::first(): mixed
```php

Devuelve el primer valor de la deque.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el primer valor de la deque.

## Errores/Excepciones

`UnderflowException` si está vacía.

## Ejemplos

Ejemplo de `Ds\Deque::first`

```
<?php
$deque = new \Ds\Deque([1, 2, 3]);
var_dump($deque->first());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(1)
