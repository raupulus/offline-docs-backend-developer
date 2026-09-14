---
title: La clase EvPeriodic
source_url: https://www.php.net/manual/es/class.evperiodic.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evperiodic.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18450
---

## Introducción

Los observadores periódicos son una especie de temporizadores, pero son muy versátiles.

A diferencia de `EvTimer`, los observadores `EvPeriodic` no se basan en un tiempo real (o un tiempo relativo, el tiempo físico que transcurre), sino en un tiempo de reloj (tiempo absoluto, calendario o de reloj). La diferencia es que un tiempo de reloj puede ser más rápido o más lento que un tiempo real, y los saltos en el tiempo no son raros (por ejemplo, durante un ajuste).

Un observador `EvPeriodic` puede ser configurado para ser lanzado después de puntos específicos en el tiempo. Por ejemplo, si un observador `EvPeriodic` está configurado para lanzarse *"en 10 segundos"* (es decir, EvLoop::now + `10.0`, es decir, un tiempo absoluto, y no un retraso), y el reloj del sistema se reinicia a *enero del año pasado*, entonces tomará un año o más para lanzar el evento (a diferencia de `EvTimer` que se lanzará `10` segundos después de su inicio, ya que utiliza un retraso máximo relativo).

Al igual que con los temporizadores, se garantiza que la función de retrollamada sea llamada únicamente cuando el punto en el tiempo en el que se supone que debe lanzarse haya pasado. Si varios temporizadores se vuelven listos al mismo tiempo durante la misma iteración del bucle, entonces aquellos con valores de retraso máximo más cercanos serán llamados antes que aquellos con valores de retraso máximo más lejanos (pero esto ya no es cierto cuando una función de retrollamada llama recursivamente al método EvLoop::run).

## Sinopsis de la clase

EvPeriodic

EvPeriodic

extends

EvWatcher

Propiedades

public

offset

public

interval

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`offset`  
Al repetirse, contendrá el valor de la posición, de lo contrario, será el punto absoluto en el tiempo (el valor de la posición pasado al método EvPeriodic::set, aunque *libev* puede modificar este valor para una mejor estabilidad numérica).

`interval`  
El valor del intervalo actual. Puede ser modificado en cualquier momento, pero los cambios no surten efecto hasta que el temporizador periódico no se lance, o cuando se llame al método EvPeriodic::again.
