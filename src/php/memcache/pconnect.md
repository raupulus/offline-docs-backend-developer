---
title: Memcache::pconnect
description: Establece una conexión persistente a un servidor de caché
source_url: https://www.php.net/manual/es/memcache.pconnect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/pconnect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46220
---

Memcache::pconnect

memcache_pconnect

Establece una conexión persistente a un servidor de caché

## Descripción

```php
Memcache::pconnect(string $host, [int $port], [int $timeout]): bool
```php

```php
Memcache::pconnect(string $host, [int $port], [int $timeout]): Memcache
```

`Memcache::pconnect` es similar a la función `Memcache::connect` con la diferencia de que la conexión será persistente. Este tipo de conexión no se cierra al finalizar el script ni por la función `Memcache::close`.

## Parámetros

`host`  
Especifica el host donde memcache escucha conexiones. Este parámetro puede también especificar otros transportes como `unix:///path/to/memcached.sock` para utilizar sockets Unix, y, en este caso, `port` debe también definirse a `0`.

`port`  
Especifica el puerto donde memcache escucha conexiones. Defínase este parámetro a `0` al utilizar sockets Unix.

`timeout`  
Valor en segundos que será utilizado para conectarse al demonio. Piénsese dos veces antes de cambiar el valor por omisión de un segundo - podría perderse todos los beneficios de utilizar la caché si la conexión es demasiado lenta.

## Valores devueltos

Retorna un objeto Memcache o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcache::pconnect`

```php
<?php

/* API procedimental */
$memcache_obj = memcache_pconnect('memcache_host', 11211);

/* API orientada a objetos */

$memcache_obj = new Memcache;
$memcache_obj->pconnect('memcache_host', 11211);

?>

   
```

## Véase también

Memcache::connect
