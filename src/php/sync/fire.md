---
title: SyncEvent::fire
description: Lanza/define el evento
source_url: https://www.php.net/manual/es/syncevent.fire.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncevent/fire.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93530
---

SyncEvent::fire

Lanza/define el evento

## Descripción

```php
public SyncEvent::fire(): bool
```php

Lanza/define un objeto `SyncEvent`. Mantiene varios hilos en espera si el objeto de evento ha sido creado con un valor manual a `true`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SyncEvent::fire`

```
<?php
// En una aplicación web:
$event = new SyncEvent("GetAppReport");
$event->fire();

// En un cron:
$event = new SyncEvent("GetAppReport");
$event->wait();
?>

   
```php

## Véase también

SyncEvent::reset

SyncEvent::wait
