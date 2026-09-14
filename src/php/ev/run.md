---
title: Ev::run
description: Inicia la verificación de eventos y llama a las funciones de retrollamada
  para el bucle por defecto
source_url: https://www.php.net/manual/es/ev.run.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev/run.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 17860
---

Ev::run

Inicia la verificación de eventos y llama a las funciones de retrollamada para el bucle por defecto

## Descripción

```php
final public static Ev::run([int $flags]): void
```php

Inicia la verificación de eventos y llama a las funciones de retrollamada *para el bucle por defecto*. Retorna cuando una función de retrollamada llama al método Ev::stop, o cuando los flags son diferentes de cero (en cuyo caso, el valor retornado será `true`), o bien cuando no hay más observadores activos que referencian el bucle (EvWatcher::keepalive vale `true`), en cuyo caso, el valor retornado será `false`. El valor retornado puede generalmente ser interpretado como: *si `true`, aún hay trabajo por hacer*.

## Parámetros

`flags`  
El parámetro opcional `flags` puede ser uno de los siguientes valores:

| `flags` | Descripción |
|----|----|
| `0` | El comportamiento por omisión, descrito arriba |
| `Ev::RUN_ONCE` | Bloquea al menos un (pone en espera, pero no bucla más) |
| `Ev::RUN_NOWAIT` | No bloquea en absoluto (recupera/gestiona los eventos pero no espera) |

Lista de valores posibles de `flags`

Ver las [constantes de flags de ejecución](#ev.constants.run-flags).

## Valores devueltos

No se retorna ningún valor.

## Véase también

Ev::stop

EvLoop::run
