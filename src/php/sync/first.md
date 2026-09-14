---
title: SyncSharedMemory::first
description: Verifica si el objeto es la primera instancia en todo el sistema de la
  memoria compartida nombrada
source_url: https://www.php.net/manual/es/syncsharedmemory.first.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncsharedmemory/first.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93720
---

SyncSharedMemory::first

Verifica si el objeto es la primera instancia en todo el sistema de la memoria compartida nombrada

## Descripción

```php
public SyncSharedMemory::first(): bool
```php

Recupera el estado de primera instancia del objeto `SyncSharedMemory` en todo el sistema.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `SyncSharedMemory::first`

```
<?php
$mem = new SyncSharedMemory("AppReportName", 1024);
if ($mem->first())
{
    // Realizar el trabajo de inicialización la primera vez aquí.
}

var_dump($mem->first());

$mem2 = new SyncSharedMemory("AppReportName", 1024);

var_dump($mem2->first());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(false)

## Véase también

SyncSharedMemory::write

SyncSharedMemory::read
