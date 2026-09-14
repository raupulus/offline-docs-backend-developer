---
title: SyncSharedMemory::write
description: Copia los datos en la memoria compartida nombrada
source_url: https://www.php.net/manual/es/syncsharedmemory.write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncsharedmemory/write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93750
---

SyncSharedMemory::write

Copia los datos en la memoria compartida nombrada

## Descripción

```php
public SyncSharedMemory::write([string $string], [int $start])
```php

Copia los datos en la memoria compartida nombrada.

## Parámetros

`string`  
Los datos a escribir en la memoria compartida.

> [!NOTE]
> Si el tamaño de los datos excede el tamaño de la memoria compartida, el número de bytes escritos devueltos será inferior a la longitud de la entrada.

`start`  
El inicio/desplazamiento, en bytes, para comenzar la escritura.

> [!NOTE]
> Si el valor es negativo, la posición de inicio comenzará en el número especificado de bytes desde el final del segmento de memoria compartida.

## Valores devueltos

Un integer que contiene el número de bytes escritos en la memoria compartida.

## Ejemplos

Ejemplo de `SyncSharedMemory::write`

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
var_dump($result);

$result = $mem->write("report.txt", -3);
var_dump($result);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(10)
    int(3)

## Véase también

SyncSharedMemory::\_\_construct

SyncSharedMemory::first

SyncSharedMemory::write

SyncSharedMemory::read
