---
title: Swoole\Client::__construct
description: Crea un cliente TCP/UDP síncrono o asíncrono Swoole, con o sin SSL.
source_url: https://www.php.net/manual/es/swoole-client.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/client/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 90980
---

Swoole\Client::\_\_construct

Crea un cliente TCP/UDP síncrono o asíncrono Swoole, con o sin SSL.

## Descripción

```php
public Swoole\Client::__construct(int $sock_type, [int $is_async])
```php

## Parámetros

`sock_type`  
El tipo de socket: SWOOLE_TCP, SWOOLE_UDP, SWOOLE_ASYNC, SWOOLE_SSL, SWOOLE_KEEP.

`is_async`  
Cliente síncrono o asíncrono.
