---
title: GearmanClient::error
description: Devuelve el último error encontrado en forma de string
source_url: https://www.php.net/manual/es/gearmanclient.error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25130
---

GearmanClient::error

Devuelve el último error encontrado en forma de

string

## Descripción

```php
public GearmanClient::error(): string
```php

Devuelve el último error encontrado en forma de `string`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `string` legible por humanos que representa el último error ocurrido, o `false` si no hay mensaje de error disponible.

## Véase también

GearmanClient::getErrno
