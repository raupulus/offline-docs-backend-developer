---
title: EvTimer::__construct
description: Construye un objeto EvTimer watcher
source_url: https://www.php.net/manual/es/evtimer.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evtimer/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18610
---

EvTimer::\_\_construct

Construye un objeto EvTimer watcher

## Descripción

```php
public EvTimer::__construct(float $after, float $repeat, callable $callback, [mixed $data], [int $priority])
```php

Construye un objeto EvTimer watcher.

## Parámetros

`after`  
Configura el tiempo para lanzar el trigger después de `after` segundos.

`repeat`  
Si este argumento vale `0.0`, entonces el watcher se detendrá automáticamente cuando se alcance el tiempo máximo de espera. Si este argumento es positivo, entonces el timer lanzará automáticamente el trigger cada segundo siguiente, hasta que se detenga manualmente.

`callback`  
Ver las [funciones de retrollamada Watcher](#ev.watcher-callbacks).

`data`  
Datos personalizados asociados con el watcher.

`priority`  
[Las prioridades del Watcher](#ev.constants.watcher-pri)

## Ejemplos

timers simples

```
<?php
// Crea e inicia un timer lanzado después de 2 segundos
$w1 = new EvTimer(2, 0, function () {
    echo "2 segundos pasados\n";
});

// Crea e inicia un timer lanzado después de 2 segundos, y lo repite cada segundo
// hasta que no se detenga manualmente
$w2 = new EvTimer(2, 1, function ($w) {
    echo "es llamado cada segundo, es iniciado después de 2 segundos\n";
    echo "iteración = ", Ev::iteration(), PHP_EOL;

    // Detiene el watcher después de 5 iteraciones
    Ev::iteration() == 5 and $w->stop();
    // Detiene el watcher si llamadas posteriores causan más de 10 iteraciones
    Ev::iteration() >= 10 and $w->stop();
});

// Crea un timer detenido. Estará inactivo hasta que no se inicie manualmente
$w_stopped = EvTimer::createStopped(10, 5, function($w) {
    echo "Función de retrollamada del timer creado detenido\n";

    // Detiene el watcher después de 2 iteraciones
    Ev::iteration() >= 2 and $w->stop();
});

// Bucle mientras Ev::stop() es llamado o mientras todos los watchers no se detienen
Ev::run();

// Inicia y bloquea si está en funcionamiento
$w_stopped->start();
echo "Ejecución de una sola iteración\n";
Ev::run(Ev::RUN_ONCE);

echo "Reinicia el segundo watcher y intenta manejar los mismos eventos, pero no bloquea\n";
$w2->again();
Ev::run(Ev::RUN_NOWAIT);

$w = new EvTimer(10, 0, function() {});
echo "Ejecución de un bucle bloqueante\n";
Ev::run();
echo "FIN\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    2 segundos pasados
    es llamado cada segundo, es iniciado después de 2 segundos
    iteración = 1
    es llamado cada segundo, es iniciado después de 2 segundos
    iteración = 2
    es llamado cada segundo, es iniciado después de 2 segundos
    iteración = 3
    es llamado cada segundo, es iniciado después de 2 segundos
    iteración = 4
    es llamado cada segundo, es iniciado después de 2 segundos
    iteración = 5
    Ejecución de una sola iteración
    Función de retrollamada del timer creado detenido
    Reinicia el segundo watcher y intenta manejar los mismos eventos, pero no bloquea
    Ejecución de un bucle bloqueante
    es llamado cada segundo, es iniciado después de 2 segundos
    iteración = 8
    es llamado cada segundo, es iniciado después de 2 segundos
    iteración = 9
    es llamado cada segundo, es iniciado después de 2 segundos
    iteración = 10
    FIN

## Véase también

EvTimer::createStopped

EvPeriodic

ev_timer - repetición de un tiempo de espera máximo

Ser inteligente con los tiempos de espera máximo
