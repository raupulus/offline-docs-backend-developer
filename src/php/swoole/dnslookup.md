---
title: Swoole\Async::dnsLookup
description: Busca de manera asíncrona y no bloqueante la dirección IP de un host.
source_url: https://www.php.net/manual/es/swoole-async.dnslookup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/async/dnslookup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 322606e4f
order: 90690
---

Swoole\Async::dnsLookup

Busca de manera asíncrona y no bloqueante la dirección IP de un host.

## Descripción

```php
public static Swoole\Async::dnsLookup(string $hostname, callable $callback): void
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

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
