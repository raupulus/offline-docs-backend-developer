---
title: Memcache::delete
description: Elimina un elemento del servidor de caché
source_url: https://www.php.net/manual/es/memcache.delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46140
---

Memcache::delete

memcache_delete

Elimina un elemento del servidor de caché

## Descripción

```php
Memcache::delete(string $key, [int $exptime]): bool
```php

```php
memcache_delete(Memcache $memcache, string $key, [int $exptime]): bool
```

`Memcache::delete` elimina el elemento identificado por la clave `key`.

## Parámetros

`key`  
La clave asociada al elemento a eliminar.

`exptime`  
Este argumento obsoleto no es soportado, y su valor por omisión es `0` segundos. No se debe utilizar este argumento.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL memcache 3.0.5 | El argumento `exptime` está deprecado y no debería ser proporcionado. Valores distintos de `0` pueden provocar errores inesperados. |

## Ejemplos

Ejemplo con `Memcache::delete`

```php
<?php

/* API procedimental */
$memcache_obj = memcache_connect('memcache_host', 11211);

/* el elemento será eliminado por el servidor de caché */
memcache_delete($memcache_obj, 'key_to_delete');

/* API orientada a objetos */
$memcache_obj = new Memcache;
$memcache_obj->connect('memcache_host', 11211);

$memcache_obj->delete('key_to_delete');

?>

   
```

## Véase también

Memcache::set

Memcache::replace
