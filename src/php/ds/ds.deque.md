---
title: La clase Deque
source_url: https://www.php.net/manual/es/class.ds-deque.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds.deque.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_revision: 4d17b7b49
order: 16530
---

## Introducción

Un Deque (pronunciado “deck”) es una secuencia de valores en un búfer contiguo que crece y se contrae automáticamente. El nombre es una abreviación inglesa común de “double-ended queue” (cola de doble final) y es usado internamente por `Ds\Queue`.

Dos punteros son usados para mantener el seguimiento de una cabecera y una cola. Los punteros pueden “envolver alrededor” el final del búfer, lo cual evita la necesidad de mover otros valores alrededor para hacer un espacio. Esto permite que hacer cambios y deshacer cambios sean muy rápidos —  algo en que `Ds\Vector` no puede competir.

Accediendo a un valor por el índice requiere una traducción entre el índice y su posición correspondiente en el búfer: `((cabecera + posición) % capacidad)`.

## Fortalezas

Soporta la sintaxis array (corchetes)., Utiliza menos memoria total que un `array` para el mismo número de valores., Automáticamente libera la memoria asignada cuando su tamaño cae lo suficientemente bajo., `get`, `set`, `push`, `pop`, `shift`, y `unshift` son todos O(1).

## Debilidades

La capacidad debe ser una potencia de 2., `insert` y `remove` son O(n).

## Sinopsis de la clase

Ds\Deque

Ds\Deque

Ds\Sequence

ArrayAccess

Constantes

const

int

Ds\Deque::MIN_CAPACITY

8

Métodos

## Constantes predefinidas

`Ds\Deque::MIN_CAPACITY`  

## Historial de cambios

| Versión       | Descripción                              |
|---------------|------------------------------------------|
| PECL ds 1.3.0 | La clase ahora implementa `ArrayAccess`. |
