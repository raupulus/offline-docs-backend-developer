---
title: Memcache::connect
description: Establece una conexión con el servidor Memcache
source_url: https://www.php.net/manual/es/memcache.connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46120
---

Memcache::connect

memcache_connect

Establece una conexión con el servidor Memcache

## Descripción

```php
Memcache::connect(string $host, [int $port], [int $timeout]): bool
```php

```php
memcache_connect(string $host, [int $port], [int $timeout]): Memcache
```

`Memcache::connect` establece una conexión con el servidor de caché `Memcache`. La conexión, que ha sido abierta utilizando la función `Memcache::connect` se cerrará automáticamente al final del script. No obstante, puede cerrarse manualmente utilizando la función `Memcache::close`.

## Parámetros

`host`  
Especifica el host donde memcache escucha para conexiones. Este parámetro puede también especificar otros transportes como `unix:///path/to/memcached.sock` para utilizar sockets Unix, y en este caso, `port` debe también ser definido a `0`.

`port`  
Especifica el puerto donde memcache escucha para conexiones. Defina este parámetro a `0` al utilizar sockets Unix.

Nota: Por omisión, el parámetro `port` toma el valor de la opción de configuración [memcache.default_port](#ini.memcache.default-port) si no es especificado. Por esta razón, es recomendable especificar explícitamente el puerto al llamar a este método.

`timeout`  
Valor en segundos que será utilizado para conectarse al demonio. Considérelo dos veces antes de cambiar el valor por omisión de un segundo - podría perderse todos los beneficios de utilizar la caché si la conexión es demasiado lenta.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcache::connect`

```php
<?php

/* API procedimental */

$memcache_obj = memcache_connect('memcache_host', 11211);

/* API orientada a objetos */

$memcache = new Memcache;
$memcache->connect('memcache_host', 11211);

?>

   
```

## Notas

> [!WARNING]
> Cuando el parámetro `port` no es especificado, este método tomará el valor de la directiva de configuración INI [memcache.default_port](#ini.memcache.default-port). Si este valor ha sido modificado en otro lugar de la aplicación, esto puede conducir a resultados inesperados: por esta razón, es recomendable siempre especificar el puerto explícitamente al llamar al método.

## Véase también

Memcache::pconnect

Memcache::close
