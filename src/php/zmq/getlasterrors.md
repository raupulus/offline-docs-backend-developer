---
title: ZMQPoll::getLastErrors
description: Obtener los errores del sondeo
source_url: https://www.php.net/manual/es/zmqpoll.getlasterrors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqpoll/getlasterrors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: ab5614596
order: 109290
---

ZMQPoll::getLastErrors

Obtener los errores del sondeo

## Descripción

```php
public ZMQPoll::getLastErrors(): array
```php

Devuelve los ID de los objetos que poseen errores en el último sondeo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devueve un array que contiene los ID de los elementos que poseen errores en el último sondeo. Se devuelve un array vacío si no hay errores.
