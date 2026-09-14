---
title: SplDoublyLinkedList::add
description: Añadir/insertar un nuevo valor en el índice especificado
source_url: https://www.php.net/manual/es/spldoublylinkedlist.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/spldoublylinkedlist/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 83770
---

SplDoublyLinkedList::add

Añadir/insertar un nuevo valor en el índice especificado

## Descripción

```php
public SplDoublyLinkedList::add(int $index, mixed $value): void
```php

Inserta el valor dado por `value` en el índice especificado por `index`, reorganizando el valor anterior a ese índice (y todos los valores subsiguientes) a través de la lista.

## Parámetros

`index`  
El índice donde insertar el nuevo valor.

`value`  
El nuevo valor para `index`.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una `OutOfRangeException` cuando `index` está fuera de los límites o cuando `index` no puede ser analizado como un integer.
