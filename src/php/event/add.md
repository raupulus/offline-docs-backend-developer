---
title: Event::add
description: Pone un evento en espera
source_url: https://www.php.net/manual/es/event.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/event/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: a916b9bd3
order: 18810
---

Event::add

Pone un evento en espera

## Descripción

```php
public Event::add([float $timeout]): bool
```php

Pone un evento en espera. Un evento que no tiene el estado en espera nunca se lanzará, y la retrollamada del evento nunca se llamará. Utilizando Event::del un evento puede ser reprogramado por el usuario cuando lo desee.

Si Event::add es llamado en un evento ya en espera, libevent lo dejará en espera y lo reprogramará con el nuevo timeout (si se da). En el caso de que el timeout no esté especificado, Event::add no tiene ningún efecto.

## Parámetros

`timeout`  
Timeout en segundos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Adición de una señal personalizada

```
<?php
/*
Ejecute en una ventana de terminal:

$ php examples/signal.php

En otra ventana de terminal, encuentre el pid y envíe SIGTERM, por ejemplo:

$ ps aux | grep examp
ruslan    3976  0.2  0.0 139896 11256 pts/1    S+   10:25   0:00 php examples/signal.php
ruslan    3978  0.0  0.0   9572   864 pts/2    S+   10:26   0:00 grep --color=auto examp

$ kill -TERM 3976

En la primera ventana del terminal, debería ver lo siguiente:

Señal atrapada 15
*/

class MyEventSignal {
    private $base, $ev;
    public function __construct($base) {
        $this->base = $base;
        $this->ev = Event::signal($base, SIGTERM, array($this, 'eventSighandler'));
        $this->ev->add();
    }
    public function eventSighandler($no, $c) {
        echo "Señal atrapada $no\n";
        $this->base->exit();
    }
}

$base = new EventBase();
$c = new MyEventSignal($base);

$base->loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Señal atrapada 15

Adición de un temporizador

```
<?php

$base = new EventBase();
$n = 2;
$e = Event::timer($base, function($n) use (&$e) {
    echo "$n segundos transcurridos\n";
    $e->delTimer();
}, $n);
$e->add($n);
$base->loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    2 segundos transcurridos

## Véase también

Event::add

Event::del

Event::signal

Event::timer
