---
title: radius_close
description: Libera todos los recursos
source_url: https://www.php.net/manual/es/function.radius-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_revision: 9ac4d06c0
order: 67570
---

radius_close

Libera todos los recursos

## Descripción

```php
radius_close(resource $radius_handle): bool
```php

No es necesario llamar a esta función debido a que php libera todos los recursos al final de cada petición.

## Parámetros

`radius_handle`  
El recurso RADIUS.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
