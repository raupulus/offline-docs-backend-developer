---
title: Memcache::setCompressThreshold
description: Activa la compresión automática de los valores grandes
source_url: https://www.php.net/manual/es/memcache.setcompressthreshold.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/setcompressthreshold.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46250
---

Memcache::setCompressThreshold

Activa la compresión automática de los valores grandes

## Descripción

```php
Memcache::setCompressThreshold(int $threshold, [float $min_savings]): bool
```php

```php
memcache_set_compress_threshold(Memcache $memcache, int $threshold, [float $min_savings]): bool
```

`Memcache::setCompressThreshold` activa la compresión automática de los valores grandes.

> [!NOTE]
> Esta función fue añadida en la versión 2.0.0 de Memcache.

## Parámetros

`threshold`  
Controla el tamaño mínimo de valor antes de intentar comprimir automáticamente.

`min_saving`  
Especifica el número mínimo de ahorro para guardar los valores comprimidos. El valor proporcionado debe estar entre 0 y 1. El valor por omisión es 0.2, lo que da un mínimo de 20% de ahorro de compresión.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcache::setCompressThreshold`

```php
<?php

/* API orientada a objetos */

$memcache_obj = new Memcache;
$memcache_obj->addServer('memcache_host', 11211);
$memcache_obj->setCompressThreshold(20000, 0.2);

/* API procedimental */

$memcache_obj = memcache_connect('memcache_host', 11211);
memcache_set_compress_threshold($memcache_obj, 20000, 0.2);

?>

   
```
