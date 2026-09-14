---
title: eio_busy
description: Incrementar artificialmente la carga. Podría ser útil en pruebas, evaluaciones
  comparativas
source_url: https://www.php.net/manual/es/function.eio-busy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-busy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16680
---

eio_busy

Incrementar artificialmente la carga. Podría ser útil en pruebas, evaluaciones comparativas

## Descripción

```php
eio_busy(int $delay, [int $pri], [callable $callback], [mixed $data]): resource
```php

`eio_busy` incrementa artificialmente la carga tomanto `delay` segundos para ejecutarse. Puede usarse para depuración, o evaluaciones comparativas.

## Parámetros

`delay`  
Retraso en segundos

`pri`  
La prioridad de la petición: `EIO_PRI_DEFAULT`, `EIO_PRI_MIN`, `EIO_PRI_MAX`, o `null`. Si `null` es pasado, el parámetro `pri`, internamente, es definido a `EIO_PRI_DEFAULT`.

`callback`  
Esta llamada de retorno se llama cuando está hecho todo el grupo de peticiones.

`data`  
Variable arbitraria pasada a `callback`.

## Valores devueltos

`eio_busy` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.

## Véase también

eio_nop
