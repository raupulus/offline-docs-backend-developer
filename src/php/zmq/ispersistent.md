---
title: ZMQContext::isPersistent
description: Indicar si el contexto es persistente
source_url: https://www.php.net/manual/es/zmqcontext.ispersistent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqcontext/ispersistent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_revision: 331fbfeac
order: 109110
---

ZMQContext::isPersistent

Indicar si el contexto es persistente

## Descripción

```php
public ZMQContext::isPersistent(): bool
```php

Indica si el contexto es persistente. Un contexto persistente es necesario para conexiones persistentes, ya que cada socket se asigna a partir de un contexto.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el contexto es persistente y `false` si no lo es.
