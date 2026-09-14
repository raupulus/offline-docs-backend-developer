---
title: Zookeeper::getState
description: Devuelve el estado de la conexión zookeeper
source_url: https://www.php.net/manual/es/zookeeper.getstate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/getstate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109680
---

Zookeeper::getState

Devuelve el estado de la conexión zookeeper

## Descripción

```php
public Zookeeper::getState(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el estado de la conexión zookeeper en caso de éxito, y false en caso de fallo.

## Errores/Excepciones

Este método emite un error/advertencia PHP cuando no se puede obtener el estado de la conexión zookeeper.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Véase también

Zookeeper::\_\_construct

Zookeeper::connect

Zookeeper::getClientId

Estados de ZooKeeper

ZookeeperException
