---
title: SplDoublyLinkedList::offsetSet
description: Establece el valor del índice específicado
source_url: https://www.php.net/manual/es/spldoublylinkedlist.offsetset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/spldoublylinkedlist/offsetset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 83870
---

SplDoublyLinkedList::offsetSet

Establece el valor del índice específicado

## Descripción

```php
public SplDoublyLinkedList::offsetSet(int $index, mixed $value): void
```php

Establece el valor del índice dado por `index` al valor especificado por `value`.

## Parámetros

`index`  
El índice a establer. Si `null`, el siguiente valor se añadirá después del último elemento.

`value`  
El nuevo valor para `index`.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una `OutOfRangeException` cuando `index` está fuera de los límites o cuando `index` no se puede analizar como un entero.
