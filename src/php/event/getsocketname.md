---
title: EventListener::getSocketName
description: Recupera la dirección actual a la que está ligado el socket de escucha
source_url: https://www.php.net/manual/es/eventlistener.getsocketname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventlistener/getsocketname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 20370
---

EventListener::getSocketName

Recupera la dirección actual a la que está ligado el socket de escucha

## Descripción

```php
public static EventListener::getSocketName(string $address, [mixed $port]): bool
```php

Recupera la dirección actual a la que está ligado el socket de escucha.

## Parámetros

`address`  
Parámetro de salida. La dirección IP según la familia de direcciones del socket.

`port`  
Parámetro de salida. El puerto al que está ligado el socket.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
