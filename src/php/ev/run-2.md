---
title: EvLoop::run
description: Comienza a verificar los eventos y a llamar a las funciones de retrollamada
  de la bucle
source_url: https://www.php.net/manual/es/evloop.run.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/run.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18320
---

EvLoop::run

Comienza a verificar los eventos y a llamar a las funciones de retrollamada de la bucle

## Descripción

```php
public EvLoop::run([int $flags]): void
```php

Comienza a verificar los eventos y a llamar a las funciones de retrollamada para la bucle de evento actual. El método se detiene cuando una función de retrollamada llama al método Ev::stop o cuando los flags son diferentes de cero (en cuyo caso, el valor devuelto es `true`) o cuando no hay ningún watcher activo que referencie la bucle (EvWatcher::keepalive vale `true`), en cuyo caso, el valor devuelto será `false`. El valor devuelto puede generalmente ser interpretado como *si `true`, aún hay trabajo por hacer*.

## Parámetros

`flags`  
El argumento opcional `flags` puede tomar uno de los valores siguientes:

| `flags` | Descripción |
|----|----|
| `0` | El comportamiento por omisión, descrito anteriormente |
| `Ev::RUN_ONCE` | No bloquear más de un evento (espera, pero no bucla) |
| `Ev::RUN_NOWAIT` | Sin bloqueo (recupera, gestiona los eventos, pero no espera) |

Lista de valores posibles para `flags`

Ver las [constantes de los flags de ejecución](#ev.constants.run-flags).

## Valores devueltos

No se retorna ningún valor.

## Véase también

EvLoop::stop

Ev::run
