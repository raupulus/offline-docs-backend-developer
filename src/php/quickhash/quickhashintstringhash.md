---
title: La clase QuickHashIntStringHash
source_url: https://www.php.net/manual/es/class.quickhashintstringhash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintstringhash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67360
---

## Introducción

Esta clase envuelve un array que contiene números enteros, donde los valores son strings. Los arrays también están disponibles como una implementación de la interfaz ArrayAccess.

Los hashes también pueden ser recorridos con [`foreach`](#control-structures.foreach) ya que la interfaz Iterator está implementada. El orden en el que los elementos son devueltos no está garantizado.

## Sinopsis de la clase

QuickHashIntStringHash

QuickHashIntStringHash

Constantes

const

int

QuickHashIntStringHash::CHECK_FOR_DUPES

1

const

int

QuickHashIntStringHash::DO_NOT_USE_ZEND_ALLOC

2

const

int

QuickHashIntStringHash::HASHER_NO_HASH

256

const

int

QuickHashIntStringHash::HASHER_JENKINS1

512

const

int

QuickHashIntStringHash::HASHER_JENKINS2

1024

Métodos

## Constantes predefinidas

`QuickHashIntStringHash::CHECK_FOR_DUPES`  
Si está activado, añadir elementos duplicados a un conjunto (a través de QuickHashIntStringHash::add o QuickHashIntStringHash::loadFromFile) resultará en la eliminación de estos elementos del conjunto. Esto tomará más tiempo, por lo que sólo debe usarse si es necesario.

`QuickHashIntStringHash::DO_NOT_USE_ZEND_ALLOC`  
Desactiva el uso del gestor de memoria interno de PHP para las estructuras de juego internas. Con esta opción activada, las asignaciones internas no contarán hacia los parámetros [memory_limit](#ini.memory-limit).

`QuickHashIntStringHash::HASHER_NO_HASH`  
Selecciona no usar una función de hash, sino simplemente usar un módulo para encontrar el índice de la lista de cubos. Esto no es más rápido que el hash normal, y da más colisiones.

`QuickHashIntStringHash::HASHER_JENKINS1`  
Esta es la función de hash por defecto para transformar los hashes enteros en índices de lista de cubos.

`QuickHashIntStringHash::HASHER_JENKINS2`  
Selecciona un algoritmo de hash de variantes.
