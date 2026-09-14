---
title: SplPriorityQueue::setExtractFlags
description: Establece el modo de extracción
source_url: https://www.php.net/manual/es/splpriorityqueue.setextractflags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splpriorityqueue/setextractflags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 85410
---

SplPriorityQueue::setExtractFlags

Establece el modo de extracción

## Descripción

```php
public SplPriorityQueue::setExtractFlags(int $flags): int
```php

## Parámetros

`flags`  
Define lo que se extrae por SplPriorityQueue::current, SplPriorityQueue::top y SplPriorityQueue::extract.

- `SplPriorityQueue::EXTR_DATA` (0x00000001): Extraer los datos

- `SplPriorityQueue::EXTR_PRIORITY` (0x00000002): Extraer la prioridad

- `SplPriorityQueue::EXTR_BOTH` (0x00000003): Extraer un array con ambos

El modo por omisión es `SplPriorityQueue::EXTR_DATA`.

## Valores devueltos

Devuelve las banderas de extracción.
