---
title: SplDoublyLinkedList::offsetUnset
description: Borra el valor de el índice específicado
source_url: https://www.php.net/manual/es/spldoublylinkedlist.offsetunset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/spldoublylinkedlist/offsetunset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 83880
---

SplDoublyLinkedList::offsetUnset

Borra el valor de el índice específicado

## Descripción

```php
public SplDoublyLinkedList::offsetUnset(int $index): void
```php

Borra el valor del índice específicado.

## Parámetros

`index`  
El índice a borrar.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una `OutOfRangeException` cuando `index` está fuera de los límites o cuando `index` no se puede analizar como un entero.
