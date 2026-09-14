---
title: radius_request_authenticator
description: Devuelve el identificador solicitado
source_url: https://www.php.net/manual/es/function.radius-request-authenticator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-request-authenticator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67770
---

radius_request_authenticator

Devuelve el identificador solicitado

## Descripción

```php
radius_request_authenticator(resource $radius_handle): string
```php

El identificador solicitado es necesario para la recuperación de datos como contraseñas y claves de cifrado.

## Parámetros

`radius_handle`  
El recurso RADIUS.

## Valores devueltos

Devuelve el identificador solicitado como string o `false` en caso de error.

## Véase también

radius_demangle
