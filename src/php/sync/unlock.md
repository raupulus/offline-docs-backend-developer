---
title: SyncMutex::unlock
description: Desbloquea el mutex
source_url: https://www.php.net/manual/es/syncmutex.unlock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncmutex/unlock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93590
---

SyncMutex::unlock

Desbloquea el mutex

## Descripción

```php
public SyncMutex::unlock([bool $all]): bool
```php

Decrementa el contador interno de un objeto `SyncMutex`. Cuando el contador interno llega a cero, el bloqueo actual del objeto se libera.

## Parámetros

`all`  
Especifica si se debe o no establecer el contador interno a cero y, por lo tanto, liberar el bloqueo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SyncMutex::unlock`

```
<?php
$mutex = new SyncMutex("UniqueName");

$mutex->lock();

/* ... */

$mutex->unlock();
?>

   
```php

## Véase también

SyncMutex::lock
