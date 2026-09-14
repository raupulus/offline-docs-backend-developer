---
title: eio_sendfile
description: Transferir información entre descriptores de ficheros
source_url: https://www.php.net/manual/es/function.eio-sendfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-sendfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 17110
---

eio_sendfile

Transferir información entre descriptores de ficheros

## Descripción

```php
eio_sendfile(mixed $out_fd, mixed $in_fd, int $offset, int $length, [int $pri], [callable $callback], [string $data]): resource
```php

`eio_sendfile` copia información entre un descriptor de fichero y otror. Véase la página del manual `SENDFILE(2)` para más detalles.

## Parámetros

`out_fd`  
Un flujo de salida, un recurso Socket, o un descriptor de fichero. Debería ser abierto para escritura.

`in_fd`  
Un flujo de entrada, un recurso Socket, o un descriptor de fichero. Debería ser abierto para lectura.

`offset`  
El índice dentro del fichero fuente.

`length`  
El número de bytes a copiar.

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

`eio_sendfile` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.
