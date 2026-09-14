---
title: EvLoop::nowUpdate
description: Establece el tiempo actual solicitándolo al kernel y actualiza el tiempo
  devuelto por EvLoop::now durante la ejecución
source_url: https://www.php.net/manual/es/evloop.nowupdate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/nowupdate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18280
---

EvLoop::nowUpdate

Establece el tiempo actual solicitándolo al kernel y actualiza el tiempo devuelto por EvLoop::now durante la ejecución

## Descripción

```php
public EvLoop::nowUpdate(): void
```php

Establece el tiempo actual solicitándolo al kernel y actualiza el tiempo devuelto por EvLoop::now durante la ejecución. Se trata de una operación costosa en términos de rendimiento que normalmente se ejecuta automáticamente en el método EvLoop::run.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Véase también

EvLoop::now

Ev::nowUpdate
