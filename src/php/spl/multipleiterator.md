---
title: La clase MultipleIterator
source_url: https://www.php.net/manual/es/class.multipleiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/multipleiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: 4d17b7b49
order: 82740
---

## Introducción

Un iterador que itera secuencialmente sobre varios iteradores.

## Sinopsis de la clase

MultipleIterator

implements

Iterator

Constantes

public

const

int

MultipleIterator::MIT_NEED_ANY

public

const

int

MultipleIterator::MIT_NEED_ALL

public

const

int

MultipleIterator::MIT_KEYS_NUMERIC

public

const

int

MultipleIterator::MIT_KEYS_ASSOC

Métodos

## Constantes predefinidas

`MultipleIterator::MIT_NEED_ANY`  
No exige que los iteradores sean todos válidos en una iteración.

`MultipleIterator::MIT_NEED_ALL`  
Exige que los iteradores sean todos válidos en una iteración.

`MultipleIterator::MIT_KEYS_NUMERIC`  
Las claves se crean a partir de las posiciones de los iteradores.

`MultipleIterator::MIT_KEYS_ASSOC`  
Las claves se crean a partir de las informaciones asociadas de los iteradores.
