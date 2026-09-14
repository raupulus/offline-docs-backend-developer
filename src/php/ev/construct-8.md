---
title: EvPeriodic::__construct
description: Construye un objeto watcher EvPeriodic
source_url: https://www.php.net/manual/es/evperiodic.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evperiodic/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 8e2cfbdce
order: 18420
---

EvPeriodic::\_\_construct

Construye un objeto watcher EvPeriodic

## Descripción

```php
public EvPeriodic::__construct(float $offset, string $interval, callable $reschedule_cb, callable $callback, [mixed $data], [int $priority])
```php

Construye un objeto watcher EvPeriodic y lo inicia automáticamente. El método EvPeriodic::createStopped crea un watcher periódico detenido.

## Parámetros

`offset`  
Ver los [modos de operación del watcher periódico](#ev.periodic-modes)

`interval`  
Ver los [modos de operación del watcher periódico](#ev.periodic-modes)

`reschedule_cb`  
Función de retrollamada Reschedule. Puede pasarse el valor `null`. Ver los [modos de operación del watcher periódico](#ev.periodic-modes)

`callback`  
Ver las [funciones de retrollamada de los Watchers](#ev.watcher-callbacks) .

`data`  
Datos personalizados para asociar con el watcher.

`priority`  
[Prioridad del Watcher](#ev.constants.watcher-pri)

## Ejemplos

Temporizador periódico. Utilizando la retrollamada de replanificación

```
<?php
// Cada 10.5 segundos

function reschedule_cb ($watcher, $now) {
 return $now + (10.5 - fmod($now, 10.5));
}

$w = new EvPeriodic(0., 0., "reschedule_cb", function ($w, $revents) {
 echo time(), PHP_EOL;
});
Ev::run();
?>

   
```php

Temporizador periódico. Llamado cada 10.5 segundos

```
<?php
// Cada 10.5 segundos a partir de ahora
$w = new EvPeriodic(fmod(Ev::now(), 10.5), 10.5, NULL, function ($w, $revents) {
 echo time(), PHP_EOL;
});
Ev::run();
?>

   
```php

Watcher cada hora

```
<?php
$hourly = EvPeriodic(0, 3600, NULL, function () {
 echo "una vez por hora\n";
});
?>

   
```php

## Véase también

Los modos de operación del watcher periódico

EvTimer

EvPeriodic::createStopped
