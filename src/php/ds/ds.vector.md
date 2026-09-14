---
title: La clase Vector
source_url: https://www.php.net/manual/es/class.ds-vector.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds.vector.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_revision: 94b069b11
order: 16620
---

## Introducción

Un Vector es una secuencia de valores en un buffer que crece y se encoge automáticamente. Esta es la más eficiente estructura secuencial debido a que el índice de un valor es un mapeo directo a su índice en el buffer, y el factor de crecimiento no está ligado a un multiplo o exponente específico.

## Fortalezas

Soporta la sintaxis array (corchetes)., Usa menos memoria general que un `array` para el mismo número de valores., Automáticamente libera la memoria asignada cuando su tamaño cae lo suficientemente bajo., La capacidad no tiene que ser una potencia de 2., `get`, `set`, `push`, `pop` son todos O(1).

## Debilidades

`shift`, `unshift`, `insert` y `remove` son todos O(n).

## Sinopsis de la clase

Ds\Vector

Ds\Vector

Ds\Sequence

ArrayAccess

Constantes

const

int

Ds\Vector::MIN_CAPACITY

8

Métodos

## Constantes predefinidas

`Ds\Vector::MIN_CAPACITY`  

## Historial de cambios

| Versión       | Descripción                                 |
|---------------|---------------------------------------------|
| PECL ds 1.3.0 | La clase ahora implementa `ArrayAccess`.    |
| PECL ds 1.2.0 | `Ds\Vector::MIN_CAPACITY` cambió de 10 a 8. |
