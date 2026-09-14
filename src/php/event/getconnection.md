---
title: EventHttpRequest::getConnection
description: Devuelve un objeto EventHttpConnection
source_url: https://www.php.net/manual/es/eventhttprequest.getconnection.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttprequest/getconnection.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 20180
---

EventHttpRequest::getConnection

Devuelve un objeto EventHttpConnection

## Descripción

```php
public EventHttpRequest::closeConnection(): EventHttpConnection
```php

Devuelve un objeto `EventHttpConnection` que representa una conexión HTTP asociada a la petición.

> [!WARNING]
> La API Libevent permite que los objetos de petición HTTP no estén ligados a una conexión HTTP. Sin embargo, no se puede disociar `EventHttpRequest` de `EventHttpConnection`. Por lo tanto, se construye el objeto `EventHttpConnection` sobre la marcha. Dado que no se dispone de información sobre el evento de base, la base DNS, ni sobre la función de retrollamada asociada al cierre de la conexión, se establecen estos campos como indefinidos.

El método EventHttpRequest::getConnection es habitualmente útil cuando se debe definir una función de retrollamada para asociarla al cierre de la conexión. Ver el método EventHttpConnection::setCloseCallback.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto `EventHttpConnection`.

## Véase también

EventHttpConnection::setCloseCallback

EventHttpRequest::getBufferEvent
