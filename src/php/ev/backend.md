---
title: Ev::backend
description: Devuelve un integer que describe el backend utilizado por libev
source_url: https://www.php.net/manual/es/ev.backend.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev/backend.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 17760
---

Ev::backend

Devuelve un integer que describe el backend utilizado por libev

## Descripción

```php
final public static Ev::backend(): int
```php

Devuelve un integer que describe el backend utilizado por *libev*. Ver los [flags de Backend](#ev.constants.watcher-backends).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un integer (máscara de bytes) que describe el backend utilizado por *libev*.

## Véase también

EvEmbed

Ev::embeddableBackends

Ev::recommendedBackends

Ev::supportedBackends

Los flags de Backend
