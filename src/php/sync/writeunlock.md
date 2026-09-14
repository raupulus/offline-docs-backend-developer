---
title: SyncReaderWriter::writeunlock
description: Libera un bloqueo de escritura
source_url: https://www.php.net/manual/es/syncreaderwriter.writeunlock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncreaderwriter/writeunlock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93650
---

SyncReaderWriter::writeunlock

Libera un bloqueo de escritura

## Descripción

```php
public SyncReaderWriter::writeunlock(): bool
```php

Libera un bloqueo de escritura en un objeto `SyncReaderWriter`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SyncReaderWriter::writeunlock`

```
<?php
$readwrite = new SyncReaderWriter("FileCacheLock");
$readwrite->writelock();
/* ... */
$readwrite->writeunlock();
?>

   
```php

## Véase también

SyncReaderWriter::writelock
