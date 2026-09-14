---
title: Memcache::getServerStatus
description: Retorna el estado del servidor
source_url: https://www.php.net/manual/es/memcache.getserverstatus.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/getserverstatus.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46180
---

Memcache::getServerStatus

memcache_get_server_status

Retorna el estado del servidor

## Descripción

```php
Memcache::getServerStatus(string $host, [int $port]): int
```php

```php
memcache_get_server_status(Memcache $memcache, string $host, [int $port]): int
```

`Memcache::getServerStatus` retorna el estado en línea/fuera de línea del servidor.

> [!NOTE]
> Esta función fue añadida en la versión 2.1.0 de Memcache.

## Parámetros

`host`  
Apunta al host donde memcache escucha conexiones.

`port`  
Apunta al puerto donde memcache escucha conexiones.

## Valores devueltos

Retorna el estado del servidor. 0 si el servidor falla, un valor diferente de cero en caso contrario.

## Ejemplos

Ejemplo con `Memcache::getServerStatus`

```php
<?php

/* API orientada a objetos */
$memcache = new Memcache;
$memcache->addServer('memcache_host', 11211);
echo $memcache->getServerStatus('memcache_host', 11211);

/* API procedimental */
$memcache = memcache_connect('memcache_host', 11211);
echo memcache_get_server_status($memcache, 'memcache_host', 11211);

?>

   
```

## Véase también

Memcache::addServer

Memcache::setServerParams
