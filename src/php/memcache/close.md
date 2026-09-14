---
title: Memcache::close
description: Cierra la conexión con el servidor Memcache
source_url: https://www.php.net/manual/es/memcache.close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46110
---

Memcache::close

memcache_close

Cierra la conexión con el servidor Memcache

## Descripción

```php
Memcache::close(): bool
```php

```php
memcache_close(Memcache $memcache): bool
```

`Memcache::close` cierra la conexión al servidor `Memcache`. Esta función no cierra las conexiones persistentes que serán cerradas únicamente durante el reinicio del servidor web.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcache::close`

```php
<?php

/* API procedimental */
$memcache_obj = memcache_connect('memcache_host', 11211);
/*
haga algo aquí ...
*/
memcache_close($memcache_obj);

/* API orientada a objetos */
$memcache_obj = new Memcache;
$memcache_obj->connect('memcache_host', 11211);
/*
haga algo aquí ...
*/
$memcache_obj->close();

?>

   
```

## Véase también

Memcache::connect

Memcache::pconnect
