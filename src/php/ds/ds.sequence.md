---
title: La interfaz Sequence
source_url: https://www.php.net/manual/es/class.ds-sequence.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds.sequence.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 16590
---

## Introducción

Una Sequence describe el comportamiento de los valores dispuestos en una sola dimensión lineal. Algunos lenguajes se refieren a esto como una "Lista". Es similar a un array que utiliza claves enteras incrementales, con la excepción de algunas características: Los valores siempre serán indexados como \[0, 1, 2, …, size - 1\]., Solo los valores por índice en el rango \[0, size - 1\] están permitidos.

Casos de uso: En cualquier lugar donde se utilizaría un array como lista (sin preocuparse por las claves)., Una alternativa más eficiente a `SplDoublyLinkedList` y `SplFixedArray`.

## Sinopsis de la interfaz

Ds\Sequence

extends

Ds\Collection

ArrayAccess

Métodos

Métodos heredados

## Historial de cambios

| Versión       | Descripción                                 |
|---------------|---------------------------------------------|
| PECL ds 1.3.0 | Esta interfaz ahora extiende `ArrayAccess`. |
