---
title: La clase SyncMutex
source_url: https://www.php.net/manual/es/class.syncmutex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncmutex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93600
---

## Introducción

Una implementación multiplataforma, nativa de los objetos Mutex nombrados o no nombrados.

Un Mutex es un objeto de exclusión mutua que restringe el acceso a un recurso compartido (i.e. un fichero) a una sola instancia. Los Mutex contables adquieren el mutex una sola vez y, internamente, rastrean el número de veces que el mutex es bloqueado. El Mutex es desbloqueado tan pronto como sale del ámbito o es desbloqueado el mismo número de veces que ha sido bloqueado.

## Sinopsis de la clase

SyncMutex

SyncMutex

Métodos
