---
title: La clase SyncSharedMemory
source_url: https://www.php.net/manual/es/class.syncsharedmemory.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncsharedmemory.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93760
---

## Introducción

Una implementación nativa, coherente y multiplataforma de objetos de memoria compartida nombrada.

La memoria compartida permite a dos procesos distintos comunicarse sin necesidad de tuberías o sockets complejos. Existen varias implementaciones de memoria compartida basadas en enteros para PHP. La memoria compartida nombrada es una alternativa.

Los objetos de sincronización (por ejemplo, SyncMutex) son siempre necesarios para proteger la mayoría de los usos de la memoria compartida.

## Sinopsis de la clase

SyncSharedMemory

SyncSharedMemory

Métodos
