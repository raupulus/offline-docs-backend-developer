---
title: EvWatcher::clear
description: Borra el estado de espera del observador
source_url: https://www.php.net/manual/es/evwatcher.clear.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evwatcher/clear.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18650
---

EvWatcher::clear

Borra el estado de espera del observador

## Descripción

```php
public EvWatcher::clear(): int
```php

Si el observador está en espera, este método borra su estado de espera (`pending`) y devuelve su bitset `revents` (como si su función de retrollamada hubiera sido invocada). Si el observador no está en espera, este método no hará nada, y devolverá `0`.

Algunas veces, es útil interrogar un observador en lugar de esperar a que su función de retrollamada sea invocada, y esto es precisamente lo que permite hacer este método.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

En el caso de que el observador esté en espera, devuelve el bitset `revents`, como si su [función de retrollamada](#ev.watcher-callbacks) fuera invocada. De lo contrario, devuelve `0`.
