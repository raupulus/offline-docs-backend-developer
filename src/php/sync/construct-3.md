---
title: SyncReaderWriter::__construct
description: Construye un nuevo objeto SyncReaderWriter
source_url: https://www.php.net/manual/es/syncreaderwriter.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncreaderwriter/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93610
---

SyncReaderWriter::\_\_construct

Construye un nuevo objeto SyncReaderWriter

## Descripción

```php
public SyncReaderWriter::__construct([string $name], [int $autounlock])
```php

Construye un objeto de lectura/escritura nombrado o no.

## Parámetros

`name`  
El nombre del objeto si está nombrado.

> [!NOTE]
> Si el nombre ya existe, el objeto debe poder ser abierto con el usuario actual que ejecuta el proceso, o se emitirá una excepción conteniendo el mensaje de error.

> [!NOTE]
> En Windows, `name` no debe contener barras invertidas.

`autounlock`  
Especifica si se debe desbloquear automáticamente el objeto al final del script PHP.

> [!WARNING]
> Si el objeto es un objeto de lectura/escritura con el autounlock en `false`, el objeto está bloqueado en lectura o en escritura, y el script PHP terminará antes del desbloqueo del objeto, y por lo tanto, el objeto subyacente terminará en un estado no consistente.

## Valores devueltos

El nuevo objeto `SyncReaderWriter`.

## Errores/Excepciones

Se emite una excepción si el objeto de lectura/escritura no puede ser creado o abierto.

## Ejemplos

Ejemplo con `SyncReaderWriter::__construct`

```
<?php
$readwrite = new SyncReaderWriter("FileCacheLock");
$readwrite->readlock();
/* ... */
$readwrite->readunlock();

$readwrite->writelock();
/* ... */
$readwrite->writeunlock();
?>

   
```php

## Véase también

SyncReaderWriter::readlock

SyncReaderWriter::readunlock

SyncReaderWriter::writelock

SyncReaderWriter::writeunlock
