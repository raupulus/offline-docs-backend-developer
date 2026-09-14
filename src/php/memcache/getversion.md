---
title: Memcache::getVersion
description: Devuelve el número de versión del servidor
source_url: https://www.php.net/manual/es/memcache.getversion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/getversion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46200
---

Memcache::getVersion

memcache_get_version

Devuelve el número de versión del servidor

## Descripción

```php
Memcache::getVersion(): string
```php

```php
memcache_get_version(Memcache $memcache): string
```

`Memcache::getVersion` devuelve una cadena con el número de versión del servidor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `string` con el número de versión del servidor o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcache::getVersion`

```php
<?php

/* API orientada a objetos */
$memcache = new Memcache;
$memcache->connect('memcache_host', 11211);
echo $memcache->getVersion();

/* API procedimental */
$memcache = memcache_connect('memcache_host', 11211);
echo memcache_get_version($memcache);

?>

   
```

## Véase también

Memcache::getExtendedStats

Memcache::getStats
