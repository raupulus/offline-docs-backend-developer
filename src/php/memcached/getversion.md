---
title: Memcached::getVersion
description: Lee las informaciones de versión del pool de servidores
source_url: https://www.php.net/manual/es/memcached.getversion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/getversion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46650
---

Memcached::getVersion

Lee las informaciones de versión del pool de servidores

## Descripción

```php
public Memcached::getVersion(): array
```php

`Memcached::getVersion` devuelve un array que contiene las informaciones de versión disponibles de todos los servidores memcache.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Array de versiones de servidores, una por servidor.

## Ejemplos

Ejemplo con `Memcached::getVersion`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

print_r($m->getVersion());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [localhost:11211] => 1.2.6
    )
