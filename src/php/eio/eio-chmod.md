---
title: eio_chmod
description: Cambiar los permisos de fichero/directorio
source_url: https://www.php.net/manual/es/function.eio-chmod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-chmod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16700
---

eio_chmod

Cambiar los permisos de fichero/directorio

## Descripción

```php
eio_chmod(string $path, int $mode, [int $pri], [callable $callback], [mixed $data]): resource
```php

`eio_chmod` cambia los permisos de un fichero o directorio. Los nuevos permisos son especificados mediandte `mode`.

## Parámetros

`path`  
La ruta al fichero o directorio objetivo

> [!WARNING]
> Evite las rutas relativas.

`mode`  
Los nuevos permisos. P.ej. `0644`.

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

`eio_chmod` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.

## Véase también

eio_chown
