---
title: eio_fallocate
description: Permitir al llamador manipular directamente el espacio de disco asignado
  a un fichero
source_url: https://www.php.net/manual/es/function.eio-fallocate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-fallocate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: dfd68fd22
order: 16760
---

eio_fallocate

Permitir al llamador manipular directamente el espacio de disco asignado a un fichero

## Descripción

```php
eio_fallocate(mixed $fd, int $mode, int $offset, int $length, [int $pri], [callable $callback], [mixed $data]): resource
```php

`eio_fallocate` permite al llamador manipular directamente el espacio de disco asignado al fichero especificado por el descriptor de fichero `fd` para el rango de bytes empezando por `offset` y continuando `length` bytes.

> [!NOTE]
> Se debería usar *OR* entre `EIO_O_CREAT` y `EIO_O_WRONLY` o `EIO_O_RDWR`

## Parámetros

`fd`  
Un flujo, un recurso Socket, o un descriptor numérico de fichero, p.ej., devuelto por `eio_open`.

`mode`  
Actualmente sólo está soportada una bandera para el modo: `EIO_FALLOC_FL_KEEP_SIZE` (lo mismo que la constante POSIX `FALLOC_FL_KEEP_SIZE`).

`offset`  
Especifica el inicio del rango de bytes.

`length`  
Especifica la longitud del rango de bytes.

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

`eio_fallocate` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.
