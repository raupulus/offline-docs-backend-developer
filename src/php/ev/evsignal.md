---
title: La clase EvSignal
source_url: https://www.php.net/manual/es/class.evsignal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evsignal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18520
---

## Introducción

Los watchers `EvSignal` lanzarán un evento cuando el proceso reciba una señal específica una o varias veces. A pesar de que las señales sean asíncronas, *libev* intentará hacer lo posible para entregar las señales de forma síncrona, es decir, al igual que cualquier otro evento.

No hay límite para el número de watchers para la misma señal, pero solo en la misma loop, es decir, se puede vigilar `SIGINT` en la loop por defecto, y para `SIGIO` en otra loop, pero no está permitido vigilar `SIGINT` tanto en la loop por defecto como en otra loop al mismo tiempo. En este momento, `SIGCHLD` está permanentemente vinculado a la loop por defecto.

Si es posible y está soportado, *libev* instalará su manejador con `SA_RESTART` (o equivalente) activado, por lo tanto, las llamadas al sistema no deberían ser interrumpidas. En el caso de un problema con las llamadas al sistema que se vieran interrumpidas por señales, todas las señales pueden ser bloqueadas en un watcher `EvCheck` y desbloqueadas en un watcher `EvPrepare`.

## Sinopsis de la clase

EvSignal

EvSignal

extends

EvWatcher

Propiedades

public

signum

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`signum`  
El número de la señal. Ver las constantes exportadas por la extensión *pcntl*. Ver también la página del manual para `signal(7)`.
