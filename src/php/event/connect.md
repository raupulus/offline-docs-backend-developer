---
title: EventBufferEvent::connect
description: Conecta el descriptor de fichero del búfer de eventos a la dirección
  proporcionada, o al socket UNIX
source_url: https://www.php.net/manual/es/eventbufferevent.connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 19390
---

EventBufferEvent::connect

Conecta el descriptor de fichero del búfer de eventos a la dirección proporcionada, o al socket UNIX

## Descripción

```php
public EventBufferEvent::connect(string $addr): bool
```php

Conecta el descriptor de fichero del búfer de eventos a la dirección proporcionada (opcionalmente, proporcionando el puerto), o al socket UNIX.

Si el socket no está asignado al búfer de eventos, este método asigna un nuevo socket y lo hace no bloqueante internamente.

Para resolver los nombres DNS (de forma asíncrona), utilice el método EventBufferEvent::connectHost.

## Parámetros

`addr`  
Debe contener una dirección IP con, opcionalmente, el número del puerto, o una ruta hacia el socket UNIX. Los formatos reconocidos son :

    [IPv6Address]:port
    [IPv6Address]
    IPv6Address
    IPv4Address:port
    IPv4Address
    unix:path

          

Tenga en cuenta que el prefijo `'unix:'` actualmente no distingue entre mayúsculas y minúsculas.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `EventBufferEvent::connect`

```
<?php
/*
 * 1. Conexión a la dirección 127.0.0.1 en el puerto 80
 * llamando al método EventBufferEvent::connect().
 *
 * 2. Solicitud /index.cphp a través de HTTP/1.0
 * utilizando el búfer de salida.
 *
 * 3. Lee la respuesta de forma asíncrona y la muestra en stdout.
 */

/* Función de retrollamada de lectura */
function readcb($bev, $base) {
    $input = $bev->getInput();

    while (($n = $input->remove($buf, 1024)) > 0) {
        echo $buf;
    }
}

/* Función de retrollamada de evento */
function eventcb($bev, $events, $base) {
    if ($events & EventBufferEvent::CONNECTED) {
        echo "Conectado.\n";
    } elseif ($events & (EventBufferEvent::ERROR | EventBufferEvent::EOF)) {
        if ($events & EventBufferEvent::ERROR) {
            echo "Error DNS: ", $bev->getDnsErrorString(), PHP_EOL;
        }

        echo "Cierre\n";
        $base->exit();
        exit("Hecho !\n");
    }
}

$base = new EventBase();

echo "paso 1\n";
$bev = new EventBufferEvent($base, /* usar socket interno */ NULL,
    EventBufferEvent::OPT_CLOSE_ON_FREE | EventBufferEvent::OPT_DEFER_CALLBACKS);
if (!$bev) {
    exit("Fallo al crear el socket bufferevent\n");
}

echo "paso 2\n";
$bev->setCallbacks("readcb", /* writecb */ NULL, "eventcb", $base);
$bev->enable(Event::READ | Event::WRITE);

echo "paso 3\n";
/* Envía la solicitud */
$output = $bev->getOutput();
if (!$output->add(
    "GET /index.cphp HTTP/1.0\r\n".
    "Connection: Close\r\n\r\n"
)) {
    exit("Fallo al añadir la solicitud en el búfer de salida\n");
}

/* Conexión al host de forma asíncrona.
 * Conocemos la IP, y por lo tanto, no necesitamos resolución DNS. */
if (!$bev->connect("127.0.0.1:80")) {
    exit("Imposible conectar al host\n");
}

/* Distribuye los eventos pendientes */
$base->dispatch();

   
```php

Resultado del ejemplo anterior es similar a:

    paso 1
    paso 2
    paso 3
    Conectado.
    HTTP/1.1 200 OK
    Server: nginx/1.2.6
    Date: Sat, 09 Mar 2013 10:06:58 GMT
    Content-Type: text/html; charset=utf-8
    Connection: close
    X-Powered-By: PHP/5.4.11--pl2-gentoo

    sdfsdfsf
    Cierre
    Hecho !

Conexión a un socket UNIX, lectura de la respuesta desde el servidor, y visualización en una consola

```
<?php
class MyUnixSocketClient {
    private $base, $bev;

    function __construct($base, $sock_path) {
        $this->base = $base;
        $this->bev = new EventBufferEvent($base, NULL, EventBufferEvent::OPT_CLOSE_ON_FREE,
            array ($this, "read_cb"), NULL, array ($this, "event_cb"));

        if (!$this->bev->connect("unix:$sock_path")) {
            trigger_error("Fallo al conectar al socket `$sock_path'", E_USER_ERROR);
        }

        $this->bev->enable(Event::READ);
    }

    function __destruct() {
        if ($this->bev) {
            $this->bev->free();
            $this->bev = NULL;
        }
    }

    function dispatch() {
        $this->base->dispatch();
    }

    function read_cb($bev, $unused) {
        $in = $bev->input;

        printf("Recepción de %ld bytes\n", $in->length);
        printf("----- datos ----\n");
        printf("%ld:\t%s\n", (int) $in->length, $in->pullup(-1));

        $this->bev->free();
        $this->bev = NULL;
        $this->base->exit(NULL);
    }

    function event_cb($bev, $events, $unused) {
        if ($events & EventBufferEvent::ERROR) {
            echo "Error desde bufferevent\n";
        }

        if ($events & (EventBufferEvent::EOF | EventBufferEvent::ERROR)) {
            $bev->free();
            $bev = NULL;
        } elseif ($events & EventBufferEvent::CONNECTED) {
            $bev->output->add("test\n");
        }
    }
}

if ($argc <= 1) {
    exit("La ruta hacia el socket no está proporcionada\n");
}
$sock_path = $argv[1];

$base = new EventBase();
$cl = new MyUnixSocketClient($base, $sock_path);
$cl->dispatch();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Recepción de 5 bytes
    ----- datos ----
    5:  test

## Véase también

EventBufferEvent::connectHost
