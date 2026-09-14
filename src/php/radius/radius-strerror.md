---
title: radius_strerror
description: Devuelve un mensaje de error
source_url: https://www.php.net/manual/es/function.radius-strerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-strerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_revision: 9ac4d06c0
order: 67810
---

radius_strerror

Devuelve un mensaje de error

## Descripción

```php
radius_strerror(resource $radius_handle): string
```php

Si las funciones radio fallan entonces guardan un mensaje de error. Este mensaje de error puede ser obtenido con esta función.

## Parámetros

`radius_handle`  
El recurso RADIUS.

## Valores devueltos

Devuelve mensajes de error como string de funciones radio fallidas.
