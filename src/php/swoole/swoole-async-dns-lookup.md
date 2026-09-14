---
title: swoole_async_dns_lookup
description: Busca de manera asíncrona y no bloqueante la dirección IP de un host
source_url: https://www.php.net/manual/es/function.swoole-async-dns-lookup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/functions/swoole-async-dns-lookup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_revision: 17623bf36
order: 90390
---

swoole_async_dns_lookup

Busca de manera asíncrona y no bloqueante la dirección IP de un host

## Descripción

```php
swoole_async_dns_lookup(string $hostname, callable $callback): bool
```php

## Parámetros

`hostname`  
El nombre de host.

`callback`  
```php
callback(string $hostname, string $ip): mixed
```

`hostname`  
El nombre de host.

`IP`  
La dirección IP.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
