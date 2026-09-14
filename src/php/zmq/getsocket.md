---
title: ZMQContext::getSocket
description: Crear un nuevo socket
source_url: https://www.php.net/manual/es/zmqcontext.getsocket.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqcontext/getsocket.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 109100
---

ZMQContext::getSocket

Crear un nuevo socket

## Descripción

```php
public ZMQContext::getSocket(int $type, [string $persistent_id], [callable $on_new_socket]): ZMQSocket
```php

Método rápido para crear nuevos sockets desde un contexto. Si el contexto no es persistente, el parámetro `persistent_id` es ignorado y el socket se convierte en no persistente. `on_new_socket` solamente se invoca cuando se crea una estructura de socket subyacente.

## Parámetros

`type`  
Constante `ZMQ::SOCKET_*` para especificar el tipo de socket.

`persistent_id`  
Si se especifica `persistent_id`, el socket será persistente durante varias peticiones.

`on_new_socket`  
Función de retrollamada que es ejecutada cuando se crea una nueva estrucutra de socket. Esta función no es invocada si la conexión persistente subyacente es reutilizada. La retrollamada toma ZMQSocket y persistent_id como dos argumentos.

## Valores devueltos

Devuelve un objeto `ZMQSocket`.

## Errores/Excepciones

Lanza una `ZMQSocketException` en caso de error.

## Ejemplos

Un ejemplo de `ZMQContext`

Uso básico

```
<?php
/* Asignar un nuevo contexto */
$context = new ZMQContext();

/* Crear un nuevo socket */
$socket = $context->getSocket(ZMQ::SOCKET_REQ, 'my sock');

/* Conectar con el socket */
$socket->connect("tcp://example.com:1234");

/* Enviar una petición */
$socket->send("Hello there");

/* Recibir la respuesta */
$message = $socket->recv();
echo "Received message: {$message}\n";
?>

    
```php
