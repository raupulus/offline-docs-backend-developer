---
title: Swoole\Client::sendto
description: Envía datos a la dirección UDP remota.
source_url: https://www.php.net/manual/es/swoole-client.sendto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/client/sendto.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 91100
---

Swoole\Client::sendto

Envía datos a la dirección UDP remota.

## Descripción

```php
public Swoole\Client::sendto(string $ip, int $port, string $data): bool
```php

El cliente swoole debe ser de tipo SWOOLE_SOCK_UDP o SWOOLE_SOCK_UDP6.

## Parámetros

`ip`  
La dirección IP del host remoto, IPv4 o IPv6.

`port`  
El número de puerto del host remoto.

`data`  
Los datos a enviar que deben ser inferiores a 64K.

## Valores devueltos
