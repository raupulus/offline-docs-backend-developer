---
title: La clase RecursiveArrayIterator
source_url: https://www.php.net/manual/es/class.recursivearrayiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursivearrayiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 82970
---

## Introducción

Este iterador permite destruir y modificar valores y claves mientras se iteran arrays y objetos de la misma manera que con `ArrayIterator`. Adicionalmente es posible iterar la entrada del iterador actual.

## Sinopsis de la clase

RecursiveArrayIterator

extends

ArrayIterator

implements

RecursiveIterator

Constantes heredadas

Constantes

public

const

int

RecursiveArrayIterator::CHILD_ARRAYS_ONLY

Métodos

Métodos heredados

## Constantes predefinidas

## RecursiveArrayIterator Flags

`RecursiveArrayIterator::CHILD_ARRAYS_ONLY`  
Trata sólo los array (no objetos) como si tuvieran hijos para la itaración recursiva.
