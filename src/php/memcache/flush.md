---
title: Memcache::flush
description: Elimina todos los elementos existentes en el servidor de caché
source_url: https://www.php.net/manual/es/memcache.flush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/flush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46150
---

Memcache::flush

Elimina todos los elementos existentes en el servidor de caché

## Descripción

```php
Memcache::flush(): bool
```php

```php
memcache_flush(Memcache $memcache): bool
```

`Memcache::flush` invalida inmediatamente todos los elementos existentes en el servidor de caché. `Memcache::flush` no libera ningún recurso actualmente, solo marca todos los elementos como expirados, por lo que la memoria ocupada será reutilizada con nuevos elementos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcache::flush`

```php
<?php

/* API procedimental */
$memcache_obj = memcache_connect('memcache_host', 11211);

memcache_flush($memcache_obj);

/* API orientada a objetos */

$memcache_obj = new Memcache;
$memcache_obj->connect('memcache_host', 11211);

$memcache_obj->flush();

?>

   
```
