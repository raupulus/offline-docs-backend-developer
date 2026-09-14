---
title: La clase EvFork
source_url: https://www.php.net/manual/es/class.evfork.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evfork.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18080
---

## Introducción

Los observadores Fork son llamados cuando un `fork()` ha sido detectado (habitualmente, porque señalado a *libev* al llamar al método EvLoop::fork). La invocación se realiza antes de que el bucle de eventos bloquee el siguiente y antes de la llamada de los observadores `EvCheck`, y solo en el hijo después del fork. Tenga en cuenta que si alguien llama a EvLoop::fork en el proceso incorrecto, el gestor de fork será llamado también.

## Sinopsis de la clase

EvFork

EvFork

extends

EvWatcher

Propiedades heredadas

Métodos

Métodos heredados
