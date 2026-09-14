---
title: SplDoublyLinkedList::setIteratorMode
description: Establece el modo de iteración
source_url: https://www.php.net/manual/es/spldoublylinkedlist.setiteratormode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/spldoublylinkedlist/setiteratormode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: e5202c6e4
order: 83940
---

SplDoublyLinkedList::setIteratorMode

Establece el modo de iteración

## Descripción

```php
public SplDoublyLinkedList::setIteratorMode(int $mode): int
```php

## Parámetros

`mode`  
Hay dos conjuntos ortogonales de los modos que se pueden establecer:

- La dirección de la iteración (ya sea uno o el otro):

  - `SplDoublyLinkedList::IT_MODE_LIFO` (Estilo de pila)

  - `SplDoublyLinkedList::IT_MODE_FIFO` (Estilo de cola)

- El comportamiento del iterador (ya sea uno o el otro):

  - `SplDoublyLinkedList::IT_MODE_DELETE` (Los elementos son eliminados por el iterador)

  - `SplDoublyLinkedList::IT_MODE_KEEP` (Los elementos son recorridos por el iterador)

El modo predeterminado es: `SplDoublyLinkedList::IT_MODE_FIFO` \| `SplDoublyLinkedList::IT_MODE_KEEP`

> [!WARNING]
> La dirección de iteración no se puede cambiar para las clases `SplStack` y `SplQueue`, siempre es `SplDoublyLinkedList::IT_MODE_FIFO`. Si se intenta modificar, se producirá una `RuntimeException`.

## Valores devueltos

Devuelve los diferentes modos y banderas que afectan a la iteración.
