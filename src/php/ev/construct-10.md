---
title: EvSignal::__construct
description: Construye un objeto watcher EvSignal
source_url: https://www.php.net/manual/es/evsignal.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evsignal/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 184764a63
order: 18490
---

EvSignal::\_\_construct

Construye un objeto watcher EvSignal

## Descripción

```php
public EvSignal::__construct(int $signum, callable $callback, [mixed $data], [int $priority])
```php

Construye un objeto watcher EvSignal y lo inicia automáticamente. Para un watcher de señal detenido, utilice en su lugar el método EvSignal::createStopped.

## Parámetros

`signum`  
Número de la señal. Consulte las constantes exportadas por la extensión *pcntl*. Consulte también la página del manual del sistema `signal(7)`.

`callback`  
Consulte las [funciones de retrollamada de los Watchers](#ev.watcher-callbacks).

`data`  
Datos personalizados para asociar con el watcher.

`priority`  
[Prioridad del Watcher](#ev.constants.watcher-pri)

## Ejemplos

Gestión de una señal SIGTERM

```
<?php
$w = new EvSignal(SIGTERM, function ($watcher) {
    echo "¡Señal SIGTERM recibida!\n";
    $watcher->stop();
});

Ev::run();
?>

   
```php

## Véase también

EvSignal::createStopped
