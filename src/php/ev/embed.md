---
title: EvLoop::embed
description: Crea una instancia del observador EvEmbed asociado con el objeto EvLoop
  actual
source_url: https://www.php.net/manual/es/evloop.embed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/embed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18210
---

EvLoop::embed

Crea una instancia del observador EvEmbed asociado con el objeto EvLoop actual

## Descripción

```php
final public EvLoop::embed(string $other, [string $callback], [string $data], [string $priority]): EvEmbed
```php

Crea una instancia del observador `EvEmbed` asociado con el objeto `EvLoop` actual.

## Parámetros

Todos los argumentos tienen el mismo significado que para el método EvEmbed::\_\_construct.

## Valores devueltos

Devuelve el objeto EvEmbed en caso de éxito.

## Véase también

EvEmbed::\_\_construct
