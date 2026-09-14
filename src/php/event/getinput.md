---
title: EventBufferEvent::getInput
description: Devuelve el búfer de entrada asociado con el búfer de eventos actual
source_url: https://www.php.net/manual/es/eventbufferevent.getinput.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/getinput.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 59a1bbcb6
order: 19480
---

EventBufferEvent::getInput

Devuelve el búfer de entrada asociado con el búfer de eventos actual

## Descripción

```php
public EventBufferEvent::getInput(): EventBuffer
```php

Devuelve el búfer de entrada asociado con el búfer de eventos actual. Un búfer de entrada es un almacenamiento para los datos a leer.

Téngase en cuenta que también hay propiedades de `entrada` para la clase `EventBufferEvent`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una instancia del búfer de entrada `EventBuffer` asociado con el búfer de eventos actual.

## Ejemplos

Función de retrollamada para un evento de lectura en el búfer

```
<?php
function readcb($bev, $base) {
    $input = $bev->input; //$bev->getInput();

    while (($n = $input->remove($buf, 1024)) > 0) {
        echo $buf;
    }
}
?>

   
```php

## Véase también

EventBufferEvent::getOutput
