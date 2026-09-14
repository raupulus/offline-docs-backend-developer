---
title: SyncMutex::lock
description: Obtiene un bloqueo exclusivo
source_url: https://www.php.net/manual/es/syncmutex.lock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncmutex/lock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93580
---

SyncMutex::lock

Obtiene un bloqueo exclusivo

## Descripción

```php
public SyncMutex::lock([int $wait]): bool
```php

Obtiene un bloqueo exclusivo sobre un objeto `SyncMutex`. Si el bloqueo ya está adquirido, entonces este método incrementará el contador interno.

## Parámetros

`wait`  
El número de milisegundos a esperar para la obtención del bloqueo exclusivo. Un valor de -1 significa que se espera indefinidamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SyncMutex::lock`

```
<?php
$mutex = new SyncMutex("UniqueName");

if (!$mutex->lock(3000))
{
    echo "Imposible bloquear el mutex.";

    exit();
}

/* ... */

$mutex->unlock();
?>

   
```php

## Véase también

SyncMutex::unlock
