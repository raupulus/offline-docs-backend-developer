---
title: SyncSemaphore::lock
description: Disminuye el contador del objeto SyncSemaphore o espera
source_url: https://www.php.net/manual/es/syncsemaphore.lock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncsemaphore/lock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93680
---

SyncSemaphore::lock

Disminuye el contador del objeto SyncSemaphore o espera

## Descripción

```php
public SyncSemaphore::lock([int $wait]): bool
```php

Disminuye el contador del objeto `SyncSemaphore` o espera hasta que el semáforo tenga un valor diferente de cero.

## Parámetros

`wait`  
El número de milisegundos a esperar por el semáforo. Un valor de -1 significa que se espera indefinidamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SyncSemaphore::lock`

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

SyncSemaphore::unlock
