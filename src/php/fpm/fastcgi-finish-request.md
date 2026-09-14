---
title: fastcgi_finish_request
description: Descarga todos los datos de la respuesta al cliente
source_url: https://www.php.net/manual/es/function.fastcgi-finish-request.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fpm/functions/fastcgi-finish-request.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fpm
translation_status: ready
translation_revision: 0ba9e74eb
order: 24260
---

fastcgi_finish_request

Descarga todos los datos de la respuesta al cliente

## Descripción

```php
fastcgi_finish_request(): bool
```php

Esta función descarga todos los datos de la respuesta al cliente y finaliza la solicitud. Esto permite que las tareas que consumen tiempo se realicen sin dejar la conexión con el cliente abierta.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
