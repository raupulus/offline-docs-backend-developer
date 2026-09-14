---
title: La clase QuickHashStringIntHash
source_url: https://www.php.net/manual/es/class.quickhashstringinthash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashstringinthash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67490
---

## Introducción

Esta clase envuelve un hash que contiene strings, donde los valores son enteros. Los hashes también están disponibles como una implementación de la interfaz ArrayAccess.

Los hashes también pueden ser recorridos con [`foreach`](#control-structures.foreach) ya que la interfaz Iterator está implementada. El orden en el que los elementos son devueltos no está garantizado.

## Sinopsis de la clase

QuickHashStringIntHash

QuickHashStringIntHash

Constantes

const

int

QuickHashStringIntHash::CHECK_FOR_DUPES

1

const

int

QuickHashStringIntHash::DO_NOT_USE_ZEND_ALLOC

2

Métodos

## Constantes predefinidas

`QuickHashStringIntHash::CHECK_FOR_DUPES`  
Si está activado, la adición de elementos duplicados a un hash (vía QuickHashStringIntHash::add o QuickHashStringIntHash::loadFromFile) resultará en la eliminación de estos elementos del hash. Esto tomará tiempo adicional, por lo que solo se debe usar esta opción si es necesario.

`QuickHashStringIntHash::DO_NOT_USE_ZEND_ALLOC`  
Desactiva el uso del gestor de memoria interno de PHP para las estructuras de hash internas. Con esta opción activada, las asignaciones internas no serán consideradas en los parámetros [memory_limit](#ini.memory-limit).
