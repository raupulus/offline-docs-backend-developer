---
title: EventHttp::setAllowedMethods
description: Define los métodos HTTP soportados y aceptados en las peticiones en este
  servidor, y pasados a las funciones de retrollamada de los usuarios
source_url: https://www.php.net/manual/es/eventhttp.setallowedmethods.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttp/setallowedmethods.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 19900
---

EventHttp::setAllowedMethods

Define los métodos HTTP soportados y aceptados en las peticiones en este servidor, y pasados a las funciones de retrollamada de los usuarios

## Descripción

```php
public EventHttp::setAllowedMethods(int $methods): void
```php

Define los métodos HTTP soportados y aceptados en las peticiones en este servidor, y pasados a las funciones de retrollamada de los usuarios.

Si no son soportados, generarán una respuesta `"405 Method not allowed"`.

Por omisión, los siguientes métodos están incluidos: `GET`, `POST`, `HEAD`, `PUT`, y `DELETE`. Ver las constantes `EventHttpRequest::CMD_*`.

## Parámetros

`methods`  
Una máscara de [constantes `EventHttpRequest::CMD_*`](#eventhttprequest.constants).

## Valores devueltos

No se retorna ningún valor.
