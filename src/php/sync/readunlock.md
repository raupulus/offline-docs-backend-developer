---
title: SyncReaderWriter::readunlock
description: Libera un bloqueo de lectura
source_url: https://www.php.net/manual/es/syncreaderwriter.readunlock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncreaderwriter/readunlock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93630
---

SyncReaderWriter::readunlock

Libera un bloqueo de lectura

## Descripción

```php
public SyncReaderWriter::readunlock(): bool
```php

Libera un bloqueo de lectura sobre un objeto `SyncReaderWriter`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SyncReaderWriter::readunlock`

```
<?php
$readwrite = new SyncReaderWriter("FileCacheLock");
$readwrite->readlock();
/* ... */
$readwrite->readunlock();
?>

   
```php

## Véase también

SyncReaderWriter::readlock
