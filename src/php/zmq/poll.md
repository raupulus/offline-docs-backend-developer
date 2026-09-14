---
title: ZMQPoll::poll
description: Sondear los elementos
source_url: https://www.php.net/manual/es/zmqpoll.poll.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqpoll/poll.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: d53089934
order: 109300
---

ZMQPoll::poll

Sondear los elementos

## Descripción

```php
public ZMQPoll::poll(array $readable, array $writable, [int $timeout]): int
```php

Sondea los elementos en el conjunto de sondeo actual. Los elementos legibles y escribibles son devueltos en los parámetros `readable` y `writable` respectivamente. Se puede utilizar `ZMQPoll::getLastErrors` para comprobar si existen errores.

## Parámetros

`readable`  
Un array donde se sevuelven los flujos de PHP/ZMQSockets legibles. El array se limpiará al inicio de la operación.

`writable`  
Un array donde se sevuelven los flujos de PHP/ZMQSockets escribibles. El array se limpiará al inicio de la operación.

`timeout`  
Tiempo de espera de la operación. -1 significa que el sondeo esperará hasta que al menos un elemento tenga actividad. Observe que desde la versión 1.0.0, el tiempo de espera del sondeo está definido en milisegundos, en lugar de en microsegundos.

## Valores devueltos

Devuelve un número entero que representa la cantidad de elementos con actividad.

## Errores/Excepciones

Lanza una `ZMQPollException` en caso de error.

## Ejemplos

Un ejemplo de `ZMQPoll`

Crear un servidor de sondeos sencillo

```
<?php

/* Crear un socket, patrón de petición-respuesta (socket de respuesta) */
$context = new ZMQContext();
$server  = $context->getSocket(ZMQ::SOCKET_REP);

/* Vincular al puerta 5555 en 127.0.0.1 */
$server->bind("tcp://127.0.0.1:5555");

/* Crear un conjunto de sondeo nuevo para mensajes entrantes/salientes */
$poll = new ZMQPoll();

/* Añadir el objeto y escuchar la entrada/salida del sondeo */
$id = $poll->add($server, ZMQ::POLL_IN | ZMQ::POLL_OUT);
echo "Se añaió el objeto con id " . $id . "\n";

/* Inicializar los arrays readable y writable */
$readable = array();
$writable = array();

while (true) {
   /* Cantidad de eventos recuperados */
   $events = 0;

   try {
       /* Sondear hasta que haya algo que hacer */
       $events = $poll->poll($readable, $writable, -1);
       $errors = $poll->getLastErrors();

       if (count($errors) > 0) {
           foreach ($errors as $error) {
               echo "Error al sondear el objeto " . $error . "\n";
           }
       }
   } catch (ZMQPollException $e) {
       echo "Fallón el sondeo: " . $e->getMessage() . "\n";
   }

   if ($events > 0) {
       /* Recorrer los objetos legibles y los mensajes recibidos */
       foreach ($readable as $r) {
           try {
               echo "Mensaje recibido: " . $r->recv() . "\n";
           } catch (ZMQException $e) {
               echo "Falló la recepción: " . $e->getMessage() . "\n";
           }
       }

       /* Recorrer los objetos escribibles y enviar de vuelta los mensajes */
       foreach ($writable as $w) {
           try {
               $w->send("Got it!");
           } catch (ZMQException $e) {
               echo "Falló el envío: " . $e->getMessage() . "\n";
           }
       }
   }
}
?>

    
```php
