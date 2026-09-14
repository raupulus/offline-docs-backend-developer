---
title: EventListener::__construct
description: Crea un nuevo oyente de conexión asociado con la base de eventos
source_url: https://www.php.net/manual/es/eventlistener.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventlistener/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: a47dff201
order: 20330
---

EventListener::\_\_construct

Crea un nuevo oyente de conexión asociado con la base de eventos

## Descripción

```php
public EventListener::__construct(EventBase $base, callable $cb, mixed $data, int $flags, int $backlog, mixed $target)
```php

Crea un nuevo oyente de conexión asociado con la base de eventos.

## Parámetros

`base`  
Base de eventos asociada.

`cb`  
Un `callable` que será invocado cuando una nueva conexión sea recibida.

`data`  
Datos de usuario personalizados adjuntos al parámetro `cb`.

`flags`  
Una máscara de constantes `EventListener::OPT_*`. Ver las [constantes EventListener](#eventlistener.constants).

`backlog`  
Controla el número máximo de conexiones en espera que la pila de red permite esperar en un estado "aún no aceptado"; ver la documentación de la función `listen` de su sistema para más detalles. Si el parámetro `backlog` es negativo, Libevent intenta obtener un buen valor para este parámetro; si es cero, Event asume que la función del sistema `listen` ya ha sido llamada en el socket (`target`).

`target`  
Puede ser un string, un recurso de socket, o un flujo asociado con un socket. En el caso de que este parámetro sea un string, será analizado como dirección IP. Será analizado como socket de dominio UNIX si está prefijado por `'unix:'`, por ejemplo, `'unix:/tmp/my.sock'`.

## Historial de cambios

| Versión          | Descripción                                        |
|------------------|----------------------------------------------------|
| PECL event 1.5.0 | Se añadió el soporte para sockets de dominio UNIX. |

## Ejemplos

Ejemplo con `EventListener::__construct`

```
<?php
/*
 * Un simple servidor de eco, basado en un oyente de conexión libevent.
 *
 * Uso:
 * 1) En una terminal Windows, ejecute:
 *
 * $ php listener.php 9881
 *
 * 2) En otra terminal Windows, abra la siguiente conexión:
 *
 * $ nc 127.0.0.1 9881
 *
 * 3) Comience a escribir. El servidor debería repetir las entradas.
 */

class MyListenerConnection {
    private $bev, $base;

    public function __destruct() {
        $this->bev->free();
    }

    public function __construct($base, $fd) {
        $this->base = $base;

        $this->bev = new EventBufferEvent($base, $fd, EventBufferEvent::OPT_CLOSE_ON_FREE);

        $this->bev->setCallbacks(array($this, "echoReadCallback"), NULL,
            array($this, "echoEventCallback"), NULL);

        if (!$this->bev->enable(Event::READ)) {
            echo "Imposible habilitar READ\n";
            return;
        }
    }

    public function echoReadCallback($bev, $ctx) {
        // Copia todos los datos desde el buffer de entrada hacia el buffer de salida

        // Variante #1
        $bev->output->addBuffer($bev->input);

        /* Variante #2 */
        /*
        $input    = $bev->getInput();
        $output = $bev->getOutput();
        $output->addBuffer($input);
        */
    }

    public function echoEventCallback($bev, $events, $ctx) {
        if ($events & EventBufferEvent::ERROR) {
            echo "Error desde bufferevent\n";
        }

        if ($events & (EventBufferEvent::EOF | EventBufferEvent::ERROR)) {
            //$bev->free();
            $this->__destruct();
        }
    }
}

class MyListener {
    public $base,
        $listener,
        $socket;
    private $conn = array();

    public function __destruct() {
        foreach ($this->conn as &$c) $c = NULL;
    }

    public function __construct($port) {
        $this->base = new EventBase();
        if (!$this->base) {
            echo "Imposible abrir la base del evento";
            exit(1);
        }

        // Variante #1
        /*
        $this->socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
        if (!socket_bind($this->socket, '0.0.0.0', $port)) {
            echo "Imposible enlazar el socket\n";
            exit(1);
        }
        $this->listener = new EventListener($this->base,
            array($this, "acceptConnCallback"), $this->base,
            EventListener::OPT_CLOSE_ON_FREE | EventListener::OPT_REUSEABLE,
            -1, $this->socket);
         */

        // Variante #2
         $this->listener = new EventListener($this->base,
             array($this, "acceptConnCallback"), $this->base,
             EventListener::OPT_CLOSE_ON_FREE | EventListener::OPT_REUSEABLE, -1,
             "0.0.0.0:$port");

        if (!$this->listener) {
            echo "No se pudo crear el oyente";
            exit(1);
        }

        $this->listener->setErrorCallback(array($this, "accept_error_cb"));
    }

    public function dispatch() {
        $this->base->dispatch();
    }

    // Esta función de retrollamada es llamada cuando hay datos para leer desde $bev
    public function acceptConnCallback($listener, $fd, $address, $ctx) {
        // ¡Tenemos una nueva conexión! Se le define un bufferevent. */
        $base = $this->base;
        $this->conn[] = new MyListenerConnection($base, $fd);
    }

    public function accept_error_cb($listener, $ctx) {
        $base = $this->base;

        fprintf(STDERR, "Error recibido %d (%s) en el oyente. "
            ."Cerrando.\n",
            EventUtil::getLastSocketErrno(),
            EventUtil::getLastSocketError());

        $base->exit(NULL);
    }
}

$port = 9808;

if ($argc > 1) {
    $port = (int) $argv[1];
}
if ($port <= 0 || $port > 65535) {
    exit("Puerto inválido");
}

$l = new MyListener($port);
$l->dispatch();
?>

   
```php
