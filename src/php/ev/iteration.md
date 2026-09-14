---
title: Ev::iteration
description: Devuelve el número de veces que el bucle de eventos por omisión ha sido
  solicitado para un nuevo evento
source_url: https://www.php.net/manual/es/ev.iteration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev/iteration.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 17810
---

Ev::iteration

Devuelve el número de veces que el bucle de eventos por omisión ha sido solicitado para un nuevo evento

## Descripción

```php
final public static Ev::iteration(): int
```php

Devuelve el número de veces que el bucle de eventos por omisión ha sido solicitado para un nuevo evento. Puede ser útil como contador de generación.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de solicitudes del bucle de eventos por omisión.

## Véase también

Ev::depth
