---
title: Memcached::resetServerList
description: Elimina todos los servidores de la lista de servidores
source_url: https://www.php.net/manual/es/memcached.resetserverlist.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/resetserverlist.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: false
translation_revision: 1d8068ecb
order: 46750
---

Memcached::resetServerList

Elimina todos los servidores de la lista de servidores

## Descripción

```php
public Memcached::resetServerList(): bool
```php

`Memcached::resetserverlist` elimina todos los servidores de la lista de servidores conocidos, dejándola vacía.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

Memcached::addServer, Memcached::addServers
