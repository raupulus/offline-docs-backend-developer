---
title: SyncReaderWriter::writelock
description: Espera un bloqueo de escritura exclusivo
source_url: https://www.php.net/manual/es/syncreaderwriter.writelock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncreaderwriter/writelock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93640
---

SyncReaderWriter::writelock

Espera un bloqueo de escritura exclusivo

## Descripción

```php
public SyncReaderWriter::writelock([int $wait]): bool
```php

Obtiene un bloqueo de escritura exclusivo sobre un objeto `SyncReaderWriter`.

## Parámetros

`wait`  
El número de milisegundos para esperar el bloqueo. Un valor de -1 significa que se espera indefinidamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SyncReaderWriter::writelock`

```
<?php
$readwrite = new SyncReaderWriter("FileCacheLock");
$readwrite->writelock();
/* ... */
$readwrite->writeunlock();
?>

   
```php

## Véase también

SyncReaderWriter::writeunlock
