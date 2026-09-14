---
title: Ejemplos
source_url: https://www.php.net/manual/es/stomp.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_revision: d0ec3a70d
order: 87480
---

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

/* Enviar un mensaje a la cola 'foo' */
$stomp->send($queue, $msg);

/* suscribirse a mensajes de la cola 'foo' */
$stomp->subscribe($queue);

/* leer una trama (frame) */
$frame = $stomp->readFrame();

if ($frame->body === $msg) {
    var_dump($frame);

    /* reconocer que la trama (frame) fue recibida */
    $stomp->ack($frame);
}

/* cerrar conexión */
unset($stomp);

?>

   
```

Resultado del ejemplo anterior es similar a:

    object(StompFrame)#2 (3) {
      ["command"]=>
      string(7) "MESSAGE"
      ["headers"]=>
      array(5) {
        ["message-id"]=>
        string(41) "ID:php.net-55293-1257226743606-4:2:-1:1:1"
        ["destination"]=>
        string(10) "/queue/foo"
        ["timestamp"]=>
        string(13) "1257226805828"
        ["expires"]=>
        string(1) "0"
        ["priority"]=>
        string(1) "0"
      }
      ["body"]=>
      string(3) "bar"
    }

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

/* Enviar un mensaje a la cola 'foo' */
stomp_send($link, $queue, $msg, array('transaction' => 't1'));

/* confirmar una transacción */
stomp_commit($link, 't1');

/* suscribirse a mensajes de la cola 'foo' */
stomp_subscribe($link, $queue);

/* leer una trama (frame) */
$frame = stomp_read_frame($link);

if ($frame['body'] === $msg) {
    var_dump($frame);

    /* reconocer que la trama fue recibida */
    stomp_ack($link, $frame['headers']['message-id']);
}

/* cerrar conexión */
stomp_close($link);

?>

   
```

Resultado del ejemplo anterior es similar a:

    array(3) {
      ["command"]=>
      string(7) "MESSAGE"
      ["body"]=>
      string(3) "bar"
      ["headers"]=>
      array(6) {
        ["transaction"]=>
        string(2) "t1"
        ["message-id"]=>
        string(41) "ID:php.net-55293-1257226743606-4:3:-1:1:1"
        ["destination"]=>
        string(10) "/queue/foo"
        ["timestamp"]=>
        string(13) "1257227037059"
        ["expires"]=>
        string(1) "0"
        ["priority"]=>
        string(1) "0"
      }
    }
