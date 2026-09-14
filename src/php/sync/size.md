---
title: SyncSharedMemory::size
description: Devuelve el tamaño de la memoria compartida nombrada
source_url: https://www.php.net/manual/es/syncsharedmemory.size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncsharedmemory/size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93740
---

SyncSharedMemory::size

Devuelve el tamaño de la memoria compartida nombrada

## Descripción

```php
public SyncSharedMemory::size(): int
```php

Recupera el tamaño de la memoria compartida de un objeto `SyncSharedMemory`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un integer que contiene el tamaño de la memoria compartida. Este será el mismo tamaño que se pasó al constructor.

## Ejemplos

Ejemplo de `SyncSharedMemory::size`

```
<?php
$mem = new SyncSharedMemory("AppReportName", 1024);
var_dump($mem->size());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(1024)

## Véase también

SyncSharedMemory::\_\_construct

SyncSharedMemory::write

SyncSharedMemory::read
