---
title: Ev::now
description: Devuelve el tiempo de inicio de la última iteración del bucle de eventos
  por omisión
source_url: https://www.php.net/manual/es/ev.now.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev/now.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 17820
---

Ev::now

Devuelve el tiempo de inicio de la última iteración del bucle de eventos por omisión

## Descripción

```php
final public static Ev::now(): float
```php

Devuelve el tiempo de inicio de la última iteración del bucle de eventos por omisión. Es el tiempo en el que se basan los temporizadores (`EvTimer` y `EvPeriodic`), y referirse a este es a menudo más rápido que llamar al método Ev::time.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de segundos que representan el tiempo de inicio de la última iteración del bucle de eventos por omisión.

## Véase también

Ev::nowUpdate
