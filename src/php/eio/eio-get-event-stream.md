---
title: eio_get_event_stream
description: Obtiene un flujo que representa una variable usada en comnunicaciones
  internas con libeio
source_url: https://www.php.net/manual/es/function.eio-get-event-stream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-get-event-stream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16850
---

eio_get_event_stream

Obtiene un flujo que representa una variable usada en comnunicaciones internas con libeio

## Descripción

```php
eio_get_event_stream(): mixed
```php

`eio_get_event_stream` adquiere un flujo que representa una variable usada en comunicaciones internas con libeio. Se podría usar para vinculaciones con algún bucle de eventos proporcionado por otra extensión PECL, por ejemplo libevent.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`eio_get_event_stream` devuelve un flujo en caso de éxito; de otro modo devuelve `null`

## Ejemplos

Usar eio con libevent

```
<?php
function mi_eio_poll($df, $eventos, $argumento) {
    /* Algunas regulaciones de libevent podrían ir aquí .. */
    if (eio_nreqs()) {
        eio_poll();
    }
    /* .. y aquí */
}

function my_res_cb($d, $r) {
    var_dump($r); var_dump($d);
}

$base = event_base_new();
$evento = event_new();

$df = eio_get_event_stream();
var_dump($df);

eio_nop(EIO_PRI_DEFAULT, "my_res_cb", "nop data");
eio_mkdir("/tmp/abc-eio-temp", 0750, EIO_PRI_DEFAULT, "my_res_cb", "mkdir data");
/* algunas llamadas eio_* aquí ... */

// establecer la banderas del evento
event_set($evento, $df, EV_READ /*| EV_PERSIST*/, "mi_eio_poll", array($evento, $base));

// establecer la base del evento
event_base_set($evento, $base);

// habilitar el evento
event_add($evento);

// iniciar el bucle de eventos
event_base_loop($base);

/* Lo mismo estará disponible mediante interfaz libevent con buffer */
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(3)
    int(0)
    string(8) "nop data"
    int(0)
    string(10) "mkdir data"
