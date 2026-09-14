---
title: SyncSemaphore::unlock
description: Incrementa el contador del objeto SyncSemaphore
source_url: https://www.php.net/manual/es/syncsemaphore.unlock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncsemaphore/unlock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93690
---

SyncSemaphore::unlock

Incrementa el contador del objeto SyncSemaphore

## Descripción

```php
public SyncSemaphore::unlock([int $prevcount]): bool
```php

Incrementa el contador del objeto `SyncSemaphore`.

## Parámetros

`prevcount`  
Devuelve el contador anterior del semáforo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SyncSemaphore::unlock`

```
<?php
$semaphore = new SyncSemaphore("LimitedResource_2clients", 2);

if (!$semaphore->lock(3000))
{
    echo "Imposible desbloquear el semáforo.";

    exit();
}

/* ... */

$semaphore->unlock();
?>

   
```php

## Véase también

SyncSemaphore::lock
