---
title: EvPeriodic::set
description: Configura el watcher
source_url: https://www.php.net/manual/es/evperiodic.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evperiodic/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18440
---

EvPeriodic::set

Configura el watcher

## Descripción

```php
public EvPeriodic::set(float $offset, float $interval): void
```php

(Re-)Configura el watcher EvPeriodic.

## Parámetros

`offset`  
El mismo significado que para el método EvPeriodic::\_\_construct. Ver los [modos de operación del watcher periódico](#ev.periodic-modes)

`interval`  
El mismo significado que para el método EvPeriodic::\_\_construct. Ver los [modos de operación del watcher periódico](#ev.periodic-modes)

## Valores devueltos

No se retorna ningún valor.
