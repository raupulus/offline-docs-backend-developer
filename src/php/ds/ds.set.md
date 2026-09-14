---
title: La clase Set
source_url: https://www.php.net/manual/es/class.ds-set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds.set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 94b069b11
order: 16600
---

## Introducción

Un Set es una secuencia de valores únicos. Esta implementación utiliza la misma tabla de hash que `Ds\Map`, donde los valores se utilizan como claves y el valor mapeado se ignora.

## Fortalezas

Los valores pueden ser de cualquier tipo, incluyendo objetos., Soporte de la sintaxis de array (corchetes)., El orden de inserción se preserva., Libera automáticamente la memoria asignada cuando su tamaño se vuelve suficientemente pequeño., `add`, `remove` y `contains` son todos de complejidad O(1).

## Debilidades

No soporta: `push`, `pop`, `insert`, `shift`, o `unshift`., `get` es de complejidad O(n) si hay valores eliminados en el búfer antes del índice accedido, O(1) en caso contrario.

## Sinopsis de la clase

Ds\Set

Ds\Set

Ds\Collection

ArrayAccess

Constantes

const

int

Ds\Set::MIN_CAPACITY

8

Métodos

## Constantes predefinidas

`Ds\Set::MIN_CAPACITY`  

## Historial de cambios

| Versión       | Descripción                                |
|---------------|--------------------------------------------|
| PECL ds 1.3.0 | Esta clase implementa ahora `ArrayAccess`. |
| PECL ds 1.2.7 | Se añadió el método Ds\Set::map.           |
| PECL ds 1.2.0 | `Ds\Set::MIN_CAPACITY` cambió de 16 a 8.   |
