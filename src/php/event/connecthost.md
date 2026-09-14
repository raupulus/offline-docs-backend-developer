---
title: EventBufferEvent::connectHost
description: Conexión a un host con resolución de DNS asíncrona (opcional)
source_url: https://www.php.net/manual/es/eventbufferevent.connecthost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/connecthost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 19400
---

EventBufferEvent::connectHost

Conexión a un host con resolución de DNS asíncrona (opcional)

## Descripción

```php
public EventBufferEvent::connectHost(EventDnsBase $dns_base, string $hostname, int $port, [int $family]): bool
```php

Resuelve el nombre de host DNS, buscando la dirección del tipo `family` (constante `EventUtil::AF_*`). Si la resolución del nombre falla, la función de retrollamada del evento será llamada con un evento de error. Si la resolución tiene éxito, se realizará un intento de conexión, de manera similar a como lo hace el método EventBufferEvent::connect.

El parámetro `dns_base` es opcional. Puede ser `null`, o bien un objeto creado con el método EventDnsBase::\_\_construct. Para una resolución de nombre de host asíncrona, pase una fuente de evento de base DNS válida. De lo contrario, la resolución del nombre de host será bloqueante.

> [!NOTE]
> `EventDnsBase` solo está disponible si `Event` está configurado con la opción `--with-event-extra` (biblioteca `event_extra`, *el soporte de las funcionalidades específicas de libevent incluyendo HTTP, DNS y RPC*).

> [!NOTE]
> EventBufferEvent::connectHost requiere `libevent-2.0.3-alpha` o posteriores.

## Parámetros

`dns_base`  
Objeto `EventDnsBase` en el caso donde el DNS debe ser resuelto de manera asíncrona. De lo contrario, `null`.

`hostname`  
El nombre de host al cual se intenta realizar la conexión. Los formatos reconocidos son:

     www.example.com (hostname)
     1.2.3.4 (ipv4address)
     ::1 (ipv6address)
    [::1] ([ipv6address])

          

`port`  
El número del puerto

`family`  
Familia de la dirección. `EventUtil::AF_UNSPEC`, `EventUtil::AF_INET` o `EventUtil::AF_INET6`. Ver las [constantes EventUtil](#eventutil.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `EventBufferEvent::connectHost`

```
<?php
/* Función de retrollamada de lectura */
function readcb($bev, $base) {
    //$input = $bev->input; //$bev->getInput();

    //$pos = $input->search("TTP");
    $pos = $bev->input->search("TTP");

    while (($n = $bev->input->remove($buf, 1024)) > 0) {
        echo $buf;
    }
}

/* Función de retrollamada del evento */
function eventcb($bev, $events, $base) {
    if ($events & EventBufferEvent::CONNECTED) {
        echo "Conectado.\n";
    } elseif ($events & (EventBufferEvent::ERROR | EventBufferEvent::EOF)) {
        if ($events & EventBufferEvent::ERROR) {
            echo "Error DNS: ", $bev->getDnsErrorString(), PHP_EOL;
        }

        echo "Cerrando\n";
        $base->exit();
        exit("Hecho !\n");
    }
}

$base = new EventBase();

$dns_base = new EventDnsBase($base, TRUE); // Resolución DNS asíncrona
if (!$dns_base) {
    exit("Fallo en la inicialización de la base DNS\n");
}

$bev = new EventBufferEvent($base, /* uso de un socket interno */ NULL,
    EventBufferEvent::OPT_CLOSE_ON_FREE | EventBufferEvent::OPT_DEFER_CALLBACKS,
    "readcb", /* writecb */ NULL, "eventcb", $base
);
if (!$bev) {
    exit("Fallo al crear el socket bufferevent\n");
}

//$bev->setCallbacks("readcb", /* writecb */ NULL, "eventcb", $base);
$bev->enable(Event::READ | Event::WRITE);

$output = $bev->output; //$bev->getOutput();
if (!$output->add(
    "GET {$argv[2]} HTTP/1.0\r\n".
    "Host: {$argv[1]}\r\n".
    "Connection: Close\r\n\r\n"
)) {
    exit("Fallo al añadir la solicitud en el búfer de salida\n");
}

if (!$bev->connectHost($dns_base, $argv[1], 80, EventUtil::AF_UNSPEC)) {
    exit("Imposible conectar al host {$argv[1]}\n");
}

$base->dispatch();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Conectado.
    HTTP/1.0 301 Moved Permanently
    Location: http://www.google.co.uk/
    Content-Type: text/html; charset=UTF-8
    Date: Sat, 09 Mar 2013 12:21:19 GMT
    Expires: Mon, 08 Apr 2013 12:21:19 GMT
    Cache-Control: public, max-age=2592000
    Server: gws
    Content-Length: 221
    X-XSS-Protection: 1; mode=block
    X-Frame-Options: SAMEORIGIN

    <HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
    <TITLE>301 Moved</TITLE></HEAD><BODY>
    <H1>301 Moved</H1>
    The document has moved
    <A HREF="http://www.google.co.uk/">here</A>.
    </BODY></HTML>
    Cerrando
    Hecho !

## Véase también

EventBufferEvent::connect
