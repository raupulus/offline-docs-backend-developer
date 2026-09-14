---
title: EvPeriodic::at
description: Devuelve el tiempo absoluto en el que este watcher será llamado la próxima
  vez
source_url: https://www.php.net/manual/es/evperiodic.at.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evperiodic/at.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18410
---

EvPeriodic::at

Devuelve el tiempo absoluto en el que este watcher será llamado la próxima vez

## Descripción

```php
public EvPeriodic::at(): float
```php

Devuelve el tiempo absoluto en el que este watcher será llamado la próxima vez. Esto no es lo mismo que el argumento de posición del método EvPeriodic::set o el método EvPeriodic::\_\_construct, pero funciona también en modo intervalo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el tiempo absoluto en el que este watcher será llamado la próxima vez, en segundos.
