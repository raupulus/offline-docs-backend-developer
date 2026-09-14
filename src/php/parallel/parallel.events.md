---
title: La clase parallel\Events
source_url: https://www.php.net/manual/es/class.parallel-events.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel.events.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60310
---

## El bucle de eventos

El bucle de eventos supervisa el estado de los conjuntos de futuros y/o canales (objetivos) para realizar operaciones de lectura (parallel\Future::value, parallel\Channel::recv) y escritura (parallel\Channel::send) cuando los objetivos se vuelven disponibles y las operaciones pueden ser realizadas sin bloquear el bucle de eventos.

## Sinopsis de la clase

parallel\Events

final

parallel\Events

Countable

Traversable

Entrada

Objetivos

Comportamiento

Sondeo
