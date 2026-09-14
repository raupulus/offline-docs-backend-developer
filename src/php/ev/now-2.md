---
title: EvLoop::now
description: Devuelve el "event loop time" actual
source_url: https://www.php.net/manual/es/evloop.now.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/now.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18270
---

EvLoop::now

Devuelve el "event loop time" actual

## Descripción

```php
public EvLoop::now(): float
```php

Devuelve el "event loop time" actual, que es la duración durante la cual el bucle de eventos recibe eventos y inicia sus análisis. Este timestamp no cambia mientras las retrollamadas están en ejecución, y es también el tiempo base utilizado para los temporizadores relativos. Puede considerarse como el timestamp del evento en curso (o más exactamente, el utilizado por libev).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el timestamp del bucle de eventos, en segundos.

## Véase también

Ev::now
