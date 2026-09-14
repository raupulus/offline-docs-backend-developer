---
title: La clase CachingIterator
source_url: https://www.php.net/manual/es/class.cachingiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/cachingiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: 4d17b7b49
order: 81760
---

## Introducción

Este objeto soporta las iteraciones en caché sobre otro iterador.

## Sinopsis de la clase

CachingIterator

extends

IteratorIterator

implements

ArrayAccess

Countable

Stringable

Constantes

public

const

int

CachingIterator::CALL_TOSTRING

public

const

int

CachingIterator::CATCH_GET_CHILD

public

const

int

CachingIterator::TOSTRING_USE_KEY

public

const

int

CachingIterator::TOSTRING_USE_CURRENT

public

const

int

CachingIterator::TOSTRING_USE_INNER

public

const

int

CachingIterator::FULL_CACHE

Métodos

Métodos heredados

## Constantes predefinidas

`CachingIterator::CALL_TOSTRING`  
Convierte todos los elementos en strings.

`CachingIterator::CATCH_GET_CHILD`  
No lanza ninguna excepción al intentar acceder a un hijo.

`CachingIterator::TOSTRING_USE_KEY`  
Utiliza [key](#cachingiterator.key) durante la conversión en string.

`CachingIterator::TOSTRING_USE_CURRENT`  
Utiliza [current](#cachingiterator.current) durante la conversión en string.

`CachingIterator::TOSTRING_USE_INNER`  
Utiliza [inner](#iteratoriterator.getinneriterator) durante la conversión en string.

`CachingIterator::FULL_CACHE`  
Almacena en caché todos los datos leídos.

## Historial de cambios

| Versión | Descripción                                             |
|---------|---------------------------------------------------------|
| 8.0.0   | La clase `CachingIterator` implementa ahora Stringable. |
