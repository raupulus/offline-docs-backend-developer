---
title: EvTimer::createStopped
description: Crea un objeto EvTimer watcher detenido
source_url: https://www.php.net/manual/es/evtimer.createstopped.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evtimer/createstopped.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 18620
---

EvTimer::createStopped

Crea un objeto EvTimer watcher detenido

## Descripción

```php
final public static EvTimer::createStopped(float $after, float $repeat, callable $callback, [mixed $data], [int $priority]): EvTimer
```php

Crea un objeto EvTimer watcher detenido. A diferencia del método EvTimer::\_\_construct, este método no inicia automáticamente el watcher.

## Parámetros

`after`  
Configura el tiempo para lanzar un trigger después de `after` segundos.

`repeat`  
Si este parámetro vale `0.0`, entonces el watcher se detendrá automáticamente una vez alcanzado el tiempo máximo de espera. Si este parámetro es positivo, entonces el timer lanzará automáticamente el trigger cada segundo siguiente, hasta que se detenga manualmente.

`callback`  
Ver las [funciones de retrollamada Watcher](#ev.watcher-callbacks).

`data`  
Datos personales asociados al watcher.

`priority`  
[Las prioridades del Watcher](#ev.constants.watcher-pri)

## Valores devueltos

Retorna un objeto EvTimer watcher en caso de éxito.

## Ejemplos

Monitoreo de modificaciones en /var/log/messages. Detecta actualizaciones olvidadas añadiendo un segundo de demora

```
<?php
$timer = EvTimer::createStopped(0., 1.02, function ($w) {
    $w->stop();

    $stat = $w->data;

    // 1 segundo después de la modificación más reciente del fichero
    printf("Tamaño actual: %ld\n", $stat->attr()['size']);
});

$stat = new EvStat("/var/log/messages", 0., function () use ($timer) {
    // Reinicia el watcher timer
    $timer->again();
});

$timer->data = $stat;

Ev::run();
?>

   
```php

## Véase también

EvTimer::\_\_construct

EvPeriodic
