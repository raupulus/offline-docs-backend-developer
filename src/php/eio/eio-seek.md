---
title: eio_seek
description: Reposiciona el cursor de un fichero abierto
source_url: https://www.php.net/manual/es/function.eio-seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_reviewed: false
translation_revision: 4e5389401
order: 17100
---

eio_seek

Reposiciona el cursor de un fichero abierto

## Descripción

```php
eio_seek(mixed $fd, int $offset, int $whence, [int $pri], [callable $callback], [mixed $data]): resource
```php

`eio_seek` reposiciona el desplazamiento del fichero abierto asociado al flujo, a la instancia de `Socket`, o al descriptor de fichero especificado por `fd` al valor del argumento `offset` conforme a la directiva `whence`.

## Parámetros

`fd`  
Un flujo, una `Socket`, o un descriptor de fichero numérico

`offset`  
Punto de partida desde el cual los datos comenzarán a ser leídos.

`whence`  
Los valores de `whence` son : `EIO_SEEK_SET` - Posiciona a `offset` bytes., `EIO_SEEK_CUR` - Posiciona a la posición actual más `offset`., `EIO_SEEK_END` - Posiciona al final del fichero más `offset`.

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
Variable arbitraria a pasar a la función de devolución de llamada `callback`.

## Valores devueltos

`eio_seek` devuelve el recurso solicitado en caso de éxito, o `false` si ocurre un error.
