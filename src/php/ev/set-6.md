---
title: EvStat::set
description: Configura el watcher
source_url: https://www.php.net/manual/es/evstat.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evstat/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18570
---

EvStat::set

Configura el watcher

## Descripción

```php
public EvStat::set(string $path, float $interval): void
```php

Configura el watcher.

## Parámetros

`path`  
La ruta de acceso para la cual se esperará un cambio de estado.

`interval`  
Intervalo de detección de modificaciones; debe normalmente valer `0.0` para dejar que *libev* elija un buen valor.

## Valores devueltos

No se retorna ningún valor.
