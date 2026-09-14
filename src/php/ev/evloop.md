---
title: La clase EvLoop
source_url: https://www.php.net/manual/es/class.evloop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18390
---

## Introducción

Representa un bucle de eventos que siempre es distinto del *bucle por defecto*. A diferencia del *bucle por defecto*, no puede gestionar los watchers `EvChild`.

Al utilizar hilos, se debe crear un bucle por hilo, y utilizar el *bucle por defecto* en el hilo padre.

El *bucle de eventos por defecto* es inicializado automáticamente por *Ev*. Es accesible a través de los métodos de la clase `Ev` o mediante el método EvLoop::defaultLoop.

## Sinopsis de la clase

EvLoop

final

EvLoop

Propiedades

public

data

public

backend

public

is_default_loop

public

iteration

public

pending

public

io_interval

public

timeout_interval

public

depth

Métodos

## Propiedades

`data`  
Datos personalizados para adjuntar al bucle

`backend`  
*Solo lectura*. Los [flags del backend](#ev.constants.watcher-backends) que indican el backend de eventos en uso.

`is_default_loop`  
*Solo lectura*. `true` si es el bucle de eventos por defecto.

`iteration`  
El contador de iteración actual del bucle. Ver el método Ev::iteration.

`pending`  
El número de watchers pendientes. `0` indica que no hay watchers pendientes.

`io_interval`  
Un valor alto para `io_interval` permite a *libev* pasar más tiempo recolectando los eventos `EvIo`, así, más eventos pueden ser gestionados por iteración, pero esto aumentará la latencia. Los tiempos de espera máximos (tanto para `EvPeriodic` como para `EvTimer`) no se verán afectados. Establecer esta opción a un valor distinto de cero introducirá una llamada adicional a `sleep()` en la mayoría de las iteraciones del bucle. El tiempo de pausa asegura que *libev* no consultará `EvIo` más de una vez durante este intervalo, en promedio. La mayoría de los programas pueden beneficiarse estableciendo `io_interval` a un valor cercano a `0.1`, lo cual es generalmente suficiente para los servidores interactivos (y no destinados a juegos). Generalmente no tiene sentido establecer este valor a menos de `0.01`, ya que se acerca a la granularidad a nivel de tiempos de la mayoría de los sistemas.

Ver también las [ funciones que controlan los bucles de eventos](http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#FUNCTIONS_CONTROLLING_EVENT_LOOPS).

`timeout_interval`  
Un valor alto para `timeout_interval` permite a *libev* pasar más tiempo recolectando los tiempos de espera máximos, pero como consecuencia aumenta la latencia, el estrés y la inexactitud (la función de retrollamada del watcher será llamada más tarde). Los watchers `EvIo` no se verán afectados. Establecer este valor a un valor no nulo no introducirá ninguna sobrecarga adicional a *libev*. Ver también las [ funciones que controlan los bucles de eventos](http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#FUNCTIONS_CONTROLLING_EVENT_LOOPS).

`depth`  
La profundidad de la recursión. Ver el método Ev::depth.
