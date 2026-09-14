---
title: Zookeeper::getClientId
description: Devuelve el identificador de sesión del cliente, sólo válido si la conexión
  está actualmente establecida (es decir, si el último estado del observador es ZOO_CONNECTED_STATE).
source_url: https://www.php.net/manual/es/zookeeper.getclientid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/getclientid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109650
---

Zookeeper::getClientId

Devuelve el identificador de sesión del cliente, sólo válido si la conexión está actualmente establecida (es decir, si el último estado del observador es ZOO_CONNECTED_STATE).

## Descripción

```php
public Zookeeper::getClientId(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el identificador de sesión del cliente en caso de éxito, y false en caso de fallo.

## Errores/Excepciones

Este método emite un error/advertencia de PHP cuando el cliente no ha podido obtener el identificador de sesión.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Véase también

Zookeeper::\_\_construct

Zookeeper::connect

Zookeeper::getState

Estados de ZooKeeper

ZookeeperException
