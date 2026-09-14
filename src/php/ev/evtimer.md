---
title: La clase EvTimer
source_url: https://www.php.net/manual/es/class.evtimer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evtimer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 18640
---

## Introducción

Los observadores `EvTimer` son observadores relativamente simples que generan un evento después de un tiempo especificado y, opcionalmente, se repiten a intervalos regulares.

Los temporizadores se basan en tiempo real, por lo que si un temporizador programa un evento que finaliza después de una hora y se reinicia el reloj del sistema a *enero del año pasado*, volverá a estar fuera de tiempo después de una hora (aproximadamente). "Aproximadamente" porque la detección de saltos en el tiempo es difícil y ciertas inexactitudes son inevitables.

Se garantiza que la función de retrollamada se llamará solo después de que expire el tiempo de espera máximo (y no exactamente en ese momento preciso, por lo que en sistemas con una resolución de reloj baja, puede introducirse un pequeño retraso). Si varios temporizadores están listos durante la misma iteración del bucle, el que tenga el valor de tiempo de espera máximo más cercano se invocará antes que otro con la misma prioridad pero con un valor de tiempo de espera más lejano (aunque esto ya no es cierto cuando una función de retrollamada llama recursivamente al método EvLoop::run).

El temporizador en sí hará todo lo posible para no derivar, pero si un temporizador está configurado para ejecutarse cada `10` segundos, entonces normalmente se ejecutará exactamente cada `10` segundos. Sin embargo, si el script no puede mantener el temporizador porque tarda más que sus `10` segundos, el temporizador no podrá ejecutarse más de una vez por iteración del bucle de eventos.

## Sinopsis de la clase

EvTimer

EvTimer

extends

EvWatcher

Propiedades

public

repeat

public

remaining

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`repeat`  
Si esta propiedad vale `0.0`, entonces se detendrá automáticamente una vez alcanzado el tiempo de espera máximo. Si es positivo, entonces el temporizador se configurará automáticamente para ejecutarse cada segundo siguiente, hasta que no se detenga manualmente.

`remaining`  
Devuelve el tiempo restante antes de que el temporizador se ejecute. Si el temporizador está activo, entonces este tiempo será relativo al tiempo del bucle de eventos actual, de lo contrario, será relativo al valor del tiempo de espera máximo configurado actualmente.

Asimismo, después de instanciar un `EvTimer` con un valor de `after` en `5.0` y un valor de `repeat` en `7.0`, `remaining` devolverá `5.0`. Cuando el temporizador se inicia y pasa un segundo, `remaining` devolverá `4.0`. Cuando el temporizador expire y se reinicie, devolverá aproximadamente `7.0` (probablemente un poco menos, ya que la invocación de la función de retrollamada también lleva algo de tiempo), y así sucesivamente.
