---
title: EventHttpConnection::__construct
description: Construye un objeto EventHttpConnection
source_url: https://www.php.net/manual/es/eventhttpconnection.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttpconnection/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: a47dff201
order: 19970
---

EventHttpConnection::\_\_construct

Construye un objeto EventHttpConnection

## Descripción

```php
public EventHttpConnection::__construct(EventBase $base, EventDnsBase $dns_base, string $address, int $port, [EventSslContext $ctx])
```php

Construye un objeto EventHttpConnection.

## Parámetros

`base`  
Base de evento asociada.

`dns_base`  
Si vale `null`, la resolución del nombre de host será bloqueante.

`address`  
La dirección de conexión.

`port`  
El puerto de conexión.

`ctx`  
El objeto de la clase `EventSslContext`. Activa OpenSSL.

> [!NOTE]
> Este parámetro solo está disponible si `Event` ha sido compilado con soporte OpenSSL, y únicamente con la versión `Libevent 2.1.0-alpha` y superiores.

## Historial de cambios

| Versión          | Descripción                         |
|------------------|-------------------------------------|
| PECL event 1.9.0 | Añadido soporte de OpenSSL (`ctx`). |
