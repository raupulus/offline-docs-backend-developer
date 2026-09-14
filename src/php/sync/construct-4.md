---
title: SyncSemaphore::__construct
description: Construye un nuevo objeto SyncSemaphore
source_url: https://www.php.net/manual/es/syncsemaphore.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncsemaphore/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93670
---

SyncSemaphore::\_\_construct

Construye un nuevo objeto SyncSemaphore

## Descripción

```php
public SyncSemaphore::__construct([string $name], [int $initialval], [bool $autounlock])
```php

Construye un semáforo con nombre o sin nombre.

## Parámetros

`name`  
El nombre del semáforo si tiene nombre.

> [!NOTE]
> Si el nombre ya existe, el objeto debe poder ser abierto por el usuario actual que ejecuta el proceso, o se emitirá una excepción con el mensaje de error.

`initialval`  
El valor inicial del semáforo. Este será el número de bloqueos que pueden ser obtenidos.

`autounlock`  
Especifica si se debe desbloquear automáticamente el semáforo al final del script PHP.

> [!WARNING]
> Si el objeto es un semáforo con nombre cuyo autounlock es `false`, el objeto está bloqueado, y el script PHP termina antes de que el objeto sea desbloqueado, entonces el semáforo subyacente terminará en un estado no consistente.

## Valores devueltos

El nuevo objeto `SyncSemaphore`.

## Errores/Excepciones

Se emitirá una excepción si el semáforo no puede ser creado o abierto.

## Ejemplos

Ejemplo con `SyncSemaphore::__construct`

```
<?php
$semaphore = new SyncSemaphore("LimitedResource_2clients", 2);

if (!$semaphore->lock(3000))
{
    echo "Imposible bloquear el semáforo.";

    exit();
}

/* ... */

$semaphore->unlock();
?>

   
```php

## Véase también

SyncSemaphore::lock

SyncSemaphore::unlock
