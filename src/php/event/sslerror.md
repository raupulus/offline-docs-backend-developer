---
title: EventBufferEvent::sslError
description: Devuelve el error OpenSSL más reciente reportado por el buffer de eventos
source_url: https://www.php.net/manual/es/eventbufferevent.sslerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/sslerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 19560
---

EventBufferEvent::sslError

Devuelve el error OpenSSL más reciente reportado por el buffer de eventos

## Descripción

```php
public EventBufferEvent::sslError(): string
```php

Devuelve el error OpenSSL más reciente reportado por el buffer de eventos.

> [!NOTE]
> Este método solo está disponible si `Event` ha sido compilado con soporte OpenSSL.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la cadena de error OpenSSL reportada por el buffer de eventos o `false` si no hay más errores que devolver.

## Ejemplos

Ejemplo con `EventBufferEvent::sslError`

```
<?php
// Esta función de retrollamada será llamada cuando ocurran eventos
// en el oyente de eventos, es decir, cierre de conexión, o cuando ocurra
// un error.
function ssl_event_cb($bev, $events, $ctx) {
    if ($events & EventBufferEvent::ERROR) {
        // Recupera los errores desde la pila de errores SSL
        while ($err = $bev->sslError()) {
            fprintf(STDERR, "Bufferevent error %s.\n", $err);
        }
    }

    if ($events & (EventBufferEvent::EOF | EventBufferEvent::ERROR)) {
        $bev->free();
    }
}
?>

   
```php

## Véase también

EventBufferEvent::sslRenegotiate
