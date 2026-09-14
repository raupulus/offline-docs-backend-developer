---
title: EventSslContext::__construct
description: Construye un contexto OpenSSL para usar con las clases Event
source_url: https://www.php.net/manual/es/eventsslcontext.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventsslcontext/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 20410
---

EventSslContext::\_\_construct

Construye un contexto OpenSSL para usar con las clases Event

## Descripción

```php
public EventSslContext::__construct(string $method, string $options)
```php

Crea un contexto SSL que contiene el puntero hacia `SSL_CTX` (ver el manual del sistema).

## Parámetros

`method`  
Una de las constantes [`EventSslContext::*_METHOD`](#eventsslcontext.constants).

`options`  
Un array asociativo de opciones de contexto SSL. Una de las constantes [`EventSslContext::OPT_*`](#eventsslcontext.constants).

## Ejemplos

Ejemplo con `EventSslContext::__construct`

```
<?php
$ctx = new EventSslContext(EventSslContext::SSLv3_SERVER_METHOD, array(
     EventSslContext::OPT_LOCAL_CERT        => $local_cert,
     EventSslContext::OPT_LOCAL_PK          => $local_pk,
     EventSslContext::OPT_PASSPHRASE        => "echo server",
     EventSslContext::OPT_VERIFY_PEER       => true,
     EventSslContext::OPT_ALLOW_SELF_SIGNED => false,
));
?>

   
```php
