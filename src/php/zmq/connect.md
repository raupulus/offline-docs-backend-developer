---
title: ZMQSocket::connect
description: Contectar el socket
source_url: https://www.php.net/manual/es/zmqsocket.connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqsocket/connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: d53089934
order: 109350
---

ZMQSocket::connect

Contectar el socket

## Descripción

```php
public ZMQSocket::connect(string $dsn, [bool $force]): ZMQSocket
```php

Contecta el socket a un extremo remoto. El extremo está definido en formato `transporte://dirección` donde transporte es uno de los siguientes: inproc, ipc, tcp, pgm o epgm.

## Parámetros

`dsn`  
El DSN de la conexión, por ejemplo `transporte://dirección`.

`force`  
Intenta la conexión incluso si elm socket ya ha sido conectado al extremo dado.

## Valores devueltos

Devuelve el objeto actual.

## Errores/Excepciones

Lanza una `ZMQSocketException` en caso de error.

## Ejemplos

Un ejemplo de `ZMQContext`

Construir un nuevo contexto y asignar un socket de petición

```
<?php
/* Nombre de host del servidor */
$dsn = "tcp://127.0.0.1:5555";

/* Crear un socket */
$socket = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REQ, 'my socket');

/* Obtener una lista de los extremos conectados */
$endpoints = $socket->getEndpoints();

/* Comprobar si el socket está conectado */
if (!in_array($dsn, $endpoints['connect'])) {
    echo "<p>Conectando a $dsn</p>";
    $socket->connect($dsn);
} else {
    echo "<p>Ya se ha contectado a $dsn</p>";
}

/* Enviar y recibir */
$socket->send("¡Hola!");
$message = $socket->recv();

echo "<p>El servidor dice: {$message}</p>";
?>

    
```php
