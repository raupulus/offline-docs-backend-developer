---
title: EventBufferEvent::getOutput
description: Devuelve el búfer de salida asociado con el búfer de evento actual
source_url: https://www.php.net/manual/es/eventbufferevent.getoutput.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/getoutput.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 59a1bbcb6
order: 19490
---

EventBufferEvent::getOutput

Devuelve el búfer de salida asociado con el búfer de evento actual

## Descripción

```php
public EventBufferEvent::getOutput(): EventBuffer
```php

Devuelve el búfer de salida asociado con el búfer de evento actual. Un búfer de salida es un almacenamiento para los datos a escribir.

Tenga en cuenta que también hay propiedades de `salida` para la clase `EventBufferEvent`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una instancia del búfer de salida `EventBuffer` asociado con el búfer de eventos actual.

## Ejemplos

Ejemplo con `EventBufferEvent::getOutput`

```
<?php
$base = new EventBase();

$dns_base = new EventDnsBase($base, TRUE); // Uso de la resolución async DNS
if (!$dns_base) {
    exit("Fallo al inicializar la base DNS\n");
}

$bev = new EventBufferEvent($base, /* usar socket interno */ NULL,
    EventBufferEvent::OPT_CLOSE_ON_FREE | EventBufferEvent::OPT_DEFER_CALLBACKS,
    "readcb", /* writecb */ NULL, "eventcb", $base
);
if (!$bev) {
    exit("Fallo al crear el socket bufferevent\n");
}

$bev->enable(Event::READ | Event::WRITE);

$output = $bev->getOutput();
if (!$output->add(
    "GET {$argv[2]} HTTP/1.0\r\n".
    "Host: {$argv[1]}\r\n".
    "Connection: Close\r\n\r\n"
)) {
    exit("Fallo al añadir la solicitud en el búfer de salida\n");
}

/* ... */
?>

   
```php

## Véase también

EventBufferEvent::getInput
