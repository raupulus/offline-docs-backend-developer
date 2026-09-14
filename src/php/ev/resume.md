---
title: Ev::resume
description: Reanuda el bucle de eventos por defecto previamente detenido
source_url: https://www.php.net/manual/es/ev.resume.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev/resume.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 17850
---

Ev::resume

Reanuda el bucle de eventos por defecto previamente detenido

## Descripción

```php
final public static Ev::resume(): void
```php

Los métodos Ev::suspend y Ev::resume suspenden y reanudan un bucle.

Todos los watchers timer serán suspendidos durante el tiempo entre *la suspensión* y la *reanudación* y todos los watchers *periodic* serán reprogramados (y perderán todos los eventos que hayan ocurrido durante el tiempo de esta suspensión).

Tras la llamada al método Ev::suspend, no está permitido llamar a una función en el bucle proporcionado distinto del método Ev::resume. Además, no está permitido llamar al método Ev::resume sin una llamada previa al método Ev::suspend.

La llamada a una *suspensión*/*reanudación* tiene como efecto secundario la actualización del tiempo del bucle de eventos (ver el método Ev::nowUpdate).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Véase también

Ev::suspend
