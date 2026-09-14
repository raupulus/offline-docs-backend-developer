---
title: ZMQContext::__construct
description: Construir un nuevo objeto ZMQContext
source_url: https://www.php.net/manual/es/zmqcontext.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqcontext/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: d53089934
order: 109080
---

ZMQContext::\_\_construct

Construir un nuevo objeto ZMQContext

## Descripción

```php
public ZMQContext::__construct([int $io_threads], [bool $is_persistent])
```php

Construye un nuevo contexto ZMQ. Este se emplea para inicializar sockets. Se requiere una conexión persistente para inicializar sockets persistentes.

## Parámetros

`io_threads`  
Número de hilos de entrada/salida del contexto.

`is_persistent`  
Si el contexto es persistente. Los contextos persistentes se almacenan durante múltiples peticiones, por lo que son un requisito para los sockets persistentes.

## Errores/Excepciones

Lanza una `ZMQContextException` si la inicialización del contexto falla.

## Ejemplos

Un ejemplo de `ZMQContext`

Construir un nuevo contexto y asignarle un socket de petición

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
?>

    
```php
