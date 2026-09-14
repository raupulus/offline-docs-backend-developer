---
title: ZMQSocket::recv
description: Recibir un mensaje
source_url: https://www.php.net/manual/es/zmqsocket.recv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqsocket/recv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 109430
---

ZMQSocket::recv

Recibir un mensaje

## Descripción

```php
public ZMQSocket::recv([int $mode]): string
```php

Recibe un mensaje de un socket. Por defecto, la recepción quedará en espera hasta que haya disponible un mensaje, a menos que se emplee la bandera `ZMQ::MODE_DONTWAIT`. Se puede emplear la opción de socket `ZMQ::SOCKOPT_RCVMORE` para recibir mensajes multiparte. Véase `ZMQSocket::setSockOpt` para más información.

## Parámetros

`mode`  
Proporcionar banderas de modo para recibir mensajes multiparte o hacer que la operación no quede en espera. Véanse las constantes `ZMQ::MODE_*`.

## Valores devueltos

Devuelve el mensaje. Si se emplea `ZMQ::MODE_DONTWAIT` y la operación debería quedar en espera, se devolverá `false`.

## Errores/Excepciones

Lanza una `ZMQSocketException` en caso de error.

## Ejemplos

Un ejemplo de send/recv

Envío / respuesta sin esperas

```
<?php

/* Crear un nuevo objeto cola, debe existir un servidor en el otro extremo */
$cola = new ZMQSocket(new ZMQContext(), ZMQ::SOCKET_REQ);
$cola->connect("tcp://127.0.0.1:5555");

/* Asginar el socket 1 a la cola, enviar y recibir */
$reintentos = 5;
$sending = true;

/* Iniciar y recorrer */
do {
    try {
        /* Intentar enviar / recibir */
        if ($sending) {
            echo "Enviando el mensaje\n";
            $cola->send("Este es un mensaje", ZMQ::MODE_DONTWAIT);
            $sending = false;
        } else {
            echo "Respuesta obtenida: " . $cola->recv(ZMQ::MODE_DONTWAIT) . "\n";
            break;
        }
    } catch (ZMQSocketException $e) {
        /* EAGAIN significa que la operación tendrá que esperar, reintentar */
        if ($e->getCode() === ZMQ::ERR_EAGAIN) {
            echo " - EAGAIN, reintentando ($reintentos)\n";
        } else {
            die(" - Error: " . $e->getMessage());
        }
    }
    /* Dormir un poco entre operaciones */
    usleep(5);
} while (--$reintentos);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Enviando el mensaje
     - Unable to execute operation, retrying (4)
    Respuesta obtenida: Este es un mensaje
