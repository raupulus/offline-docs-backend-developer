---
title: La clase EvChild
source_url: https://www.php.net/manual/es/class.evchild.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evchild.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18000
---

## Introducción

Los watchers `EvChild` se activan cuando el proceso recibe un `SIGCHLD` en respuesta a cambios de estado de los hijos (típicamente, cuando un hijo muere o termina). Está permitido instalar un watcher `EvChild` después de que el hijo haya sido forkeado (lo que implica que ya debe existir), siempre que el bucle de eventos no haya comenzado (o continuado desde un watcher), es decir, forkear y luego registrar inmediatamente un watcher para el hijo es el método correcto, pero forkear y registrar un watcher después de algunas iteraciones del bucle de eventos o en la próxima invocación de la función de retrollamada no es el método correcto.

Solo está permitido registrar watchers `EvChild` en el *bucle por defecto*.

## Sinopsis de la clase

EvChild

EvChild

extends

EvWatcher

Propiedades

public

pid

public

rpid

public

rstatus

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`pid`  
*Solo lectura*. El ID del proceso relacionado con los watchers, o `0` que significa todos los IDs de proceso.

`rpid`  
*Solo lectura*. El ID del proceso que ha detectado un cambio de estado.

`rstatus`  
*Solo lectura*. El estado de salida del proceso causado por `rpid`.
