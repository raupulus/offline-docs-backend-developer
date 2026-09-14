---
title: EventHttp::removeServerAlias
description: Elimina un alias en el servidor
source_url: https://www.php.net/manual/es/eventhttp.removeserveralias.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttp/removeserveralias.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: da9d81816
order: 19890
---

EventHttp::removeServerAlias

Elimina un alias en el servidor

## Descripción

```php
public EventHttp::removeServerAlias(string $alias): bool
```php

Elimina un alias en el servidor, previamente añadido con el método EventHttp::addServerAlias

## Parámetros

`alias`  
El alias a eliminar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventHttp::addServerAlias
