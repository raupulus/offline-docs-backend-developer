---
title: La clase QuickHashIntSet
source_url: https://www.php.net/manual/es/class.quickhashintset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67230
---

## Introducción

Esta clase envuelve un conjunto que contiene números enteros.

Los conjuntos pueden ser utilizados para almacenar valores únicos con [`foreach`](#control-structures.foreach) ya que la interfaz Iterator está implementada. El orden en el que los elementos son devueltos no está garantizado.

## Sinopsis de la clase

QuickHashIntSet

QuickHashIntSet

Constantes

const

int

QuickHashIntSet::CHECK_FOR_DUPES

1

const

int

QuickHashIntSet::DO_NOT_USE_ZEND_ALLOC

2

const

int

QuickHashIntSet::HASHER_NO_HASH

256

const

int

QuickHashIntSet::HASHER_JENKINS1

512

const

int

QuickHashIntSet::HASHER_JENKINS2

1024

Métodos

## Constantes predefinidas

`QuickHashIntSet::CHECK_FOR_DUPES`  
Si está activado, la adición de elementos duplicados a un conjunto (a través de QuickHashIntSet::add o QuickHashIntSet::loadFromFile) resultará en la eliminación de estos elementos del conjunto. Esto tomará más tiempo, por lo que solo se debe utilizar esta opción si es necesario.

`QuickHashIntSet::DO_NOT_USE_ZEND_ALLOC`  
Desactiva el uso del gestor de memoria interno de PHP para las estructuras de juego internas. Con esta opción activada, las asignaciones internas no contarán para los parámetros [memory_limit](#ini.memory-limit).

`QuickHashIntSet::HASHER_NO_HASH`  
Selecciona no utilizar una función de hash, sino simplemente utilizar un módulo para encontrar el índice de la lista de cubos. Esto no es más rápido que el hash normal, y da más colisiones.

`QuickHashIntSet::HASHER_JENKINS1`  
Esta es la función de hash por omisión para transformar los hash enteros en índice de lista de cubos.

`QuickHashIntSet::HASHER_JENKINS2`  
Selecciona un algoritmo de hash de variante.
