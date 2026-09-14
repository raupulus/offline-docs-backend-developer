---
title: SyncEvent::wait
description: Espera a que el objeto SyncEvent sea lanzado
source_url: https://www.php.net/manual/es/syncevent.wait.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncevent/wait.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93550
---

SyncEvent::wait

Espera a que el objeto SyncEvent sea lanzado

## Descripción

```php
public SyncEvent::wait([int $wait]): bool
```php

Espera a que el objeto `SyncEvent` sea lanzado.

## Parámetros

`wait`  
El número de milisegundos a esperar a que el evento sea lanzado. Un valor de -1 significa que se espera indefinidamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SyncEvent::wait`

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

SyncEvent::fire
