---
title: Memcached::deleteMulti
description: Elimina varios elementos
source_url: https://www.php.net/manual/es/memcached.deletemulti.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/deletemulti.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: false
translation_revision: 1d8068ecb
order: 46470
---

Memcached::deleteMulti

Elimina varios elementos

## Descripción

```php
public Memcached::deleteMulti(array $keys, [int $time]): array
```php

Elimina el array de claves `keys` del servidor.

## Parámetros

`keys`  
Las claves a eliminar.

`time`  
El tiempo de espera del servidor para eliminar los elementos.

> [!NOTE]
> A partir de memcached 1.3.0 (publicado en 2009) esta funcionalidad ya no está soportada. Pasar un valor distinto de cero para `time` causará que la eliminación falle. Memcached::getResultCode devolverá `MEMCACHED_INVALID_ARGUMENTS`.

## Valores devueltos

Devuelve un array indexado por `keys`. Cada elemento es `true` si la clave correspondiente fue eliminada, o una de las constantes `Memcached::RES_*` si la eliminación correspondiente falló.

Memcached::getResultCode devolverá el código de resultado de la última operación de eliminación ejecutada, es decir, la operación de eliminación del último elemento de `keys`.

## Véase también

Memcached::delete, Memcached::deleteByKey, Memcached::deleteMultiByKey
