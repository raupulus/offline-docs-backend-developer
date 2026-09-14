---
title: Zookeeper::connect
description: Crea un manejador para comunicarse con Zookeeper
source_url: https://www.php.net/manual/es/zookeeper.connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 999d171f3
order: 109570
---

Zookeeper::connect

Crea un manejador para comunicarse con Zookeeper

## Descripción

```php
public Zookeeper::connect(string $host, [callable $watcher_cb], [int $recv_timeout]): void
```php

Este método crea una nueva conexión y una sesión zookeeper que corresponde a esa conexión. El establecimiento de la sesión es asíncrono, lo que significa que la sesión no debe considerarse establecida hasta que se reciba un evento ZOO_CONNECTED_STATE.

## Parámetros

`host`  
Separados por comas, cada par host:puerto corresponde a un servidor zk. Por ejemplo, «127.0.0.1:3000,127.0.0.1:3001,127.0.0.1:3002».

`watcher_cb`  
La función de devolución de llamada de observación global. Cuando se activen las notificaciones, se invocará esta función.

`recv_timeout`  
El tiempo de espera para esta sesión, sólo válido si la conexión está actualmente conectada (es decir, el último estado del observador es ZOO_CONNECTED_STATE).

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Este método emite un error/advertencia de PHP si el número de parámetros o tipos es incorrecto o si la instancia no ha podido ser inicializada.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Véase también

Zookeeper::\_\_construct

ZookeeperException
