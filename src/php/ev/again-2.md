---
title: EvTimer::again
description: Reinicia el watcher Timer
source_url: https://www.php.net/manual/es/evtimer.again.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evtimer/again.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18600
---

EvTimer::again

Reinicia el watcher Timer

## Descripción

```php
public EvTimer::again(): void
```php

Este método funciona como si el Timer hubiera terminado y reinicia su ciclo. La semántica exacta es:

1.  si el Timer está en espera, su estado se limpia.

2.  si el Timer está en ejecución, pero no debe reiniciarse, entonces se detendrá (como si hubiera terminado normalmente).

3.  si el Timer debe reiniciarse, el método lo iniciará si es necesario (con el valor `repeat`), o reiniciará el Timer al valor de la variable `repeat`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Véase también

EvWatcher::stop
