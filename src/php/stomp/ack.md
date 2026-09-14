---
title: Stomp::ack
description: Confirmar la recepción y el consumo de un mensaje
source_url: https://www.php.net/manual/es/stomp.ack.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/stomp/ack.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_reviewed: false
translation_revision: 9c7e8795c
order: 87540
---

Stomp::ack

stomp_ack

Confirmar la recepción y el consumo de un mensaje

## Descripción

Estilo orientado a objetos (método):

```php
public Stomp::ack(mixed $msg, [array $headers]): bool
```php

Estilo procedimental:

```php
stomp_ack(resource $link, mixed $msg, [array $headers]): bool
```

Confirmar el consumo de un mensaje desde una suscripción enviando el cliente una trama ACK de confirmación.

## Parámetros

`link`  
Estilo procedimental únicamente: El identificador stomp devuelto por la función`stomp_connect`.

`msg`  
El mensaje/Id del mensaje a ser confirmado.

`headers`  
Array asociativo que contiene los encabezados adicionales (ejemplo: receipt).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Estilo orientado a objetos

```php
<?php

$queue  = '/queue/foo';
$msg    = 'bar';

/* conexión */
try {
    $stomp = new Stomp('tcp://localhost:61613');
} catch(StompException $e) {
    die('Connection failed: ' . $e->getMessage());
}

/* enviar un mensaje a la cola 'foo' */
$stomp->send($queue, $msg);

/* suscribirse a mensajes de la cola 'foo' */
$stomp->subscribe($queue);

/* leer una trama */
$frame = $stomp->readFrame();

if ($frame->body === $msg) {
    /* confirmar que la trama fue recibida */
    $stomp->ack($frame);
}

/* eliminar la suscripción */
$stomp->unsubscribe($queue);

/* cerrar la conexión */
unset($stomp);

?>

    
```

Estilo procedimental

```php
<?php

$queue  = '/queue/foo';
$msg    = 'bar';

/* conexión */
$link = stomp_connect('ssl://localhost:61612');

/* comprobar la conexión */
if (!$link) {
    die('Connection failed: ' . stomp_connect_error());
}

/* iniciar una transacción */
stomp_begin($link, 't1');

/* enviar un mensaje a la cola 'foo' */
stomp_send($link, $queue, $msg, array('transaction' => 't1'));

/* validar una transacción */
stomp_commit($link, 't1');

/* suscribirse a mensajes de la cola 'foo' */
stomp_subscribe($link, $queue);

/* leer una trama */
$frame = stomp_read_frame($link);

if ($frame['body'] === $msg) {
    /* confirmar que la trama fue recibida */
    stomp_ack($link, $frame['headers']['message-id']);
}

/* eliminar la suscripción */
stomp_unsubscribe($link, $queue);

/* cerrar la conexión */
stomp_close($link);

?>

    
```

## Notas

> [!NOTE]
> Un encabezado de transacción puede ser especificado, indicando que la confirmación de los mensajes debe ser parte de la transacción.

> [!TIP]
> Stomp es, por naturaleza, asíncrono. Una comunicación síncrona puede ser implementada añadiendo un encabezado receipt. Esto hará que los métodos no devuelvan nada hasta que el mensaje de confirmación no haya sido recibido o hasta que el tiempo de espera no sea alcanzado.
