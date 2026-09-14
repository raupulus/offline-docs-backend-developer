---
title: EventHttp::accept
description: Permite a un servidor HTTP aceptar las conexiones en el socket o recurso
  especificado
source_url: https://www.php.net/manual/es/eventhttp.accept.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttp/accept.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 85d72c538
order: 19850
---

EventHttp::accept

Permite a un servidor HTTP aceptar las conexiones en el socket o recurso especificado

## Descripción

```php
public EventHttp::accept(mixed $socket): bool
```php

Permite a un servidor HTTP aceptar las conexiones en el socket o recurso especificado. El socket debe estar listo para aceptar las conexiones.

Puede ser llamado varias veces para aceptar las conexiones en diferentes sockets.

> [!NOTE]
> Para enlazar un socket, una conexión `listen` y una conexión `accept` en el socket en una sola llamada, utilice el método EventHttp::bind. EventHttp::accept solo es necesario si un socket está listo para aceptar las conexiones.

## Parámetros

`socket`  
Socket, flujo, o descriptor numérico de fichero representando un socket listo para aceptar las conexiones.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `EventHttp::accept`

```
<?php

$base = new EventBase();
$http = new EventHttp($base);

$addresses = [
     8091 => "127.0.0.1",
     8092 => "127.0.0.2",
];
$i = 0;

$socket = array();

foreach ($addresses as $port => $ip) {
    echo $ip, " ", $port, PHP_EOL;
    $socket[$i] = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    if (!socket_bind($socket[$i], $ip, $port)) {
        exit("fallo de socket_bind\n");
    }
    socket_listen($socket[$i], 0);
    socket_set_nonblock($socket[$i]);

    if (!$http->accept($socket[$i])) {
        echo "La aceptación ha fallado\n";
        exit(1);
    }

    ++$i;
}

$http->setCallback("/some-page", function() {
 echo "(some-page)\n";
    echo "URI : ", $req->getUri(), PHP_EOL;
    $req->sendReply(200, "OK");
    echo "OK\n";
});

$http->setDefaultCallback(function($req) {
    echo "URI : ", $req->getUri(), PHP_EOL;
    $req->sendReply(200, "OK");
    echo "OK\n";
});

$signal = Event::signal($base, SIGINT, function () use ($base) {
    echo "SIGINT recibido. Deteniendo...\n";
    $base->stop();
});
$signal->add();

$base->dispatch();
echo "END\n";

// No cerramos los sockets, sabiendo que Libevent ya establece
// los flags CLOSE_ON_FREE y CLOSE_ON_EXEC en el descriptor
// de fichero con los sockets.
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Cliente:
    $ nc 127.0.0.1 8091
    GET /about HTTP/1.0
    Connection: close

    HTTP/1.0 200 OK
    Content-Type: text/html; charset=ISO-8859-1
    Connection: close

    Servidor:
    127.0.0.1 8091
    127.0.0.2 8092
    URI : /about
    OK

## Véase también

EventHttp::bind
