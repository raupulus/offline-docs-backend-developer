---
title: Ev::feedSignal
description: Simula la recepción de una señal
source_url: https://www.php.net/manual/es/ev.feedsignal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev/feedsignal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 17790
---

Ev::feedSignal

Simula la recepción de una señal

## Descripción

```php
final public static Ev::feedSignal(int $signum): void
```php

Simula la recepción de una señal. Es seguro llamar a esta función en cualquier momento, desde cualquier contexto, incluyendo desde un gestor de señales, o desde un hilo aleatorio. Su principal utilización es personalizar el gestor de señales en el proceso.

A diferencia del método Ev::feedSignalEvent, este método funciona según la loop que ha registrado la señal.

## Parámetros

`signum`  
Número de la señal. Ver la página man de `signal(7)` para más detalles. Se pueden utilizar las constantes exportadas por la extensión `pcntl`.

## Valores devueltos

No se retorna ningún valor.

## Véase también

Ev::feedSignalEvent
