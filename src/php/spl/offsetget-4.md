---
title: SplDoublyLinkedList::offsetGet
description: Devuelve el valor del índice específicado
source_url: https://www.php.net/manual/es/spldoublylinkedlist.offsetget.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/spldoublylinkedlist/offsetget.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 83860
---

SplDoublyLinkedList::offsetGet

Devuelve el valor del índice específicado

## Descripción

```php
public SplDoublyLinkedList::offsetGet(int $index): mixed
```php

## Parámetros

`index`  
El índice con el valor.

## Valores devueltos

El valor específicado en `index`.

## Errores/Excepciones

Lanza una `OutOfRangeException` cuando `index` está fuera de los límites o cuando `index` no se puede analizar como un entero.
