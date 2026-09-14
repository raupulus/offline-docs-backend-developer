---
title: La clase Thread
source_url: https://www.php.net/manual/es/class.thread.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/thread.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66770
---

## Introducción

Cuando el método start de un Thread es llamado, el código del método run será ejecutado de forma paralela en un Thread separado.

Después de la ejecución del método run, el Thread se terminará inmediatamente, será vinculado al Thread original posteriormente.

> [!WARNING]
> Basarse en el motor para determinar cuándo un Thread será vinculado puede provocar un comportamiento no deseado. El desarrollador debe ser explícito en la medida de lo posible.

## Sinopsis de la clase

Thread

Thread

extends

Threaded

Countable

Traversable

ArrayAccess

Métodos

Métodos heredados
