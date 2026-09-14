---
title: EvStat::prev
description: Devuelve el conjunto anterior devuelto por EvStat::attr
source_url: https://www.php.net/manual/es/evstat.prev.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evstat/prev.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18560
---

EvStat::prev

Devuelve el conjunto anterior devuelto por EvStat::attr

## Descripción

```php
public EvStat::prev(): void
```php

Idéntico al método EvStat::attr pero devuelve el conjunto anterior de valores.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array con la misma estructura que el array devuelto por el método EvStat::attr. El array contendrá los valores detectados previamente.

## Véase también

EvStat::attr

EvStat::stat
