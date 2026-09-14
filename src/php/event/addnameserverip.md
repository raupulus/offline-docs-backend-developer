---
title: EventDnsBase::addNameserverIp
description: Añade un servidor de nombres a la base DNS
source_url: https://www.php.net/manual/es/eventdnsbase.addnameserverip.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventdnsbase/addnameserverip.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: da9d81816
order: 19740
---

EventDnsBase::addNameserverIp

Añade un servidor de nombres a la base DNS

## Descripción

```php
public EventDnsBase::addNameserverIp(string $ip): bool
```php

Añade un servidor de nombres a evdns_base.

## Parámetros

`ip`  
El string que representa el servidor de nombres; puede ser una dirección IPv4, una dirección IPv6, una dirección IPv4 con un puerto (`IPv4:Port`), o una dirección IPv6 con un puerto (`[IPv6]:Port`).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
