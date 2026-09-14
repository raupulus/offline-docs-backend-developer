---
title: La clase SplDoublyLinkedList
source_url: https://www.php.net/manual/es/class.spldoublylinkedlist.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/spldoublylinkedlist.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: 4d17b7b49
order: 84000
---

## Introducción

La clase SplDoublyLinkedList proporciona las principales funcionalidades de una lista doblemente enlazada.

## Sinopsis de la clase

SplDoublyLinkedList

implements

Iterator

Countable

ArrayAccess

Serializable

Constantes

public

const

int

SplDoublyLinkedList::IT_MODE_LIFO

public

const

int

SplDoublyLinkedList::IT_MODE_FIFO

public

const

int

SplDoublyLinkedList::IT_MODE_DELETE

public

const

int

SplDoublyLinkedList::IT_MODE_KEEP

Métodos

## Constantes predefinidas

## Dirección de Iteración

`SplDoublyLinkedList::IT_MODE_LIFO`  
La lista será iterada en un orden de última entrada, primera salida, como una pila.

`SplDoublyLinkedList::IT_MODE_FIFO`  
La lista será iterada en un orden de entrada y salida, como una cola.

## Comportamiento de Iteración

`SplDoublyLinkedList::IT_MODE_DELETE`  
La iteración eliminará los elementos iterados.

`SplDoublyLinkedList::IT_MODE_KEEP`  
La iteración no eliminará los elementos iterados.
