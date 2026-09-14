---
title: Swoole\Client::connect
description: Conecta al puerto TCP o UDP remoto.
source_url: https://www.php.net/manual/es/swoole-client.connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/client/connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 90970
---

Swoole\Client::connect

Conecta al puerto TCP o UDP remoto.

## Descripción

```php
public Swoole\Client::connect(string $host, [int $port], [int $timeout], [int $flag]): bool
```php

## Parámetros

`host`  
El nombre de host de la dirección remota.

`port`  
El número de puerto de la dirección remota.

`timeout`  
El tiempo de espera (en segundos) de conexión/envío/recepción, el valor por omisión es de 0,1 s.

`flag`  
Si el tipo de cliente es UDP, el \$flag indica si se debe activar la configuración udp_connect. Si la configuración udp_connect está activada, el cliente solo recibirá los datos de la ip:puerto especificada. Si el tipo de cliente es TCP y el \$flag está definido en 1, se debe utilizar swoole_client_select para verificar el estado de la conexión antes de enviar/recibir.

## Valores devueltos

Si la conexión es establecida.
