---
title: eio_dup2
description: Duplicar un descriptor de fichero
source_url: https://www.php.net/manual/es/function.eio-dup2.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-dup2.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16740
---

eio_dup2

Duplicar un descriptor de fichero

## Descripción

```php
eio_dup2(mixed $fd, mixed $fd2, [int $pri], [callable $callback], [mixed $data]): resource
```php

`eio_dup2` duplica un descriptor de fichero.

## Parámetros

`fd`  
Un flujo, un recurso Socket, o un descriptor de fichero numérico origen

`fd2`  
Un flujo, un recurso Socket, o un descriptor de fichero numérico objetivo

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

`eio_dup2` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.
