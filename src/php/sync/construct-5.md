---
title: SyncSharedMemory::__construct
description: Construye un nuevo objeto SyncSharedMemory
source_url: https://www.php.net/manual/es/syncsharedmemory.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncsharedmemory/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93710
---

SyncSharedMemory::\_\_construct

Construye un nuevo objeto SyncSharedMemory

## Descripción

```php
public SyncSharedMemory::__construct(string $name, int $size)
```php

Construye un objeto de memoria compartida con nombre.

## Parámetros

`name`  
El nombre del objeto de memoria compartida.

> [!NOTE]
> Si el nombre ya existe, debe poder ser abierto por el usuario actual que el proceso está en ejecución o se lanzará una excepción con un mensaje de error sin significado.

`size`  
El tamaño, en bytes, de la memoria compartida a reservar.

> [!NOTE]
> La cantidad de memoria no puede ser redimensionada posteriormente. Solicite suficiente almacenamiento de antemano.

## Valores devueltos

El nuevo objeto `SyncSharedMemory`.

## Errores/Excepciones

Se lanza una excepción si el objeto de memoria compartida no puede ser creado o abierto.

## Ejemplos

Ejemplo de `SyncSharedMemory::__construct`

```
<?php
// Probablemente se deberá proteger la memoria compartida con otros objetos de sincronización.
// La memoria compartida desaparece cuando la última referencia a ella desaparece.
$mem = new SyncSharedMemory("AppReportName", 1024);
if ($mem->first())
{
    // Realizar el trabajo de inicialización la primera vez aquí.
}

$result = $mem->write(json_encode(array("name" => "my_report.txt")));
?>

   
```php

## Véase también

SyncSharedMemory::first

SyncSharedMemory::size

SyncSharedMemory::write

SyncSharedMemory::read
