---
title: Ds\Deque::pop
description: Elimina y devuelve el último valor
source_url: https://www.php.net/manual/es/ds-deque.pop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/pop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14640
---

Ds\Deque::pop

Elimina y devuelve el último valor

## Descripción

```php
public Ds\Deque::pop(): mixed
```php

Elimina y devuelve el último valor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El último valor eliminado.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\Deque::pop`

```
<?php
$deque = new \Ds\Deque([1, 2, 3]);

var_dump($deque->pop());
var_dump($deque->pop());
var_dump($deque->pop());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(3)
    int(2)
    int(1)
