---
title: La clase PriorityQueue
source_url: https://www.php.net/manual/es/class.ds-priorityqueue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds.priorityqueue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 16570
---

## Introducción

Una PriorityQueue es muy similar a una Queue. Los valores son empujados en la cola con una prioridad asignada, y el valor con la prioridad más alta estará siempre en la cabeza de la cola.

Implementado utilizando un montículo máximo.

> [!NOTE]
> "Primero en entrar, primero en salir" se preserva para los valores con la misma prioridad.

> [!NOTE]
> Iterar sobre una PriorityQueue es destructivo, equivalente a operaciones de desapilamiento sucesivas hasta que la cola esté vacía.

## Sinopsis de la clase

Ds\PriorityQueue

Ds\PriorityQueue

Ds\Collection

Constantes

const

int

Ds\PriorityQueue::MIN_CAPACITY

8

Métodos

## Constantes predefinidas

`Ds\PriorityQueue::MIN_CAPACITY`
