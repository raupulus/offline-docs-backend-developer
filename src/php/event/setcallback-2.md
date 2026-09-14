---
title: EventListener::setCallback
description: El propósito de setCallback
source_url: https://www.php.net/manual/es/eventlistener.setcallback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventlistener/setcallback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: a47dff201
order: 20380
---

EventListener::setCallback

El propósito de setCallback

## Descripción

```php
public EventListener::setCallback(callable $cb, [mixed $arg]): void
```php

Coloca una retrollamada para el evento de conexión, y, opcionalmente, argumentos para esta retrollamada.

## Parámetros

`cb`  
La nueva retrollamada para las nuevas conexiones. Ignorada si vale `null`.

Debe corresponder al siguiente prototipo:

```php
callback([EventListener $listener], [mixed $fd], [array $address], [mixed $arg]): void
```

`listener`  
El objeto `EventListener`.

`fd`  
El descriptor de fichero o un recurso asociado a la escucha.

`address`  
Array de dos elementos: la dirección IP y el puerto del *servidor*.

`arg`  
Datos de usuario personalizados adjuntos a la retrollamada.

`arg`  
Datos de usuario personalizados adjuntos a la retrollamada. Ignorados si valen `null`.

## Valores devueltos

No se retorna ningún valor.
