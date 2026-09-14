---
title: Swoole\Client::send
description: Envía datos al socket TCP remoto.
source_url: https://www.php.net/manual/es/swoole-client.send.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/client/send.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 91080
---

Swoole\Client::send

Envía datos al socket TCP remoto.

## Descripción

```php
public Swoole\Client::send(string $data, [string $flag]): int
```php

## Parámetros

`data`  
Los datos a enviar que pueden ser una string o binarios.

`flag`  

## Valores devueltos

Si el cliente envía datos con éxito, devuelve la longitud de los datos enviados. O devuelve false y define \$swoole_client-\>errCode. Para el cliente síncrono, no hay límite para los datos a enviar. Para el cliente asíncrono, el límite para los datos a enviar es socket_buffer_size.
