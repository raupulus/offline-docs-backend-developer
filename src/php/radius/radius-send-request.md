---
title: radius_send_request
description: Envía una solicitud y espera una respuesta
source_url: https://www.php.net/manual/es/function.radius-send-request.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-send-request.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67790
---

radius_send_request

Envía una solicitud y espera una respuesta

## Descripción

```php
radius_send_request(resource $radius_handle): int
```php

Una vez que se ha construido una solicitud Radius, esta es enviada mediante la función `radius_send_request`.

La función `radius_send_request` envía la solicitud y espera una respuesta válida, intentando de nuevo, según el método `round-robin` siempre que sea necesario.

## Parámetros

`radius_handle`  
El recurso RADIUS.

## Valores devueltos

Si se recibe una respuesta válida, `radius_send_request` devuelve el código Radius que especifica el tipo de respuesta. Esto es, típicamente, `RADIUS_ACCESS_ACCEPT`, `RADIUS_ACCESS_REJECT` o `RADIUS_ACCESS_CHALLENGE`. Si no se recibe ninguna respuesta válida, `radius_send_request` devolverá `false`.

## Véase también

radius_create_request
