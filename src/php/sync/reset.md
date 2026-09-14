---
title: SyncEvent::reset
description: Reinicializa manualmente un evento
source_url: https://www.php.net/manual/es/syncevent.reset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncevent/reset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93540
---

SyncEvent::reset

Reinicializa manualmente un evento

## Descripción

```php
public SyncEvent::reset(): bool
```php

Reinicializa un objeto `SyncEvent` que ha sido lanzado/definido. Solo válido para los objetos de evento manuales.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SyncEvent::reset`

```
<?php
// En una aplicación web:
$event = new SyncEvent("DemoApplication", true);
$event->wait();

// En un cron:
$event = new SyncEvent("DemoApplication", true);
$event->reset();
/* ... Realizar algunas tareas de mantenimiento ... */
$event->fire();
?>

   
```php

## Véase también

SyncEvent::fire

SyncEvent::reset

SyncEvent::wait
