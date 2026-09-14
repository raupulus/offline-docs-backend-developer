---
title: La clase EvWatcher
source_url: https://www.php.net/manual/es/class.evwatcher.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evwatcher.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18740
---

## Introducción

La clase `EvWatcher` es una clase base para todos los watchers (`EvCheck`, `EvChild` etc.). Dado que el constructor de la clase `EvWatcher` es abstract, no se puede (y no se debe) crear objetos EvWatcher directamente.

## Sinopsis de la clase

EvWatcher

abstract

EvWatcher

Propiedades

public

is_active

public

data

public

is_pending

public

priority

Métodos

## Propiedades

`is_active`  
*Solo lectura*. `true` si el watcher está activo, `false` en caso contrario.

`data`  
Datos de usuario personalizados asociados con el watcher

`is_pending`  
*Solo lectura*. Si el watcher está pendiente, es decir, si el watcher tiene eventos pendientes, pero su función de retrollamada aún no ha sido llamada, `false` en caso contrario. Mientras el watcher esté pendiente (pero no activo), otro *no puede* modificar sus prioridades.

`priority`  
`int` Rango de `Ev::MINPRI` a `Ev::MAXPRI`. Los watchers pendientes con una prioridad alta serán llamados antes que los watchers con una prioridad baja, pero la prioridad no puede hacer que un watcher nunca sea ejecutado (excepto para los watchers `EvIdle`). Los watchers `EvIdle` proporcionan funcionalidades para suprimir la invocación cuando hay eventos con una prioridad más alta pendientes.
