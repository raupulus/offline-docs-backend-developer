---
title: GearmanClient::setContext
description: Define el contexto de una aplicación
source_url: https://www.php.net/manual/es/gearmanclient.setcontext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/setcontext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25220
---

GearmanClient::setContext

Define el contexto de una aplicación

## Descripción

```php
public GearmanClient::setContext(string $data): bool
```php

Define una cadena arbitraria para proporcionar como contexto de la aplicación que podrá ser recuperada más tarde mediante el método GearmanClient::context.

## Parámetros

`data`  
Datos de contexto

## Valores devueltos

Siempre devuelve `true`.

## Véase también

GearmanClient::context
