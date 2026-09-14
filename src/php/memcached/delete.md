---
title: Memcached::delete
description: Elimina un elemento
source_url: https://www.php.net/manual/es/memcached.delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46450
---

Memcached::delete

Elimina un elemento

## Descripción

```php
public Memcached::delete(string $key, [int $time]): bool
```php

Elimina el elemento representado por la clave `key` del servidor.

## Parámetros

`key`  
La clave a eliminar.

`time`  
La duración de eliminación en el servidor.

> [!NOTE]
> A partir de memcached 1.3.0 (publicado en 2009) esta funcionalidad ya no está soportada. Pasar un valor distinto de cero para `time` causará que la eliminación falle. Memcached::getResultCode devolverá `MEMCACHED_INVALID_ARGUMENTS`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. El método Memcached::getResultCode devuelve `Memcached::RES_NOTFOUND` si la clave no existe.

## Ejemplos

Ejemplo con `Memcached::delete`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

$m->delete('key1');
?>

    
```php

## Véase también

Memcached::deleteByKey, Memcached::deleteMulti
