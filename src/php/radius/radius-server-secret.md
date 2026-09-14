---
title: radius_server_secret
description: Devuelve el secreto compartido
source_url: https://www.php.net/manual/es/function.radius-server-secret.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-server-secret.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67800
---

radius_server_secret

Devuelve el secreto compartido

## Descripción

```php
radius_server_secret(resource $radius_handle): string
```php

El secreto compartido es necesario para el restablecimiento de los datos como las contraseñas y las claves de cifrado.

## Parámetros

`radius_handle`  
El recurso RADIUS.

## Valores devueltos

Devuelve el secreto compartido del servidor como un string o `false` en caso de error.
