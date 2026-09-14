---
title: Zookeeper::getRecvTimeout
description: Devuelve el tiempo de espera para esta sesión, sólo válido si la conexión
  está actualmente establecida (es decir, si el último estado del observador es ZOO_CONNECTED_STATE).
  Este valor puede cambiar tras una reconexión con el servidor.
source_url: https://www.php.net/manual/es/zookeeper.getrecvtimeout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/getrecvtimeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109670
---

Zookeeper::getRecvTimeout

Devuelve el tiempo de espera para esta sesión, sólo válido si la conexión está actualmente establecida (es decir, si el último estado del observador es ZOO_CONNECTED_STATE). Este valor puede cambiar tras una reconexión con el servidor.

## Descripción

```php
public Zookeeper::getRecvTimeout(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el tiempo de espera para esta sesión en caso de éxito, y false en caso de fallo.

## Errores/Excepciones

Este método emite un error/advertencia PHP cuando la operación falla.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Véase también

Zookeeper::\_\_construct

Zookeeper::connect

ZookeeperException
