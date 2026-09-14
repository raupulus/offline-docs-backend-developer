---
title: SyncSharedMemory::read
description: Copia de datos de la memoria compartida nombrada
source_url: https://www.php.net/manual/es/syncsharedmemory.read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncsharedmemory/read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93730
---

SyncSharedMemory::read

Copia de datos de la memoria compartida nombrada

## Descripción

```php
public SyncSharedMemory::read([int $start], [int $length])
```php

Copia de datos de la memoria compartida nombrada.

## Parámetros

`start`  
El inicio/desplazamiento, en bytes, para comenzar la lectura.

> [!NOTE]
> Si el valor es negativo, la posición de inicio comenzará en el número especificado de bytes desde el final del segmento de memoria compartida.

`length`  
El número de bytes a leer.

> [!NOTE]
> Si no se especifica, la lectura se detendrá al final del segmento de memoria compartida.
>
> Si el valor es negativo, la lectura se detendrá en el número especificado de bytes desde el final del segmento de memoria compartida.

## Valores devueltos

Un string que contiene los datos leídos de la memoria compartida.

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

$result = $mem->write("report.txt");

$result = $mem->read(3, -4);
var_dump($result);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(3) "ort"

## Véase también

SyncSharedMemory::\_\_construct

SyncSharedMemory::first

SyncSharedMemory::write

SyncSharedMemory::read
