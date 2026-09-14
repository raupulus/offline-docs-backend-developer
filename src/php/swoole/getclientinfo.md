---
title: Swoole\Server::getClientInfo
description: Devuelve la información de conexión por la descripción del fichero.
source_url: https://www.php.net/manual/es/swoole-server.getclientinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/server/getclientinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: e6be4fb01
order: 92640
---

Swoole\Server::getClientInfo

Devuelve la información de conexión por la descripción del fichero.

## Descripción

```php
public Swoole\Server::getClientInfo(int $fd, [int $reactor_id], [bool $ignore_error]): array
```php

## Parámetros

`fd`  
Los descriptores de ficheros.

`reactor_id`  
El identificador del thread Reactor donde se establece la conexión.

`ignore_error`  
Ignorar los errores o no, si se establece en true, la información de conexión será devuelta incluso si la conexión está cerrada.

## Valores devueltos

Devuelve la información sobre la conexión del cliente.
