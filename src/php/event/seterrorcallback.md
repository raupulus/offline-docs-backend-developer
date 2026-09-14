---
title: EventListener::setErrorCallback
description: Define la función de retrollamada en el evento de error
source_url: https://www.php.net/manual/es/eventlistener.seterrorcallback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventlistener/seterrorcallback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: a47dff201
order: 20390
---

EventListener::setErrorCallback

Define la función de retrollamada en el evento de error

## Descripción

```php
public EventListener::setErrorCallback(string $cb): void
```php

Define la función de retrollamada en el evento de error.

## Parámetros

`cb`  
La función de retrollamada para el error. Debe corresponder al siguiente prototipo:

```php
callback([EventListener $listener], [mixed $data]): void
```

`listener`  
El objeto `EventListener`.

`data`  
Datos personalizados del usuario para asociar a la función de retrollamada.

## Valores devueltos

## Véase también

EventListener::setCallback
