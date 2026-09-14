---
title: eio_sync_file_range
description: Sincornizar un segmento de fichero con el disco
source_url: https://www.php.net/manual/es/function.eio-sync-file-range.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-sync-file-range.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 17200
---

eio_sync_file_range

Sincornizar un segmento de fichero con el disco

## Descripción

```php
eio_sync_file_range(mixed $fd, int $offset, int $nbytes, int $flags, [int $pri], [callable $callback], [mixed $data]): resource
```php

`eio_sync_file_range` permite un control preciso al sincronizar el fichero abierto mencionado por el descriptor de fichero `fd` con el disco.

## Parámetros

`fd`  
El descriptor de fichero

`offset`  
El byte de inicio del rango del archivo a ser sincronizado

`nbytes`  
Especifica la longitud del rango a ser sincronizado, en bytes. Si `nbytes` es cero, son sicronizados todos los bytes desde `offset` hasta el final del fichero.

`flags`  
Una máscara de bits. Puede incluir cualquiera de los siguientes valores: `EIO_SYNC_FILE_RANGE_WAIT_BEFORE`, `EIO_SYNC_FILE_RANGE_WRITE`, `EIO_SYNC_FILE_RANGE_WAIT_AFTER`. Estas banderas tienen el mismo significado que sus homónimas *SYNC_FILE_RANGE\_\** (véase la página del manual `SYNC_FILE_RANGE(2)`).

`pri`  
La prioridad de la petición: `EIO_PRI_DEFAULT`, `EIO_PRI_MIN`, `EIO_PRI_MAX`, o `null`. Si `null` es pasado, el parámetro `pri`, internamente, es definido a `EIO_PRI_DEFAULT`.

`callback`  
La función de retrollamada `callback` es llamada cuando la petición está terminada. Debe corresponder al siguiente prototipo:

```
void callback(mixed $data, int $result[, resource $req]);
```php

`data`  
representa los datos personalizados pasados a la petición.

`result`  
representa el valor resultante específico de la petición; básicamente, el valor retornado por la llamada al sistema correspondiente.

`req`  
es el recurso opcional de la petición que puede ser utilizado con funciones como `eio_get_last_error`.

`data`  
Variable arbitraria pasada a `callback`.

## Valores devueltos

`eio_sync_file_range` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.
