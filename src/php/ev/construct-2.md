---
title: EvChild::__construct
description: Construye el objeto de observación EvChild
source_url: https://www.php.net/manual/es/evchild.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evchild/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 17970
---

EvChild::\_\_construct

Construye el objeto de observación EvChild

## Descripción

```php
public EvChild::__construct(int $pid, bool $trace, callable $callback, [mixed $data], [int $priority])
```php

Construye el objeto observador `EvChild`.

Llama a la retrollamada cuando se recibe un cambio de estado de un proceso cuyo ID `pid` (o de cualquier *PID* si vale `0`) (un cambio de estado ocurre cuando el proceso termina o es eliminado, o cuando el parámetro `trace` vale `true`, cuando el proceso es detenido o continuado). En otras palabras, cuando el proceso recibe un `SIGCHLD`, *Ev* recuperará todos los estados de salida/espera para todos los hijos modificados/zombies y llamará a la retrollamada.

Es válido instalar un observador en el hijo después de que un `EvChild` haya salido, pero antes de que el bucle de eventos haya iniciado su siguiente iteración. Por ejemplo, primero, se llama a `fork`, luego el nuevo proceso hijo puede salir, y solo entonces, un observador `EvChild` es instalado en el padre para el nuevo *PID*.

Se podrá acceder a los estados de salida/de traza así como a los `pid` utilizando las propiedades `rstatus` y `rpid` del objeto observador.

El número de observadores *PID* por *PID* no está limitado. Todos serán llamados.

El método EvChild::createStopped no inicia (activa) el nuevo observador creado.

## Parámetros

`pid`  
Espera los cambios de estado de los procesos PID (o cualquier proceso si PID vale `0`).

`trace`  
Si vale `false`, solo activa el observador cuando el proceso termina. De lo contrario (`true`), activa el observador cuando el proceso es detenido o continuado.

`callback`  
Ver las [retrollamadas de los observadores](#ev.watcher-callbacks).

`data`  
Datos personalizados asociados con el observador.

`priority`  
[Retrollamadas del observador](#ev.constants.watcher-pri)

## Véase también

EvLoop::child
