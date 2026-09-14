---
title: SyncReaderWriter::readlock
description: Obtiene un bloqueo de lectura
source_url: https://www.php.net/manual/es/syncreaderwriter.readlock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncreaderwriter/readlock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93620
---

SyncReaderWriter::readlock

Obtiene un bloqueo de lectura

## Descripción

```php
public SyncReaderWriter::readlock([int $wait]): bool
```php

Obtiene un bloqueo de lectura en un objeto `SyncReaderWriter`.

## Parámetros

`wait`  
El número de milisegundos de espera para obtener un bloqueo. Un valor de -1 significa que se espera indefinidamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SyncReaderWriter::readlock`

```
<?php
$readwrite = new SyncReaderWriter("FileCacheLock");
$readwrite->readlock();
/* ... */
$readwrite->readunlock();
?>

   
```php

## Véase también

SyncReaderWriter::readunlock
