---
title: Ev::feedSignalEvent
description: Simula un evento de señal en el bucle por omisión
source_url: https://www.php.net/manual/es/ev.feedsignalevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev/feedsignalevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 17800
---

Ev::feedSignalEvent

Simula un evento de señal en el bucle por omisión

## Descripción

```php
final public static Ev::feedSignalEvent(int $signum): void
```php

Simula un evento de señal en el bucle por omisión. Ev reaccionará a esta llamada como si la señal especificada por el argumento `signal` hubiera ocurrido.

## Parámetros

`signum`  
Número de la señal. Ver la página man de `signal(7)` para más detalles. Ver también las constantes exportadas por la extensión `pcntl`.

## Valores devueltos

No se retorna ningún valor.

## Véase también

Ev::feedSignal
