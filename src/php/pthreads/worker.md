---
title: La clase Worker
source_url: https://www.php.net/manual/es/class.worker.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/worker.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66990
---

## Introducción

Los Threads Worker tienen un contexto persistente, por lo tanto, pueden ser utilizados mediante Threads en la mayoría de los casos.

Cuando un Worker es iniciado, el método run será ejecutado, pero el Thread no se detendrá hasta que una de las siguientes condiciones se cumpla:

- el Worker está fuera de alcance (no hay referencias restantes);

- el desarrollador llama a shutdown;

- el script muere.

Esto significa que el desarrollador puede reutilizar el contexto durante toda la ejecución; colocar objetos en la pila del Worker hará que el Worker ejecute el método run sobre los objetos apilados.

## Sinopsis de la clase

Worker

Worker

extends

Thread

Traversable

Countable

ArrayAccess

Métodos

Métodos heredados
