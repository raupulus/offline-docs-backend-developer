---
title: SyncMutex::__construct
description: Construye un nuevo objeto SyncMutex
source_url: https://www.php.net/manual/es/syncmutex.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncmutex/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93570
---

SyncMutex::\_\_construct

Construye un nuevo objeto SyncMutex

## Descripción

```php
public SyncMutex::__construct([string $name])
```php

Construye un objeto contable nombrado o no.

## Parámetros

`name`  
El nombre del mutex si se trata de un objeto mutex nombrado.

> [!NOTE]
> Si el nombre ya existe, debe ser capaz de ser abierto por el usuario actual ejecutando el proceso, o bien se lanzará una excepción con el mensaje de error correspondiente.

## Valores devueltos

El nuevo objeto `SyncMutex`.

## Errores/Excepciones

Se lanza una excepción si el mutex no puede ser creado o abierto.

## Ejemplos

Ejemplo con `SyncMutex::__construct` y un mutex nombrado con un tiempo de espera máximo para el bloqueo

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

Ejemplo con `SyncMutex::__construct` y un mutex no nombrado

```
<?php
$mutex = new SyncMutex();

$mutex->lock();

/* ... */

$mutex->unlock();
?>

   
```php

## Véase también

SyncMutex::lock

SyncMutex::unlock
