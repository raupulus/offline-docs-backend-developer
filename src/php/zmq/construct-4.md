---
title: ZMQSocket::__construct
description: Construir un nuevo ZMQSocket
source_url: https://www.php.net/manual/es/zmqsocket.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqsocket/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 109360
---

ZMQSocket::\_\_construct

Construir un nuevo ZMQSocket

## Descripción

```php
public ZMQSocket::__construct(ZMQContext $context, int $type, [string $persistent_id], [callable $on_new_socket])
```php

Construye un objeto ZMQSocket. Se puede utilizar el parámetro `persistent_id` para asignar un socket persistente. Un socket persistente tiene que ser asignado desde un contexto persistente, por lo que permanece conectado durante múltiples peticiones. Se puede emplear el parámetro `persistent_id` para recordar el mismo socket durante múltiples peticiones. `on_new_socket` es llamado solamente cuando se crea un nueva estructura de socket subyacente.

## Parámetros

`context`  
Un objeto ZMQContext.

`type`  
El tipo de socket. Véanse las constantes `ZMQ::SOCKET_*`.

`persistent_id`  
Si se especifica `persistent_id`, el socket será persistente durante múltiples peticiones. Si `context` no es persistente, el socket recurrirá al modo no persistente.

`on_new_socket`  
Función de retrollamada que es ejecutada cuando se crea una nueva estrucutra de socket. Esta función no es invocada si la conexión persistente subyacente es reutilizada.

```php
callback(ZMQSocket $socket, [string $persistent_id])
```

## Errores/Excepciones

Lanza una `ZMQSocketException` en caso de error.

## Ejemplos

Un ejemplo de `ZMQSocket`

Utilizar una callback para bind/connect del socket

```php
<?php

/*
  El socket es persistente, por lo que esta función es llamada solamente en la
  primera petición del script.
*/
function on_new_socket_cb(ZMQSocket $socket, $persistent_id = null)
{
    if ($persistent_id === 'server') {
        $socket->bind("tcp://localhost:12122");
    } else {
        $socket->connect("tcp://localhost:12122");
    }
}

/* Asignar un nuevo contexto */
$context = new ZMQContext();

/* Crear un nuevo socket */
$socket = $context->getSocket(ZMQ::SOCKET_REP, 'server', 'on_new_socket_cb');

$message = $socket->recv();
echo "Mensaje recibido: {$message}\n";
?>

     
```
