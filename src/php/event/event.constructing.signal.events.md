---
title: Construcción de un evento de tipo señal
source_url: https://www.php.net/manual/es/event.constructing.signal.events.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/event.constructing.signal.events.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 18970
---

## Construcción de un evento de tipo señal

Un evento puede también supervisar las señales de estilo POSIX. Para construir un gestor para una señal, utilice el método Event::\_\_construct con el flag `Event::SIGNAL` o el método factorial Event::signal.

Gestión de una señal `SIGTERM`

```php
<?php
/*
Ejecute este ejemplo en un terminal:

$ php examples/signal.php

En otro terminal, encuentre el pid y envíe la señal SIGTERM, es decir:

$ ps aux | grep examp
ruslan    3976  0.2  0.0 139896 11256 pts/1    S+   10:25   0:00 php examples/signal.php
ruslan    3978  0.0  0.0   9572   864 pts/2    S+   10:26   0:00 grep --color=auto examp
$ kill -TERM 3976

En el primer terminal, debería capturar lo siguiente:

Caught signal 15
*/
class MyEventSignal {
    private $base, $ev;

    public function __construct($base) {
        $this->base = $base;
        $this->ev = Event::signal($base, SIGTERM, array($this, 'eventSighandler'));
        $this->ev->add();
    }

    public function eventSighandler($no, $c) {
        echo "Caught signal $no\n";
        $this->base->exit();
    }
}

$base = new EventBase();
$c    = new MyEventSignal($base);

$base->loop();
?>

  
```

Tenga en cuenta que las funciones de retrollamada de una señal se ejecutan en el bucle de eventos después de que la señal haya ocurrido, por lo tanto, es más seguro para la señal llamar a funciones desde el bucle que no se supone que se llamen desde un gestor de señales POSIX clásico.

Véase también la [ programación de red fácil, portable y no bloqueante con Libevent; Construcción de un evento de tipo señal](http://www.wangafu.net/~nickm/libevent-book/Ref4_event.html#_constructing_signal_events).
