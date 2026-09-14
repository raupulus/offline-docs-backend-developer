---
title: La clase QuickHashIntHash
source_url: https://www.php.net/manual/es/class.quickhashinthash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashinthash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67130
---

## Introducción

Esta clase envuelve un hash que contiene números enteros, donde los valores son también números enteros. Los hashes están disponibles como implementación de la interfaz ArrayAccess.

Los hashes pueden ser iterados con [`foreach`](#control-structures.foreach) ya que la interfaz Iterator está también implementada. El orden en el que los elementos son devueltos no está garantizado.

## Sinopsis de la clase

QuickHashIntHash

QuickHashIntHash

Constantes

const

int

QuickHashIntHash::CHECK_FOR_DUPES

1

const

int

QuickHashIntHash::DO_NOT_USE_ZEND_ALLOC

2

const

int

QuickHashIntHash::HASHER_NO_HASH

256

const

int

QuickHashIntHash::HASHER_JENKINS1

512

const

int

QuickHashIntHash::HASHER_JENKINS2

1024

Métodos

## Constantes predefinidas

`QuickHashIntHash::CHECK_FOR_DUPES`  
Si está activado, la adición de elementos duplicados a un hash (vía QuickHashIntHash::add o QuickHashIntHash::loadFromFile) resultará en la eliminación de estos elementos del hash. Esto tomará más tiempo, por lo que úselo solo si es necesario.

`QuickHashIntHash::DO_NOT_USE_ZEND_ALLOC`  
Desactiva el uso del gestor de memoria interno de PHP para las estructuras de juego internas. Con esta opción activada, las asignaciones internas no contarán en los parámetros [memory_limit](#ini.memory-limit).

`QuickHashIntHash::HASHER_NO_HASH`  
Selecciona no usar una función de hash, sino simplemente usar un módulo para encontrar el índice de la lista de cubos. Esto no es más rápido que el hash normal, y da más colisiones.

`QuickHashIntHash::HASHER_JENKINS1`  
Esta es la función de hash por defecto para transformar los hashes enteros en índice de lista de cubos.

`QuickHashIntHash::HASHER_JENKINS2`  
Selecciona un algoritmo de hash de variante.
