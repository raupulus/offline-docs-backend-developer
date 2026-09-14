---
title: eio_write
description: Escribir en un fichero
source_url: https://www.php.net/manual/es/function.eio-write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 17260
---

eio_write

Escribir en un fichero

## Descripción

```php
eio_write(mixed $fd, string $str, [int $length], [int $offset], [int $pri], [callable $callback], [mixed $data]): resource
```php

`eio_write` escribe hasta `length` bytes desde `str` en el índice `offset` desde el principo del fichero.

## Parámetros

`fd`  
Un flujo, un recurso Socket, o un descriptor numérico de fichero, p.ej., devuelto por `eio_open`.

`str`  
La cadena fuente

`length`  
Número máximo de bytes a escribir.

`offset`  
ïndice desde el principio del fichero.

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

`eio_write` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.

## Véase también

eio_open
