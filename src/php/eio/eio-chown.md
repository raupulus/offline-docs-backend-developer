---
title: eio_chown
description: Cambiar el propietario de un fichero/directorio
source_url: https://www.php.net/manual/es/function.eio-chown.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-chown.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 184764a63
order: 16710
---

eio_chown

Cambiar el propietario de un fichero/directorio

## Descripción

```php
eio_chown(string $path, int $uid, [int $gid], [int $pri], [callable $callback], [mixed $data]): resource
```php

`eio_chown` cambia el propietario de un fichero o directorio. El nuevo propietario es especificado por `uid`, y el grupo por `gid`.

## Parámetros

`path`  
La ruta al fichero o directorio.

> [!WARNING]
> Evite las rutas relativas.

`uid`  
El ID de usuario. Se ignora si es aigual a -1.

`gid`  
El ID de grupo. Se ignora si es aigual a -1.

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

`eio_chown` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.

## Véase también

eio_chmod
