---
title: EvTimer::set
description: Configura el observador
source_url: https://www.php.net/manual/es/evtimer.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evtimer/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18630
---

EvTimer::set

Configura el observador

## Descripción

```php
public EvTimer::set(float $after, float $repeat): void
```php

Configura el observador

## Parámetros

`after`  
Configura el temporizador del trigger para que se lance después de `after` segundos.

`repeat`  
Si este argumento vale `0.0`, entonces el observador será automáticamente detenido si se alcanza el tiempo de espera máximo. Si este argumento es positivo, entonces el temporizador lanzará automáticamente el trigger en cada segundo siguiente, hasta que no sea detenido manualmente.

## Valores devueltos

No se retorna ningún valor.
