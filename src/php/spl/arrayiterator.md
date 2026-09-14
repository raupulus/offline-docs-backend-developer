---
title: La clase ArrayIterator
source_url: https://www.php.net/manual/es/class.arrayiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: 077aab268
order: 81340
---

## Introducción

Permite la eliminación de elementos y la modificación de claves o valores durante la iteración de `array`s o de `object`s.

Para recorrer el mismo array varias veces, se recomienda instanciar `ArrayObject` y utilizar la instancia de `ArrayIterator` ya sea creada implícitamente utilizando [`foreach`](#control-structures.foreach) para iterar sobre el array almacenado internamente, o creando una llamando manualmente al método ArrayObject::getIterator.

## Sinopsis de la clase

ArrayIterator

implements

SeekableIterator

ArrayAccess

Serializable

Countable

Constantes

public

const

int

ArrayIterator::STD_PROP_LIST

public

const

int

ArrayIterator::ARRAY_AS_PROPS

Métodos

## Constantes predefinidas

## Flags de ArrayIterator

`ArrayIterator::STD_PROP_LIST`  
Las propiedades del objeto conservan sus funcionalidades normales cuando son accedidas como lista (`var_dump`, [`foreach`](#control-structures.foreach), etc.).

`ArrayIterator::ARRAY_AS_PROPS`  
Las entradas pueden ser accedidas como propiedades (lectura y escritura).
